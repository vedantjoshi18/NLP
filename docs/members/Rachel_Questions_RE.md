# Member-Wise Submission Document: Rachel
**Course**: Natural Language Programming (CSEAM631P)  
**Programme**: B.Tech CS AIML-C, School of Engineering and Technology, CHRIST (Deemed to be University)  
**Activity**: CIA Component - 1 (Question 1) - Rule-Based Chatbot Using Python RE  
**Team Member**: Rachel  
**Register No**: [Enter Register Number Here]  
**Application Domain**: Classroom Assistance Bot  

---

## Member Contribution Summary
Rachel contributed **6 unique problem statements and query intents** addressing class student strength, minor degree programs, certificate programs, subject faculty assignment, course credits, and faculty mentor-mentee mapping:
1. **Q4**: Class Strength Information Retrieval
2. **Q12**: Minor Program Information Retrieval
3. **Q13**: Certificate Program Information Retrieval
4. **Q18**: Subject Faculty Identification
5. **Q19**: Course Credit Information Retrieval
6. **Q21**: Mentor and Mentee Information Retrieval

---

## Detailed Question & Regular Expression Breakdown

### Question 1: Class Strength Information Retrieval (Q4)
* **Problem Statement**: Providing total student count and demographic distribution for Section C.
* **Sample User Queries**:
  * *"How many students are in our class?"*
  * *"What's our class strength?"*
  * *"How many people are in our section?"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:how\s+many\s+students|class\s+strength|strength\s+of\s+(?:the\s+|our\s+)?class|how\s+many\s+people)\b'
  ```
* **RE Concepts Applied**:
  * Phrase Alternation `|`: Captures varied conversational phrases used by students and teachers.
  * Word boundary `\b`: Avoids partial match issues.
* **Dynamic Information Extraction & Handling**:
  Queries the `class_info['strength']` record and dynamically displays total students, boys, and girls.
* **Expected Chatbot Response**:
  ```text
  📊 [Class Strength]
  Total Students: 68 (Boys: 42, Girls: 26)
  ```

---

### Question 2: Minor Program Information Retrieval (Q12)
* **Problem Statement**: Explaining interdisciplinary minor programs, credit structures, and eligible tracks.
* **Sample User Queries**:
  * *"What are the minors?"*
  * *"How do minors work?"*
  * *"Which minor programs are available?"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:what\s+(?:are|is)|how\s+do|which|tell\s+me\s+about)?\s*(?:the\s*)?minors?(?:\s+program)?\b'
  ```
* **RE Concepts Applied**:
  * Plural quantifier `s?`: Matches both *"minor"* and *"minors"*.
  * Grouping `(?:what (?:are|is)|...)`: Handles different interrogative pronouns.
* **Dynamic Information Extraction & Handling**:
  Pulls minor degree details from `programs['minors']` and lists required credits (18) and available tracks.
* **Expected Chatbot Response**:
  ```text
  🎓 [Interdisciplinary Minor Degree]
  • Requirement: 18 Credits across 4 semesters
  • Tracks Available: Data Science (Stats Dept), Internet of Things (ECE Dept), Financial Technology (Commerce)
  • Eligibility: Minimum 7.0 CGPA
  ```

---

### Question 3: Certificate Program Information Retrieval (Q13)
* **Problem Statement**: Guiding students to industry-aligned value-added certification courses offered by the department.
* **Sample User Queries**:
  * *"What certificate programs are available?"*
  * *"How can I pursue a certificate?"*
  * *"Tell me about certificate courses"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:what|how|tell\s+me\s+about|which)?\s*certificate\s*(?:programs?|courses?)\b'
  ```
* **RE Concepts Applied**:
  * Synonymous noun matching `(?:programs?|courses?)`: Matches both "certificate program" and "certificate course".
  * Quantifiers `?`: Matches singular and plural forms flexibly.
* **Dynamic Information Extraction & Handling**:
  Loads active industry partner programs from `programs['certificate']` (AWS, Polygon, NVIDIA DLI).
* **Expected Chatbot Response**:
  ```text
  📜 [Value Added Certificate Courses] (Duration: 30 Contact Hours (1 Credit equivalent))
  Available Offerings:
    • Generative AI & LLM Application Development (Industry Partner: AWS)
    • Full-Stack Web3 & Blockchain (Industry Partner: Polygon)
    • Applied Deep Learning for Computer Vision (Industry Partner: NVIDIA DLI)
  ```

---

### Question 4: Subject Faculty Identification (Q18)
* **Problem Statement**: Identifying the professor in charge for any given subject code or acronym.
* **Sample User Queries**:
  * *"Who teaches AI?"*
  * *"Which faculty handles DBMS?"*
  * *"Who is our subject teacher for ML?"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:who\s+teaches|which\s+faculty\s+handles|subject\s+teacher\s+for|who\s+takes)\s+(?P<subject>\w+)\b'
  ```
* **RE Concepts Applied**:
  * Word sequence `\w+`: Extracts alphanumeric subject keys.
  * Named Capturing Group `(?P<subject>\w+)`: Dynamically extracts the subject token into a named slot.
* **Dynamic Information Extraction & Handling**:
  Extracts `subject`, checks dictionary presence in `subjects`, and retrieves the designated faculty member's name.
* **Expected Chatbot Response**:
  ```text
  👨‍🏫 [Faculty In-Charge]
  Subject: Artificial Intelligence (AI)
  Faculty: Dr. K. Saravanan
  ```

---

### Question 5: Course Credit Information Retrieval (Q19)
* **Problem Statement**: Giving credit weightage and lecture-tutorial-practical (L-T-P) distribution for academic courses.
* **Sample User Queries**:
  * *"How many credits does AI have?"*
  * *"What are the credits for DBMS?"*
  * *"Credits for ML"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:how\s+many\s+credits(?:\s+does)?|what\s+are\s+the\s+credits\s+for|credits?\s+(?:for|of)|credit\s+value\s+of)\s+(?P<subject>\w+)\b'
  ```
* **RE Concepts Applied**:
  * Auxiliary verb matching `(?:\s+does)?`: Correctly handles questions like *"how many credits does AI have"*.
  * Named Capturing Group `(?P<subject>\w+)`: Dynamically extracts the subject code.
* **Dynamic Information Extraction & Handling**:
  Looks up the subject in `subjects` and formats credits and contact-hour breakdown.
* **Expected Chatbot Response**:
  ```text
  🎯 [Course Credit Details]
  Subject: Artificial Intelligence (AI)
  Credits: 4 Credits (3 Lectures + 2 Practical Hours (L-T-P: 3-0-2))
  ```

---

### Question 6: Mentor and Mentee Information Retrieval (Q21)
* **Problem Statement**: Facilitating mentor identification by student roll number, or displaying mentee lists assigned to specific professors.
* **Sample User Queries**:
  * *"Who is my mentor for roll 15?"*
  * *"Which students are under Professor Deepa?"*
  * *"Who is my mentor?"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:mentor\s+(?:for|of)\s*(?:roll\s*)?(?P<roll>\d+)|(?:mentees?|students?)\s+(?:are\s+)?(?:under|of)\s*(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+)|who\s+is\s+my\s+mentor)\b'
  ```
* **RE Concepts Applied**:
  * Multi-branch Named Capturing Groups:
    * `(?P<roll>\d+)`: Captures integer student roll number using special sequence `\d+`.
    * `(?P<faculty>[a-zA-Z\s]+)`: Captures faculty surname using character class `[a-zA-Z\s]`.
  * Alternation `|`: Selects appropriate branch depending on whether roll number or faculty name was queried.
* **Dynamic Information Extraction & Handling**:
  - If `roll` is present: Computes which range `[start, end]` contains the roll number and outputs the assigned mentor and cabin.
  - If `faculty` is present: Locates the faculty's mentee allocation and prints their roll number bracket.
* **Expected Chatbot Response (By Roll Number)**:
  ```text
  🧑‍🏫 [Mentor Allocation]
  Roll Number: 15
  Assigned Mentor: Dr. K. Saravanan (Cabin 305, Block II)
  ```
* **Expected Chatbot Response (By Faculty Name)**:
  ```text
  🧑‍🏫 [Mentee List]
  Faculty: Prof. Deepa V.
  Mentees: Roll 24 to 46 (Total: 23 students)
  Cabin: Cabin 210, Block II
  ```

---

## Verification & Execution Evidence
All 6 rules were integrated into `classroom_bot/rules/rachel.py` and unit tested in `tests/test_rachel_rules.py`.
* Automated test execution status: **100% Passed (6/6 tests)**.
