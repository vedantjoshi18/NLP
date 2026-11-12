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
  5. Where is section C?
* **Rules**:
  * Match user inquiries asking for the physical room number, floor, or building location of Section C.
  * Retrieve classroom venue details (Room 312, Ground Floor, GF-B3) from the class information database verified from the 6th Semester Timetable.
  * Dynamically format and return the classroom location details.
* **Regular Expressions**:
  ```python
  r'\b(?:where\s+(?:is|are|do\s+we\s+have)\s+(?:our\s+)?(?:classroom|class\s*room|class|section\s*c|lectures?)|which\s+room|what\s+room|class\s+location|classroom|class\s*room)\b'
  ```

---

### Question 2: Class Timetable Retrieval
* **Questions**:
  1. What is our timetable?
  2. Show today's class schedule.
  3. Monday schedule
  4. Timetable for Tuesday
  5. When do we have AI?
  6. When do we have NLP?
* **Rules**:
  * Identify requests for daily class schedules, specific subject timing slots, or the complete weekly timetable.
  * Use named capturing groups `(?P<sched_subj>[a-zA-Z\s]+?)` for subject-level time queries ("When do we have NLP?"), and `(?P<day_pre>...)` / `(?P<day_post>...)` for day-wise queries.
  * If a subject is captured, dynamically look up and return all scheduled weekly slots from the official timetable. If a day is captured, return that day's lecture slots. If omitted, return the complete weekly timetable.
* **Regular Expressions**:
  ```python
  r'\b(?:when\s+(?:do\s+we\s+have|is)\s+(?P<sched_subj>[a-zA-Z\s]+?)(?:\s+class|\s+lecture)?$|(?P<day_pre>monday|tuesday|wednesday|thursday|friday|saturday|today)\s+(?:timetable|schedule|routine)|(?:timetable|schedule|routine)(?:\s+(?:for|on)?\s*(?P<day_post>monday|tuesday|wednesday|thursday|friday|saturday|today))?)\b'
  ```

---

### Question 3: Open Elective Information Retrieval
* **Questions**:
  1. What are the open electives?
  2. Which open electives can I choose?
  3. Tell me about open electives.
  4. Open electives
  5. Available open electives.
* **Rules**:
  * Match queries asking for the university open elective course catalog.
  * Extract all available open elective course offerings verified from `Open Elective List.xlsx`: Data Modeling and Visualization, Prompt Engineering, Introduction to Ethical Hacking, Computer Vision, and Generative AI, along with offering faculty, credits, and student enrollment totals.
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
  1. Give me the syllabus for NLP.
  2. What are the units in DL?
  3. Show Unit 2 of AI syllabus.
  4. Syllabus of DIP
  5. Syllabus for Professional Ethics.
* **Rules**:
  * Match queries requesting curriculum units or course syllabus details.
  * Extract the optional unit number using `(?P<unit>\d+)` and the subject code/title using `(?P<subject>[a-zA-Z\s]+?)`.
  * If a unit number is provided, return that specific unit's topics; if omitted, list all five units for the requested subject across all current 6th semester subjects (NLP, DL, DIP, PE, SIR, SLP, AEC).
* **Regular Expressions**:
  ```python
  r'\b(?:syllabus|units?)(?:\s+(?P<unit>\d+))?\s*(?:of|for|in)\s+(?P<subject>[a-zA-Z\s]+?)(?:\s+syllabus|\?|$)\b'
  ```
