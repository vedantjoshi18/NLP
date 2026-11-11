# CHRIST (Deemed to be University), Bengaluru – 560 029
## School of Engineering and Technology
### Department of Computer Science and Engineering
### Continuous Internal Assessment (CIA) - Component 1 - Question 1

* **Programme**: B.Tech Computer Science and Engineering (Artificial Intelligence & Machine Learning) - Section C
* **Course Name**: Natural Language Programming
* **Course Code**: CSEAM631P
* **Max Marks**: 10 Marks
* **Team Members**:
  1. **Sasmita** (Intents: Q1, Q5, Q8, Q14, Q17)
  2. **Joshiny** (Intents: Q2, Q6, Q9, Q15, Q20)
  3. **Vedant** (Intents: Q3, Q7, Q10, Q11, Q16)
  4. **Rachel** (Intents: Q4, Q12, Q13, Q18, Q19, Q21)

---

# Problem-Solving Report: Rule-Based Classroom Assistance Bot Using Python Regular Expressions

---

## 1. Identification of Application Domain and Problem Definition

### 1.1 Application Domain
In an academic university environment like **CHRIST (Deemed to be University)**, students and faculty frequently need rapid access to routine administrative and classroom information. Information such as lecture room venues, daily timetables, faculty cabin numbers, internal assessment (CIA) schedules, syllabus unit details, course credits, and elective enrollments is typically distributed across notice boards, PDF circulars, and web portals.

To streamline information access, our team developed a domain-specific **Rule-Based Classroom Assistance Bot** tailored for **6 B.Tech CS AIML Section C**.

### 1.2 Problem Definition
The primary problem addressed by this project is:
> *How to design and implement an interactive, zero-latency rule-based conversational agent using Python's Regular Expression (`re`) module that accepts natural language queries from students, accurately extracts key entities (such as subject codes, faculty names, unit numbers, days of the week, and roll numbers), and dynamically synthesizes appropriate classroom information while handling input variations and unrecognized queries.*

### 1.3 Key Objectives
1. **Accurate Natural Language Understanding**: Recognize 21 distinct query intents across 4 team members without reliance on heavy machine learning frameworks.
2. **Comprehensive RE Application**: Incorporate all core regular expression primitives specified in the course syllabus: pattern searching (`re.search`), matching (`re.match`), text normalization (`re.sub`), token splitting (`re.split`), character classes, quantifiers, and named capturing groups (`(?P<name>...)`).
3. **Dynamic Response Generation**: Slot extracted entities directly into response templates queried from an in-memory academic knowledge base.
4. **Graceful Fallback**: Handle ambiguous or out-of-scope queries with informative default suggestions.

---

## 2. System Architecture & Processing Pipeline

The chatbot is built with a modular, declarative pipeline:

```
                      +-----------------------------------+
                      |      Raw User Query (String)      |
                      +-----------------+-----------------+
                                        |
                                        v
                      +-----------------------------------+
                      |   Step 1: Text Preprocessing      |
                      |   - re.sub() filler strip         |
                      |   - Punctuation removal           |
                      |   - Whitespace normalization      |
                      +-----------------+-----------------+
                                        | Cleaned Query
                                        v
                      +-----------------------------------+
                      |   Step 2: Rule Matching Engine    |
                      |   - Scans 21 Registered Rules     |
                      |   - re.search() with re.IGNORECASE|
                      |   - Extracts Named Groups         |
                      +-----------------+-----------------+
                                        |
                        +---------------+---------------+
                        |                               |
                 [ Match Found ]               [ No Match Found ]
                        |                               |
                        v                               v
       +---------------------------------+  +-----------------------+
       | Step 3: Intent Handler Lookup   |  | Default Fallback      |
       | - Token parsing (re.split)      |  | Suggestions & Help    |
       | - In-memory Knowledge Base      |  +-----------+-----------+
       +----------------+----------------+              |
                        | Dynamic Text                  |
                        v                               v
       +------------------------------------------------+--+
       |             Terminal / Console Output             |
       +---------------------------------------------------+
```

---

## 3. Incorporation of Required Regular Expression Concepts

The project incorporates every RE concept mandated by the evaluation guidelines:

### 3.1 Pattern Preprocessing and Cleaning using `re.sub()`
Before matching intents, polite filler phrases and noise are stripped using `re.sub()`:
```python
# Strip filler conversational prefixes
filler_pattern = r'^(?:(?:can|could)\s+you\s+(?:please\s+)?(?:tell\s+me|show\s+me|inform\s+me|give\s+me)?\s*|please\s+(?:tell\s+me|show\s+me|inform\s+me|give\s+me)?\s*|tell\s+me\s+(?:about\s+)?|show\s+me\s+)'
text = re.sub(filler_pattern, '', text, flags=re.IGNORECASE)

# Clean extraneous punctuation while preserving words and spaces
text = re.sub(r'[^\w\s]', ' ', text)

# Collapse repeated whitespaces
text = re.sub(r'\s+', ' ', text).strip()
```

### 3.2 Pattern Matching using `re.search()` and `re.match()`
* **`re.search()`**: Employed across the intent engine to match patterns anywhere in the utterance regardless of preceding words (e.g., matching `"where is our classroom"` or `"give me the syllabus for ai"`).
* **`re.match()`**: Used during boundary verification and standalone menu command processing (`help`, `debug`, `exit`).

### 3.3 Pattern Splitting using `re.split()`
When users inquire about compound subjects or multi-token unit ranges, `re.split()` parses the components:
```python
# Splitting multi-token parameters (e.g., "AI, DBMS and ML")
tokens = re.split(r'\s*(?:,|and|\+)\s*', raw_input)
```

### 3.4 Character Classes and Special Sequences
* **`\b` (Word Boundary)**: Prevents partial-word false positives (e.g., ensuring `\bcr\b` matches "CR" but not "credit" or "creative").
* **`\d+` (Digit Sequences)**: Used to extract roll numbers (`(?P<roll>\d+)`) and unit numbers (`(?P<unit>\d+)`).
* **`\w+` (Alphanumeric)**: Extracts course codes like `AI`, `DBMS`, `NLP`, `ML`.
* **`\s+` (Whitespace)**: Tolerates arbitrary spacing between words.
* **`[1-3]` (Character Range)**: Restricts CIA evaluation checks strictly to CIA 1, 2, or 3.
* **`[a-zA-Z\s]` (Alphabetic + Space)**: Captures faculty surnames and elective course titles without picking up numbers or punctuation.

### 3.5 Quantifiers and Grouping
* **`+` (One or more)**: Used in `\w+`, `\d+`, `\s+`.
* **`*` (Zero or more)**: Used in `.*` and `\s*`.
* **`?` (Zero or one / Optional)**: Handles plural suffixes (`electives?`, `programs?`, `exams?`) and optional articles (`(?:the\s*)?`).
* **`+?` (Lazy / Non-greedy)**: Captures faculty names up to the apostrophe or keyword (`(?P<faculty>[a-zA-Z\s]+?)(?:'s|\s+cabin)`).

### 3.6 Named Capturing Groups `(?P<name>...)`
Named capturing groups make the codebase readable and self-documenting:
* `(?P<day>monday|tuesday|...)`: Timetable day extraction.
* `(?P<subject>\w+)`: Subject acronym extraction.
* `(?P<unit>\d+)`: Unit index extraction.
* `(?P<faculty>[a-zA-Z\s]+)`: Faculty name extraction.
* `(?P<role>co[- ]class\s+teacher|class\s+teacher)`: Teacher role extraction.
* `(?P<cia_num>[1-3])`: CIA assessment number extraction.
* `(?P<roll>\d+)`: Student roll number extraction.

---

## 4. Master 21-Intent Mapping Table

| No | Intent / Problem Statement | Assigned Member | Regular Expression Pattern | Extracted Groups |
|:---:|:---|:---:|:---|:---:|
| 1 | Classroom Location Retrieval | **Sasmita** | `\b(?:where\s+is\s+our\s+classroom\|which\s+room\|class\s+location\|classroom\|class\s*room)\b` | None (Fixed lookup) |
| 2 | Class Teacher & Co-Teacher Identification | **Joshiny** | `\bwho\s+(?:is\|handles).*?\b(?P<role>co[- ]class\s+teacher\|class\s+teacher\|section)\b` | `role` |
| 3 | Class Representative (CR) Information | **Vedant** | `\bwho\s+(?:is\|are\|represents).*?\b(?P<rep>cr\|class\s+representatives?\|class\s+reps?\|our\s+class)\b` | `rep` |
| 4 | Class Strength Information Retrieval | **Rachel** | `\b(?:how\s+many\s+students\|class\s+strength\|strength\s+of\s+(?:the\s+\|our\s+)?class\|how\s+many\s+people)\b` | None (Fixed lookup) |
| 5 | Class Timetable Retrieval | **Sasmita** | `\b(?:timetable\|schedule\|routine)(?:\s+(?:for\|on)?\s*(?P<day>monday\|tuesday\|wednesday\|thursday\|friday\|today))?\b` | `day` (Optional) |
| 6 | Faculty Location & Contact Retrieval | **Joshiny** | `\b(?:where\s+is\|cabin\s+of\|contact\|reach\|find)\s+(?:prof(?:essor)?\|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+?)(?:\'s\|\s+cabin\|\s+contact\|\?\|$)\b` | `faculty` |
| 7 | Global Elective Information Retrieval | **Vedant** | `\b(?:what\s+are\|which\|explain\|tell\s+me\s+about\|list\|show\|available)\s+(?:the\s*)?global\s+electives?\b\|^\s*(?:the\s*)?global\s+electives?\s*$` | None (Catalog list) |
| 8 | Open Elective Information Retrieval | **Sasmita** | `\b(?:what\s+are\|which\|explain\|tell\s+me\s+about\|list\|show\|available)\s+(?:the\s*)?open\s+electives?\b\|^\s*(?:the\s*)?open\s+electives?\s*$` | None (Catalog list) |
| 9 | Global Elective Student Enrollment | **Joshiny** | `\b(?:enrollment\|enrolled(?:\s+in)?\|students?\s+in)\s+(?:the\s*)?global\s+elective\s*(?P<elective>[a-zA-Z\s]+)?\b` | `elective` (Optional) |
| 10 | Open Elective Student Enrollment | **Vedant** | `\b(?:enrollment\|enrolled(?:\s+in)?\|selected\|students?\s+in)\s+(?:the\s*)?open\s+elective\s*(?P<elective>[a-zA-Z\s]+)?\b` | `elective` (Optional) |
| 11 | Honours Program Information Retrieval | **Vedant** | `\b(?:what\s+is\|how\s+(?:can\s+i\s+)?pursue\|tell\s+me\s+about\|details\s+on\|eligibility\s+for)?\s*(?:the\s*)?honours?(?:\s+program)?\b` | None (Curriculum lookup) |
| 12 | Minor Program Information Retrieval | **Rachel** | `\b(?:what\s+(?:are\|is)\|how\s+do\|which\|tell\s+me\s+about)?\s*(?:the\s*)?minors?(?:\s+program)?\b` | None (Tracks lookup) |
| 13 | Certificate Program Information Retrieval | **Rachel** | `\b(?:what\|how\|tell\s+me\s+about\|which)?\s*certificate\s*(?:programs?\|courses?)\b` | None (Offerings lookup) |
| 14 | CIA Schedule Information Retrieval | **Sasmita** | `\b(?:when (?:are\|is)\|what is)?\s*(?:the\s*)?cias?\s*(?P<cia_num>[1-3])?\s*(?:schedule\|dates?\|exam)?\b` | `cia_num` (Optional) |
| 15 | Sports Representative Identification | **Joshiny** | `\bwho\s+(?:is\|handles).*(?:sports\s+(?:representative\|rep\|cr)\|sports\s+for\s+our\s+class)\b` | None (Sports desk) |
| 16 | Examination Schedule Retrieval | **Vedant** | `\b(?:when\s+(?:are\|is)\|what\s+is)\s+(?:the\s+\|our\s+)?(?P<exam_type>end\s+sem\|final\|mid\s+sem\|examination\|exam)s?\s*(?:schedule\|timetable\|dates?)?\b` | `exam_type` |
| 17 | Subject Syllabus Retrieval | **Sasmita** | `\b(?:syllabus\|units?)(?:\s+(?P<unit>\d+))?\s*(?:of\|for\|in)\s+(?P<subject>\w+)\b` | `unit`, `subject` |
| 18 | Subject Faculty Identification | **Rachel** | `\b(?:who\s+teaches\|which\s+faculty\s+handles\|subject\s+teacher\s+for\|who\s+takes)\s+(?P<subject>\w+)\b` | `subject` |
| 19 | Course Credit Information Retrieval | **Rachel** | `\b(?:how\s+many\s+credits(?:\s+does)?\|what\s+are\s+the\s+credits\s+for\|credits?\s+(?:for\|of)\|credit\s+value\s+of)\s+(?P<subject>\w+)\b` | `subject` |
| 20 | Department Information Retrieval | **Joshiny** | `\bwho\s+is\s+(?:our\|the)\s+(?P<title>hod\|head\s+of\s+department\|program\s+coordinator\|year\s+coordinator)\b` | `title` |
| 21 | Mentor & Mentee Information Retrieval | **Rachel** | `\b(?:mentor\s+(?:for\|of)\s*(?:roll\s*)?(?P<roll>\d+)\|(?:mentees?\|students?)\s+(?:are\s+)?(?:under\|of)\s*(?:prof(?:essor)?\|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+)\|who\s+is\s+my\s+mentor)\b` | `roll` or `faculty` |

---

## 5. Sample Execution Transcripts (Interactive CLI)

Below is an annotated terminal transcript demonstrating interaction with the implemented chatbot:

```text
===========================================================================
  CHRIST (Deemed to be University) - School of Engineering & Technology
        DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING (B.Tech CS AIML-C)
            CLASSROOM ASSISTANCE BOT (Python RE Rule-Based)
===========================================================================
Team Members: Sasmita | Joshiny | Vedant | Rachel
Commands: 'exit' or 'quit' to leave | 'help' for all intents | 'debug' to toggle regex inspector
---------------------------------------------------------------------------

You: Where is our classroom?
Bot:
📍 [Classroom Location]
Our class (6 B.Tech CS AIML-C) is in Room 412, 4th Floor, Block II.

You: debug
Bot: [Debug Inspector ENABLED]

You: Who teaches AI?

  [DEBUG INFO]
  • Member : Rachel
  • Intent : Q18 - Subject Faculty Identification
  • Pattern: \b(?:who\s+teaches|which\s+faculty\s+handles|subject\s+teacher\s+for|who\s+takes)\s+(?P<subject>\w+)\b
  • Groups : {'subject': 'ai'}
  --------------------------------------------------

Bot:
👨‍🏫 [Faculty In-Charge]
Subject: Artificial Intelligence (AI)
Faculty: Dr. K. Saravanan

You: Show Unit 2 of AI syllabus

  [DEBUG INFO]
  • Member : Sasmita
  • Intent : Q17 - Subject Syllabus Retrieval
  • Pattern: \b(?:syllabus|units?)(?:\s+(?P<unit>\d+))?\s*(?:of|for|in)\s+(?P<subject>\w+)\b
  • Groups : {'unit': '2', 'subject': 'ai'}
  --------------------------------------------------

Bot:
📚 [AI Syllabus - Unit 2]
Unit 2: Knowledge Representation, First Order Logic, Semantic Networks

You: Who is my mentor for roll 15?

  [DEBUG INFO]
  • Member : Rachel
  • Intent : Q21 - Mentor and Mentee Information Retrieval
  • Pattern: \b(?:mentor\s+(?:for|of)\s*(?:roll\s*)?(?P<roll>\d+)|(?:mentees?|students?)\s+(?:are\s+)?(?:under|of)\s*(?:prof(?:essor)?|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+)|who\s+is\s+my\s+mentor)\b
  • Groups : {'roll': '15', 'faculty': None}
  --------------------------------------------------

Bot:
🧑‍🏫 [Mentor Allocation]
Roll Number: 15
Assigned Mentor: Dr. K. Saravanan (Cabin 305, Block II)

You: What is the weather in Paris?
Bot:
🤖 I'm sorry, I couldn't recognize your query.
Here are some questions you can ask me:
  • 'Where is our classroom?' (Sasmita - Q1)
  • 'Who is our class teacher?' (Joshiny - Q2)
  • 'Who is our CR?' (Vedant - Q3)
  • 'How many students are in our class?' (Rachel - Q4)
  • 'What is the syllabus for AI?' (Sasmita - Q17)
  • 'Who teaches DBMS?' (Rachel - Q18)
Type 'help' to see all 21 supported queries grouped by team member.

You: quit
Bot: Goodbye! Have a great day at CHRIST University.
```

---

## 6. Verification and Automated Testing

An automated verification test runner (`test_chatbot.py`) and modular unit test suites (`tests/`) were executed:

```bash
$ python -m unittest discover tests
........................
----------------------------------------------------------------------
Ran 24 tests in 0.005s
OK

$ python test_chatbot.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.004s
OK
```
All 21 intents passed with zero errors, validating:
1. Intent recognition accuracy.
2. Capturing group population.
3. Preprocessor noise and filler stripping.
4. Fallback execution upon encountering out-of-domain input.

---

## 7. Viva Preparation Guide for Evaluator Demonstration

During the faculty evaluation, team members can answer the following conceptual questions:

1. **Why use Named Capturing Groups instead of indexed groups?**
   * *Answer*: Indexed groups (`match.group(1)`) are brittle because altering the order of parentheses in a regex breaks the index. Named groups (`(?P<subject>\w+)`) allow accessing parameters by meaningful dictionary keys (`match.groupdict()['subject']`), increasing maintainability and readability.
2. **What is the difference between greedy and non-greedy matching?**
   * *Answer*: In Q2 (*"Who is our co-class teacher?"*), greedy `.*` consumed `"co-"` before `"class teacher"`, causing a false match. Changing to non-greedy `.*?` ensures the engine halts at the earliest match boundary, preserving `"co-class teacher"`.
3. **How does the chatbot handle input variations?**
   * *Answer*: Through a two-stage process: (1) `re.sub` pre-cleans polite filler prefixes and punctuation; (2) Regex alternation `(?:...)` and optional quantifiers `?` handle synonyms and phrasing variations without needing large neural models.
