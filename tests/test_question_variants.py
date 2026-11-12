"""Test suite testing all natural language variants for all 21 intents."""
import unittest
from classroom_bot.engine import ChatbotEngine

class TestQuestionVariants(unittest.TestCase):
    def setUp(self):
        self.engine = ChatbotEngine()

    def assert_intent(self, query: str, expected_id: int):
        result = self.engine.process_query(query)
        self.assertTrue(result["matched"], f"Query '{query}' failed to match any rule!")
        self.assertEqual(result["id"], expected_id, f"Query '{query}' matched Q{result['id']} instead of Q{expected_id}")

    # Q1: Classroom Location
    def test_q1_variants(self):
        variants = [
            "Where is our classroom?",
            "Which room is our class in?",
            "Tell me our class location.",
            "What room is our class?",
            "Where is section C?",
            "Classroom",
            "Class location",
            "Where do we have our class?",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 1)

    # Q2: Class Teacher & Co-Class Teacher
    def test_q2_variants(self):
        variants_ct = [
            "Who is our class teacher?",
            "Who handles our section?",
            "Who is the class teacher for Section C?",
            "Class teacher",
        ]
        for q in variants_ct:
            with self.subTest(q=q):
                res = self.engine.process_query(q)
                self.assertEqual(res["id"], 2)
                self.assertIn("Poongodi", res["response"])

        variants_co = [
            "Who is our co-class teacher?",
            "Who is our co class teacher?",
            "Co class teacher",
        ]
        for q in variants_co:
            with self.subTest(q=q):
                res = self.engine.process_query(q)
                self.assertEqual(res["id"], 2)
                self.assertIn("Jeno", res["response"])

    # Q3: Class Representatives
    def test_q3_variants(self):
        variants = [
            "Who is our CR?",
            "Who are the class representatives?",
            "Who represents our class?",
            "Class rep",
            "Class representative",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 3)

    # Q4: Class Strength
    def test_q4_variants(self):
        variants = [
            "How many students are in our class?",
            "What's our class strength?",
            "How many people are in our section?",
            "Class strength",
            "Total students in our class",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 4)

    # Q5: Timetable & Subject Slots
    def test_q5_variants(self):
        variants = [
            "What is our timetable?",
            "Show today's class schedule.",
            "Monday schedule",
            "Timetable for Tuesday",
            "When do we have AI?",
            "When do we have NLP?",
            "When is Deep Learning?",
            "Daywise timetable",
            "Day wise schedule",
            "Show timetable for Wednesday",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 5)

    # Q6: Faculty Location
    def test_q6_variants(self):
        variants = [
            "Where is Professor Poongodi's cabin?",
            "How can I contact Dr Vinodha?",
            "Where can I find Amos Bortiew?",
            "Cabin of Dr Jeno",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 6)

    # Q7: Global Electives Catalog
    def test_q7_variants(self):
        variants = [
            "What are the global electives?",
            "Which global electives are available?",
            "Explain global electives.",
            "Global electives",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 7)

    # Q8: Open Electives Catalog
    def test_q8_variants(self):
        variants = [
            "What are the open electives?",
            "Which open electives can I choose?",
            "Tell me about open electives.",
            "Open electives",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 8)

    # Q9: Global Elective Enrollment
    def test_q9_variants(self):
        variants = [
            "Who has enrolled in Global Elective Quantum Computing?",
            "How many students take this global elective?",
            "Global elective enrollment",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 9)

    # Q10: Open Elective Enrollment
    def test_q10_variants(self):
        variants = [
            "Who selected Open Elective Data Modeling and Visualization?",
            "How many students are taking open elective?",
            "List open elective enrollments.",
            "Which open elective did Rachel take?",
            "What open elective is Vedant enrolled in?",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 10)

    # Q11: Honours Program
    def test_q11_variants(self):
        variants = [
            "What is honours?",
            "How can I pursue honours?",
            "Tell me about the honours program.",
            "Honours program",
            "List honours students",
            "Honours students",
            "Who is taking honours?",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 11)

    # Q12: Minor Program
    def test_q12_variants(self):
        variants = [
            "What are the minors?",
            "How do minors work?",
            "Which minor programs are available?",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 12)

    # Q13: Certificate Program
    def test_q13_variants(self):
        variants = [
            "What certificate programs are available?",
            "How can I pursue a certificate?",
            "Tell me about certificate courses.",
            "Who did AWS ML Associate?",
            "List certification students",
            "Who completed certifications?",
            "Certificate students",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 13)

    # Q14: CIA Schedule
    def test_q14_variants(self):
        variants = [
            "When are the CIAs?",
            "What is the CIA schedule?",
            "When is CIA 1?",
            "When is CIA 2?",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 14)

    # Q15: Sports Rep
    def test_q15_variants(self):
        variants = [
            "Who is our sports representative?",
            "Who handles sports for our class?",
            "Who is the sports CR?",
            "Sports rep",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 15)

    # Q16: Exam Schedule
    def test_q16_variants(self):
        variants = [
            "When are our exams?",
            "What is the examination timetable?",
            "When is the next exam?",
            "When is end sem?",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 16)

    # Q17: Syllabus
    def test_q17_variants(self):
        variants = [
            "Give me the syllabus for NLP.",
            "What are the units in DL?",
            "Show Unit 2 of AI syllabus.",
            "Syllabus of DIP",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 17)

    # Q18: Subject Faculty
    def test_q18_variants(self):
        variants = [
            "Who teaches AI?",
            "Who teaches NLP?",
            "Which faculty handles Deep Learning?",
            "Who takes Professional Ethics?",
            "Faculty for Server Integration",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 18)

    # Q19: Course Credits
    def test_q19_variants(self):
        variants = [
            "How many credits does AI have?",
            "How many credits does NLP have?",
            "What are the credits for DL?",
            "Credits for DIP",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 19)

    # Q20: Department Leadership
    def test_q20_variants(self):
        variants = [
            "Who is our HOD?",
            "Who is the head of department?",
            "Who is the program coordinator?",
            "Who is the year coordinator?",
            "Department office",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 20)

    # Q21: Mentors
    def test_q21_variants(self):
        variants = [
            "Who is my mentor for roll 15?",
            "Which students are under Dr Poongodi?",
            "Who is my mentor?",
            "When is mentoring?",
        ]
        for q in variants:
            with self.subTest(q=q):
                self.assert_intent(q, 21)

    # Help Command
    def test_help_command(self):
        for cmd in ["help", "commands", "menu"]:
            with self.subTest(cmd=cmd):
                res = self.engine.process_query(cmd)
                self.assertTrue(res["matched"])
                self.assertEqual(res["id"], 0)
                self.assertIn("SUPPORTED QUERIES & QUESTIONS THE BOT CAN ANSWER", res["response"])
                self.assertIn("Where is our classroom?", res["response"])

if __name__ == "__main__":
    unittest.main()
