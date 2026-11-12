"""Sasmita's 5 Questions & Intent Handlers."""
import re
from typing import Optional, Dict, Any
from classroom_bot.resolver import resolve_subject, find_schedule_for_subject

def handle_classroom_location(match: re.Match, kb: Dict[str, Any]) -> str:
    info = kb["class_info"]
    return (
        f"📍 [Classroom Location]\n"
        f"Class: {info['section']} ({info.get('semester', '6th Semester')})\n"
        f"Room: {info['room']}, {info['floor']}, {info['block']}\n"
        f"Department: {info['department']}"
    )

def handle_timetable(match: re.Match, kb: Dict[str, Any]) -> str:
    gd = match.groupdict()
    sched_subj = gd.get("sched_subj")
    day = gd.get("day_pre") or gd.get("day_post") or gd.get("day")
    timetable = kb["schedules"]["timetable"]

    # 1. If user asked about a specific subject time (e.g., "When do we have NLP?")
    if sched_subj:
        slots = find_schedule_for_subject(sched_subj, kb)
        canon = resolve_subject(sched_subj)
        subj_name = kb["subjects"].get(canon, {}).get("full_name", sched_subj.title()) if canon else sched_subj.title()
        if slots:
            lines = [f"📅 [Class Schedule for {subj_name}]"]
            for s in slots:
                lines.append(f"  • {s}")
            return "\n".join(lines)
        return f"Could not find scheduled slots for '{sched_subj.title()}'. Type 'timetable' to see the full schedule."

    # 2. If user asked about a specific day (e.g., "Monday schedule")
    if day:
        day_key = day.lower()
        if day_key == "today":
            day_key = "monday"  # Default reference day
        if day_key in timetable:
            return f"📅 [Timetable for {day_key.capitalize()}]\n{timetable[day_key]}"
        return f"No classes scheduled for {day_key.capitalize()} (Weekend)."

    # 3. Return full weekly schedule
    lines = ["📅 [Weekly Timetable for 6 B.Tech CS AIML-C]"]
    for d, sched in timetable.items():
        lines.append(f"  • {d.capitalize():9s}: {sched}")
    return "\n".join(lines)

def handle_open_electives(match: re.Match, kb: Dict[str, Any]) -> str:
    electives = kb["electives"]["open"]
    lines = ["🌐 [Available Open Electives - 6th Semester]"]
    for name, data in electives.items():
        lines.append(f"  • {name.title()} ({data['code']}) - Faculty: {data['faculty']} [{data['enrolled_count']} students enrolled, {data['credits']} Credits]")
    return "\n".join(lines)

def handle_cia_schedule(match: re.Match, kb: Dict[str, Any]) -> str:
    cia_num = match.groupdict().get("cia_num")
    cias = kb["schedules"]["cia"]
    if cia_num and cia_num in cias:
        return f"📝 [CIA {cia_num} Schedule]\n{cias[cia_num]}"

    lines = ["📝 [Continuous Internal Assessment (CIA) Schedule]"]
    for num, details in cias.items():
        lines.append(f"  • CIA {num}: {details}")
    return "\n".join(lines)

def handle_syllabus(match: re.Match, kb: Dict[str, Any]) -> str:
    raw_subj = match.groupdict().get("subject", "").strip()
    unit = match.groupdict().get("unit")
    canon = resolve_subject(raw_subj)
    subjects = kb["subjects"]

    if canon not in subjects:
        # Check open electives
        if canon in kb["electives"]["open"]:
            oe = kb["electives"]["open"][canon]
            return f"📚 [{oe['code']} - {canon.title()}]\nThis is a 3-credit Open Elective handled by {oe['faculty']}."
        return f"Subject '{raw_subj.upper()}' not found. Available subjects: {', '.join(s.upper() for s in subjects.keys())}."

    subj_data = subjects[canon]
    if unit:
        try:
            u_idx = int(unit) - 1
            if 0 <= u_idx < len(subj_data["units"]):
                return f"📚 [{subj_data['full_name']} ({canon.upper()}) Syllabus - Unit {unit}]\n{subj_data['units'][u_idx]}"
            return f"Unit {unit} does not exist for {canon.upper()} (Total units: {len(subj_data['units'])})."
        except ValueError:
            pass

    # Return all units
    lines = [f"📚 [Syllabus: {subj_data['full_name']} ({canon.upper()})]"]
    for u in subj_data["units"]:
        lines.append(f"  • {u}")
    return "\n".join(lines)

SASMITA_RULES = [
    {
        "id": 1,
        "name": "Classroom Location Retrieval",
        "member": "Sasmita",
        "pattern": r'\b(?:where\s+(?:is|are|do\s+we\s+have)\s+(?:our\s+)?(?:classroom|class\s*room|class|section\s*c|lectures?)|which\s+room|what\s+room|class\s+location|classroom|class\s*room)\b',
        "handler": handle_classroom_location,
        "description": "Retrieves room number, floor, and building for the class.",
    },
    {
        "id": 14,
        "name": "CIA Schedule Information Retrieval",
        "member": "Sasmita",
        "pattern": r'\b(?:when (?:are|is)|what is)?\s*(?:the\s*)?cias?\s*(?P<cia_num>[1-3])?\s*(?:schedule|dates?|exam)?\b',
        "handler": handle_cia_schedule,
        "description": "Extracts CIA number using character class [1-3] and named group (?P<cia_num>...).",
    },
    {
        "id": 17,
        "name": "Subject Syllabus Retrieval",
        "member": "Sasmita",
        "pattern": r'\b(?:syllabus|units?)(?:\s+(?P<unit>\d+))?\s*(?:of|for|in)\s+(?P<subject>[a-zA-Z\s]+?)(?:\s+syllabus|\?|$)\b',
        "handler": handle_syllabus,
        "description": "Extracts unit number (?P<unit>\\d+) and subject code (?P<subject>[a-zA-Z\\s]+?).",
    },
    {
        "id": 8,
        "name": "Open Elective Information Retrieval",
        "member": "Sasmita",
        "pattern": r'\b(?:what\s+are|which|explain|tell\s+me\s+about|list|show|available)\s+(?:the\s*)?open\s+electives?\b|^\s*(?:the\s*)?open\s+electives?\s*$',
        "handler": handle_open_electives,
        "description": "Lists available open electives with offering faculty and credits.",
    },
    {
        "id": 5,
        "name": "Class Timetable Retrieval",
        "member": "Sasmita",
        "pattern": r'\b(?:when\s+(?:do\s+we\s+have|is)\s+(?P<sched_subj>[a-zA-Z\s]+?)(?:\s+class|\s+lecture)?$|(?P<day_pre>monday|tuesday|wednesday|thursday|friday|saturday|today)\s+(?:timetable|schedule|routine)|(?:timetable|schedule|routine)(?:\s+(?:for|on)?\s*(?P<day_post>monday|tuesday|wednesday|thursday|friday|saturday|today))?)\b',
        "handler": handle_timetable,
        "description": "Retrieves day-wise, subject-wise (e.g. 'When do we have AI?'), or complete weekly timetable.",
    },
]

def match_sasmita_rule(query: str, kb: Dict[str, Any]) -> Optional[str]:
    for rule in SASMITA_RULES:
        match = re.search(rule["pattern"], query, re.IGNORECASE)
        if match:
            return rule["handler"](match, kb)
    return None
