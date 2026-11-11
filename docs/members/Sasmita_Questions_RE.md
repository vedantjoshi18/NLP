# Member-Wise Submission Document: Sasmita
**Course**: Natural Language Programming (CSEAM631P)  
**Programme**: B.Tech CS AIML-C, School of Engineering and Technology, CHRIST (Deemed to be University)  
**Activity**: CIA Component - 1 (Question 1) - Rule-Based Chatbot Using Python RE  
**Team Member**: Sasmita  
**Register No**: [Enter Register Number Here]  
**Application Domain**: Classroom Assistance Bot  

---

## Member Contribution Summary
Sasmita contributed **5 unique problem statements and query intents** related to classroom infrastructure, academic scheduling, open electives, and curriculum syllabus:
1. **Q1**: Classroom Location Retrieval
2. **Q5**: Class Timetable Retrieval
3. **Q8**: Open Elective Information Retrieval
4. **Q14**: CIA Schedule Information Retrieval
5. **Q17**: Subject Syllabus Retrieval

---

## Detailed Question & Regular Expression Breakdown

### Question 1: Classroom Location Retrieval
* **Problem Statement**: Enabling students and visitors to locate the specific classroom, floor, and block for Section C.
* **Sample User Queries**:
  * *"Where is our classroom?"*
  * *"Which room is our class in?"*
  * *"Tell me our class location."*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:where\s+is\s+our\s+classroom|which\s+room|class\s+location|classroom|class\s*room)\b'
  ```
* **RE Concepts Applied**:
  * Word boundaries `\b`: Ensures matching whole words and prevents partial string collisions.
  * Non-capturing group `(?:...)`: Groups alternative query phrases without memory overhead.
  * Alternation `|`: Matches different natural language ways students ask for the room.
  * Whitespace sequence `\s+`: Accommodates variable spacing between words.
* **Dynamic Information Extraction & Handling**:
  Queries the `class_info` dictionary in the knowledge base and dynamically formats room, floor, and block.
* **Expected Chatbot Response**:
  ```text
  📍 [Classroom Location]
  Our class (6 B.Tech CS AIML-C) is in Room 412, 4th Floor, Block II.
  ```

---

### Question 2: Class Timetable Retrieval (Q5)
* **Problem Statement**: Providing day-wise lecture schedules or the full weekly timetable on demand.
* **Sample User Queries**:
  * *"What is our timetable?"*
  * *"Show monday schedule"*
  * *"Show today's class schedule"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:timetable|schedule|routine)(?:\s+(?:for|on)?\s*(?P<day>monday|tuesday|wednesday|thursday|friday|today))?\b'
  ```
* **RE Concepts Applied**:
  * Named Capturing Group `(?P<day>...)`: Captures the specific day of the week requested by the user into the variable dictionary.
  * Optional group `(?:\s+...)?`: Allows users to ask either for a specific day or for the complete weekly routine.
  * Alternation `|`: Restricts days to valid academic weekdays (`monday|tuesday|...`).
* **Dynamic Information Extraction & Handling**:
  Extracts `match.groupdict().get("day")`. If a day is captured, filters the schedule for that specific day. If omitted, generates the complete weekly schedule dynamically.
* **Expected Chatbot Response (Day-Specific)**:
  ```text
  📅 [Timetable for Monday]
  09:00 AI | 10:00 DBMS | 11:15 NLP | 12:15 Lunch | 01:15-03:15 NLP Lab
  ```
* **Expected Chatbot Response (Full Week)**:
  ```text
  📅 [Weekly Timetable for 6 B.Tech CS AIML-C]
    • Monday   : 09:00 AI | 10:00 DBMS | 11:15 NLP | 12:15 Lunch | 01:15-03:15 NLP Lab
    • Tuesday  : 09:00 ML | 10:00 AI | 11:15 Global Elective | 12:15 Lunch | 01:15-03:15 AI Lab
    • Wednesday: 09:00 Open Elective | 10:00 DBMS | 11:15 ML | 12:15 Lunch | 01:15-03:15 ML Lab
    • Thursday : 09:00 NLP | 10:00 Global Elective | 11:15 AI | 12:15 Lunch | 01:15 Library / Seminar
    • Friday   : 09:00 DBMS | 10:00 ML | 11:15 Open Elective | 12:15 Lunch | 01:15-03:15 Project Work
  ```

---

### Question 3: Open Elective Information Retrieval (Q8)
* **Problem Statement**: Assisting students in exploring available university-wide open electives, offering departments, and credit weights.
* **Sample User Queries**:
  * *"What are the open electives?"*
  * *"Which open electives can I choose?"*
  * *"Tell me about open electives"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:what\s+are|which|explain|tell\s+me\s+about|list|show|available)\s+(?:the\s*)?open\s+electives?\b|^\s*(?:the\s*)?open\s+electives?\s*$'
  ```
* **RE Concepts Applied**:
  * Anchors `^` and `$`: Matches exact short inputs like `"open electives"`.
  * Quantifiers `?`: Matches optional plural forms (`electives?`) and optional prefixes.
  * Non-capturing alternation `(?:...)`: Handles natural query starters (*"what are"*, *"which"*, *"explain"*).
* **Dynamic Information Extraction & Handling**:
  Iterates over the `electives['open']` registry to build a formatted list of course codes, departments, and credits.
* **Expected Chatbot Response**:
  ```text
  🌐 [Available Open Electives]
    • Digital Marketing (OE601) - Offered by School of Business [3 Credits]
    • Financial Literacy (OE602) - Offered by Commerce [3 Credits]
    • Creative Writing (OE603) - Offered by English & Languages [3 Credits]
  ```

---

### Question 4: CIA Schedule Information Retrieval (Q14)
* **Problem Statement**: Providing dates, formats, and deadlines for Continuous Internal Assessment (CIA) tests.
* **Sample User Queries**:
  * *"When are the CIAs?"*
  * *"What is the CIA schedule?"*
  * *"When is CIA 2?"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:when (?:are|is)|what is)?\s*(?:the\s*)?cias?\s*(?P<cia_num>[1-3])?\s*(?:schedule|dates?|exam)?\b'
  ```
* **RE Concepts Applied**:
  * Character Class `[1-3]`: Restricts the assessment number strictly to CIA 1, 2, or 3.
  * Named Capturing Group `(?P<cia_num>[1-3])`: Dynamically isolates the specific CIA number requested.
  * Nested non-capturing groups `(?:...)`: Flexibly accepts variations like *"when are the cias"* vs *"what is the cia 2 date"*.
* **Dynamic Information Extraction & Handling**:
  If `cia_num` is captured, returns the precise date and format for that evaluation. Otherwise, lists the entire semester assessment roadmap.
* **Expected Chatbot Response**:
  ```text
  📝 [CIA 2 Schedule]
  March 23, 2026 to March 28, 2026 (Mid-Sem Written Exam - 50 Marks converted)
  ```

---

### Question 5: Subject Syllabus Retrieval (Q17)
* **Problem Statement**: Retrieving unit-level module topics or the complete curriculum for semester subjects.
* **Sample User Queries**:
  * *"Give me the syllabus for AI"*
  * *"What are the units in DBMS?"*
  * *"Show Unit 2 of AI syllabus"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:syllabus|units?)(?:\s+(?P<unit>\d+))?\s*(?:of|for|in)\s+(?P<subject>\w+)\b'
  ```
* **RE Concepts Applied**:
  * Special sequence `\d+` with Named Group `(?P<unit>\d+)`: Extracts the integer unit number.
  * Word character class `\w+` with Named Group `(?P<subject>\w+)`: Dynamically captures the subject acronym (e.g., `ai`, `dbms`, `nlp`, `ml`).
  * Optional quantifier `?`: Allows queries without a unit number to fetch the complete multi-unit syllabus.
* **Dynamic Information Extraction & Handling**:
  Maps the captured `subject` to knowledge base records. If a `unit` index is provided, bounds checks and displays that unit's exact topic list.
* **Expected Chatbot Response**:
  ```text
  📚 [AI Syllabus - Unit 2]
  Unit 2: Knowledge Representation, First Order Logic, Semantic Networks
  ```

---

## Verification & Execution Evidence
All 5 rules were integrated into `classroom_bot/rules/sasmita.py` and unit tested in `tests/test_sasmita_rules.py`.
* Automated test execution status: **100% Passed (5/5 tests)**.
