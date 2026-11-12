"""Rachel's 6 Questions & Intent Handlers."""
import re
from typing import Optional, Dict, Any

def handle_class_strength(match: re.Match, kb: Dict[str, Any]) -> str:
    st = kb["class_info"]["strength"]
    total = st.get("total", "N/A")
    boys = st.get("boys")
    girls = st.get("girls")
    if boys and girls:
        return f"📊 [Class Strength]\nTotal Students: {total} (Boys: {boys}, Girls: {girls})"
    return f"📊 [Class Strength]\nTotal Students: {total}"

def handle_minors_program(match: re.Match, kb: Dict[str, Any]) -> str:
    minors = kb["programs"]["minors"]
    opts = ", ".join(minors["options"])
    return (
        f"🎓 [{minors['title']}]\n"
        f"• Requirement: {minors['extra_credits']} Credits across 4 semesters\n"
        f"• Tracks Available: {opts}\n"
        f"• Eligibility: {minors['eligibility']}"
    )

def handle_certificate_program(match: re.Match, kb: Dict[str, Any]) -> str:
    cert = kb["programs"]["certificate"]
    lines = [f"📜 [{cert['title']}] (Duration: {cert['duration']})", "Available Certifications in Our Class:"]
    for c in cert["current_offerings"]:
        lines.append(f"  • {c}")
    lines.append(f"\nRegistration: {cert['registration']}")
    return "\n".join(lines)

def handle_subject_faculty(match: re.Match, kb: Dict[str, Any]) -> str:
    subj = match.groupdict().get("subject", "").lower()
    subjects = kb["subjects"]
    if subj in subjects:
        data = subjects[subj]
        return f"👨‍🏫 [Faculty In-Charge]\nSubject: {data['full_name']} ({subj.upper()})\nFaculty: {data['faculty']}"
    return f"Subject '{subj.upper()}' not found. Available subjects: {', '.join(s.upper() for s in subjects.keys())}."

def handle_course_credits(match: re.Match, kb: Dict[str, Any]) -> str:
    subj = match.groupdict().get("subject", "").lower()
    subjects = kb["subjects"]
    if subj in subjects:
        data = subjects[subj]
        return f"🎯 [Course Credit Details]\nSubject: {data['full_name']} ({subj.upper()})\nCredits: {data['credits']} Credits ({data['structure']})"
    return f"Subject '{subj.upper()}' not found. Available subjects: {', '.join(s.upper() for s in subjects.keys())}."

def handle_mentor_mentee(match: re.Match, kb: Dict[str, Any]) -> str:
    gd = match.groupdict()
    roll_str = gd.get("roll")
    faculty = gd.get("faculty")
    groups = kb["mentors"]["groups"]

    if roll_str:
        try:
            roll = int(roll_str)
            for g in groups:
                if g["range"][0] <= roll <= g["range"][1]:
                    return f"🧑‍🏫 [Mentor Allocation]\nRoll Number: {roll}\nAssigned Mentor: {g['mentor']} ({g['cabin']})"
            return f"Roll Number {roll} out of bounds (1 to 68)."
        except ValueError:
            pass

    if faculty:
        fac_clean = faculty.strip().lower()
        for g in groups:
            if any(part in g["mentor"].lower() for part in fac_clean.split()):
                return f"🧑‍🏫 [Mentee List]\nFaculty: {g['mentor']}\nMentees: Roll {g['range'][0]} to {g['range'][1]} (Total: {g['count']} students)\nCabin: {g['cabin']}"
        return f"Faculty '{faculty.title()}' not found in mentor list."

    # General mentor list
    lines = ["🧑‍🏫 [Class Mentor-Mentee Distribution]"]
    for g in groups:
        lines.append(f"  • {g['mentor']}: Roll {g['range'][0]} to {g['range'][1]} ({g['cabin']})")
    return "\n".join(lines)

RACHEL_RULES = [
    {
        "id": 4,
        "name": "Class Strength Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:how\s+many\s+students|class\s+strength|strength\s+of\s+(?:the\s+|our\s+)?class|how\s+many\s+people)\b',
        "handler": handle_class_strength,
        "description": "Matches class strength queries using phrase alternation and word boundaries.",
    },
    {
        "id": 12,
        "name": "Minor Program Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:what\s+(?:are|is)|how\s+do|which|tell\s+me\s+about)?\s*(?:the\s*)?minors?(?:\s+program)?\b',
        "handler": handle_minors_program,
        "description": "Matches minor program inquiries with optional prefixes and pluralization.",
    },
    {
        "id": 13,
        "name": "Certificate Program Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:what|how|tell\s+me\s+about|which)?\s*certificate\s*(?:programs?|courses?)\b',
        "handler": handle_certificate_program,
        "description": "Matches certificate queries using optional prefixes and alternate suffixes.",
    },
    {
        "id": 18,
        "name": "Subject Faculty Identification",
        "member": "Rachel",
        "pattern": r'\b(?:who\s+teaches|which\s+faculty\s+handles|subject\s+teacher\s+for|who\s+takes)\s+(?P<subject>\w+)\b',
        "handler": handle_subject_faculty,
        "description": "Extracts subject code dynamically with named group (?P<subject>\\w+).",
    },
    {
        "id": 19,
        "name": "Course Credit Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:how\s+many\s+credits(?:\s+does)?|what\s+are\s+the\s+credits\s+for|credits?\s+(?:for|of)|credit\s+value\s+of)\s+(?P<subject>\w+)\b',
        "handler": handle_course_credits,
        "description": "Extracts subject code dynamically using named group (?P<subject>\\w+) for credit lookup.",
    },
    {
        "id": 21,
        "name": "Mentor and Mentee Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:mentor\s+(?:for|of)\s*(?:roll\s*)?(?P<roll>\d+)|(?:mentees?|students?)\s+(?:are\s+)?(?:under|of)\s*(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+)|who\s+is\s+my\s+mentor)\b',
        "handler": handle_mentor_mentee,
        "description": "Multi-branch named capturing groups (?P<roll>\\d+) vs (?P<faculty>[a-zA-Z\\s]+).",
    },
]

def match_rachel_rule(query: str, kb: Dict[str, Any]) -> Optional[str]:
    for rule in RACHEL_RULES:
        match = re.search(rule["pattern"], query, re.IGNORECASE)
        if match:
            return rule["handler"](match, kb)
    return None
