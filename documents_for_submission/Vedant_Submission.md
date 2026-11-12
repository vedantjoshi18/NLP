CIA1- COMPONENT 1
Name: Vedant
Group No: 6

---

### Question 1: Class Representative Information Retrieval
* **Questions**:
  1. Who is our CR?
  2. Who are the class representatives?
  3. Who represents our class?
  4. Class rep
  5. Class representative
* **Rules**:
  * Match queries asking for the identity and contact channels of elected Class Representatives (CRs).
  * Use the named capturing group `(?P<rep>...)` to identify representative keywords.
  * Retrieve and display class representatives' names, official student emails, and roll numbers.
* **Regular Expressions**:
  ```python
  r'\b(?:who\s+(?:is|are|represents)\s+(?:our\s+)?)?(?P<rep>class\s+representatives?|class\s+reps?|\bcr\b)\b|\bwho\s+represents\s+our\s+class\b'
  ```

---

### Question 2: Global Elective Information Retrieval
* **Questions**:
  1. What are the global electives?
  2. Which global electives are available?
  3. Explain global electives.
  4. Global electives
  5. What global electives can we take?
* **Rules**:
  * Identify requests for the global elective course catalog.
  * Extract all available global elective titles, course codes, offering engineering departments, and credit values.
  * Format and present the global elective catalog list.
* **Regular Expressions**:
  ```python
  r'\b(?:what\s+are|which|explain|tell\s+me\s+about|list|show|available)\s+(?:the\s*)?global\s+electives?\b|^\s*(?:the\s*)?global\s+electives?\s*$'
  ```

---

### Question 3: Open Elective Subject and Student Enrollment Retrieval
* **Questions**:
  1. Who selected Open Elective Data Modeling and Visualization?
  2. How many students are taking open elective?
  3. List open elective enrollments.
  4. Which open elective did Rachel take?
  5. What open elective is Vedant enrolled in?
* **Rules**:
  * Match queries seeking enrollment statistics, registered peer student lists, or individual student open elective selections verified from `Open Elective List.xlsx`.
  * Support lookup by elective title via named group `(?P<elective>[a-zA-Z\s]+)?` OR lookup by student name/regno via named group `(?P<student_query>[a-zA-Z\s\d]+?)`.
  * If a student name is captured (e.g. Rachel, Vedant), return their specific elective allotment and register number. If an elective title is captured, return the total registered count and student roster. If a general count/summary is asked, return enrollments across all 5 open electives.
* **Regular Expressions**:
  ```python
  r'\b(?:(?:(?:list|show)\s+)?open\s+electives?\s+enrollments?|(?:enrollment|enrolled(?:\s+in)?|(?:who\s+)?selected|who\s+chose|(?:how\s+many\s+)?students?\s+(?:in|(?:are\s+)?taking|take))\s+(?:the\s*)?open\s+electives?\s*(?P<elective>[a-zA-Z\s]+)?|(?:open\s+elective\s+(?:of|for)|(?:which|what)\s+open\s+elective\s+(?:did|is))\s+(?P<student_query>[a-zA-Z\s\d]+?)(?:\s+take|\s+choose|\s+enrolled(?:\s+in)?|\?|$))\b'
  ```

---

### Question 4: Honours Program Information Retrieval
* **Questions**:
  1. What is honours?
  2. How can I pursue honours?
  3. Tell me about the honours program.
  4. Honours program
  5. What is the eligibility for honours?
* **Rules**:
  * Match user questions regarding the B.Tech Honours degree track.
  * Fetch requirements: 20 extra credits over Semesters 5 to 8, CGPA cutoff requirement (minimum 7.5 CGPA with zero backlogs), Wednesday 11:00 - 14:00 timetable slot, and 6th semester honours courses (Cloud Architecture & DevSecOps, Quantum Computing Fundamentals) from the official timetable.
  * Format and output the honours program guidelines.
* **Regular Expressions**:
  ```python
  r'\b(?:what\s+is|how\s+(?:can\s+i\s+)?pursue|tell\s+me\s+about|details\s+on|eligibility\s+for)?\s*(?:the\s*)?honours?(?:\s+program|\s+courses?|\s+subjects?)?\b'
  ```

---

### Question 5: Examination Schedule Retrieval
* **Questions**:
  1. When are our exams?
  2. What is the examination timetable?
  3. When is the next exam?
  4. When is end sem?
  5. Tell me the exam schedule.
* **Rules**:
  * Identify requests for university examination dates and timings.
  * Dynamically capture the exam category using named group `(?P<exam_type>end\s+sem|final|mid\s+sem|examination|exam)`.
  * Fetch and return end-semester theory examination windows (May 5 - May 22, 2026), practical / lab assessment dates (April 20 - April 28, 2026), and exam time slots.
* **Regular Expressions**:
  ```python
  r'\b(?:when\s+(?:are|is)|what\s+is)\s+(?:the\s+|our\s+)?(?:next\s+)?(?P<exam_type>end\s+sem|final|mid\s+sem|examination|exam)s?\s*(?:schedule|timetable|dates?)?\b'
  ```
