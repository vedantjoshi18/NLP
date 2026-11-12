# tests/test_vedant_rules.py
import unittest
from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.rules.vedant import match_vedant_rule

class TestVedantRules(unittest.TestCase):
    def test_q3_class_representative(self):
        for q in ["who is our cr", "who are the class representatives", "who represents our class"]:
            resp = match_vedant_rule(q, KNOWLEDGE_BASE)
            self.assertIsNotNone(resp, f"Query '{q}' failed to match Q3")
            self.assertIn("Rahul M.", resp)
            self.assertIn("Ananya Sharma", resp)

    def test_q7_global_electives(self):
        resp = match_vedant_rule("what are the global electives", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("Quantum Computing", resp)

    def test_q10_open_elective_enrollment(self):
        resp = match_vedant_rule("who selected open elective data modeling and visualization", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("20 students", resp)

    def test_q11_honours_program(self):
        for q in ["what is honours", "how can i pursue honours", "tell me about the honours program"]:
            resp = match_vedant_rule(q, KNOWLEDGE_BASE)
            self.assertIsNotNone(resp, f"Query '{q}' failed to match Q11")
            self.assertIn("20", resp)

    def test_q16_exam_schedule(self):
        resp = match_vedant_rule("when are our exams", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("May 5, 2026", resp)

if __name__ == "__main__":
    unittest.main()
