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
