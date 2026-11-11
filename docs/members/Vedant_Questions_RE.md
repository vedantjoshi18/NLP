# Member-Wise Submission Document: Vedant
**Course**: Natural Language Programming (CSEAM631P)  
**Programme**: B.Tech CS AIML-C, School of Engineering and Technology, CHRIST (Deemed to be University)  
**Activity**: CIA Component - 1 (Question 1) - Rule-Based Chatbot Using Python RE  
**Team Member**: Vedant  
**Register No**: [Enter Register Number Here]  
**Application Domain**: Classroom Assistance Bot  

---

## Member Contribution Summary
Vedant contributed **5 unique problem statements and query intents** covering student class representation, global elective catalog details, open elective student enrollment statistics, honours degree curriculum, and university examination timetables:
1. **Q3**: Class Representative Information Retrieval
2. **Q7**: Global Elective Information Retrieval
3. **Q10**: Open Elective Subject and Student Enrollment Retrieval
4. **Q11**: Honours Program Information Retrieval
5. **Q16**: Examination Schedule Retrieval

---

## Detailed Question & Regular Expression Breakdown

### Question 1: Class Representative (CR) Information (Q3)
* **Problem Statement**: Enabling students to look up who the elected Class Representatives are, along with their student email IDs and roll numbers.
* **Sample User Queries**:
  * *"Who is our CR?"*
  * *"Who are the class representatives?"*
  * *"Who represents our class?"*
* **Regular Expression Pattern**:
  ```python
  r'\bwho\s+(?:is|are|represents).*?\b(?P<rep>cr|class\s+representatives?|class\s+reps?|our\s+class)\b'
  ```
* **RE Concepts Applied**:
  * Non-greedy wildcard `.*?`: Allows polite connecting words without swallowing the trailing keyword.
  * Named Capturing Group `(?P<rep>...)`: Extracts the representation intent category.
  * Quantifier `?`: Matches singular or plural variations (`representative` vs `representatives`, `rep` vs `reps`).
* **Dynamic Information Extraction & Handling**:
  Fetches the list of CRs from `leadership['cr']` and builds a dynamic directory response.
* **Expected Chatbot Response**:
  ```text
  👥 [Class Representatives (CR)]
    • Rahul M. (Roll: 2362001) - rahul.m@cs.christuniversity.in
    • Ananya Sharma (Roll: 2362002) - ananya.s@cs.christuniversity.in
  ```

---

### Question 2: Global Elective Information Retrieval (Q7)
* **Problem Statement**: Assisting students in discovering the global electives offered in the semester, including credit values and offering engineering departments.
* **Sample User Queries**:
  * *"What are the global electives?"*
  * *"Which global electives are available?"*
  * *"Explain global electives"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:what\s+are|which|explain|tell\s+me\s+about|list|show|available)\s+(?:the\s*)?global\s+electives?\b|^\s*(?:the\s*)?global\s+electives?\s*$'
  ```
* **RE Concepts Applied**:
  * Anchored exact match `^\s*...$`: Handles standalone queries like `"global electives"` directly.
  * Grouping and Alternation `(?:what are|which|explain|...)`: Accurately handles diverse intent starters.
  * Word boundary `\b`: Avoids false matches inside larger compound words.
* **Dynamic Information Extraction & Handling**:
  Iterates over `electives['global']` in the knowledge base and generates an itemized course list.
* **Expected Chatbot Response**:
  ```text
  🌍 [Offered Global Electives]
    • Quantum Computing (GE601) - Dept: Physics/CSE [3 Credits]
    • Robotics And Automation (GE602) - Dept: Mechanical [3 Credits]
    • Cyber Forensics (GE603) - Dept: IT & Cyber [3 Credits]
  ```

---

### Question 3: Open Elective Subject & Student Enrollment Retrieval (Q10)
* **Problem Statement**: Providing enrollment metrics and listing enrolled peer students for university open electives.
* **Sample User Queries**:
  * *"Who selected Open Elective Digital Marketing?"*
  * *"How many students enrolled in open elective?"*
  * *"List open elective enrollments"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:enrollment|enrolled(?:\s+in)?|selected|students?\s+in)\s+(?:the\s*)?open\s+elective\s*(?P<elective>[a-zA-Z\s]+)?\b'
  ```
* **RE Concepts Applied**:
  * Named Capturing Group `(?P<elective>[a-zA-Z\s]+)?`: Dynamically isolates the target open elective name.
  * Optional prepositions and verbs `(?:enrollment|enrolled|selected)`: Broadens coverage for student query phrasing.
* **Dynamic Information Extraction & Handling**:
  Extracts `elective`. If specified, filters open electives dictionary and returns the total tally and sample registered peers. If omitted, returns an overview of all open electives.
* **Expected Chatbot Response**:
  ```text
  📖 [Open Elective Enrollment: Digital Marketing]
  Total Enrolled: 32 students
  Sample Enrolled Students: Aman J., Bhavana K., Chetan L.
  ```

---

### Question 4: Honours Program Information Retrieval (Q11)
* **Problem Statement**: Informing students of eligibility criteria, credit requirements, and registration procedures for the B.Tech Honours program.
* **Sample User Queries**:
  * *"What is honours?"*
  * *"How can I pursue honours?"*
  * *"Tell me about the honours program"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:what\s+is|how\s+(?:can\s+i\s+)?pursue|tell\s+me\s+about|details\s+on|eligibility\s+for)?\s*(?:the\s*)?honours?(?:\s+program)?\b'
  ```
* **RE Concepts Applied**:
  * Word boundary `\b`: Bounds the search strictly to whole words.
  * Optional modal sequences `(?:can\s+i\s+)?`: Accommodates conversational questions (*"how can I pursue..."*).
  * Optional noun suffix `(?:\s+program)?`: Matches both *"honours"* and *"honours program"*.
* **Dynamic Information Extraction & Handling**:
  Loads program specifications from `programs['honours']` and outputs requirements, CGPA threshold (7.5), and registration portal directions.
* **Expected Chatbot Response**:
  ```text
  🎓 [B.Tech Honours in CS AIML]
  • Requirement: 20 extra credits beyond standard curriculum (Semesters 5 to 8 (5 credits per semester))
  • Eligibility: Minimum 7.5 CGPA with zero standing backlogs
  • Registration: Apply via KP Portal during odd semester registration
  ```

---

### Question 5: Examination Schedule Retrieval (Q16)
* **Problem Statement**: Displaying university End Semester theory exam dates, lab/practical assessment windows, and timings.
* **Sample User Queries**:
  * *"When are our exams?"*
  * *"What is the examination timetable?"*
  * *"When is the end sem exam?"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:when\s+(?:are|is)|what\s+is)\s+(?:the\s+|our\s+)?(?P<exam_type>end\s+sem|final|mid\s+sem|examination|exam)s?\s*(?:schedule|timetable|dates?)?\b'
  ```
* **RE Concepts Applied**:
  * Possessive / Article Alternation `(?:the\s+|our\s+)?`: Accommodates both *"when are the exams"* and *"when are our exams"*.
  * Named Capturing Group `(?P<exam_type>...)`: Distinguishes between *"end sem"*, *"final"*, and general *"exam"*.
  * Plural quantifier `s?`: Matches both singular *"exam"* and plural *"exams"*.
* **Dynamic Information Extraction & Handling**:
  Extracts `exam_type` and retrieves end-semester theory exam dates, practical lab windows, and daily session timings.
* **Expected Chatbot Response**:
  ```text
  📋 [Examination Schedule]
  • End Semester Theory Exams: May 5, 2026 to May 18, 2026 (Theory Exams: 9:30 AM - 12:30 PM)
  • Practical / Lab Examinations: April 24, 2026 to April 30, 2026 (Lab Exams)
  ```

---

## Verification & Execution Evidence
All 5 rules were integrated into `classroom_bot/rules/vedant.py` and unit tested in `tests/test_vedant_rules.py`.
* Automated test execution status: **100% Passed (5/5 tests)**.
