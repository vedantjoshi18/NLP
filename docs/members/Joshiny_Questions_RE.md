# Member-Wise Submission Document: Joshiny
**Course**: Natural Language Programming (CSEAM631P)  
**Programme**: B.Tech CS AIML-C, School of Engineering and Technology, CHRIST (Deemed to be University)  
**Activity**: CIA Component - 1 (Question 1) - Rule-Based Chatbot Using Python RE  
**Team Member**: Joshiny  
**Register No**: [Enter Register Number Here]  
**Application Domain**: Classroom Assistance Bot  

---

## Member Contribution Summary
Joshiny contributed **5 unique problem statements and query intents** addressing classroom leadership, faculty cabins, department administration, sports representation, and global elective enrollments:
1. **Q2**: Class Teacher and Co-Class Teacher Identification
2. **Q6**: Faculty Location and Contact Information Retrieval
3. **Q9**: Global Elective Subject and Student Enrollment Retrieval
4. **Q15**: Sports Representative Identification
5. **Q20**: Department Information Retrieval

---

## Detailed Question & Regular Expression Breakdown

### Question 1: Class Teacher & Co-Class Teacher Identification (Q2)
* **Problem Statement**: Enabling students to identify their assigned class teacher or co-class teacher along with cabin locations and university contact details.
* **Sample User Queries**:
  * *"Who is our class teacher?"*
  * *"Who handles our section?"*
  * *"Who is our co-class teacher?"*
* **Regular Expression Pattern**:
  ```python
  r'\bwho\s+(?:is|handles).*?\b(?P<role>co[- ]class\s+teacher|class\s+teacher|section)\b'
  ```
* **RE Concepts Applied**:
  * Non-greedy quantifier `*?`: Prevents greedy match overshooting so that `"co-class teacher"` is correctly captured.
  * Hyphen and character class `[- ]`: Matches either hyphenated (`co-class`) or space-separated (`co class`) notation.
  * Named Capturing Group `(?P<role>...)`: Isolates whether the inquiry targets the main class teacher or the co-class teacher.
* **Dynamic Information Extraction & Handling**:
  Inspects the captured `role`. If `"co"` is present in the role string, returns Prof. Deepa V.'s profile; otherwise returns Dr. K. Saravanan's profile.
* **Expected Chatbot Response (Class Teacher)**:
  ```text
  👨‍🏫 [Class Teacher]
  Name: Dr. K. Saravanan
  Location: Cabin 305, Block II (3rd Floor)
  Email: saravanan.k@christuniversity.in
  Ext: 4123
  ```
* **Expected Chatbot Response (Co-Class Teacher)**:
  ```text
  👩‍🏫 [Co-Class Teacher]
  Name: Prof. Deepa V.
  Location: Cabin 210, Block II (2nd Floor)
  Email: deepa.v@christuniversity.in
  Ext: 4110
  ```

---

### Question 2: Faculty Location and Contact Information Retrieval (Q6)
* **Problem Statement**: Locating specific faculty cabins, email addresses, and extension numbers by name.
* **Sample User Queries**:
  * *"Where is Professor Saravanan's cabin?"*
  * *"How can I contact Dr Deepa?"*
  * *"Where to find Professor XYZ?"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:where\s+is|cabin\s+of|contact|reach|find)\s+(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+?)(?:\'s|\s+cabin|\s+contact|\?|$)\b'
  ```
* **RE Concepts Applied**:
  * Optional honorifics `(?:prof(?:essor)?|dr\.?)`: Matches both "Prof", "Professor", and "Dr." with optional period.
  * Named Capturing Group `(?P<faculty>[a-zA-Z\s]+?)`: Dynamically extracts the professor's name using alphabetical characters and spaces.
  * Lazy Quantifier `+?`: Prevents capturing trailing punctuation, apostrophes, or inquiry nouns (*"cabin"*, *"contact"*).
* **Dynamic Information Extraction & Handling**:
  Matches extracted tokens against faculty names in leadership and subject registries, generating personalized contact cards.
* **Expected Chatbot Response**:
  ```text
  🏢 [Faculty Contact]
  Dr. K. Saravanan (Class Teacher)
  Cabin: Cabin 305, Block II (3rd Floor)
  Email: saravanan.k@christuniversity.in | Ext: 4123
  ```

---

### Question 3: Global Elective Subject & Student Enrollment Retrieval (Q9)
* **Problem Statement**: Checking how many students have registered for a specific global elective and listing sample enrolled peers.
* **Sample User Queries**:
  * *"Who enrolled in global elective quantum computing?"*
  * *"How many students take this global elective?"*
  * *"Show students in global elective robotics"*
* **Regular Expression Pattern**:
  ```python
  r'\b(?:enrollment|enrolled(?:\s+in)?|students?\s+in)\s+(?:the\s*)?global\s+elective\s*(?P<elective>[a-zA-Z\s]+)?\b'
  ```
* **RE Concepts Applied**:
  * Optional prepositions `(?:\s+in)?`: Matches both *"enrolled in"* and *"enrolled"*.
  * Named Capturing Group `(?P<elective>[a-zA-Z\s]+)?`: Dynamically isolates the global elective title.
  * Character classes `[a-zA-Z\s]`: Safely captures multi-word course names (e.g., *"quantum computing"*, *"robotics and automation"*).
* **Dynamic Information Extraction & Handling**:
  If a specific elective is captured, looks up enrollment tally and enrolled student names. If omitted, outputs a summary table for all global electives.
* **Expected Chatbot Response**:
  ```text
  🌐 [Global Elective Enrollment: Quantum Computing]
  Total Enrolled: 24 students
  Sample Enrolled Students: Aditya V., Kavya R., Nikhil P.
  ```

---

### Question 4: Sports Representative Identification (Q15)
* **Problem Statement**: Directing students to the class sports representative for intra-university athletic tournaments and equipment requisitions.
* **Sample User Queries**:
  * *"Who is our sports representative?"*
  * *"Who handles sports for our class?"*
  * *"Who is the sports CR?"*
* **Regular Expression Pattern**:
  ```python
  r'\bwho\s+(?:is|handles).*(?:sports\s+(?:representative|rep|cr)|sports\s+for\s+our\s+class)\b'
  ```
* **RE Concepts Applied**:
  * Non-capturing nested groups `(?:...)`: Consolidates variations (*"sports representative"*, *"sports rep"*, *"sports cr"*, *"sports for our class"*).
  * Word boundary `\b`: Ensures accurate keyword boundaries.
* **Dynamic Information Extraction & Handling**:
  Queries the `leadership['sports_cr']` object and formats representative credentials and office location.
* **Expected Chatbot Response**:
  ```text
  🏆 [Sports Representative]
  Name: Rohan Gowda
  Role: Sports Class Representative
  Email: rohan.g@cs.christuniversity.in
  Desk: Sports Directorate, Ground Floor, Central Block
  ```

---

### Question 5: Department Information Retrieval (Q20)
* **Problem Statement**: Providing information about department leadership, including Head of Department (HOD) and Program Coordinators.
* **Sample User Queries**:
  * *"Who is our HOD?"*
  * *"Who is the program coordinator?"*
  * *"Who is the year coordinator?"*
* **Regular Expression Pattern**:
  ```python
  r'\bwho\s+is\s+(?:our|the)\s+(?P<title>hod|head\s+of\s+department|program\s+coordinator|year\s+coordinator)\b'
  ```
* **RE Concepts Applied**:
  * Named Capturing Group `(?P<title>...)`: Categorizes which administrative authority the student is asking about.
  * Alternation `|`: Distinctly maps acronyms (`hod`) and written forms (`head of department`).
* **Dynamic Information Extraction & Handling**:
  Evaluates the captured `title` string and routes dynamically to the HOD, AIML Program Coordinator, or 3rd-Year Coordinator.
* **Expected Chatbot Response (HOD)**:
  ```text
  🏛️ [Head of Department]
  Dr. Balakrishnan R. (Department of Computer Science & Engineering)
  Office: Room 101, Ground Floor, Block II
  ```
* **Expected Chatbot Response (Program Coordinator)**:
  ```text
  🏛️ [Program Coordinator]
  Dr. Smitha Rao (B.Tech CS AIML Coordinator)
  Office: Room 101, Ground Floor, Block II
  ```

---

## Verification & Execution Evidence
All 5 rules were integrated into `classroom_bot/rules/joshiny.py` and unit tested in `tests/test_joshiny_rules.py`.
* Automated test execution status: **100% Passed (5/5 tests)**.
