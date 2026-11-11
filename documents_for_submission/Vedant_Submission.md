CIA1- COMPONENT 1
Name: Vedant
Group No: 6

---

### Question 1: Class Representative Information Retrieval
* **Questions**:
  1. Who is our CR?
  2. Who are the class representatives?
  3. Who represents our class?
  4. Tell me our CR details.
  5. Who are the class reps for Section C?
* **Rules**:
  * Match queries asking for the identity and contact channels of elected Class Representatives (CRs).
  * Use the named capturing group `(?P<rep>...)` to identify the representative keyword.
  * Retrieve and display both class representatives' full names, official student emails, and roll numbers.
* **Regular Expressions**:
  ```python
  r'\bwho\s+(?:is|are|represents).*?\b(?P<rep>cr|class\s+representatives?|class\s+reps?|our\s+class)\b'
  ```

---

### Question 2: Global Elective Information Retrieval
* **Questions**:
  1. What are the global electives?
  2. Which global electives are available?
  3. Explain global electives.
  4. List global electives.
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
  1. Who selected Open Elective Digital Marketing?
  2. How many students are taking open elective?
  3. List open elective enrollments for Financial Literacy.
  4. Who enrolled in open elective Creative Writing?
  5. Show students in open elective.
* **Rules**:
  * Match queries seeking enrollment statistics and registered peer student lists for open electives.
  * Extract the elective title using named capturing group `(?P<elective>[a-zA-Z\s]+)?`.
  * If a specific open elective is captured, return the total registered count and sample enrolled students; otherwise, output a summary of enrollments across all open electives.
* **Regular Expressions**:
  ```python
  r'\b(?:enrollment|enrolled(?:\s+in)?|selected|students?\s+in)\s+(?:the\s*)?open\s+elective\s*(?P<elective>[a-zA-Z\s]+)?\b'
  ```

---

### Question 4: Honours Program Information Retrieval
* **Questions**:
  1. What is honours?
  2. How can I pursue honours?
  3. Tell me about the honours program.
  4. What is the eligibility for honours?
  5. How many credits for honours program?
* **Rules**:
  * Match user questions regarding the B.Tech Honours degree track.
  * Fetch requirements: 20 extra credits over Semesters 5 to 8, CGPA cutoff requirement (minimum 7.5 CGPA with zero backlogs), and portal registration procedures.
  * Format and output the honours program guidelines.
* **Regular Expressions**:
  ```python
  r'\b(?:what\s+is|how\s+(?:can\s+i\s+)?pursue|tell\s+me\s+about|details\s+on|eligibility\s+for)?\s*(?:the\s*)?honours?(?:\s+program)?\b'
  ```

---

### Question 5: Examination Schedule Retrieval
* **Questions**:
  1. When are our exams?
  2. What is the examination timetable?
  3. When is the end sem exam?
  4. When are final exams?
  5. Tell me the exam schedule.
* **Rules**:
  * Identify requests for university examination dates and timings.
  * Dynamically capture the exam category using named group `(?P<exam_type>end\s+sem|final|mid\s+sem|examination|exam)`.
  * Fetch and return end-semester theory examination windows, daily exam time slots, and lab/practical assessment dates.
* **Regular Expressions**:
  ```python
  r'\b(?:when\s+(?:are|is)|what\s+is)\s+(?:the\s+|our\s+)?(?P<exam_type>end\s+sem|final|mid\s+sem|examination|exam)s?\s*(?:schedule|timetable|dates?)?\b'
  ```
