CIA1- COMPONENT 1
Name: Sasmita
Group No: 6

---

### Question 1: Classroom Location Retrieval
* **Questions**:
  1. Where is our classroom?
  2. Which room is our class in?
  3. Tell me our class location.
  4. What room is our class?
  5. Classroom location please.
* **Rules**:
  * Match user inquiries asking for the physical room number, floor, or building location of the section.
  * Retrieve classroom venue details (Room 412, 4th Floor, Block II) from the class information database.
  * Dynamically format and return the classroom location details.
* **Regular Expressions**:
  ```python
  r'\b(?:where\s+is\s+our\s+classroom|which\s+room|class\s+location|classroom|class\s*room)\b'
  ```

---

### Question 2: Class Timetable Retrieval
* **Questions**:
  1. What is our timetable?
  2. Show today's class schedule.
  3. Show monday schedule.
  4. What is our routine for wednesday?
  5. What is the class timetable on friday?
* **Rules**:
  * Identify requests for daily class schedules or the complete weekly timetable.
  * Use the named capturing group `(?P<day>...)` to extract the specific weekday requested (e.g., monday, tuesday).
  * If a day is captured, dynamically look up and return that day's lecture slots. If omitted, return the complete weekly timetable.
* **Regular Expressions**:
  ```python
  r'\b(?:timetable|schedule|routine)(?:\s+(?:for|on)?\s*(?P<day>monday|tuesday|wednesday|thursday|friday|today))?\b'
  ```

---

### Question 3: Open Elective Information Retrieval
* **Questions**:
  1. What are the open electives?
  2. Which open electives can I choose?
  3. Tell me about open electives.
  4. List open electives.
  5. Available open electives.
* **Rules**:
  * Match queries asking for the university open elective course catalog.
  * Extract all available open elective course offerings, course codes, offering schools/departments, and credit values.
  * Generate and display a structured listing of open electives.
* **Regular Expressions**:
  ```python
  r'\b(?:what\s+are|which|explain|tell\s+me\s+about|list|show|available)\s+(?:the\s*)?open\s+electives?\b|^\s*(?:the\s*)?open\s+electives?\s*$'
  ```

---

### Question 4: CIA Schedule Information Retrieval
* **Questions**:
  1. When are the CIAs?
  2. What is the CIA schedule?
  3. When is CIA 1?
  4. When is CIA 2?
  5. Tell me CIA 3 submission dates.
* **Rules**:
  * Identify student queries regarding Continuous Internal Assessment (CIA) test schedules and evaluation windows.
  * Capture the specific assessment number using character class `[1-3]` and named capturing group `(?P<cia_num>[1-3])`.
  * If a CIA number is extracted, return the exact examination dates and mark weightage for that assessment; otherwise, display the complete semester CIA timeline.
* **Regular Expressions**:
  ```python
  r'\b(?:when (?:are|is)|what is)?\s*(?:the\s*)?cias?\s*(?P<cia_num>[1-3])?\s*(?:schedule|dates?|exam)?\b'
  ```

---

### Question 5: Subject Syllabus Retrieval
* **Questions**:
  1. Give me the syllabus for AI.
  2. What are the units in DBMS?
  3. Show Unit 2 of AI syllabus.
  4. What is the syllabus of NLP?
  5. Show Unit 1 for ML.
* **Rules**:
  * Match queries requesting curriculum units or course syllabus details.
  * Extract the optional unit number using `(?P<unit>\d+)` and the mandatory subject code using `(?P<subject>\w+)`.
  * If a unit number is provided, return that specific unit's topics; if omitted, list all five units for the requested subject.
* **Regular Expressions**:
  ```python
  r'\b(?:syllabus|units?)(?:\s+(?P<unit>\d+))?\s*(?:of|for|in)\s+(?P<subject>\w+)\b'
  ```
