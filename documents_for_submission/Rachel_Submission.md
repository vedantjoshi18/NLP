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
  5. Tell me the class strength.
* **Rules**:
  * Match user queries inquiring about total enrolled students or section headcount using phrase alternation and word boundaries.
  * Retrieve total student count (68), boys count (42), and girls count (26) from the class information registry.
  * Dynamically generate and format the class strength report.
* **Regular Expressions**:
  ```python
  r'\b(?:how\s+many\s+students|class\s+strength|strength\s+of\s+(?:the\s+|our\s+)?class|how\s+many\s+people)\b'
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
  * Extract requirements: 18 extra credits across 4 semesters, CGPA cutoff (7.0), and available tracks (Data Science, IoT, FinTech).
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
  4. Which certificate courses can we take?
  5. What are the value-added certificate offerings?
* **Rules**:
  * Identify student inquiries regarding short-term, value-added certification courses.
  * Fetch current industry-aligned certifications in our class (AWS ML Associate, Microsoft Azure AI 900, Azure BI Data Analyst, AWS Solutions Architect, AI-200).
  * Format and output certificate names, student counts, course duration, and registration directions.
* **Regular Expressions**:
  ```python
  r'\b(?:what|how|tell\s+me\s+about|which)?\s*certificate\s*(?:programs?|courses?)\b'
  ```

---

### Question 4: Subject Faculty Identification
* **Questions**:
  1. Who teaches AI?
  2. Who teaches NLP?
  3. Which faculty handles Deep Learning?
  4. Who is our subject teacher for Digital Image Processing?
  5. Who takes Professional Ethics?
* **Rules**:
  * Match queries asking for the teacher or faculty in charge of an academic course.
  * Dynamically capture the target subject code/acronym using the named capturing group `(?P<subject>\w+)`.
  * Query the subjects database using the captured key and return the designated faculty member's name and subject details.
* **Regular Expressions**:
  ```python
  r'\b(?:who\s+teaches|which\s+faculty\s+handles|subject\s+teacher\s+for|who\s+takes)\s+(?P<subject>\w+)\b'
  ```

---

### Question 5: Course Credit Information Retrieval
* **Questions**:
  1. How many credits does AI have?
  2. What are the credits for DBMS?
  3. How many credits is ML?
  4. Credits for NLP.
  5. What is the credit value of AI?
* **Rules**:
  * Match queries seeking the credit weightage or contact-hour structure of a subject.
  * Dynamically extract the subject code via named capturing group `(?P<subject>\w+)`.
  * Retrieve credit score and L-T-P (Lecture-Tutorial-Practical) hour breakdown from the course repository and return a dynamic answer.
* **Regular Expressions**:
  ```python
  r'\b(?:how\s+many\s+credits(?:\s+does)?|what\s+are\s+the\s+credits\s+for|credits?\s+(?:for|of)|credit\s+value\s+of)\s+(?P<subject>\w+)\b'
  ```

---

### Question 6: Mentor and Mentee Information Retrieval
* **Questions**:
  1. Who is my mentor for roll 15?
  2. Which students are under Professor Deepa?
  3. Who is my mentor?
  4. Show mentees of Dr Saravanan.
  5. Mentor for roll 45.
* **Rules**:
  * Match queries regarding mentor-mentee allocations using multi-branch pattern matching.
  * Extract student roll number via named group `(?P<roll>\d+)` OR faculty name via named group `(?P<faculty>[a-zA-Z\s]+)`.
  * If a roll number is extracted, locate and return the specific assigned faculty mentor and cabin.
  * If a faculty name is extracted, calculate and return their assigned mentee roll range and batch count.
* **Regular Expressions**:
  ```python
  r'\b(?:mentor\s+(?:for|of)\s*(?:roll\s*)?(?P<roll>\d+)|(?:mentees?|students?)\s+(?:are\s+)?(?:under|of)\s*(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+)|who\s+is\s+my\s+mentor)\b'
  ```
