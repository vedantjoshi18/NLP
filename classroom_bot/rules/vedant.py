"""Vedant's 5 Questions & Intent Handlers."""
import re
from typing import Optional, Dict, Any

def handle_cr_info(match: re.Match, kb: Dict[str, Any]) -> str:
    crs = kb["leadership"]["cr"]
    lines = ["👥 [Class Representatives (CR)]"]
    for cr in crs:
        lines.append(f"  • {cr['name']} (Roll: {cr['roll']}) - {cr['contact']}")
    return "\n".join(lines)

def handle_global_electives(match: re.Match, kb: Dict[str, Any]) -> str:
    electives = kb["electives"]["global"]
    lines = ["🌍 [Offered Global Electives]"]
    for name, data in electives.items():
        lines.append(f"  • {name.title()} ({data['code']}) - Dept: {data['dept']} [{data['credits']} Credits]")
    return "\n".join(lines)

def handle_open_elective_enrollment(match: re.Match, kb: Dict[str, Any]) -> str:
    elective = match.groupdict().get("elective", "").strip().lower()
    open_electives = kb["electives"]["open"]
    
    matched_elective = None
    if elective:
        for name, data in open_electives.items():
            if elective in name or name in elective:
                matched_elective = (name, data)
                break

    if matched_elective:
        name, data = matched_elective
        students = ", ".join(data["sample_students"])
        return f"📖 [Open Elective Enrollment: {name.title()}]\nTotal Enrolled: {data['enrolled_count']} students\nSample Enrolled Students: {students}"

    lines = ["📖 [Open Electives Enrollment Summary]"]
    for name, data in open_electives.items():
        lines.append(f"  • {name.title()}: {data['enrolled_count']} students enrolled")
    return "\n".join(lines)

def handle_honours_program(match: re.Match, kb: Dict[str, Any]) -> str:
    hon = kb["programs"]["honours"]
    return (
        f"🎓 [{hon['title']}]\n"
        f"• Requirement: {hon['extra_credits']} extra credits beyond standard curriculum ({hon['duration']})\n"
        f"• Eligibility: {hon['eligibility']}\n"
        f"• Registration: {hon['registration']}"
    )

def handle_exam_schedule(match: re.Match, kb: Dict[str, Any]) -> str:
    exams = kb["schedules"]["exam"]
    return (
        f"📋 [Examination Schedule]\n"
        f"• End Semester Theory Exams: {exams['end_sem']}\n"
        f"• Practical / Lab Examinations: {exams['practicals']}"
    )

VEDANT_RULES = [
    {
        "id": 3,
        "name": "Class Representative Information Retrieval",
        "member": "Vedant",
        "pattern": r'\bwho\s+(?:is|are|represents).*?\b(?P<rep>cr|class\s+representatives?|class\s+reps?|our\s+class)\b',
        "handler": handle_cr_info,
        "description": "Matches queries asking for class representatives using named group (?P<rep>...).",
    },
    {
        "id": 7,
        "name": "Global Elective Information Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:what\s+are|which|explain|tell\s+me\s+about|list)?\s*(?:the\s*)?global\s+electives?\b',
        "handler": handle_global_electives,
        "description": "Lists all global electives offered with credit count and offering departments.",
    },
    {
        "id": 10,
        "name": "Open Elective Subject and Student Enrollment Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:enrollment|enrolled(?:\s+in)?|selected|students?\s+in)\s+(?:the\s*)?open\s+elective\s*(?P<elective>[a-zA-Z\s]+)?\b',
        "handler": handle_open_elective_enrollment,
        "description": "Extracts open elective name using named group (?P<elective>...) and returns enrollments.",
    },
    {
        "id": 11,
        "name": "Honours Program Information Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:what\s+is|how\s+(?:can\s+i\s+)?pursue|tell\s+me\s+about|details\s+on|eligibility\s+for)?\s*(?:the\s*)?honours?(?:\s+program)?\b',
        "handler": handle_honours_program,
        "description": "Explains honours program eligibility (7.5 CGPA) and credit structure.",
    },
    {
        "id": 16,
        "name": "Examination Schedule Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:when\s+(?:are|is)|what\s+is)\s+(?:the\s+|our\s+)?(?P<exam_type>end\s+sem|final|mid\s+sem|examination|exam)s?\s*(?:schedule|timetable|dates?)?\b',
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
