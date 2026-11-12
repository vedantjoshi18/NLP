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
            (10, "who selected open elective data modeling and visualization", "Vedant"),
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
                self.assertTrue(result["matched"], f"Query '{query}' failed to match intent Q{q_id}!")
                self.assertEqual(result["id"], q_id, f"Query '{query}' matched wrong intent Q{result['id']} instead of Q{q_id}")
                self.assertEqual(result["member"], expected_member)
                self.assertTrue(len(result["response"]) > 10)

    def test_fallback_unrecognized(self):
        result = self.engine.process_query("What is the weather on Mars today?")
        self.assertFalse(result["matched"])
        self.assertIn("couldn't recognize", result["response"])

if __name__ == "__main__":
    unittest.main()
