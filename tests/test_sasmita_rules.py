# tests/test_sasmita_rules.py
import unittest
from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.rules.sasmita import match_sasmita_rule

class TestSasmitaRules(unittest.TestCase):
    def test_q1_classroom_location(self):
        for q in ["where is our classroom", "which room is our class in", "tell me our class location"]:
            resp = match_sasmita_rule(q, KNOWLEDGE_BASE)
            self.assertIsNotNone(resp, f"Query '{q}' failed to match Q1")
            self.assertIn("Room 412", resp)

    def test_q5_timetable(self):
        resp_full = match_sasmita_rule("what is our timetable", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_full)
        self.assertIn("Monday", resp_full)
        resp_mon = match_sasmita_rule("show monday schedule", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_mon)
        self.assertIn("09:00 AI", resp_mon)

    def test_q8_open_electives(self):
        resp = match_sasmita_rule("what are the open electives", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("Digital Marketing", resp)

    def test_q14_cia_schedule(self):
        resp_all = match_sasmita_rule("when are the cias", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_all)
        self.assertIn("CIA 1", resp_all)
        resp_cia2 = match_sasmita_rule("when is cia 2", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_cia2)
        self.assertIn("March 23", resp_cia2)

    def test_q17_syllabus(self):
        resp_all = match_sasmita_rule("give me the syllabus for ai", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_all)
        self.assertIn("Unit 1", resp_all)
        resp_unit2 = match_sasmita_rule("show unit 2 of ai syllabus", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_unit2)
        self.assertIn("Knowledge Representation", resp_unit2)

if __name__ == "__main__":
    unittest.main()
