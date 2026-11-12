"""Rachel's 6 Questions & Intent Handlers."""
import re
from typing import Optional, Dict, Any
from classroom_bot.resolver import resolve_subject, find_faculty

def handle_class_strength(match: re.Match, kb: Dict[str, Any]) -> str:
    st = kb["class_info"]["strength"]
    total = st.get("total", 55)
    boys = st.get("boys", 35)
    girls = st.get("girls", 20)
    note = st.get("note", "6 B.Tech CS AIML-C")
    return (
        f"[Class Strength - 6 B.Tech CS AIML-C]\n"
        f"Total Students: {total}\n"
        f"Gender Breakdown: {boys} Boys, {girls} Girls\n"
        f"Note: {note}"
    )

def handle_minors_program(match: re.Match, kb: Dict[str, Any]) -> str:
    minors = kb["programs"]["minors"]
    opts = ", ".join(minors["options"])
    track_blocks = []
    if "tracks" in minors:
        for tkey, tinfo in minors["tracks"].items():
            t_lines = [f"  [{tinfo['title']} - {tinfo['count']} Students]"]
            t_lines.append(f"    Offering: {tinfo.get('offering', 'School of Business and Management')}")
            t_lines.append("    Individual Enrolled Students:")
            for sname in tinfo["students"]:
                t_lines.append(f"      - {sname}")
            track_blocks.append("\n".join(t_lines))
    tracks_str = "\n".join(track_blocks) if track_blocks else ""
    extra_str = f"\n\nMinors Enrolled Students:\n{tracks_str}" if tracks_str else ""
    return (
        f"[Interdisciplinary Minor Degree]\n"
        f"Requirement: {minors['extra_credits']} Credits across 4 semesters\n"
        f"Tracks Available: {opts}\n"
        f"Timetable Slot: {minors.get('schedule', 'Wednesdays 11:00 - 14:00')}\n"
        f"Eligibility: {minors['eligibility']}"
        f"{extra_str}"
    )

def handle_certificate_program(match: re.Match, kb: Dict[str, Any]) -> str:
    gd = match.groupdict()
    cert_query = (gd.get("cert_name") or "").strip().lower()
    cert_data = kb["programs"]["certificate"]
    certs_dict = cert_data.get("certifications", {})

    # If user queried about a specific certification (e.g. "Who did AWS ML Associate?")
    if cert_query:
        matched = None
        for cname, cinfo in certs_dict.items():
            if cert_query in cname or cname in cert_query or any(w in cname for w in cert_query.split() if len(w) > 3):
                matched = (cname, cinfo)
                break
        if matched:
            cname, cinfo = matched
            stud_lines = "\n".join(f"  - {s}" for s in cinfo["students"])
            return (
                f"[Certification: {cname.title()}]\n"
                f"Total Students Completed: {cinfo['count']}\n"
                f"Certified Students:\n{stud_lines}"
            )

    lines = [
        f"[Value Added Certificate Programs]",
        f"Duration: {cert_data['duration']} | Timetable Slot: {cert_data.get('schedule', 'Wednesdays 11:00 - 14:00')}",
        "Total Certified in Class: 27 students\n",
        "Individual Students by Certification Offering:",
    ]
    for cname, cinfo in certs_dict.items():
        if cinfo["count"] > 0:
            lines.append(f"\n  [{cname.title()} - {cinfo['count']} Students]")
            for s in cinfo["students"]:
                lines.append(f"    - {s}")
    lines.append(f"\nRegistration: {cert_data['registration']}")
    return "\n".join(lines)

def handle_subject_faculty(match: re.Match, kb: Dict[str, Any]) -> str:
    raw_subj = match.groupdict().get("subject", "").strip()
    canon = resolve_subject(raw_subj)
    subjects = kb["subjects"]

    if canon in subjects:
        data = subjects[canon]
        lab_str = f" | Lab Venue: {data['lab']}" if "lab" in data else ""
        return (
            f"[Faculty In-Charge]\n"
            f"Subject: {data['full_name']} ({canon.upper()})\n"
            f"Course Code: {data.get('code', 'CSE')}\n"
            f"Faculty: {data['faculty']}{lab_str}"
        )

    # Check open electives
    open_elecs = kb.get("electives", {}).get("open", {})
    if canon in open_elecs:
        oe = open_elecs[canon]
        return (
            f"[Faculty In-Charge - Open Elective]\n"
            f"Subject: {canon.title()} ({oe.get('code', 'OE')})\n"
            f"Faculty: {oe.get('faculty', 'Department Faculty')}\n"
            f"Department: {oe.get('dept', 'SET')}"
        )

    return f"Subject '{raw_subj.upper()}' not found. Available subjects: {', '.join(s.upper() for s in subjects.keys())}."

def handle_course_credits(match: re.Match, kb: Dict[str, Any]) -> str:
    raw_subj = match.groupdict().get("subject", "").strip()
    canon = resolve_subject(raw_subj)
    subjects = kb["subjects"]

    if canon in subjects:
        data = subjects[canon]
        return (
            f"[Course Credit Details]\n"
            f"Subject: {data['full_name']} ({canon.upper()})\n"
            f"Course Code: {data.get('code', 'CSE')}\n"
            f"Credits: {data['credits']} Credits ({data['structure']})"
        )

    # Check open electives
    open_elecs = kb.get("electives", {}).get("open", {})
    if canon in open_elecs:
        oe = open_elecs[canon]
        return (
            f"[Course Credit Details - Open Elective]\n"
            f"Subject: {canon.title()} ({oe.get('code', 'OE')})\n"
            f"Credits: {oe.get('credits', 3)} Credits (3 Lectures)"
        )

    return f"Subject '{raw_subj.upper()}' not found. Available subjects: {', '.join(s.upper() for s in subjects.keys())}."

def handle_mentor_mentee(match: re.Match, kb: Dict[str, Any]) -> str:
    gd = match.groupdict()
    roll_str = gd.get("roll")
    faculty = gd.get("faculty")
    mentors_info = kb.get("mentors", {})
    groups = mentors_info.get("groups", [])
    ment_hour = mentors_info.get("mentoring_hour", "Saturday 11:00 AM - 12:00 PM")

    # If asked about mentoring hour
    raw_match = match.group(0).lower()
    if "when is mentoring" in raw_match or "mentoring hour" in raw_match:
        return f"[Mentoring Schedule]\nMentoring hour is on {ment_hour}."

    if roll_str:
        try:
            roll = int(roll_str)
            # Normalize roll if 2462xxx or 1-55
            roll_short = roll % 1000 if roll > 1000000 else roll
            for g in groups:
                if g["range"][0] <= roll_short <= g["range"][1]:
                    return f"[Mentor Allocation]\nRoll Number: {roll}\nAssigned Mentor: {g['mentor']} ({g['cabin']})\nMentoring Hour: {ment_hour}"
            return f"Roll Number {roll} out of bounds (1 to 55)."
        except ValueError:
            pass

    if faculty:
        fac_clean = faculty.strip().lower()
        for g in groups:
            if any(part in g["mentor"].lower() for part in fac_clean.split()):
                return f"[Mentee List]\nFaculty: {g['mentor']}\nMentees: Roll {g['range'][0]} to {g['range'][1]} (Total: {g['count']} students)\nCabin: {g['cabin']}\nMentoring Hour: {ment_hour}"
        return f"Faculty '{faculty.title()}' not found in mentor list."

    # General mentor list
    lines = ["[Class Mentor-Mentee Distribution & Mentoring Hour]"]
    lines.append(f"Weekly Mentoring Session: {ment_hour}\n")
    for g in groups:
        lines.append(f"  - {g['mentor']}: Roll {g['range'][0]} to {g['range'][1]} ({g['cabin']})")
    return "\n".join(lines)

RACHEL_RULES = [
    {
        "id": 4,
        "name": "Class Strength Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:how\s+many\s+students|class\s+strength|strength\s+of\s+(?:the\s+|our\s+)?class|how\s+many\s+people|total\s+students|number\s+of\s+students|total\s+strength)\b',
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
        "pattern": r'\b(?:(?:what|how|which|tell\s+me\s+about|explain|list|who\s+(?:completed|did|holds|has|took))(?:\s+can\s+i\s+pursue)?\s+)?(?:the\s+)?(?:certificates?|certifications?)(?:\s+(?:programs?|courses?|students?|list))?\b|\bwho\s+(?:did|completed|holds|took)\s+(?:the\s*)?(?P<cert_name>[a-zA-Z\s\d\-]+?)(?:\s+certification|\s+cert|\?|$)\b',
        "handler": handle_certificate_program,
        "description": "Matches certificate queries or specific cert inquiries using named group (?P<cert_name>...).",
    },
    {
        "id": 18,
        "name": "Subject Faculty Identification",
        "member": "Rachel",
        "pattern": r'\b(?:who\s+teaches|which\s+faculty\s+handles|subject\s+teacher\s+for|who\s+takes|faculty\s+for)\s+(?P<subject>[a-zA-Z\s]+?)(?:\?|$)\b',
        "handler": handle_subject_faculty,
        "description": "Extracts subject code dynamically with named group (?P<subject>[a-zA-Z\\s]+?).",
    },
    {
        "id": 19,
        "name": "Course Credit Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:how\s+many\s+credits(?:\s+does)?|what\s+are\s+the\s+credits\s+for|credits?\s+(?:for|of)|credit\s+value\s+of)\s+(?P<subject>[a-zA-Z\s]+?)(?:\s+have|\s+worth|\?|$)\b',
        "handler": handle_course_credits,
        "description": "Extracts subject code dynamically using named group (?P<subject>[a-zA-Z\\s]+?) for credit lookup.",
    },
    {
        "id": 21,
        "name": "Mentor and Mentee Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:mentor\s+(?:for|of)\s*(?:roll\s*)?(?P<roll>\d+)|(?:mentees?|students?)\s+(?:are\s+)?(?:under|of)\s*(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+)|who\s+is\s+my\s+mentor|when\s+is\s+mentoring)\b',
        "handler": handle_mentor_mentee,
        "description": "Multi-branch named capturing groups (?P<roll>\\d+) vs (?P<faculty>[a-zA-Z\\s]+) and mentoring hour.",
    },
]

def match_rachel_rule(query: str, kb: Dict[str, Any]) -> Optional[str]:
    for rule in RACHEL_RULES:
        match = re.search(rule["pattern"], query, re.IGNORECASE)
        if match:
            return rule["handler"](match, kb)
    return None
