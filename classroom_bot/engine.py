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
