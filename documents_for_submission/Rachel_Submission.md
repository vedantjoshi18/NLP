CIA1- COMPONENT 1
Name: Rachel Febin Pulicken
Group No: 6

---

### Question 1: Class Strength Information Retrieval
* **Questions**:
  1. How many students are in our class?
  2. What's our class strength?
  3. How many people are in our section?
  4. What is the strength of our class?
  5. Total students in our class.
* **Rules**:
  * Match user queries inquiring about total enrolled students or section headcount using phrase alternation and word boundaries.
  * Retrieve total student count (55 verified against 6BTCS AIML-C official course roll), boys count (35), and girls count (20) from the class information registry.
  * Dynamically generate and format the class strength report.
* **Regular Expressions**:
  ```python
  r'\b(?:how\s+many\s+students|class\s+strength|strength\s+of\s+(?:the\s+|our\s+)?class|how\s+many\s+people|total\s+students|number\s+of\s+students|total\s+strength)\b'
  ```

---

### Question 2: Minor Program Information Retrieval
* **Questions**:
  1. What are the minors?
  2. How do minors work?
  3. Which minor programs are available?
  4. Tell me about minor programs.
  5. What is the eligibility for minors?
* **Rules**:
  * Identify queries asking about university interdisciplinary minor degree programs.
  * Extract requirements: 18 extra credits across 4 semesters, CGPA cutoff (7.0), timetable slot (Wednesdays 11:00 - 14:00), and available tracks (Data Science, IoT & Embedded Systems, FinTech & Blockchain).
  * Synthesize and return the structured minor degree program details.
* **Regular Expressions**:
  ```python
  r'\b(?:what\s+(?:are|is)|how\s+do|which|tell\s+me\s+about)?\s*(?:the\s*)?minors?(?:\s+program)?\b'
  ```

---

### Question 3: Certificate Program Information Retrieval
* **Questions**:
  1. What certificate programs are available?
  2. How can I pursue a certificate?
  3. Tell me about certificate courses.
  4. Who did AWS ML Associate?
  5. Who completed Azure AI Fundamentals?
* **Rules**:
  * Identify student inquiries regarding short-term value-added certification courses or lookups for peers holding specific industry certifications.
  * Extract specific certification name using named capturing group `(?P<cert_name>[a-zA-Z\s\d\-]+?)`.
  * Dynamically fetch certification records verified from `Certification Data.xlsx` (AWS Certified Machine Learning - Associate, Azure AI Fundamentals AI-900, Azure Data Analyst Associate PL-300, AWS Certified Solutions Architect - Associate, AI-200), including student recipients and timetable slots (Wednesdays 11:00 - 14:00).
* **Regular Expressions**:
  ```python
  r'\b(?:(?:what|how|which|tell\s+me\s+about|explain)(?:\s+can\s+i\s+pursue)?\s+)?(?:the\s+)?certificates?(?:\s+(?:programs?|courses?))?\b|\bwho\s+(?:did|completed|holds|took)\s+(?:the\s*)?(?P<cert_name>[a-zA-Z\s\d\-]+?)(?:\s+certification|\s+cert|\?|$)\b'
  ```

---

### Question 4: Subject Faculty Identification
* **Questions**:
  1. Who teaches AI?
  2. Who teaches NLP?
  3. Which faculty handles Deep Learning?
  4. Who takes Professional Ethics?
  5. Faculty for Server Integration.
* **Rules**:
  * Match queries asking for the teacher or faculty in charge of an academic course or laboratory.
  * Dynamically capture the target subject code or name using the lazy named capturing group `(?P<subject>[a-zA-Z\s]+?)`.
  * Query the subjects database verified from the 6th Semester Timetable (NLP: Dr. D Vinodha, DL: Dr. Amos Bortiew, DIP: Prof. Wims Magdalene Mary A, PE: Dr. Poongodi C, SIR: Dr. Kukatlapalli Pradeep Kumar, SLP: Dr. Ambily Balaram / Dr. Neethu P S) and return the designated faculty member's name and lab venue.
* **Regular Expressions**:
  ```python
  r'\b(?:who\s+teaches|which\s+faculty\s+handles|subject\s+teacher\s+for|who\s+takes|faculty\s+for)\s+(?P<subject>[a-zA-Z\s]+?)(?:\?|$)\b'
  ```

---

### Question 5: Course Credit Information Retrieval
* **Questions**:
  1. How many credits does AI have?
  2. How many credits does NLP have?
  3. What are the credits for DL?
  4. Credits for DIP.
  5. What is the credit value of PE?
* **Rules**:
  * Match queries seeking the credit weightage or contact-hour structure of a course.
  * Dynamically extract the subject name using named capturing group `(?P<subject>[a-zA-Z\s]+?)`.
  * Retrieve credit score and L-T-P-S structure (e.g., NLP: 4 Credits 3-0-2, DL: 4 Credits 3-0-2, DIP: 4 Credits 3-0-2, PE: 2 Credits 2-0-0) from the official curriculum repository and return a dynamic answer.
* **Regular Expressions**:
  ```python
  r'\b(?:how\s+many\s+credits(?:\s+does)?|what\s+are\s+the\s+credits\s+for|credits?\s+(?:for|of)|credit\s+value\s+of)\s+(?P<subject>[a-zA-Z\s]+?)(?:\s+have|\s+worth|\?|$)\b'
  ```

---

### Question 6: Mentor and Mentee Information Retrieval
* **Questions**:
  1. Who is my mentor for roll 15?
  2. Which students are under Dr Poongodi?
  3. Who is my mentor?
  4. When is mentoring?
  5. Mentor for roll 45.
* **Rules**:
  * Match queries regarding mentor-mentee allocations using multi-branch pattern matching.
  * Extract student roll number via named group `(?P<roll>\d+)` OR faculty name via named group `(?P<faculty>[a-zA-Z\s]+)` OR detect mentoring schedule queries.
  * If a roll number is extracted, locate and return the specific assigned faculty mentor and cabin.
  * If a faculty name is extracted, calculate and return their assigned mentee roll range and batch count.
  * Display weekly Saturday Mentoring Hour (11:00 AM - 12:00 PM).
* **Regular Expressions**:
  ```python
  r'\b(?:mentor\s+(?:for|of)\s*(?:roll\s*)?(?P<roll>\d+)|(?:mentees?|students?)\s+(?:are\s+)?(?:under|of)\s*(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+)|who\s+is\s+my\s+mentor|when\s+is\s+mentoring)\b'
  ```
