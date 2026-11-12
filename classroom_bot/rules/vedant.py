"""Vedant's 5 Questions & Intent Handlers."""
import re
from typing import Optional, Dict, Any
from classroom_bot.resolver import resolve_subject, find_student

def handle_cr_info(match: re.Match, kb: Dict[str, Any]) -> str:
    crs = kb["leadership"]["cr"]
    lines = ["[Class Representatives (CR)]"]
    for cr in crs:
        lines.append(f"  - {cr['name']} (Roll: {cr['roll']}) - {cr['contact']}")
    return "\n".join(lines)

def handle_global_electives(match: re.Match, kb: Dict[str, Any]) -> str:
    electives = kb["electives"]["global"]
    lines = ["[Offered Global Electives - 6th Semester]"]
    for name, data in electives.items():
        lines.append(f"  - {name.title()} ({data['code']}) - Dept: {data['dept']} [{data['credits']} Credits]")
    return "\n".join(lines)

def handle_open_elective_enrollment(match: re.Match, kb: Dict[str, Any]) -> str:
    gd = match.groupdict()
    elective = (gd.get("elective") or "").strip().lower()
    student_query = (gd.get("student_query") or "").strip()

    # 1. Query by student name / roll number (e.g. "Which open elective did Rachel take?")
    if student_query:
        students = find_student(student_query, kb)
        if students:
            lines = [f"[Open Elective Selection for '{student_query.title()}']"]
            for s in students:
                lines.append(f"  - {s['name']} (Reg No: {s['regno']}) -> {s['open_elective']}")
            return "\n".join(lines)
        return f"Student '{student_query.title()}' not found in 6BTCS AIML C class record."

    open_electives = kb["electives"]["open"]

    # 2. Query by elective title
    matched_elective = None
    if elective:
        canon_elec = resolve_subject(elective)
        for name, data in open_electives.items():
            if canon_elec and (canon_elec in name or name in canon_elec):
                matched_elective = (name, data)
                break
            if elective in name or name in elective:
                matched_elective = (name, data)
                break

    if matched_elective:
        name, data = matched_elective
        student_list = data.get("students", data.get("sample_students", []))
        stud_lines = "\n".join(f"    - {s}" for s in student_list)
        return (
            f"[Open Elective Enrollment: {name.title()}]\n"
            f"Course Code: {data.get('code', 'ADS/CSE')}\n"
            f"Faculty In-Charge: {data.get('faculty', 'Department Faculty')}\n"
            f"Total Enrolled: {data['enrolled_count']} students\n"
            f"Enrolled Students:\n{stud_lines}"
        )

    # 3. Overall summary
    lines = ["[Open Electives Enrollment Summary - 6BTCS AIML C]"]
    for name, data in open_electives.items():
        lines.append(f"  - {name.title()}: {data['enrolled_count']} students enrolled ({data.get('faculty', 'Faculty')})")
    return "\n".join(lines)

def handle_honours_program(match: re.Match, kb: Dict[str, Any]) -> str:
    hon = kb["programs"]["honours"]
    courses = "\n".join(f"  - {c}" for c in hon.get("courses_6th_sem", []))
    track_blocks = []
    if "tracks" in hon:
        for tkey, tinfo in hon["tracks"].items():
            t_lines = [f"  [{tinfo['title']} - {tinfo['count']} Students]"]
            t_lines.append(f"    6th Sem Course: {tinfo.get('courses_6th_sem', 'Honours Specialization')}")
            t_lines.append("    Individual Enrolled Students:")
            for sname in tinfo["students"]:
                t_lines.append(f"      - {sname}")
            track_blocks.append("\n".join(t_lines))
    tracks_str = "\n\n".join(track_blocks) if track_blocks else "Tracks offered in Department."
    return (
        f"[B.Tech Honours Program]\n"
        f"Requirement: {hon['extra_credits']} extra credits beyond standard curriculum ({hon['duration']})\n"
        f"Eligibility: {hon['eligibility']}\n"
        f"Timetable Slot: {hon.get('schedule', 'Wednesdays 11:00 - 14:00')}\n"
        f"Total Enrolled in Class: {hon.get('enrolled_count', 20)} students\n\n"
        f"Honours Tracks and Individual Enrolled Students:\n{tracks_str}\n\n"
        f"6th Semester Honours Courses & Faculty:\n{courses}\n"
        f"Registration: {hon['registration']}"
    )

def handle_exam_schedule(match: re.Match, kb: Dict[str, Any]) -> str:
    exams = kb["schedules"]["exam"]
    return (
        f"[Examination Schedule]\n"
        f"- End Semester Theory Exams: {exams['end_sem']}\n"
        f"- Practical / Lab Examinations: {exams['practicals']}"
    )

VEDANT_RULES = [
    {
        "id": 3,
        "name": "Class Representative Information Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:who\s+(?:is|are|represents)\s+(?:our\s+)?)?(?P<rep>class\s+representatives?|class\s+reps?|\bcr\b)\b|\bwho\s+represents\s+our\s+class\b',
        "handler": handle_cr_info,
        "description": "Matches queries asking for class representatives using named group (?P<rep>...).",
    },
    {
        "id": 7,
        "name": "Global Elective Information Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:what\s+are|which|explain|tell\s+me\s+about|list|show|available)\s+(?:the\s*)?global\s+electives?\b|^\s*(?:the\s*)?global\s+electives?\s*$',
        "handler": handle_global_electives,
        "description": "Lists all global electives offered with credit count and offering departments.",
    },
    {
        "id": 10,
        "name": "Open Elective Subject and Student Enrollment Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:(?:(?:list|show)\s+)?open\s+electives?\s+enrollments?|(?:enrollment|enrolled(?:\s+in)?|(?:who\s+)?selected|who\s+chose|(?:how\s+many\s+)?students?\s+(?:in|(?:are\s+)?taking|take))\s+(?:the\s*)?open\s+electives?\s*(?P<elective>[a-zA-Z\s]+)?|(?:open\s+elective\s+(?:of|for)|(?:which|what)\s+open\s+elective\s+(?:did|is))\s+(?P<student_query>[a-zA-Z\s\d]+?)(?:\s+take|\s+choose|\s+enrolled(?:\s+in)?|\?|$))\b',
        "handler": handle_open_elective_enrollment,
        "description": "Extracts open elective name (?P<elective>...) or student name (?P<student_query>...).",
    },
    {
        "id": 11,
        "name": "Honours Program Information Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:what\s+is|how\s+(?:can\s+i\s+)?pursue|tell\s+me\s+about|details\s+on|eligibility\s+for|list|who\s+(?:is|are)\s+(?:in|taking))?\s*(?:the\s*)?(?:honours?|honors?)(?:\s+(?:program|courses?|subjects?|students?|list))?\b',
        "handler": handle_honours_program,
        "description": "Explains honours program eligibility (7.5 CGPA), credits, and 6th sem courses from timetable.",
    },
    {
        "id": 16,
        "name": "Examination Schedule Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:when\s+(?:are|is)|what\s+is)\s+(?:the\s+|our\s+)?(?:next\s+)?(?P<exam_type>end\s+sem|final|mid\s+sem|examination|exam)s?\s*(?:schedule|timetable|dates?)?\b',
        "handler": handle_exam_schedule,
        "description": "Extracts exam category (?P<exam_type>...) and returns end sem and lab exam dates.",
    },
]

def match_vedant_rule(query: str, kb: Dict[str, Any]) -> Optional[str]:
    for rule in VEDANT_RULES:
        match = re.search(rule["pattern"], query, re.IGNORECASE)
        if match:
            return rule["handler"](match, kb)
    return None
