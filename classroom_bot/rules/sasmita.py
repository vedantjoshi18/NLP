"""Sasmita's 5 Questions & Intent Handlers."""
import re
from typing import Optional, Dict, Any

def handle_classroom_location(match: re.Match, kb: Dict[str, Any]) -> str:
    info = kb["class_info"]
    return f"📍 [Classroom Location]\nOur class ({info['section']}) is in {info['room']}, {info['floor']}, {info['block']}."

def handle_timetable(match: re.Match, kb: Dict[str, Any]) -> str:
    day = match.groupdict().get("day")
    timetable = kb["schedules"]["timetable"]
    if day:
        day_key = day.lower()
        if day_key == "today":
            day_key = "monday"  # Default reference day
        if day_key in timetable:
            return f"📅 [Timetable for {day_key.capitalize()}]\n{timetable[day_key]}"
        return f"No classes scheduled for {day_key.capitalize()} (Weekend)."
    
    # Return full weekly schedule
    lines = ["📅 [Weekly Timetable for 6 B.Tech CS AIML-C]"]
    for d, sched in timetable.items():
        lines.append(f"  • {d.capitalize():9s}: {sched}")
    return "\n".join(lines)

def handle_open_electives(match: re.Match, kb: Dict[str, Any]) -> str:
    electives = kb["electives"]["open"]
    lines = ["🌐 [Available Open Electives]"]
    for name, data in electives.items():
        lines.append(f"  • {name.title()} ({data['code']}) - {data['enrolled_count']} students enrolled [{data['credits']} Credits]")
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
    subj = match.groupdict().get("subject", "").lower()
    unit = match.groupdict().get("unit")
    subjects = kb["subjects"]

    if subj not in subjects:
        return f"Subject '{subj.upper()}' not found. Available subjects: {', '.join(s.upper() for s in subjects.keys())}."

    subj_data = subjects[subj]
    if unit:
        try:
            u_idx = int(unit) - 1
            if 0 <= u_idx < len(subj_data["units"]):
                return f"📚 [{subj.upper()} Syllabus - Unit {unit}]\n{subj_data['units'][u_idx]}"
            return f"Unit {unit} does not exist for {subj.upper()} (Total units: {len(subj_data['units'])})."
        except ValueError:
            pass

    # Return all units
    lines = [f"📚 [Syllabus: {subj_data['full_name']} ({subj.upper()})]"]
    for u in subj_data["units"]:
        lines.append(f"  • {u}")
    return "\n".join(lines)

SASMITA_RULES = [
    {
        "id": 1,
        "name": "Classroom Location Retrieval",
        "member": "Sasmita",
        "pattern": r'\b(?:where\s+is\s+our\s+classroom|which\s+room|class\s+location|classroom|class\s*room)\b',
        "handler": handle_classroom_location,
        "description": "Retrieves room number, floor, and building for the class.",
    },
    {
        "id": 5,
        "name": "Class Timetable Retrieval",
        "member": "Sasmita",
        "pattern": r'\b(?:timetable|schedule|routine)(?:\s+(?:for|on)?\s*(?P<day>monday|tuesday|wednesday|thursday|friday|today))?\b',
        "handler": handle_timetable,
        "description": "Retrieves day-wise or complete weekly class routine using named group (?P<day>...).",
    },
    {
        "id": 8,
        "name": "Open Elective Information Retrieval",
        "member": "Sasmita",
        "pattern": r'\b(?:what\s+are|which|explain|tell\s+me\s+about|list|show|available)\s+(?:the\s*)?open\s+electives?\b|^\s*(?:the\s*)?open\s+electives?\s*$',
        "handler": handle_open_electives,
        "description": "Lists available open electives with offering departments and credits.",
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
        "pattern": r'\b(?:syllabus|units?)(?:\s+(?P<unit>\d+))?\s*(?:of|for|in)\s+(?P<subject>\w+)\b',
        "handler": handle_syllabus,
        "description": "Extracts unit number (?P<unit>\\d+) and subject code (?P<subject>\\w+).",
    },
]

def match_sasmita_rule(query: str, kb: Dict[str, Any]) -> Optional[str]:
    for rule in SASMITA_RULES:
        match = re.search(rule["pattern"], query, re.IGNORECASE)
        if match:
            return rule["handler"](match, kb)
    return None
