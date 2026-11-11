"""In-memory Knowledge Base for Christ University B.Tech CS AIML Section C."""

KNOWLEDGE_BASE = {
    "class_info": {
        "section": "6 B.Tech CS AIML-C",
        "room": "Room 412",
        "floor": "4th Floor",
        "block": "Block II",
        "strength": {
            "total": 68,
            "boys": 42,
            "girls": 26,
        },
    },
    "leadership": {
        "class_teacher": {
            "name": "Dr. K. Saravanan",
            "cabin": "Cabin 305, Block II (3rd Floor)",
            "email": "saravanan.k@christuniversity.in",
            "phone_ext": "4123",
        },
        "co_class_teacher": {
            "name": "Prof. Deepa V.",
            "cabin": "Cabin 210, Block II (2nd Floor)",
            "email": "deepa.v@christuniversity.in",
            "phone_ext": "4110",
        },
        "cr": [
            {"name": "Rahul M.", "contact": "rahul.m@cs.christuniversity.in", "roll": "2362001"},
            {"name": "Ananya Sharma", "contact": "ananya.s@cs.christuniversity.in", "roll": "2362002"},
        ],
        "sports_cr": {
            "name": "Rohan Gowda",
            "contact": "rohan.g@cs.christuniversity.in",
            "role": "Sports Class Representative",
            "desk": "Sports Directorate, Ground Floor, Central Block",
        },
        "department": {
            "hod": "Dr. Balakrishnan R. (Department of Computer Science & Engineering)",
            "program_coordinator": "Dr. Smitha Rao (B.Tech CS AIML Coordinator)",
            "year_coordinator": "Dr. Suresh N. (3rd Year B.Tech Coordinator)",
            "office": "Room 101, Ground Floor, Block II",
        },
    },
    "subjects": {
        "ai": {
            "full_name": "Artificial Intelligence",
            "faculty": "Dr. K. Saravanan",
            "credits": 4,
            "structure": "3 Lectures + 2 Practical Hours (L-T-P: 3-0-2)",
            "units": [
                "Unit 1: Problem Solving, State Space Search, Heuristic Search (A*, AO*)",
                "Unit 2: Knowledge Representation, First Order Logic, Semantic Networks",
                "Unit 3: Probabilistic Reasoning, Bayesian Networks, Hidden Markov Models",
                "Unit 4: Machine Learning Fundamentals, Decision Trees, Reinforcement Learning",
                "Unit 5: Planning and Natural Language Understanding Basics",
            ],
        },
        "dbms": {
            "full_name": "Database Management Systems",
            "faculty": "Prof. Deepa V.",
            "credits": 3,
            "structure": "3 Lectures + 0 Practical Hours (L-T-P: 3-0-0)",
            "units": [
                "Unit 1: ER Modeling, Relational Model Concepts and Constraints",
                "Unit 2: Relational Algebra, Calculus, and Advanced SQL Queries",
                "Unit 3: Functional Dependencies and Normalization (1NF through BCNF)",
                "Unit 4: Transaction Processing, ACID Properties, Concurrency Control Protocols",
                "Unit 5: Storage Structures, Indexing (B-Trees, B+ Trees), and Query Optimization",
            ],
        },
        "nlp": {
            "full_name": "Natural Language Programming",
            "faculty": "Dr. Praveen Kumar",
            "credits": 4,
            "structure": "3 Lectures + 2 Lab Hours (L-T-P: 3-0-2)",
            "units": [
                "Unit 1: Introduction to NLP, Regular Expressions, Tokenization, Morphology",
                "Unit 2: Language Modeling, N-grams, Part-of-Speech Tagging",
                "Unit 3: Syntactic Parsing, Context-Free Grammars, Dependency Parsing",
                "Unit 4: Semantic Analysis, Word Embeddings (Word2Vec, GloVe), WordNet",
                "Unit 5: Sequence Models (RNN, LSTM, Transformers) and Rule-Based Chatbots",
            ],
        },
        "ml": {
            "full_name": "Machine Learning",
            "faculty": "Dr. Rekha N.",
            "credits": 4,
            "structure": "3 Lectures + 2 Lab Hours (L-T-P: 3-0-2)",
            "units": [
                "Unit 1: Supervised Learning, Linear Regression, Logistic Regression",
                "Unit 2: Support Vector Machines and Kernel Methods",
                "Unit 3: Ensemble Learning (Random Forests, Gradient Boosting)",
                "Unit 4: Unsupervised Learning, Clustering (K-Means, Hierarchical), PCA",
                "Unit 5: Neural Networks, Backpropagation, and Model Evaluation",
            ],
        },
    },
    "electives": {
        "global": {
            "quantum computing": {"code": "GE601", "credits": 3, "dept": "Physics/CSE", "enrolled_count": 24, "sample_students": ["Aditya V.", "Kavya R.", "Nikhil P."]},
            "robotics and automation": {"code": "GE602", "credits": 3, "dept": "Mechanical", "enrolled_count": 22, "sample_students": ["Harish B.", "Pooja S.", "Tarun K."]},
            "cyber forensics": {"code": "GE603", "credits": 3, "dept": "IT & Cyber", "enrolled_count": 22, "sample_students": ["Gaurav M.", "Sneha T.", "Varun D."]},
        },
        "open": {
            "digital marketing": {"code": "OE601", "credits": 3, "dept": "School of Business", "enrolled_count": 32, "sample_students": ["Aman J.", "Bhavana K.", "Chetan L."]},
            "financial literacy": {"code": "OE602", "credits": 3, "dept": "Commerce", "enrolled_count": 20, "sample_students": ["Divya N.", "Farhan Q.", "Gita S."]},
            "creative writing": {"code": "OE603", "credits": 3, "dept": "English & Languages", "enrolled_count": 16, "sample_students": ["Isha M.", "Karan W.", "Lata V."]},
        },
    },
    "programs": {
        "honours": {
            "title": "B.Tech Honours in CS AIML",
            "extra_credits": 20,
            "duration": "Semesters 5 to 8 (5 credits per semester)",
            "eligibility": "Minimum 7.5 CGPA with zero standing backlogs",
            "registration": "Apply via KP Portal during odd semester registration",
        },
        "minors": {
            "title": "Interdisciplinary Minor Degree",
            "extra_credits": 18,
            "options": ["Data Science (Stats Dept)", "Internet of Things (ECE Dept)", "Financial Technology (Commerce)"],
            "eligibility": "Minimum 7.0 CGPA",
            "registration": "Open in 4th and 5th semester",
        },
        "certificate": {
            "title": "Value Added Certificate Courses",
            "duration": "30 Contact Hours (1 Credit equivalent)",
            "current_offerings": [
                "Generative AI & LLM Application Development (Industry Partner: AWS)",
                "Full-Stack Web3 & Blockchain (Industry Partner: Polygon)",
                "Applied Deep Learning for Computer Vision (Industry Partner: NVIDIA DLI)",
            ],
            "registration": "Register through Office of Student Affairs / KP portal",
        },
    },
    "schedules": {
        "cia": {
            "1": "Feb 16, 2026 to Feb 21, 2026 (Written Exam - 25 Marks per subject)",
            "2": "March 23, 2026 to March 28, 2026 (Mid-Sem Written Exam - 50 Marks converted)",
            "3": "April 10, 2026 to April 15, 2026 (Component 3: Assignments & Mini Project)",
        },
        "exam": {
            "end_sem": "May 5, 2026 to May 18, 2026 (Theory Exams: 9:30 AM - 12:30 PM)",
            "practicals": "April 24, 2026 to April 30, 2026 (Lab Exams)",
        },
        "timetable": {
            "monday": "09:00 AI | 10:00 DBMS | 11:15 NLP | 12:15 Lunch | 01:15-03:15 NLP Lab",
            "tuesday": "09:00 ML | 10:00 AI | 11:15 Global Elective | 12:15 Lunch | 01:15-03:15 AI Lab",
            "wednesday": "09:00 Open Elective | 10:00 DBMS | 11:15 ML | 12:15 Lunch | 01:15-03:15 ML Lab",
            "thursday": "09:00 NLP | 10:00 Global Elective | 11:15 AI | 12:15 Lunch | 01:15 Library / Seminar",
            "friday": "09:00 DBMS | 10:00 ML | 11:15 Open Elective | 12:15 Lunch | 01:15-03:15 Project Work",
        },
    },
    "mentors": {
        "groups": [
            {"mentor": "Dr. K. Saravanan", "range": (1, 23), "count": 23, "cabin": "Cabin 305, Block II"},
            {"mentor": "Prof. Deepa V.", "range": (24, 46), "count": 23, "cabin": "Cabin 210, Block II"},
            {"mentor": "Dr. Praveen Kumar", "range": (47, 68), "count": 22, "cabin": "Cabin 312, Block II"},
        ],
    },
}
