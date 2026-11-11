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
  5. Tell me our co-class teacher details.
* **Rules**:
  * Match queries asking for the class teacher or co-class teacher in charge of the section.
  * Use the named capturing group `(?P<role>...)` to determine whether the user is asking for the class teacher or the co-class teacher.
  * Dynamically fetch and display the respective teacher's name, cabin room number, university email, and extension number.
* **Regular Expressions**:
  ```python
  r'\bwho\s+(?:is|handles).*?\b(?P<role>co[- ]class\s+teacher|class\s+teacher|section)\b'
  ```

---

### Question 2: Faculty Location and Contact Information Retrieval
* **Questions**:
  1. Where is Professor Saravanan's cabin?
  2. How can I contact Dr Deepa?
  3. Where to find Professor Praveen?
  4. Cabin of Dr Saravanan.
  5. How to reach Dr Rekha?
* **Rules**:
  * Identify requests to find a professor's cabin location, room number, or email contact.
  * Dynamically extract the faculty member's name using lazy matching and named capturing group `(?P<faculty>[a-zA-Z\s]+?)`.
  * Search the faculty directory in the knowledge base and return the matching cabin location, office floor, and phone extension.
* **Regular Expressions**:
  ```python
  r'\b(?:where\s+is|cabin\s+of|contact|reach|find)\s+(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+?)(?:\'s|\s+cabin|\s+contact|\?|$)\b'
  ```

---

### Question 3: Global Elective Subject and Student Enrollment Retrieval
* **Questions**:
  1. Who enrolled in global elective Quantum Computing?
  2. How many students take this global elective?
  3. Show students in global elective Robotics and Automation.
  4. Who selected global elective Cyber Forensics?
  5. Tell me global elective enrollments.
* **Rules**:
  * Match inquiries regarding student enrollment numbers and registered peer names for global electives.
  * Dynamically extract the elective title using named capturing group `(?P<elective>[a-zA-Z\s]+)?`.
  * If a specific elective is provided, return the total registered student count and sample enrolled students; otherwise, output a summary of enrollments across all global electives.
* **Regular Expressions**:
  ```python
  r'\b(?:enrollment|enrolled(?:\s+in)?|students?\s+in)\s+(?:the\s*)?global\s+elective\s*(?P<elective>[a-zA-Z\s]+)?\b'
  ```

---

### Question 4: Sports Representative Identification
* **Questions**:
  1. Who is our sports representative?
  2. Who handles sports for our class?
  3. Who is the sports CR?
  4. Tell me our sports rep.
  5. Who represents our class in sports?
* **Rules**:
  * Match queries asking for the designated sports class representative.
  * Retrieve the sports CR's full name, role title, official email, and student sports desk location.
  * Format and display the sports representative profile.
* **Regular Expressions**:
  ```python
  r'\bwho\s+(?:is|handles).*(?:sports\s+(?:representative|rep|cr)|sports\s+for\s+our\s+class)\b'
  ```

---

### Question 5: Department Information Retrieval
* **Questions**:
  1. Who is our HOD?
  2. Who is the head of department?
  3. Who is the program coordinator?
  4. Who is our year coordinator?
  5. Tell me department leadership details.
* **Rules**:
  * Match user questions inquiring about academic leadership and departmental coordinators.
  * Capture the administrative designation using named capturing group `(?P<title>...)`.
  * Resolve whether the query targets the HOD, Program Coordinator, or Year Coordinator, and return their name, role, and department office venue.
* **Regular Expressions**:
  ```python
  r'\bwho\s+is\s+(?:our|the)\s+(?P<title>hod|head\s+of\s+department|program\s+coordinator|year\s+coordinator)\b'
  ```
