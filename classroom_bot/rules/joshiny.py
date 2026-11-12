"""Joshiny's 5 Questions & Intent Handlers."""
import re
from typing import Optional, Dict, Any
from classroom_bot.resolver import find_faculty

def handle_class_teacher(match: re.Match, kb: Dict[str, Any]) -> str:
    role = (match.groupdict().get("role") or "").lower()
    leadership = kb["leadership"]
    if "co" in role:
        co = leadership["co_class_teacher"]
        return (
            f"👩‍🏫 [Co-Class Teacher]\n"
            f"Name: {co['name']}\n"
            f"Location: {co['cabin']}\n"
            f"Email: {co['email']}\n"
            f"Phone Ext: {co.get('phone_ext', 'N/A')}"
        )
    ct = leadership["class_teacher"]
    return (
        f"👨‍🏫 [Class Teacher]\n"
        f"Name: {ct['name']}\n"
        f"Location: {ct['cabin']}\n"
        f"Email: {ct['email']}\n"
        f"Phone Ext: {ct.get('phone_ext', 'N/A')}"
    )

def handle_faculty_location(match: re.Match, kb: Dict[str, Any]) -> str:
    faculty_query = match.groupdict().get("faculty", "").strip()
    results = find_faculty(faculty_query, kb)

    if results:
        lines = []
        for r in results:
            lines.append(f"🏢 [Faculty Contact: {r['name']}]")
            lines.append(f"  • Role: {r.get('role', 'Faculty')}")
            lines.append(f"  • Cabin / Location: {r.get('location', 'Faculty Room, GF-B3')}")
            if r.get("email"):
                lines.append(f"  • Email: {r['email']}")
            if r.get("ext") and r.get("ext") != "N/A":
                lines.append(f"  • Extension: {r['ext']}")
        return "\n".join(lines)

    return (
        f"Faculty '{faculty_query.title()}' not found in current semester faculty directory.\n"
        f"Key Faculty in 6BTCS AIML C:\n"
        f"  • Dr. Poongodi C (Class Teacher - Faculty Room, GF-B3)\n"
        f"  • Dr. Jeno Lovesum S P (Co-Class Teacher - Faculty Room, GF-B3)\n"
        f"  • Dr. D Vinodha (NLP - DV Lab)\n"
        f"  • Dr. Amos Bortiew (Deep Learning / AI - B6-634)\n"
        f"  • Prof. Wims Magdalene Mary A (DIP - Faculty Room)\n"
        f"  • Dr. Kukatlapalli Pradeep Kumar (Server Integration / Data Modeling)"
    )

def handle_global_elective_enrollment(match: re.Match, kb: Dict[str, Any]) -> str:
    elective = (match.groupdict().get("elective") or "").strip().lower()
    global_electives = kb["electives"]["global"]

    matched_elective = None
    if elective:
        for name, data in global_electives.items():
            if elective in name or name in elective:
                matched_elective = (name, data)
                break

    if matched_elective:
        name, data = matched_elective
        students = ", ".join(data.get("students", data.get("sample_students", []))[:5])
        return (
            f"🌐 [Global Elective Enrollment: {name.title()}]\n"
            f"Course Code: {data.get('code', 'GE')}\n"
            f"Offering Department: {data.get('dept', 'SET')}\n"
            f"Total Enrolled: {data['enrolled_count']} students\n"
            f"Sample Enrolled Students: {students}"
        )

    lines = ["🌐 [Global Electives Enrollment Summary]"]
    for name, data in global_electives.items():
        lines.append(f"  • {name.title()} ({data.get('code', 'GE')}): {data['enrolled_count']} students enrolled")
    return "\n".join(lines)

def handle_sports_cr(match: re.Match, kb: Dict[str, Any]) -> str:
    sports = kb["leadership"]["sports_cr"]
    return (
        f"🏆 [Sports Representative]\n"
        f"Name: {sports['name']}\n"
        f"Role: {sports['role']}\n"
        f"Email: {sports['contact']}\n"
        f"Desk: {sports['desk']}"
    )

def handle_department_info(match: re.Match, kb: Dict[str, Any]) -> str:
    title = match.groupdict().get("title", "").lower()
    dept = kb["leadership"]["department"]
    if "hod" in title or "head" in title:
        return f"🏛️ [Head of Department]\n{dept['hod']}\nOffice: {dept['office']}"
    elif "program" in title:
        return f"🏛️ [Program Coordinator]\n{dept['program_coordinator']}\nOffice: {dept['office']}"
    elif "year" in title:
        return f"🏛️ [Year Coordinator]\n{dept['year_coordinator']}\nOffice: {dept['office']}"
    elif "office" in title:
        return f"🏛️ [Department Office]\nLocation: {dept['office']}\nDepartment: {dept.get('dept', 'Department of AI and Data Science Engineering')}"
    return (
        f"🏛️ [Department Leadership & Office]\n"
        f"HOD: {dept['hod']}\n"
        f"Program Coordinator: {dept['program_coordinator']}\n"
        f"Year Coordinator: {dept['year_coordinator']}\n"
        f"Office: {dept['office']}"
    )

JOSHINY_RULES = [
    {
        "id": 2,
        "name": "Class Teacher and Co-Class Teacher Identification",
        "member": "Joshiny",
        "pattern": r'\b(?:who\s+(?:is|handles|takes)\s+(?:our\s+)?(?:section(?:\s*c)?|class)?\s*)?(?P<role>co[- ]class\s+teacher|co[- ]ct|class\s+teacher|\bct\b)\b|\bwho\s+handles\s+(?:our\s+)?section(?:\s*c)?\b',
        "handler": handle_class_teacher,
        "description": "Distinguishes between class teacher and co-class teacher using named group (?P<role>...).",
    },
    {
        "id": 6,
        "name": "Faculty Location and Contact Information Retrieval",
        "member": "Joshiny",
        "pattern": r'\b(?:where\s+is|cabin\s+of|contact|reach|find|where\s+can\s+i\s+find)\s+(?:prof(?:essor)?|dr\.?)?\s*(?P<faculty>[a-zA-Z\s]+?)(?:\'s|\s+cabin|\s+contact|\s+office|\?|$)\b',
        "handler": handle_faculty_location,
        "description": "Captures faculty name using lazy quantifier +? in (?P<faculty>[a-zA-Z\\s]+?).",
    },
    {
        "id": 9,
        "name": "Global Elective Subject and Student Enrollment Retrieval",
        "member": "Joshiny",
        "pattern": r'\b(?:(?:enrollment(?:\s+in)?|(?:who\s+has\s+)?enrolled(?:\s+in)?|(?:how\s+many\s+)?students?\s+(?:in|(?:are\s+)?taking|take))\s+(?:the\s*|this\s*)?global\s+electives?|global\s+electives?\s+(?:enrollment|students?))\s*(?P<elective>[a-zA-Z\s]+)?\b',
        "handler": handle_global_elective_enrollment,
        "description": "Extracts elective name using named group (?P<elective>...) and outputs enrollment stats.",
    },
    {
        "id": 15,
        "name": "Sports Representative Identification",
        "member": "Joshiny",
        "pattern": r'\b(?:who\s+(?:is|handles)\s+(?:our\s+)?)?(?:sports\s+(?:representative|rep|cr)|sports\s+for\s+our\s+class)\b',
        "handler": handle_sports_cr,
        "description": "Matches sports representative inquiries using nested non-capturing groups.",
    },
    {
        "id": 20,
        "name": "Department Information Retrieval",
        "member": "Joshiny",
        "pattern": r'\b(?:who\s+is\s+(?:our|the)\s+)?(?P<title>hod|head\s+of\s+department|program\s+coordinator|year\s+coordinator|department\s+office)\b',
        "handler": handle_department_info,
        "description": "Identifies department leadership role using named group (?P<title>...).",
    },
]

def match_joshiny_rule(query: str, kb: Dict[str, Any]) -> Optional[str]:
    for rule in JOSHINY_RULES:
        match = re.search(rule["pattern"], query, re.IGNORECASE)
        if match:
            return rule["handler"](match, kb)
    return None
