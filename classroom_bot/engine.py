"""Central Chatbot Engine aggregating all 21 rules."""
import re
from typing import Dict, Any, Optional

from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.preprocessor import preprocess_query
from classroom_bot.rules.sasmita import SASMITA_RULES
from classroom_bot.rules.joshiny import JOSHINY_RULES
from classroom_bot.rules.vedant import VEDANT_RULES
from classroom_bot.rules.rachel import RACHEL_RULES

# Prioritized order to prevent broad catch-alls (e.g. timetable, students)
# from preempting specific intent matches (e.g. CIA/exam schedules, elective enrollment).
RULE_PRIORITY_ORDER = [
    1,                 # Classroom location (matches 'where is our classroom/room/section c')
    14, 16, 21,        # Specific dates: CIA, Exams, Mentoring hour
    10, 9,             # Specific elective enrollment & student lookups
    13, 11, 12,        # Specific academic programs: Certifications, Honours, Minors
    8, 7,              # Elective catalogs: Open, Global
    2, 15, 3, 20,      # Roles & leadership: CT, Sports CR, CR, HOD/Office
    6,                 # Faculty Cabin & Contact (where is Dr/Prof X)
    18, 19, 17,        # Subject specifics: Faculty, Credits, Syllabus
    5, 4,              # General Timetable, Class Strength
]

def get_help_catalog() -> str:
    sep = "=" * 70
    return (
        f"{sep}\n"
        "SUPPORTED QUERIES & QUESTIONS THE BOT CAN ANSWER (21 INTENTS)\n"
        f"{sep}\n\n"
        "[SASMITA'S QUESTIONS]\n"
        "  Q1. Classroom Location Retrieval:\n"
        "      - Where is our classroom?\n"
        "      - Which room is our class in?\n"
        "      - What room is our class?\n"
        "      - Where is section C?\n"
        "      - Class location\n"
        "  Q5. Class Timetable & Subject Schedules:\n"
        "      - What is our timetable?\n"
        "      - Monday schedule (or Tuesday/Wednesday/Thursday/Friday/Saturday)\n"
        "      - Show today's class schedule\n"
        "      - Daywise timetable\n"
        "      - When do we have NLP?\n"
        "      - When do we have AI?\n"
        "      - When is Deep Learning?\n"
        "  Q8. Open Electives Catalog:\n"
        "      - What are the open electives?\n"
        "      - Which open electives can I choose?\n"
        "      - Tell me about open electives\n"
        "      - Available open electives\n"
        "  Q14. CIA Examination Schedule:\n"
        "      - When are the CIAs?\n"
        "      - What is the CIA schedule?\n"
        "      - When is CIA 1?\n"
        "      - When is CIA 2?\n"
        "      - When is CIA 3?\n"
        "  Q17. Subject Syllabus Retrieval:\n"
        "      - Give me the syllabus for NLP\n"
        "      - What are the units in DL?\n"
        "      - Show Unit 2 of AI syllabus\n"
        "      - Syllabus of DIP\n"
        "      - Syllabus for Professional Ethics\n\n"
        "[JOSHINY'S QUESTIONS]\n"
        "  Q2. Class Teacher & Co-Class Teacher Identification:\n"
        "      - Who is our class teacher?\n"
        "      - Who is our co-class teacher?\n"
        "      - Who handles our section?\n"
        "      - Class teacher\n"
        "      - Co class teacher\n"
        "  Q6. Faculty Location & Cabin Contact Retrieval:\n"
        "      - Where is Professor Poongodi's cabin?\n"
        "      - How can I contact Dr Vinodha?\n"
        "      - Where can I find Amos Bortiew?\n"
        "      - Cabin of Dr Jeno\n"
        "      - Where is Dr Kukatlapalli's cabin?\n"
        "  Q9. Global Electives & Student Enrollment:\n"
        "      - What are the global electives?\n"
        "      - Who enrolled in Global Elective Quantum Computing?\n"
        "      - How many students take this global elective?\n"
        "      - Global elective enrollment\n"
        "  Q15. Sports Representative Identification:\n"
        "      - Who is our sports representative?\n"
        "      - Who handles sports for our class?\n"
        "      - Who is the sports CR?\n"
        "      - Sports rep\n"
        "  Q20. Department Leadership & Office Information:\n"
        "      - Who is our HOD?\n"
        "      - Who is the head of department?\n"
        "      - Who is the program coordinator?\n"
        "      - Who is the year coordinator?\n"
        "      - Where is the department office?\n\n"
        "[VEDANT'S QUESTIONS]\n"
        "  Q3. Class Representative (CR) Identification:\n"
        "      - Who is our CR?\n"
        "      - Who are the class representatives?\n"
        "      - Who represents our class?\n"
        "      - Class rep\n"
        "  Q7. Global Electives Catalog:\n"
        "      - What are the global electives?\n"
        "      - Which global electives are available?\n"
        "      - List global electives\n"
        "  Q10. Open Elective Student Enrollment & Student Lookup:\n"
        "      - Who selected Open Elective Data Modeling and Visualization?\n"
        "      - How many students are taking open elective?\n"
        "      - List open elective enrollments\n"
        "      - Which open elective did Rachel take?\n"
        "      - What open elective is Vedant enrolled in?\n"
        "  Q11. Honours Program & Individual Students:\n"
        "      - What is honours?\n"
        "      - How can I pursue honours?\n"
        "      - Tell me about the honours program\n"
        "      - List honours students\n"
        "      - Who is taking Honours in Cyber Security?\n"
        "  Q16. Semester Examination Schedule:\n"
        "      - When are our exams?\n"
        "      - What is the examination timetable?\n"
        "      - When is the next exam?\n"
        "      - When is end sem?\n"
        "      - Exam schedule\n\n"
        "[RACHEL'S QUESTIONS]\n"
        "  Q4. Class Strength & Gender Breakdown:\n"
        "      - How many students are in our class?\n"
        "      - What's our class strength?\n"
        "      - How many people are in our section?\n"
        "      - Class strength\n"
        "      - Total students in our class\n"
        "  Q12. Minor Degree Program & Enrolled Students:\n"
        "      - What are the minors?\n"
        "      - How do minors work?\n"
        "      - Which minor programs are available?\n"
        "      - List minor students\n"
        "  Q13. Value-Added Certifications & Certified Students:\n"
        "      - What certificate programs are available?\n"
        "      - How can I pursue a certificate?\n"
        "      - List certification students\n"
        "      - Who did AWS ML Associate?\n"
        "      - Who completed Azure AI 901?\n"
        "  Q18. Subject Faculty Identification:\n"
        "      - Who teaches AI?\n"
        "      - Who teaches NLP?\n"
        "      - Which faculty handles Deep Learning?\n"
        "      - Who takes Professional Ethics?\n"
        "      - Faculty for Server Integration\n"
        "  Q19. Course Credits & Teaching Hours:\n"
        "      - How many credits does AI have?\n"
        "      - How many credits does NLP have?\n"
        "      - What are the credits for DL?\n"
        "      - Credits for DIP\n"
        "  Q21. Mentor-Mentee Allocation & Mentoring Schedule:\n"
        "      - Who is my mentor for roll 15?\n"
        "      - Which students are under Dr Poongodi?\n"
        "      - Who is my mentor?\n"
        "      - When is mentoring?\n"
        f"{sep}"
    )

class ChatbotEngine:
    def __init__(self, kb: Optional[Dict[str, Any]] = None):
        self.kb = kb or KNOWLEDGE_BASE
        all_rules = SASMITA_RULES + JOSHINY_RULES + VEDANT_RULES + RACHEL_RULES
        rule_map = {r["id"]: r for r in all_rules}
        # Order rules by semantic specificity
        self.rules = [rule_map[rid] for rid in RULE_PRIORITY_ORDER if rid in rule_map]

    def get_fallback_response(self, cleaned_query: str) -> str:
        return (
            "I'm sorry, I couldn't recognize your query.\n"
            "Here are some questions you can ask me:\n"
            "  - 'Where is our classroom?' (Sasmita - Q1)\n"
            "  - 'Who is our class teacher?' (Joshiny - Q2)\n"
            "  - 'Who is our CR?' (Vedant - Q3)\n"
            "  - 'How many students are in our class?' (Rachel - Q4)\n"
            "  - 'Show Monday schedule' (Sasmita - Q5)\n"
            "  - 'List honours students' (Vedant - Q11)\n"
            "  - 'List certification students' (Rachel - Q13)\n"
            "  - 'What is the syllabus for NLP?' (Sasmita - Q17)\n"
            "  - 'Who teaches Deep Learning?' (Rachel - Q18)\n"
            "Type 'help' to see all questions the bot can answer across all 21 intents."
        )

    def process_query(self, raw_input: str) -> Dict[str, Any]:
        cleaned = preprocess_query(raw_input)
        if not cleaned:
            return {
                "matched": False,
                "id": None,
                "intent": None,
                "member": None,
                "pattern": None,
                "groups": {},
                "response": "Please enter a question or query. Type 'help' for all questions the bot can answer.",
            }

        # Check for help command
        if cleaned in ["help", "commands", "menu"] or re.search(r'^(?:help|what\s+can\s+you\s+answer|list\s+questions)$', cleaned):
            return {
                "matched": True,
                "id": 0,
                "intent": "Help Catalog",
                "member": "System",
                "pattern": r'\bhelp\b',
                "groups": {},
                "response": get_help_catalog(),
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
