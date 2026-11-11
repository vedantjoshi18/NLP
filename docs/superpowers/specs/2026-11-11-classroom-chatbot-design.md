# Design Specification: Classroom Assistance Bot (Rule-Based Chatbot Using Python RE)

**Course**: Natural Language Programming (CSEAM631P)  
**Programme**: B.Tech CS AIML-C, School of Engineering and Technology, CHRIST (Deemed to be University), Bengaluru  
**Component**: CIA Component - 1 - Question 1 (10 Marks)  
**Date**: 2026-11-11  
**Status**: Approved Design  

---

## 1. Executive Summary & Problem Definition

### 1.1 Application Domain
**Classroom Assistance Bot** tailored for B.Tech CS AIML Section C at CHRIST (Deemed to be University). The bot serves as an automated academic enquiry agent to help students, class representatives, and faculty retrieve instant information regarding classroom location, daily schedules, syllabus, faculty contacts, mentor-mentee mappings, CIA and exam dates, and elective enrollments.

### 1.2 Team Structure & Allocation
The chatbot integrates **21 user intents / problem statements** distributed across 4 team members:
1. **Sasmita** (5 Intents: Q1, Q5, Q8, Q14, Q17)
2. **Joshiny** (5 Intents: Q2, Q6, Q9, Q15, Q20)
3. **Vedant** (5 Intents: Q3, Q7, Q10, Q11, Q16)
4. **Rachel** (6 Intents: Q4, Q12, Q13, Q18, Q19, Q21)

---

## 2. Architecture & Data Processing Pipeline

```
               [ User Input Query ]
                         │
                         ▼
          ┌─────────────────────────────┐
          │ Step 1: Query Preprocessing │
          │         (re.sub)            │
          └──────────────┬──────────────┘
                         │ Cleaned lowercase text
                         ▼
          ┌─────────────────────────────┐
          │ Step 2: Rule Matching &     │
          │         Entity Extraction   │
          │      (re.search / re.match) │
          └──────────────┬──────────────┘
                         │ Matched Rule + Named Capturing Groups
                         ▼
          ┌─────────────────────────────┐
          │ Step 3: Multi-token Split   │
          │         (re.split)          │
          └──────────────┬──────────────┘
                         │ Extracted & Normalized Entities
                         ▼
          ┌─────────────────────────────┐
          │ Step 4: Knowledge Lookup &  │
          │   Dynamic Response Gen      │
          └──────────────┬──────────────┘
                         │ Formatted Dynamic Output
                         ▼
             [ Chatbot Console Output ]
       (or Fallback Response if unrecognized)
```

### 2.1 Preprocessing with `re.sub`
- Strips leading/trailing punctuation and multiple consecutive whitespace characters: `re.sub(r'[^\w\s\?]', ' ', text)`.
- Strips polite conversational prefixes/fillers (e.g., `re.sub(r'^(?:can you\s+|please\s+|tell me\s+|could you\s+)+', '', text, flags=re.I)`).
- Normalizes to lowercase and trims whitespace.

### 2.2 Matching Engine with `re.search` and `re.match`
- Iterates through registered intent rules in priority order.
- Utilizes `re.search()` with `re.IGNORECASE` to allow intent matching regardless of where keywords appear.
- Extracts entities dynamically using named capturing groups `(?P<group_name>...)`.

### 2.3 Token Parsing with `re.split`
- For intents taking compound arguments (such as multiple subject codes or unit numbers, e.g., *"Units 1 and 2 of AI"*, or *"mentees under Prof X and Y"*), `re.split(r'\s*(?:,|and|\+)\s*', raw_string)` tokenizes individual components.

### 2.4 In-Memory Knowledge Base
Realistic mock dataset representing CHRIST University B.Tech CS AIML-C:
- **Classroom**: Block II, 4th Floor, Room 412
- **Class Strength**: 68 students (42 boys, 26 girls)
- **Leadership**:
  - Class Teacher: Dr. K. Saravanan (Cabin 305, Block II, Ext: 4123)
  - Co-Class Teacher: Prof. Deepa V. (Cabin 210, Block II, Ext: 4110)
  - CRs: Rahul M. and Ananya Sharma
  - Sports CR: Rohan Gowda
  - HOD: Dr. Balakrishnan R.
  - Program Coordinator: Dr. Smitha Rao
  - Year Coordinator: Dr. Suresh N.
- **Subjects**:
  - `AI`: Dr. K. Saravanan | 4 Credits | Units 1-5 syllabus defined
  - `DBMS`: Prof. Deepa V. | 3 Credits | Units 1-5 syllabus defined
  - `NLP`: Dr. Praveen Kumar | 4 Credits | Units 1-5 syllabus defined
  - `ML`: Dr. Rekha N. | 4 Credits | Units 1-5 syllabus defined
- **Electives**:
  - Global Electives: Quantum Computing (24 enrolled), Robotics & Automation (22 enrolled), Cyber Forensics (22 enrolled).
  - Open Electives: Digital Marketing (32 enrolled), Financial Literacy (20 enrolled), Creative Writing (16 enrolled).
- **Programs**:
  - Honours: 20 additional credits across Sem 5-8; Minimum 7.5 CGPA with 0 backlogs.
  - Minors: 18 credits in interdisciplinary branches (Data Science, IoT, Cloud).
  - Certificate: 30-hour value-added certificate courses (GenAI, AWS Cloud).
- **Schedules**:
  - CIA 1: Feb 16 – Feb 21, 2026
  - CIA 2: March 23 – March 28, 2026
  - CIA 3: Component Submissions by April 15, 2026
  - End Semester Exams: May 5 – May 18, 2026
  - Timetable: Day-by-day slot breakdown (Monday to Friday, 9:00 AM - 4:00 PM).
- **Mentorship**:
  - Dr. K. Saravanan: Roll numbers 1 to 23
  - Prof. Deepa V.: Roll numbers 24 to 46
  - Dr. Praveen Kumar: Roll numbers 47 to 68

---

## 3. Member-wise Rule Specification

### Sasmita (5 Intents)
| ID | Problem Statement | Regex Pattern | RE Concepts Used | Dynamic Response Strategy |
|---|---|---|---|---|
| Q1 | Classroom Location Retrieval | `\b(?:where is|which room|location of).*(?:classroom|class room|class location|our class|room)\b` | Non-capturing group `(?:...)`, word boundary `\b`, wildcard `.*` | Returns assigned room, floor, and block. |
| Q5 | Class Timetable Retrieval | `\b(?:timetable|schedule|routine)(?:\s+(?:for|on)?\s*(?P<day>monday\|tuesday\|wednesday\|thursday\|friday\|today))?\b` | Named group `(?P<day>...)`, optional group `?`, word boundary `\b` | Extracts day; returns day's schedule or full weekly timetable if day omitted. |
| Q8 | Open Elective Information Retrieval | `\b(?:what are|which|explain|tell me about\|list)?\s*(?:the\s*)?open electives?\b` | Optional quantifiers `?`, character class `s?` | Lists all available open electives with descriptions. |
| Q14 | CIA Schedule Information Retrieval | `\b(?:when (?:are\|is)\|what is the)?\s*cia\s*(?P<cia_num>[1-3])?\s*(?:schedule\|dates?\|exam)?\b` | Character class `[1-3]`, named group `(?P<cia_num>...)` | Extracts CIA number; displays specific CIA dates or all CIAs. |
| Q17 | Subject Syllabus Retrieval | `\b(?:syllabus\|units?)(?:\s+(?P<unit>\d+))?\s*(?:of\|for\|in)\s+(?P<subject>\w+)\b` | Named groups `(?P<unit>\d+)` and `(?P<subject>\w+)`, `re.split` | Dynamically extracts subject code and optional unit; returns units or specific unit details. |

### Joshiny (5 Intents)
| ID | Problem Statement | Regex Pattern | RE Concepts Used | Dynamic Response Strategy |
|---|---|---|---|---|
| Q2 | Class Teacher & Co-Class Teacher Identification | `\bwho (?:is\|handles).*(?P<role>co-class teacher\|class teacher\|section)\b` | Named group `(?P<role>...)`, alternation `\|` | Extracts whether user asked for class teacher or co-class teacher; returns name and contact. |
| Q6 | Faculty Location & Contact Retrieval | `\b(?:where is\|cabin of\|contact\|reach\|find)\s+(?:prof(?:essor)?\|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+?)(?:'s\|\s+cabin\|\s+contact\|\?\|$)\b` | Named group `(?P<faculty>...)`, lazy quantifier `+?`, character class `[a-zA-Z\s]` | Extracts faculty name; dynamically searches knowledge base and returns cabin and extension. |
| Q9 | Global Elective Subject & Student Enrollment | `\b(?:enrollment\|enrolled\|students? in)\s+global elective\s*(?P<elective>[a-zA-Z\s]+)?\b` | Named group `(?P<elective>...)`, optional matching | Returns enrollment count and sample registered students for specified global elective. |
| Q15 | Sports Representative Identification | `\bwho (?:is\|handles).*(?:sports (?:representative\|rep\|cr)\|sports for our class)\b` | Non-capturing group `(?:...)`, nested alternation | Identifies sports CR query; returns name, contact, and sports desk details. |
| Q20 | Department Information Retrieval | `\bwho is (?:our\|the)\s+(?P<title>hod\|head of department\|program coordinator\|year coordinator)\b` | Named capturing group `(?P<title>...)`, alternation | Resolves leadership title and returns name, designation, and office room. |

### Vedant (5 Intents)
| ID | Problem Statement | Regex Pattern | RE Concepts Used | Dynamic Response Strategy |
|---|---|---|---|---|
| Q3 | Class Representative (CR) Information | `\bwho (?:is\|are\|represents).*(?P<rep>cr|class representative|class reps?)\b` | Named group `(?P<rep>...)`, quantifier `?` | Returns names, roll numbers, and contact details of both CRs. |
| Q7 | Global Elective Information Retrieval | `\b(?:what are\|which\|explain\|tell me about\|list)?\s*(?:the\s*)?global electives?\b` | Optional grouping `?`, character class `s?` | Lists all offered global electives, credit weightage, and offering department. |
| Q10 | Open Elective Subject & Student Enrollment | `\b(?:enrollment\|enrolled\|selected\|students? in)\s+open elective\s*(?P<elective>[a-zA-Z\s]+)?\b` | Named group `(?P<elective>...)`, character class `[a-zA-Z\s]` | Returns enrollment figures and status for the requested open elective. |
| Q11 | Honours Program Information Retrieval | `\b(?:what is\|how to pursue\|tell me about\|details on\|eligibility for)?\s*(?:the\s*)?honours?(?:\s+program)?\b` | Quantifiers `?`, word boundary `\b` | Explains honours program criteria, extra credits (20), CGPA cutoff (7.5), and application process. |
| Q16 | Examination Schedule Retrieval | `\b(?:when (?:are\|is)\|what is)\s+(?:the\s*)?(?P<exam_type>end sem\|final\|mid sem\|examination\|exam)\s*(?:schedule\|timetable\|dates?)?\b` | Named group `(?P<exam_type>...)`, alternation | Extracts exam type; returns examination dates, timing, and hall ticket notification. |

### Rachel (6 Intents)
| ID | Problem Statement | Regex Pattern | RE Concepts Used | Dynamic Response Strategy |
|---|---|---|---|---|
| Q4 | Class Strength Information Retrieval | `\b(?:how many students\|class strength\|strength of class\|how many people)\b` | Alternation of phrases, word boundaries | Outputs total strength (68), breakdown of boys (42) and girls (26). |
| Q12 | Minor Program Information Retrieval | `\b(?:what (?:are\|is)\|how do\|which\|tell me about)?\s*(?:the\s*)?minors?(?:\s+program)?\b` | Non-capturing groups `(?:...)`, optional `?` | Details minor degree structure, 18 credits required, and partner departments. |
| Q13 | Certificate Program Information Retrieval | `\b(?:what\|how\|tell me about\|which)?\s*certificate\s*(?:programs?\|courses?)\b` | Quantifiers `?`, alternation `programs?\|courses?` | Details certificate courses offered by SET, 30 hours duration, certification bodies. |
| Q18 | Subject Faculty Identification | `\b(?:who teaches\|which faculty handles\|subject teacher for\|who takes)\s+(?P<subject>\w+)\b` | Named group `(?P<subject>\w+)` | Dynamically extracts subject code; looks up assigned teacher and cabin. |
| Q19 | Course Credit Information Retrieval | `\b(?:how many credits\|credits? (?:for\|of)\|credit value of)\s+(?P<subject>\w+)\b` | Named group `(?P<subject>\w+)`, quantifier `?` | Dynamically extracts subject code; returns credit count and lecture-tutorial-practical breakdown. |
| Q21 | Mentor & Mentee Information Retrieval | `\b(?:mentor for\s*(?:roll\s*)?(?P<roll>\d+)\|mentees? (?:under\|of)\s*(?:prof(?:essor)?\|dr\.?)\s*(?P<faculty>[a-zA-Z\s]+)\|who is my mentor)\b` | Multi-branch named groups `(?P<roll>\d+)` vs `(?P<faculty>[a-zA-Z\s]+)` | If roll number given, outputs assigned mentor; if faculty given, outputs assigned mentee batch. |

---

## 4. Default / Fallback Handling
When user input does not match any registered regular expression:
1. Returns a polite notification: *"I'm sorry, I couldn't identify the specific classroom inquiry."*
2. Dynamically suggests 4-5 example queries covering multiple members' areas (e.g., *"Try asking: 'Where is our classroom?', 'Who is our class teacher?', 'What is the syllabus for AI?', 'When are the CIAs?'"*).
3. Offers a `help` command that prints all 21 supported query patterns grouped by team member.

---

## 5. Verification Plan
- `test_chatbot.py` script running automated tests against all 21 intents.
- Validates that:
  - Each rule triggers the correct intent.
  - Named capturing groups are correctly populated.
  - Dynamic answers are generated without exceptions.
  - Preprocessing with `re.sub` properly handles uppercase, punctuation, and filler phrases.
  - Token splitting with `re.split` properly parses multi-part arguments.
  - Fallback logic triggers for unrecognized queries.
