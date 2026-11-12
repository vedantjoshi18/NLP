CIA1- COMPONENT 1
Name: Joshiny
Group No: 6

---

### Question 1: Class Teacher and Co-Class Teacher Identification
* **Questions**:
  1. Who is our class teacher?
  2. Who handles our section?
  3. Who is our co-class teacher?
  4. Who is the class teacher for Section C?
  5. Co class teacher
* **Rules**:
  * Match queries asking for the class teacher or co-class teacher in charge of Section 6BTCS AIML-C.
  * Use the named capturing group `(?P<role>...)` to determine whether the user is asking for the class teacher or the co-class teacher.
  * Dynamically fetch and display the respective teacher's name (Class Teacher: Dr. Poongodi C; Co-Class Teacher: Dr. Jeno Lovesum S P), location (Faculty Room, GF-B3), and official email.
* **Regular Expressions**:
  ```python
  r'\b(?:who\s+(?:is|handles|takes)\s+(?:our\s+)?(?:section(?:\s*c)?|class)?\s*)?(?P<role>co[- ]class\s+teacher|co[- ]ct|class\s+teacher|\bct\b)\b|\bwho\s+handles\s+(?:our\s+)?section(?:\s*c)?\b'
  ```

---

### Question 2: Faculty Location and Contact Information Retrieval
* **Questions**:
  1. Where is Professor Poongodi's cabin?
  2. How can I contact Dr Vinodha?
  3. Where can I find Amos Bortiew?
  4. Cabin of Dr Jeno
  5. Where is Dr Kukatlapalli's cabin?
* **Rules**:
  * Identify requests to find a professor's cabin location, room number, or email contact.
  * Dynamically extract the faculty member's name using lazy matching and named capturing group `(?P<faculty>[a-zA-Z\s]+?)`.
  * Search the faculty directory and timetable database in the knowledge base and return the matching cabin location, office floor, or laboratory venue.
* **Regular Expressions**:
  ```python
  r'\b(?:where\s+is|cabin\s+of|contact|reach|find|where\s+can\s+i\s+find)\s+(?:prof(?:essor)?|dr\.?)?\s*(?P<faculty>[a-zA-Z\s]+?)(?:\'s|\s+cabin|\s+contact|\s+office|\?|$)\b'
  ```

---

### Question 3: Global Elective Subject and Student Enrollment Retrieval
* **Questions**:
  1. Who has enrolled in Global Elective Quantum Computing?
  2. How many students take this global elective?
  3. Global elective enrollment
  4. Show students in global elective Robotics and Automation.
  5. Tell me global elective enrollments.
* **Rules**:
  * Match inquiries regarding student enrollment numbers and registered peer names for global electives.
  * Dynamically extract the elective title using named capturing group `(?P<elective>[a-zA-Z\s]+)?`.
  * If a specific elective is provided, return the total registered student count and sample enrolled students; otherwise, output a summary of enrollments across all global electives.
* **Regular Expressions**:
  ```python
  r'\b(?:(?:enrollment(?:\s+in)?|(?:who\s+has\s+)?enrolled(?:\s+in)?|(?:how\s+many\s+)?students?\s+(?:in|(?:are\s+)?taking|take))\s+(?:the\s*|this\s*)?global\s+electives?|global\s+electives?\s+(?:enrollment|students?))\s*(?P<elective>[a-zA-Z\s]+)?\b'
  ```

---

### Question 4: Sports Representative Identification
* **Questions**:
  1. Who is our sports representative?
  2. Who handles sports for our class?
  3. Who is the sports CR?
  4. Sports rep
  5. Who represents our class in sports?
* **Rules**:
  * Match queries asking for the designated sports class representative.
  * Retrieve the sports CR's full name (Rohan Gowda), role title, official email, and student sports desk location.
  * Format and display the sports representative profile.
* **Regular Expressions**:
  ```python
  r'\b(?:who\s+(?:is|handles)\s+(?:our\s+)?)?(?:sports\s+(?:representative|rep|cr)|sports\s+for\s+our\s+class)\b'
  ```

---

### Question 5: Department Information Retrieval
* **Questions**:
  1. Who is our HOD?
  2. Who is the head of department?
  3. Who is the program coordinator?
  4. Who is the year coordinator?
  5. Department office
* **Rules**:
  * Match user questions inquiring about academic leadership and departmental coordinators.
  * Capture the administrative designation using named capturing group `(?P<title>...)`.
  * Resolve whether the query targets the HOD (Dr. Michael Moses T), Program Coordinator (Dr. Poongodi C), Year Coordinator (Dr. Jeno Lovesum S P), or Department Office (Room 302, Block 1, Department of AI and Data Science Engineering), and return their name, role, and office venue.
* **Regular Expressions**:
  ```python
  r'\b(?:who\s+is\s+(?:our|the)\s+)?(?P<title>hod|head\s+of\s+department|program\s+coordinator|year\s+coordinator|department\s+office)\b'
  ```
