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

class ChatbotEngine:
    def __init__(self, kb: Optional[Dict[str, Any]] = None):
        self.kb = kb or KNOWLEDGE_BASE
        all_rules = SASMITA_RULES + JOSHINY_RULES + VEDANT_RULES + RACHEL_RULES
        rule_map = {r["id"]: r for r in all_rules}
        # Order rules by semantic specificity
        self.rules = [rule_map[rid] for rid in RULE_PRIORITY_ORDER if rid in rule_map]

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
                "id": None,
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
