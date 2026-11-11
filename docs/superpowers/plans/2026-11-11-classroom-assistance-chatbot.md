# Classroom Assistance Bot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a rule-based Classroom Assistance Chatbot using Python Regular Expressions (`re`) covering 21 user intents across 4 team members (Sasmita, Joshiny, Vedant, Rachel), satisfying all CIA-1 evaluation rubrics and generating complete submission documents and reports.

**Architecture:** A declarative rule-based engine featuring `re.sub` query preprocessing, sequential `re.search` matching with named capturing groups, `re.split` multi-token parsing, an in-memory knowledge base for dynamic responses, and default fallback handling.

**Tech Stack:** Python 3.10+, Standard Library `re`, `sys`, `unittest` (Zero external dependencies).

## Global Constraints
- Python Standard Library only (`re`, `sys`, `unittest`, `dataclasses`, `typing`).
- Every regular expression must remain clean, readable, and non-convoluted.
- All 21 intents from Part 1 & Part 2 must be fully implemented and covered by automated tests.
- Individual member documents must be generated in `docs/members/` for Sasmita, Joshiny, Vedant, and Rachel.
- A comprehensive academic report must be produced in `docs/problem_solving_report.md`.

---

### Task 1: Knowledge Base and Query Preprocessing Pipeline

**Files:**
- Create: `classroom_bot/knowledge_base.py`
- Create: `classroom_bot/preprocessor.py`
- Test: `tests/test_preprocessor.py`

**Interfaces:**
- Produces: `preprocess_query(text: str) -> str`
- Produces: `KNOWLEDGE_BASE: dict` containing department, class, subject, elective, schedule, and mentor data.

- [ ] **Step 1: Write test for preprocessor**

```python
# tests/test_preprocessor.py
import unittest
from classroom_bot.preprocessor import preprocess_query

class TestPreprocessor(unittest.TestCase):
    def test_lowercase_and_strip(self):
        self.assertEqual(preprocess_query("  WHERE IS OUR CLASSROOM?  "), "where is our classroom")

    def test_strip_filler_prefixes(self):
        self.assertEqual(preprocess_query("Please tell me who is our class teacher"), "who is our class teacher")
        self.assertEqual(preprocess_query("Can you please show the timetable"), "show the timetable")
        self.assertEqual(preprocess_query("Could you inform me when are the CIAs"), "when are the cias")

    def test_clean_punctuation(self):
        self.assertEqual(preprocess_query("Who teaches AI???"), "who teaches ai")
        self.assertEqual(preprocess_query("What are the credits for DBMS?!!"), "what are the credits for dbms")

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests/test_preprocessor.py`
Expected: FAIL (`ModuleNotFoundError: No module named 'classroom_bot'`)

- [ ] **Step 3: Implement preprocessor and knowledge base**

```python
# classroom_bot/__init__.py
# (Empty package init)
```

```python
# classroom_bot/knowledge_base.py
"""In-memory Knowledge Base for Christ University B.Tech CS AIML Section C."""

KNOWLEDGE_BASE = {
    "class_info": {
        "section": "6 B.Tech CS AIML-C",
        "room": "Room 412",
        "floor": "4th Floor",
        "block": "Block II",
        "strength": {
            "total": 68,
            "boys": 42,
            "girls": 26,
        },
    },
    "leadership": {
        "class_teacher": {
            "name": "Dr. K. Saravanan",
            "cabin": "Cabin 305, Block II (3rd Floor)",
            "email": "saravanan.k@christuniversity.in",
            "phone_ext": "4123",
        },
        "co_class_teacher": {
            "name": "Prof. Deepa V.",
            "cabin": "Cabin 210, Block II (2nd Floor)",
            "email": "deepa.v@christuniversity.in",
            "phone_ext": "4110",
        },
        "cr": [
            {"name": "Rahul M.", "contact": "rahul.m@cs.christuniversity.in", "roll": "2362001"},
            {"name": "Ananya Sharma", "contact": "ananya.s@cs.christuniversity.in", "roll": "2362002"},
        ],
        "sports_cr": {
            "name": "Rohan Gowda",
            "contact": "rohan.g@cs.christuniversity.in",
            "role": "Sports Class Representative",
            "desk": "Sports Directorate, Ground Floor, Central Block",
        },
        "department": {
            "hod": "Dr. Balakrishnan R. (Department of Computer Science & Engineering)",
            "program_coordinator": "Dr. Smitha Rao (B.Tech CS AIML Coordinator)",
            "year_coordinator": "Dr. Suresh N. (3rd Year B.Tech Coordinator)",
            "office": "Room 101, Ground Floor, Block II",
        },
    },
    "subjects": {
        "ai": {
            "full_name": "Artificial Intelligence",
            "faculty": "Dr. K. Saravanan",
            "credits": 4,
            "structure": "3 Lectures + 2 Practical Hours (L-T-P: 3-0-2)",
            "units": [
                "Unit 1: Problem Solving, State Space Search, Heuristic Search (A*, AO*)",
                "Unit 2: Knowledge Representation, First Order Logic, Semantic Networks",
                "Unit 3: Probabilistic Reasoning, Bayesian Networks, Hidden Markov Models",
                "Unit 4: Machine Learning Fundamentals, Decision Trees, Reinforcement Learning",
                "Unit 5: Planning and Natural Language Understanding Basics",
            ],
        },
        "dbms": {
            "full_name": "Database Management Systems",
            "faculty": "Prof. Deepa V.",
            "credits": 3,
            "structure": "3 Lectures + 0 Practical Hours (L-T-P: 3-0-0)",
            "units": [
                "Unit 1: ER Modeling, Relational Model Concepts and Constraints",
                "Unit 2: Relational Algebra, Calculus, and Advanced SQL Queries",
                "Unit 3: Functional Dependencies and Normalization (1NF through BCNF)",
                "Unit 4: Transaction Processing, ACID Properties, Concurrency Control Protocols",
                "Unit 5: Storage Structures, Indexing (B-Trees, B+ Trees), and Query Optimization",
            ],
        },
        "nlp": {
            "full_name": "Natural Language Programming",
            "faculty": "Dr. Praveen Kumar",
            "credits": 4,
            "structure": "3 Lectures + 2 Lab Hours (L-T-P: 3-0-2)",
            "units": [
                "Unit 1: Introduction to NLP, Regular Expressions, Tokenization, Morphology",
                "Unit 2: Language Modeling, N-grams, Part-of-Speech Tagging",
                "Unit 3: Syntactic Parsing, Context-Free Grammars, Dependency Parsing",
                "Unit 4: Semantic Analysis, Word Embeddings (Word2Vec, GloVe), WordNet",
                "Unit 5: Sequence Models (RNN, LSTM, Transformers) and Rule-Based Chatbots",
            ],
        },
        "ml": {
            "full_name": "Machine Learning",
            "faculty": "Dr. Rekha N.",
            "credits": 4,
            "structure": "3 Lectures + 2 Lab Hours (L-T-P: 3-0-2)",
            "units": [
                "Unit 1: Supervised Learning, Linear Regression, Logistic Regression",
                "Unit 2: Support Vector Machines and Kernel Methods",
                "Unit 3: Ensemble Learning (Random Forests, Gradient Boosting)",
                "Unit 4: Unsupervised Learning, Clustering (K-Means, Hierarchical), PCA",
                "Unit 5: Neural Networks, Backpropagation, and Model Evaluation",
            ],
        },
    },
    "electives": {
        "global": {
            "quantum computing": {"code": "GE601", "credits": 3, "dept": "Physics/CSE", "enrolled_count": 24, "sample_students": ["Aditya V.", "Kavya R.", "Nikhil P."]},
            "robotics and automation": {"code": "GE602", "credits": 3, "dept": "Mechanical", "enrolled_count": 22, "sample_students": ["Harish B.", "Pooja S.", "Tarun K."]},
            "cyber forensics": {"code": "GE603", "credits": 3, "dept": "IT & Cyber", "enrolled_count": 22, "sample_students": ["Gaurav M.", "Sneha T.", "Varun D."]},
        },
        "open": {
            "digital marketing": {"code": "OE601", "credits": 3, "dept": "School of Business", "enrolled_count": 32, "sample_students": ["Aman J.", "Bhavana K.", "Chetan L."]},
            "financial literacy": {"code": "OE602", "credits": 3, "dept": "Commerce", "enrolled_count": 20, "sample_students": ["Divya N.", "Farhan Q.", "Gita S."]},
            "creative writing": {"code": "OE603", "credits": 3, "dept": "English & Languages", "enrolled_count": 16, "sample_students": ["Isha M.", "Karan W.", "Lata V."]},
        },
    },
    "programs": {
        "honours": {
            "title": "B.Tech Honours in CS AIML",
            "extra_credits": 20,
            "duration": "Semesters 5 to 8 (5 credits per semester)",
            "eligibility": "Minimum 7.5 CGPA with zero standing backlogs",
            "registration": "Apply via KP Portal during odd semester registration",
        },
        "minors": {
            "title": "Interdisciplinary Minor Degree",
            "extra_credits": 18,
            "options": ["Data Science (Stats Dept)", "Internet of Things (ECE Dept)", "Financial Technology (Commerce)"],
            "eligibility": "Minimum 7.0 CGPA",
            "registration": "Open in 4th and 5th semester",
        },
        "certificate": {
            "title": "Value Added Certificate Courses",
            "duration": "30 Contact Hours (1 Credit equivalent)",
            "current_offerings": [
                "Generative AI & LLM Application Development (Industry Partner: AWS)",
                "Full-Stack Web3 & Blockchain (Industry Partner: Polygon)",
                "Applied Deep Learning for Computer Vision (Industry Partner: NVIDIA DLI)",
            ],
            "registration": "Register through Office of Student Affairs / KP portal",
        },
    },
    "schedules": {
        "cia": {
            "1": "Feb 16, 2026 to Feb 21, 2026 (Written Exam - 25 Marks per subject)",
            "2": "March 23, 2026 to March 28, 2026 (Mid-Sem Written Exam - 50 Marks converted)",
            "3": "April 10, 2026 to April 15, 2026 (Component 3: Assignments & Mini Project)",
        },
        "exam": {
            "end_sem": "May 5, 2026 to May 18, 2026 (Theory Exams: 9:30 AM - 12:30 PM)",
            "practicals": "April 24, 2026 to April 30, 2026 (Lab Exams)",
        },
        "timetable": {
            "monday": "09:00 AI | 10:00 DBMS | 11:15 NLP | 12:15 Lunch | 01:15-03:15 NLP Lab",
            "tuesday": "09:00 ML | 10:00 AI | 11:15 Global Elective | 12:15 Lunch | 01:15-03:15 AI Lab",
            "wednesday": "09:00 Open Elective | 10:00 DBMS | 11:15 ML | 12:15 Lunch | 01:15-03:15 ML Lab",
            "thursday": "09:00 NLP | 10:00 Global Elective | 11:15 AI | 12:15 Lunch | 01:15 Library / Seminar",
            "friday": "09:00 DBMS | 10:00 ML | 11:15 Open Elective | 12:15 Lunch | 01:15-03:15 Project Work",
        },
    },
    "mentors": {
        "groups": [
            {"mentor": "Dr. K. Saravanan", "range": (1, 23), "count": 23, "cabin": "Cabin 305, Block II"},
            {"mentor": "Prof. Deepa V.", "range": (24, 46), "count": 23, "cabin": "Cabin 210, Block II"},
            {"mentor": "Dr. Praveen Kumar", "range": (47, 68), "count": 22, "cabin": "Cabin 312, Block II"},
        ],
    },
}
```

```python
# classroom_bot/preprocessor.py
"""Preprocessing module using Python re.sub."""
import re

def preprocess_query(query: str) -> str:
    """Cleans punctuation, trims whitespace, removes polite filler prefixes, and lowercases text."""
    if not query:
        return ""

    text = query.strip().lower()

    # Strip conversational filler prefixes like "please tell me", "can you show", etc.
    filler_pattern = r'^(?:(?:can|could)\s+you\s+(?:please\s+)?(?:tell\s+me|show\s+me|inform\s+me|give\s+me)?\s*|please\s+(?:tell\s+me|show\s+me|inform\s+me|give\s+me)?\s*|tell\s+me\s+(?:about\s+)?|show\s+me\s+)'
    text = re.sub(filler_pattern, '', text, flags=re.IGNORECASE)

    # Replace punctuation (except alphanumeric and single spaces)
    text = re.sub(r'[^\w\s]', ' ', text)

    # Collapse multiple whitespace into a single space
    text = re.sub(r'\s+', ' ', text).strip()

    return text
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tests/test_preprocessor.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add classroom_bot/__init__.py classroom_bot/knowledge_base.py classroom_bot/preprocessor.py tests/test_preprocessor.py
git commit -m "feat: add knowledge base and regex preprocessor"
```

---

### Task 2: Sasmita's Intent Rules (Q1, Q5, Q8, Q14, Q17)

**Files:**
- Create: `classroom_bot/rules/sasmita.py`
- Test: `tests/test_sasmita_rules.py`

**Interfaces:**
- Produces: `SASMITA_RULES: list[dict]`
- Each rule contains: `id`, `name`, `member`, `pattern`, `handler(match, kb) -> str`, `description`

- [ ] **Step 1: Write test for Sasmita's 5 rules**

```python
# tests/test_sasmita_rules.py
import unittest
from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.rules.sasmita import match_sasmita_rule

class TestSasmitaRules(unittest.TestCase):
    def test_q1_classroom_location(self):
        for q in ["where is our classroom", "which room is our class in", "tell me our class location"]:
            resp = match_sasmita_rule(q, KNOWLEDGE_BASE)
            self.assertIsNotNone(resp)
            self.assertIn("Room 412", resp)

    def test_q5_timetable(self):
        resp_full = match_sasmita_rule("what is our timetable", KNOWLEDGE_BASE)
        self.assertIn("Monday", resp_full)
        resp_mon = match_sasmita_rule("show monday schedule", KNOWLEDGE_BASE)
        self.assertIn("09:00 AI", resp_mon)

    def test_q8_open_electives(self):
        resp = match_sasmita_rule("what are the open electives", KNOWLEDGE_BASE)
        self.assertIn("Digital Marketing", resp)

    def test_q14_cia_schedule(self):
        resp_all = match_sasmita_rule("when are the cias", KNOWLEDGE_BASE)
        self.assertIn("CIA 1", resp_all)
        resp_cia2 = match_sasmita_rule("when is cia 2", KNOWLEDGE_BASE)
        self.assertIn("March 23", resp_cia2)

    def test_q17_syllabus(self):
        resp_all = match_sasmita_rule("give me the syllabus for ai", KNOWLEDGE_BASE)
        self.assertIn("Unit 1", resp_all)
        resp_unit2 = match_sasmita_rule("show unit 2 of ai syllabus", KNOWLEDGE_BASE)
        self.assertIn("Knowledge Representation", resp_unit2)

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests/test_sasmita_rules.py`
Expected: FAIL (`ModuleNotFoundError: No module named 'classroom_bot.rules'`)

- [ ] **Step 3: Implement Sasmita's rules**

```python
# classroom_bot/rules/__init__.py
# (Empty package init)
```

```python
# classroom_bot/rules/sasmita.py
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
        lines.append(f"  • {name.title()} ({data['code']}) - Offered by {data['dept']} [{data['credits']} Credits]")
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
        "pattern": r'\b(?:where is|which room|location of).*(?:classroom|class room|class location|our class|room)\b',
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
        "pattern": r'\b(?:what are|which|explain|tell me about|list)?\s*(?:the\s*)?open electives?\b',
        "handler": handle_open_electives,
        "description": "Lists available open electives with offering departments and credits.",
    },
    {
        "id": 14,
        "name": "CIA Schedule Information Retrieval",
        "member": "Sasmita",
        "pattern": r'\b(?:when (?:are|is)|what is the)?\s*cia\s*(?P<cia_num>[1-3])?\s*(?:schedule|dates?|exam)?\b',
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tests/test_sasmita_rules.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add classroom_bot/rules/__init__.py classroom_bot/rules/sasmita.py tests/test_sasmita_rules.py
git commit -m "feat: add Sasmita's 5 intent rules and tests"
```

---

### Task 3: Joshiny's Intent Rules (Q2, Q6, Q9, Q15, Q20)

**Files:**
- Create: `classroom_bot/rules/joshiny.py`
- Test: `tests/test_joshiny_rules.py`

**Interfaces:**
- Produces: `JOSHINY_RULES: list[dict]`
- Produces: `match_joshiny_rule(query: str, kb: dict) -> Optional[str]`

- [ ] **Step 1: Write test for Joshiny's 5 rules**

```python
# tests/test_joshiny_rules.py
import unittest
from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.rules.joshiny import match_joshiny_rule

class TestJoshinyRules(unittest.TestCase):
    def test_q2_class_teacher(self):
        resp_ct = match_joshiny_rule("who is our class teacher", KNOWLEDGE_BASE)
        self.assertIn("Dr. K. Saravanan", resp_ct)
        resp_co = match_joshiny_rule("who is our co-class teacher", KNOWLEDGE_BASE)
        self.assertIn("Prof. Deepa V.", resp_co)

    def test_q6_faculty_location(self):
        resp = match_joshiny_rule("where is professor saravanan's cabin", KNOWLEDGE_BASE)
        self.assertIn("Cabin 305", resp)

    def test_q9_global_elective_enrollment(self):
        resp = match_joshiny_rule("who enrolled in global elective quantum computing", KNOWLEDGE_BASE)
        self.assertIn("24 students", resp)

    def test_q15_sports_representative(self):
        resp = match_joshiny_rule("who is our sports representative", KNOWLEDGE_BASE)
        self.assertIn("Rohan Gowda", resp)

    def test_q20_department_info(self):
        resp_hod = match_joshiny_rule("who is our hod", KNOWLEDGE_BASE)
        self.assertIn("Dr. Balakrishnan R.", resp_hod)
        resp_coord = match_joshiny_rule("who is the program coordinator", KNOWLEDGE_BASE)
        self.assertIn("Dr. Smitha Rao", resp_coord)

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests/test_joshiny_rules.py`
Expected: FAIL (`ModuleNotFoundError: No module named 'classroom_bot.rules.joshiny'`)

- [ ] **Step 3: Implement Joshiny's rules**

```python
# classroom_bot/rules/joshiny.py
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
    # Search teachers in leadership and subjects
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
            return f"🏢 [Faculty Contact]\n{data['faculty']} (Faculty for {data['full_name']})\nCabin: Block II Faculty Room\nSubject: {data['full_name']} ({subj_code.upper()})"
    
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
        students = ", ".join(data["sample_students"])
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
        "pattern": r'\bwho (?:is|handles).*(?P<role>co-class teacher|class teacher|section)\b',
        "handler": handle_class_teacher,
        "description": "Distinguishes between class teacher and co-class teacher using named group (?P<role>...).",
    },
    {
        "id": 6,
        "name": "Faculty Location and Contact Information Retrieval",
        "member": "Joshiny",
        "pattern": r'\b(?:where is|cabin of|contact|reach|find)\s+(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+?)(?:\'s|\s+cabin|\s+contact|\?|$)\b',
        "handler": handle_faculty_location,
        "description": "Captures faculty name using lazy quantifier +? in (?P<faculty>[a-zA-Z\\s]+?).",
    },
    {
        "id": 9,
        "name": "Global Elective Subject and Student Enrollment Retrieval",
        "member": "Joshiny",
        "pattern": r'\b(?:enrollment|enrolled|students? in)\s+global elective\s*(?P<elective>[a-zA-Z\s]+)?\b',
        "handler": handle_global_elective_enrollment,
        "description": "Extracts elective name using named group (?P<elective>...) and outputs enrollment stats.",
    },
    {
        "id": 15,
        "name": "Sports Representative Identification",
        "member": "Joshiny",
        "pattern": r'\bwho (?:is|handles).*(?:sports (?:representative|rep|cr)|sports for our class)\b',
        "handler": handle_sports_cr,
        "description": "Matches sports representative inquiries using nested non-capturing groups.",
    },
    {
        "id": 20,
        "name": "Department Information Retrieval",
        "member": "Joshiny",
        "pattern": r'\bwho is (?:our|the)\s+(?P<title>hod|head of department|program coordinator|year coordinator)\b',
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tests/test_joshiny_rules.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add classroom_bot/rules/joshiny.py tests/test_joshiny_rules.py
git commit -m "feat: add Joshiny's 5 intent rules and tests"
```

---

### Task 4: Vedant's Intent Rules (Q3, Q7, Q10, Q11, Q16)

**Files:**
- Create: `classroom_bot/rules/vedant.py`
- Test: `tests/test_vedant_rules.py`

**Interfaces:**
- Produces: `VEDANT_RULES: list[dict]`
- Produces: `match_vedant_rule(query: str, kb: dict) -> Optional[str]`

- [ ] **Step 1: Write test for Vedant's 5 rules**

```python
# tests/test_vedant_rules.py
import unittest
from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.rules.vedant import match_vedant_rule

class TestVedantRules(unittest.TestCase):
    def test_q3_class_representative(self):
        for q in ["who is our cr", "who are the class representatives", "who represents our class"]:
            resp = match_vedant_rule(q, KNOWLEDGE_BASE)
            self.assertIsNotNone(resp)
            self.assertIn("Rahul M.", resp)
            self.assertIn("Ananya Sharma", resp)

    def test_q7_global_electives(self):
        resp = match_vedant_rule("what are the global electives", KNOWLEDGE_BASE)
        self.assertIn("Quantum Computing", resp)

    def test_q10_open_elective_enrollment(self):
        resp = match_vedant_rule("who selected open elective digital marketing", KNOWLEDGE_BASE)
        self.assertIn("32 students", resp)

    def test_q11_honours_program(self):
        for q in ["what is honours", "how can i pursue honours", "tell me about the honours program"]:
            resp = match_vedant_rule(q, KNOWLEDGE_BASE)
            self.assertIsNotNone(resp)
            self.assertIn("20 extra credits", resp)

    def test_q16_exam_schedule(self):
        resp = match_vedant_rule("when are our exams", KNOWLEDGE_BASE)
        self.assertIn("May 5, 2026", resp)

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests/test_vedant_rules.py`
Expected: FAIL (`ModuleNotFoundError: No module named 'classroom_bot.rules.vedant'`)

- [ ] **Step 3: Implement Vedant's rules**

```python
# classroom_bot/rules/vedant.py
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
        f"• Requirement: {hon['extra_credits']} beyond standard curriculum ({hon['duration']})\n"
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
        "pattern": r'\bwho (?:is|are|represents).*(?P<rep>cr|class representative|class reps?)\b',
        "handler": handle_cr_info,
        "description": "Matches queries asking for class representatives using named group (?P<rep>...).",
    },
    {
        "id": 7,
        "name": "Global Elective Information Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:what are|which|explain|tell me about|list)?\s*(?:the\s*)?global electives?\b',
        "handler": handle_global_electives,
        "description": "Lists all global electives offered with credit count and offering departments.",
    },
    {
        "id": 10,
        "name": "Open Elective Subject and Student Enrollment Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:enrollment|enrolled|selected|students? in)\s+open elective\s*(?P<elective>[a-zA-Z\s]+)?\b',
        "handler": handle_open_elective_enrollment,
        "description": "Extracts open elective name using named group (?P<elective>...) and returns enrollments.",
    },
    {
        "id": 11,
        "name": "Honours Program Information Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:what is|how to pursue|tell me about|details on|eligibility for)?\s*(?:the\s*)?honours?(?:\s+program)?\b',
        "handler": handle_honours_program,
        "description": "Explains honours program eligibility (7.5 CGPA) and credit structure.",
    },
    {
        "id": 16,
        "name": "Examination Schedule Retrieval",
        "member": "Vedant",
        "pattern": r'\b(?:when (?:are|is)|what is)\s+(?:the\s*)?(?P<exam_type>end sem|final|mid sem|examination|exam)\s*(?:schedule|timetable|dates?)?\b',
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tests/test_vedant_rules.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add classroom_bot/rules/vedant.py tests/test_vedant_rules.py
git commit -m "feat: add Vedant's 5 intent rules and tests"
```

---

### Task 5: Rachel's Intent Rules (Q4, Q12, Q13, Q18, Q19, Q21)

**Files:**
- Create: `classroom_bot/rules/rachel.py`
- Test: `tests/test_rachel_rules.py`

**Interfaces:**
- Produces: `RACHEL_RULES: list[dict]`
- Produces: `match_rachel_rule(query: str, kb: dict) -> Optional[str]`

- [ ] **Step 1: Write test for Rachel's 6 rules**

```python
# tests/test_rachel_rules.py
import unittest
from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.rules.rachel import match_rachel_rule

class TestRachelRules(unittest.TestCase):
    def test_q4_class_strength(self):
        for q in ["how many students are in our class", "what's our class strength", "how many people in our section"]:
            resp = match_rachel_rule(q, KNOWLEDGE_BASE)
            self.assertIsNotNone(resp)
            self.assertIn("68 students", resp)

    def test_q12_minor_program(self):
        resp = match_rachel_rule("what are the minors", KNOWLEDGE_BASE)
        self.assertIn("18", resp)

    def test_q13_certificate_program(self):
        resp = match_rachel_rule("what certificate programs are available", KNOWLEDGE_BASE)
        self.assertIn("30 Contact Hours", resp)

    def test_q18_subject_faculty(self):
        resp_ai = match_rachel_rule("who teaches ai", KNOWLEDGE_BASE)
        self.assertIn("Dr. K. Saravanan", resp_ai)
        resp_dbms = match_rachel_rule("which faculty handles dbms", KNOWLEDGE_BASE)
        self.assertIn("Prof. Deepa V.", resp_dbms)

    def test_q19_course_credits(self):
        resp_ai = match_rachel_rule("how many credits does ai have", KNOWLEDGE_BASE)
        self.assertIn("4 Credits", resp_ai)
        resp_dbms = match_rachel_rule("what are the credits for dbms", KNOWLEDGE_BASE)
        self.assertIn("3 Credits", resp_dbms)

    def test_q21_mentor_mentee(self):
        resp_roll = match_rachel_rule("who is my mentor for roll 15", KNOWLEDGE_BASE)
        self.assertIn("Dr. K. Saravanan", resp_roll)
        resp_prof = match_rachel_rule("which students are under professor deepa", KNOWLEDGE_BASE)
        self.assertIn("Roll 24 to 46", resp_prof)

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m unittest tests/test_rachel_rules.py`
Expected: FAIL (`ModuleNotFoundError: No module named 'classroom_bot.rules.rachel'`)

- [ ] **Step 3: Implement Rachel's rules**

```python
# classroom_bot/rules/rachel.py
"""Rachel's 6 Questions & Intent Handlers."""
import re
from typing import Optional, Dict, Any

def handle_class_strength(match: re.Match, kb: Dict[str, Any]) -> str:
    st = kb["class_info"]["strength"]
    return f"📊 [Class Strength]\nTotal Students: {st['total']} (Boys: {st['boys']}, Girls: {st['girls']})"

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
    lines = [f"📜 [{cert['title']}] (Duration: {cert['duration']})", "Available Offerings:"]
    for c in cert["current_offerings"]:
        lines.append(f"  • {c}")
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
        "pattern": r'\b(?:how many students|class strength|strength of class|how many people)\b',
        "handler": handle_class_strength,
        "description": "Matches class strength queries using phrase alternation and word boundaries.",
    },
    {
        "id": 12,
        "name": "Minor Program Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:what (?:are|is)|how do|which|tell me about)?\s*(?:the\s*)?minors?(?:\s+program)?\b',
        "handler": handle_minors_program,
        "description": "Matches minor program inquiries with optional prefixes and pluralization.",
    },
    {
        "id": 13,
        "name": "Certificate Program Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:what|how|tell me about|which)?\s*certificate\s*(?:programs?|courses?)\b',
        "handler": handle_certificate_program,
        "description": "Matches certificate queries using optional prefixes and alternate suffixes.",
    },
    {
        "id": 18,
        "name": "Subject Faculty Identification",
        "member": "Rachel",
        "pattern": r'\b(?:who teaches|which faculty handles|subject teacher for|who takes)\s+(?P<subject>\w+)\b',
        "handler": handle_subject_faculty,
        "description": "Extracts subject code dynamically with named group (?P<subject>\\w+).",
    },
    {
        "id": 19,
        "name": "Course Credit Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:how many credits|credits? (?:for|of)|credit value of)\s+(?P<subject>\w+)\b',
        "handler": handle_course_credits,
        "description": "Extracts subject code dynamically using named group (?P<subject>\\w+) for credit lookup.",
    },
    {
        "id": 21,
        "name": "Mentor and Mentee Information Retrieval",
        "member": "Rachel",
        "pattern": r'\b(?:mentor for\s*(?:roll\s*)?(?P<roll>\d+)|mentees? (?:under|of)\s*(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+)|who is my mentor)\b',
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m unittest tests/test_rachel_rules.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add classroom_bot/rules/rachel.py tests/test_rachel_rules.py
git commit -m "feat: add Rachel's 6 intent rules and tests"
```

---

### Task 6: Master Bot Engine, CLI Script, and Automated Test Suite

**Files:**
- Create: `classroom_bot/engine.py`
- Create: `chatbot.py`
- Create: `test_chatbot.py`

**Interfaces:**
- Produces: `ChatbotEngine` class with `.process_query(user_input: str) -> dict` returning `{"intent": str, "member": str, "matched_pattern": str, "response": str, "groups": dict}`.
- Produces: Executable `chatbot.py` CLI runner.
- Produces: End-to-end test runner `test_chatbot.py`.

- [ ] **Step 1: Implement `classroom_bot/engine.py`**

```python
# classroom_bot/engine.py
"""Central Chatbot Engine aggregating all 21 rules."""
import re
from typing import Dict, Any, Optional

from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.preprocessor import preprocess_query
from classroom_bot.rules.sasmita import SASMITA_RULES
from classroom_bot.rules.joshiny import JOSHINY_RULES
from classroom_bot.rules.vedant import VEDANT_RULES
from classroom_bot.rules.rachel import RACHEL_RULES

class ChatbotEngine:
    def __init__(self, kb: Optional[Dict[str, Any]] = None):
        self.kb = kb or KNOWLEDGE_BASE
        # Aggregate all rules in order
        self.rules = SASMITA_RULES + JOSHINY_RULES + VEDANT_RULES + RACHEL_RULES

    def get_fallback_response(self, cleaned_query: str) -> str:
        return (
            "🤖 I'm sorry, I couldn't recognize your query.\n"
            "Here are some questions you can ask me:\n"
            "  • 'Where is our classroom?' (Sasmita - Q1)\n"
            "  • 'Who is our class teacher?' (Joshiny - Q2)\n"
            "  • 'Who is our CR?' (Vedant - Q3)\n"
            "  • 'How many students are in our class?' (Rachel - Q4)\n"
            "  • 'What is the syllabus for AI?' (Sasmita - Q17)\n"
            "  • 'Who teaches DBMS?' (Rachel - Q18)\n"
            "Type 'help' to see all 21 supported queries grouped by team member."
        )

    def process_query(self, raw_input: str) -> Dict[str, Any]:
        cleaned = preprocess_query(raw_input)
        if not cleaned:
            return {
                "matched": False,
                "intent": None,
                "member": None,
                "pattern": None,
                "groups": {},
                "response": "Please enter a question or query. Type 'help' for examples.",
            }

        # Check each rule
        for rule in self.rules:
            match = re.search(rule["pattern"], cleaned, re.IGNORECASE)
            if match:
                response = rule["handler"](match, self.kb)
                return {
                    "matched": True,
                    "id": rule["id"],
                    "intent": rule["name"],
                    "member": rule["member"],
                    "pattern": rule["pattern"],
                    "groups": match.groupdict(),
                    "response": response,
                }

        # Unrecognized fallback
        return {
            "matched": False,
            "id": None,
            "intent": "Unrecognized Query",
            "member": None,
            "pattern": None,
            "groups": {},
            "response": self.get_fallback_response(cleaned),
        }
```

- [ ] **Step 2: Create `chatbot.py` Interactive CLI**

```python
# chatbot.py
"""
Classroom Assistance Bot - Interactive CLI
CHRIST (Deemed to be University) - School of Engineering and Technology
B.Tech CS AIML-C | Course: Natural Language Programming (CSEAM631P)
Team Members: Sasmita, Joshiny, Vedant, Rachel
"""
import sys
from classroom_bot.engine import ChatbotEngine

def print_help(engine: ChatbotEngine):
    print("\n" + "=" * 70)
    print("SUPPORTED QUERIES & MEMBER MAPPING (21 INTENTS)")
    print("=" * 70)
    current_member = None
    for r in engine.rules:
        if r["member"] != current_member:
            current_member = r["member"]
            print(f"\n[{current_member.upper()}'S QUESTIONS]")
        print(f"  Q{r['id']:2d}: {r['name']:48s} | Pattern: {r['pattern'][:28]}...")
    print("=" * 70 + "\n")

def main():
    engine = ChatbotEngine()
    debug_mode = False

    print("=" * 75)
    print("  CHRIST (Deemed to be University) - School of Engineering & Technology")
    print("        DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING (B.Tech CS AIML-C)")
    print("            CLASSROOM ASSISTANCE BOT (Python RE Rule-Based)")
    print("=" * 75)
    print("Team: Sasmita | Joshiny | Vedant | Rachel")
    print("Commands: 'exit' or 'quit' to leave | 'help' for all intents | 'debug' to toggle regex inspector")
    print("-" * 75)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting bot. Goodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Bot: Goodbye! Have a great day at CHRIST University.")
            break

        if user_input.lower() == "help":
            print_help(engine)
            continue

        if user_input.lower() == "debug":
            debug_mode = not debug_mode
            status = "ENABLED" if debug_mode else "DISABLED"
            print(f"Bot: [Debug Inspector {status}]")
            continue

        result = engine.process_query(user_input)

        if debug_mode and result["matched"]:
            print("\n  [DEBUG INFO]")
            print(f"  • Member : {result['member']}")
            print(f"  • Intent : Q{result['id']} - {result['intent']}")
            print(f"  • Pattern: {result['pattern']}")
            print(f"  • Groups : {result['groups']}")
            print("  " + "-" * 50)

        print(f"\nBot:\n{result['response']}")

if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Create `test_chatbot.py` for automated validation**

```python
# test_chatbot.py
"""Automated end-to-end verification script for all 21 intents."""
import unittest
from classroom_bot.engine import ChatbotEngine

class TestChatbotEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ChatbotEngine()

    def test_all_21_intents_recognized(self):
        test_queries = [
            # Sasmita (5)
            (1, "where is our classroom", "Sasmita"),
            (5, "what is our timetable", "Sasmita"),
            (8, "what are the open electives", "Sasmita"),
            (14, "when are the cias", "Sasmita"),
            (17, "give me the syllabus for ai", "Sasmita"),
            # Joshiny (5)
            (2, "who is our class teacher", "Joshiny"),
            (6, "where is prof saravanan cabin", "Joshiny"),
            (9, "who enrolled in global elective quantum computing", "Joshiny"),
            (15, "who is our sports representative", "Joshiny"),
            (20, "who is our hod", "Joshiny"),
            # Vedant (5)
            (3, "who is our cr", "Vedant"),
            (7, "what are the global electives", "Vedant"),
            (10, "who selected open elective digital marketing", "Vedant"),
            (11, "what is honours program", "Vedant"),
            (16, "when are our exams", "Vedant"),
            # Rachel (6)
            (4, "how many students are in our class", "Rachel"),
            (12, "what are the minors", "Rachel"),
            (13, "what certificate programs are available", "Rachel"),
            (18, "who teaches ai", "Rachel"),
            (19, "how many credits does ai have", "Rachel"),
            (21, "who is my mentor for roll 15", "Rachel"),
        ]

        for q_id, query, expected_member in test_queries:
            with self.subTest(query=query, q_id=q_id):
                result = self.engine.process_query(query)
                self.assertTrue(result["matched"], f"Query '{query}' failed to match!")
                self.assertEqual(result["id"], q_id)
                self.assertEqual(result["member"], expected_member)
                self.assertTrue(len(result["response"]) > 10)

    def test_fallback_unrecognized(self):
        result = self.engine.process_query("What is the weather on Mars today?")
        self.assertFalse(result["matched"])
        self.assertIn("couldn't recognize", result["response"])

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 4: Run all test suites**

Run: `python -m unittest discover tests`
Run: `python test_chatbot.py`
Expected: ALL TESTS PASS

- [ ] **Step 5: Commit**

```bash
git add classroom_bot/engine.py chatbot.py test_chatbot.py
git commit -m "feat: implement central chatbot engine, interactive CLI, and comprehensive test suite"
```

---

### Task 7: CIA Problem-Solving Report & Member-Wise Submission Documents

**Files:**
- Create: `docs/problem_solving_report.md`
- Create: `docs/members/Sasmita_Questions_RE.md`
- Create: `docs/members/Joshiny_Questions_RE.md`
- Create: `docs/members/Vedant_Questions_RE.md`
- Create: `docs/members/Rachel_Questions_RE.md`

- [ ] **Step 1: Create `docs/problem_solving_report.md`**
Write a comprehensive report covering:
  - Title, Course details, Team details.
  - Domain Identification & Problem Definition (Classroom Assistance Bot).
  - System Architecture & Pipeline with ASCII diagram.
  - Demonstration of All Required RE Concepts with code snippets (`re.search`, `re.match`, `re.sub`, `re.split`, character classes, quantifiers, named capturing groups).
  - Complete 21-intent rule mapping table.
  - Sample test execution transcript.
  - Viva preparation Q&A for faculty evaluation.

- [ ] **Step 2: Create individual member documents in `docs/members/`**
Each document must contain:
  - Student Name & Register Number placeholder.
  - Assigned 5 (or 6) Problem Statements & Questions.
  - Detailed Regular Expression patterns.
  - RE Concepts used (quantifiers, capturing groups, etc.).
  - Extracted variables and dynamic chatbot responses.
  - Sample test queries and outputs.

- [ ] **Step 3: Verify and commit all documentation**

```bash
git add docs/problem_solving_report.md docs/members/
git commit -m "docs: add problem solving report and member-wise submission documents"
```

---

### Task 8: Verification, Test Run & Demonstration Confirmation

**Files:**
- Test execution logs: verified via CLI

- [ ] **Step 1: Run complete automated test suite**

Run: `python test_chatbot.py`
Expected: 2 passed, 21 subtests all OK.

- [ ] **Step 2: Verify CLI execution in interactive mode**

Run: `python chatbot.py` with mock inputs (`where is our classroom`, `who is our class teacher`, `give me the syllabus for ai`, `debug`, `help`, `quit`).

- [ ] **Step 3: Confirm bot is running and prompt user for real data**

Present the running bot confirmation to the user and request any real Christ University names/rooms if they wish to update the mock data.
