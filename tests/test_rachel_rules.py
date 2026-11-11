# tests/test_rachel_rules.py
import unittest
from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.rules.rachel import match_rachel_rule

class TestRachelRules(unittest.TestCase):
    def test_q4_class_strength(self):
        for q in ["how many students are in our class", "what's our class strength", "how many people in our section"]:
            resp = match_rachel_rule(q, KNOWLEDGE_BASE)
            self.assertIsNotNone(resp, f"Query '{q}' failed to match Q4")
            self.assertIn("68", resp)

    def test_q12_minor_program(self):
        resp = match_rachel_rule("what are the minors", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("18", resp)

    def test_q13_certificate_program(self):
        resp = match_rachel_rule("what certificate programs are available", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("30 Contact Hours", resp)

    def test_q18_subject_faculty(self):
        resp_ai = match_rachel_rule("who teaches ai", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_ai)
        self.assertIn("Dr. K. Saravanan", resp_ai)
        resp_dbms = match_rachel_rule("which faculty handles dbms", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_dbms)
        self.assertIn("Prof. Deepa V.", resp_dbms)

    def test_q19_course_credits(self):
        resp_ai = match_rachel_rule("how many credits does ai have", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_ai)
        self.assertIn("4 Credits", resp_ai)
        resp_dbms = match_rachel_rule("what are the credits for dbms", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_dbms)
        self.assertIn("3 Credits", resp_dbms)

    def test_q21_mentor_mentee(self):
        resp_roll = match_rachel_rule("who is my mentor for roll 15", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_roll)
        self.assertIn("Dr. K. Saravanan", resp_roll)
        resp_prof = match_rachel_rule("which students are under professor deepa", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_prof)
        self.assertIn("Roll 24 to 46", resp_prof)

if __name__ == "__main__":
    unittest.main()
