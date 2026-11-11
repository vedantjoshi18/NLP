# tests/test_joshiny_rules.py
import unittest
from classroom_bot.knowledge_base import KNOWLEDGE_BASE
from classroom_bot.rules.joshiny import match_joshiny_rule

class TestJoshinyRules(unittest.TestCase):
    def test_q2_class_teacher(self):
        resp_ct = match_joshiny_rule("who is our class teacher", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_ct)
        self.assertIn("Dr. K. Saravanan", resp_ct)
        resp_co = match_joshiny_rule("who is our co-class teacher", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_co)
        self.assertIn("Prof. Deepa V.", resp_co)

    def test_q6_faculty_location(self):
        resp = match_joshiny_rule("where is professor saravanan's cabin", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("Cabin 305", resp)

    def test_q9_global_elective_enrollment(self):
        resp = match_joshiny_rule("who enrolled in global elective quantum computing", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("24 students", resp)

    def test_q15_sports_representative(self):
        resp = match_joshiny_rule("who is our sports representative", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp)
        self.assertIn("Rohan Gowda", resp)

    def test_q20_department_info(self):
        resp_hod = match_joshiny_rule("who is our hod", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_hod)
        self.assertIn("Dr. Balakrishnan R.", resp_hod)
        resp_coord = match_joshiny_rule("who is the program coordinator", KNOWLEDGE_BASE)
        self.assertIsNotNone(resp_coord)
        self.assertIn("Dr. Smitha Rao", resp_coord)

if __name__ == "__main__":
    unittest.main()
