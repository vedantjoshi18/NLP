"""Entity and Query Resolver for Classroom Bot."""
import re
from typing import Optional, Dict, Any, List

SUBJECT_ALIASES = {
    "nlp": "nlp",
    "natural language processing": "nlp",
    "natural language programming": "nlp",
    "dl": "dl",
    "deep learning": "dl",
    "ai": "ai",
    "artificial intelligence": "ai",
    "dip": "dip",
    "digital image processing": "dip",
    "image processing": "dip",
    "pe": "pe",
    "professional ethics": "pe",
    "ethics": "pe",
    "sir": "sir",
    "server integration": "sir",
    "server integration using json and db connectivity": "sir",
    "json": "sir",
    "slp": "slp",
    "service learning": "slp",
    "service-learning": "slp",
    "service learning project": "slp",
    "aec": "aec",
    "ncc": "aec",
    "ability enhancement": "aec",
    "dbms": "dbms",
    "database": "dbms",
    "database management": "dbms",
    "database management systems": "dbms",
    "ml": "ml",
    "machine learning": "ml",
    # Open electives
    "computer vision": "computer vision",
    "cv": "computer vision",
    "data modeling": "data modeling and visualization",
    "data modeling and visualization": "data modeling and visualization",
    "dmv": "data modeling and visualization",
    "internet of things": "internet of things",
    "iot": "internet of things",
    "ethical hacking": "introduction to ethical hacking",
    "introduction to ethical hacking": "introduction to ethical hacking",
    "prompt engineering": "prompt engineering",
}

def resolve_subject(name: str) -> Optional[str]:
    """Resolves subject acronym or query string to canonical key."""
    if not name:
        return None
    cleaned = name.strip().lower()
    cleaned = re.sub(r'\b(?:class|subject|course|syllabus|paper)\b', '', cleaned).strip()
    if cleaned in SUBJECT_ALIASES:
        return SUBJECT_ALIASES[cleaned]
    for alias, key in SUBJECT_ALIASES.items():
        if alias in cleaned or cleaned in alias:
            return key
    return cleaned

def find_faculty(query: str, kb: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Searches leadership, subjects, electives, and mentors for matching faculty."""
    if not query:
        return []
    clean_q = re.sub(r'\b(?:dr|prof|professor|mr|mrs|ms)\b', '', query.strip().lower()).strip()
    words = [w for w in clean_q.split() if len(w) > 2]
    if not words:
        words = clean_q.split()

    results = []

    # Check class teacher & co-class teacher
    for role_key, role_label in [("class_teacher", "Class Teacher"), ("co_class_teacher", "Co-Class Teacher")]:
        entry = kb["leadership"].get(role_key, {})
        name = entry.get("name", "")
        if any(w in name.lower() for w in words):
            results.append({
                "name": name,
                "role": role_label,
                "location": entry.get("cabin", "Faculty Room, GF-B3"),
                "email": entry.get("email", ""),
                "ext": entry.get("phone_ext", "N/A"),
            })

    # Check HOD
    hod_str = kb["leadership"].get("department", {}).get("hod", "")
    if any(w in hod_str.lower() for w in words):
        results.append({
            "name": hod_str,
            "role": "Head of Department (HOD)",
            "location": kb["leadership"]["department"].get("office", "Department Office, GF-B3"),
            "email": "hod.aiml@christuniversity.in",
        })

    # Check subjects
    for code, subj_data in kb["subjects"].items():
        fac_name = subj_data.get("faculty", "")
        if any(w in fac_name.lower() for w in words):
            lab_info = f" | Lab: {subj_data['lab']}" if "lab" in subj_data else ""
            results.append({
                "name": fac_name,
                "role": f"Faculty for {subj_data['full_name']} ({code.upper()})",
                "location": f"Faculty Room, GF-B3{lab_info}",
                "subject": subj_data["full_name"],
            })

    # Check mentors
    for g in kb.get("mentors", {}).get("groups", []):
        m_name = g.get("mentor", "")
        if any(w in m_name.lower() for w in words):
            if not any(r["name"] == m_name for r in results):
                results.append({
                    "name": m_name,
                    "role": "Class Mentor",
                    "location": g.get("cabin", "Faculty Room"),
                })

    return results

def find_student(query: str, kb: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Finds student record by register number or name."""
    if not query:
        return []
    clean_q = query.strip().lower()
    students = kb.get("students", {})
    matches = []

    # Check exact register number
    for regno, data in students.items():
        if clean_q == regno or clean_q in regno:
            matches.append(data)
            continue
        if clean_q in data["name"].lower():
            matches.append(data)

    return matches

def find_schedule_for_subject(subj_query: str, kb: Dict[str, Any]) -> List[str]:
    """Finds every timetable slot where this subject or keyword appears."""
    canon = resolve_subject(subj_query)
    slots = []
    
    # Check if subject has direct schedule list
    if canon and canon in kb["subjects"]:
        sched_list = kb["subjects"][canon].get("schedule", [])
        if sched_list and sched_list != ["Curriculum Subject"]:
            return sched_list

    # Search raw timetable strings
    timetable = kb.get("schedules", {}).get("timetable", {})
    search_terms = [subj_query.lower()]
    if canon and canon in kb["subjects"]:
        search_terms.append(kb["subjects"][canon]["full_name"].lower())
        search_terms.append(canon)

    for day, text in timetable.items():
        for period in text.split(" | "):
            if any(term in period.lower() for term in search_terms):
                slots.append(f"{day.capitalize()}: {period.strip()}")

    return slots
