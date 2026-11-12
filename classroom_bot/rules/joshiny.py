"""Joshiny's 5 Questions & Intent Handlers."""
import re
from typing import Optional, Dict, Any

def handle_class_teacher(match: re.Match, kb: Dict[str, Any]) -> str:
    role = match.groupdict().get("role", "").lower()
    leadership = kb["leadership"]
    if "co" in role:
        co = leadership["co_class_teacher"]
        return f"👩‍🏫 [Co-Class Teacher]\nName: {co['name']}\nLocation: {co['cabin']}\nEmail: {co['email']}\nExt: {co['phone_ext']}"
    ct = leadership["class_teacher"]
    return f"👨‍🏫 [Class Teacher]\nName: {ct['name']}\nLocation: {ct['cabin']}\nEmail: {ct['email']}\nExt: {ct['phone_ext']}"

def handle_faculty_location(match: re.Match, kb: Dict[str, Any]) -> str:
    faculty_query = match.groupdict().get("faculty", "").strip().lower()
    leadership = kb["leadership"]
    ct = leadership["class_teacher"]
    co = leadership["co_class_teacher"]

    if any(part in ct["name"].lower() for part in faculty_query.split()):
        return f"🏢 [Faculty Contact]\n{ct['name']} (Class Teacher)\nCabin: {ct['cabin']}\nEmail: {ct['email']} | Ext: {ct['phone_ext']}"
    if any(part in co["name"].lower() for part in faculty_query.split()):
        return f"🏢 [Faculty Contact]\n{co['name']} (Co-Class Teacher)\nCabin: {co['cabin']}\nEmail: {co['email']} | Ext: {co['phone_ext']}"
    
    # Search subjects
    for subj_code, data in kb["subjects"].items():
        if any(part in data["faculty"].lower() for part in faculty_query.split()):
            lab_info = f" | Lab: {data['lab']}" if "lab" in data else ""
            return f"🏢 [Faculty Contact]\n{data['faculty']} (Faculty for {data['full_name']})\nLocation: Department Faculty Room, GF-B3{lab_info}\nSubject: {data['full_name']} ({subj_code.upper()})"
    
    # Search mentors
    for g in kb.get("mentors", {}).get("groups", []):
        if any(part in g["mentor"].lower() for part in faculty_query.split()):
            return f"🏢 [Faculty Contact]\n{g['mentor']} (Mentor)\nCabin: {g['cabin']}"
    
    return f"Faculty '{faculty_query.title()}' not found in current semester faculty directory."

def handle_global_elective_enrollment(match: re.Match, kb: Dict[str, Any]) -> str:
    elective = match.groupdict().get("elective", "").strip().lower()
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
        return f"🌐 [Global Elective Enrollment: {name.title()}]\nTotal Enrolled: {data['enrolled_count']} students\nSample Enrolled Students: {students}"
    
    lines = ["🌐 [Global Electives Enrollment Summary]"]
    for name, data in global_electives.items():
        lines.append(f"  • {name.title()}: {data['enrolled_count']} students enrolled")
    return "\n".join(lines)

def handle_sports_cr(match: re.Match, kb: Dict[str, Any]) -> str:
    sports = kb["leadership"]["sports_cr"]
    return f"🏆 [Sports Representative]\nName: {sports['name']}\nRole: {sports['role']}\nEmail: {sports['contact']}\nDesk: {sports['desk']}"

def handle_department_info(match: re.Match, kb: Dict[str, Any]) -> str:
    title = match.groupdict().get("title", "").lower()
    dept = kb["leadership"]["department"]
    if "hod" in title or "head" in title:
        return f"🏛️ [Head of Department]\n{dept['hod']}\nOffice: {dept['office']}"
    elif "program" in title:
        return f"🏛️ [Program Coordinator]\n{dept['program_coordinator']}\nOffice: {dept['office']}"
    elif "year" in title:
        return f"🏛️ [Year Coordinator]\n{dept['year_coordinator']}\nOffice: {dept['office']}"
    return f"🏛️ [Department Leadership]\nHOD: {dept['hod']}\nProgram Coordinator: {dept['program_coordinator']}\nOffice: {dept['office']}"

JOSHINY_RULES = [
    {
        "id": 2,
        "name": "Class Teacher and Co-Class Teacher Identification",
        "member": "Joshiny",
        "pattern": r'\bwho\s+(?:is|handles).*?\b(?P<role>co[- ]class\s+teacher|class\s+teacher|section)\b',
        "handler": handle_class_teacher,
        "description": "Distinguishes between class teacher and co-class teacher using named group (?P<role>...).",
    },
    {
        "id": 6,
        "name": "Faculty Location and Contact Information Retrieval",
        "member": "Joshiny",
        "pattern": r'\b(?:where\s+is|cabin\s+of|contact|reach|find)\s+(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+?)(?:\'s|\s+cabin|\s+contact|\?|$)\b',
        "handler": handle_faculty_location,
        "description": "Captures faculty name using lazy quantifier +? in (?P<faculty>[a-zA-Z\\s]+?).",
    },
    {
        "id": 9,
        "name": "Global Elective Subject and Student Enrollment Retrieval",
        "member": "Joshiny",
        "pattern": r'\b(?:enrollment|enrolled(?:\s+in)?|students?\s+in)\s+(?:the\s*)?global\s+elective\s*(?P<elective>[a-zA-Z\s]+)?\b',
        "handler": handle_global_elective_enrollment,
        "description": "Extracts elective name using named group (?P<elective>...) and outputs enrollment stats.",
    },
    {
        "id": 15,
        "name": "Sports Representative Identification",
        "member": "Joshiny",
        "pattern": r'\bwho\s+(?:is|handles).*(?:sports\s+(?:representative|rep|cr)|sports\s+for\s+our\s+class)\b',
        "handler": handle_sports_cr,
        "description": "Matches sports representative inquiries using nested non-capturing groups.",
    },
    {
        "id": 20,
        "name": "Department Information Retrieval",
        "member": "Joshiny",
        "pattern": r'\bwho\s+is\s+(?:our|the)\s+(?P<title>hod|head\s+of\s+department|program\s+coordinator|year\s+coordinator)\b',
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
