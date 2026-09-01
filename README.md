# 🎓 GenAI Learning Mentor

An intelligent academic tutor and revision assistant built with Streamlit, Groq Cloud API, and RAG (Retrieval-Augmented Generation) to help university students master complex subjects and prepare for exams.

---

## 📌 Problem Statement
Students often struggle to digest lengthy textbook materials, identify high-priority exam topics, and test their understanding dynamically before university examinations. This project provides personalized, adaptive tutoring, automated study roadmaps, and instant practice quizzes anchored directly to uploaded course notes.

---

## 🏗️ Architecture & Data Flow


+-------------------+       +-----------------------+       +-------------------+
|                   |       |                       |       |                   |
|   Student User    | ----> |  Streamlit Frontend   | ----> |  PDF Context Ext. |
|  (Uploads / Query)|       |     (Interactive UI)  |       |     (pypdf)       |
+-------------------+       +-----------------------+       +-------------------+
                                                                      |
                                                                      v
+-------------------+       +-----------------------+       +-------------------+
|                   |       |                       |       |                   |
| Formatted Answer/ | <---- |   Groq Inference API  | <---- | Augmented Prompt  |
| Study Plan / Quiz |       | (LPU / Open-Weights)  |       | (System + RAG)    |
+-------------------+       +-----------------------+       +-------------------+

---

## ✨ Features

1. 📚 Dynamic RAG Document QA: Upload syllabus or lecture notes (PDF) to ground LLM responses in actual course materials.

2. 💬 Concept Explanation Agent: Clear, step-by-step academic explanations designed for theory exam scoring.

3. 📝 Automated Study Roadmaps: Generates customized multi-day revision plans targeting high-weightage topics.

4. 🎯 Practice Quiz Generator: Automatically produces multiple-choice quizzes with answers and detailed rationales.

---

## 🛠️ Tech Stack

1. Language: Python 3.9+

2. Frontend / UI: Streamlit

3. LLM Engine: Groq API (High-speed cloud inference)

4. Document Processing: PyPDF

5. Environment Management: Python-Dotenv

---

## 🚀 Setup & Installation
1. Clone the repository:

git clone https://github.com/HarshitG2006/genai-learning-mentor.git

2. Install dependencies:

pip install -r requirements.txt

3. Configure Environment Variables:
    Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here

4. Run the Application:

streamlit run app.py

---

## 🎯 Prompt Engineering & Agent Roles
1. Tutor Role: Configured via system prompts to provide step-by-step breakdowns, key definitions, and exam tips.

2. Strategist Role: Designs time-boxed revision schedules aligned with academic days.

3. Examiner Role: Generates structured multiple-choice questions with answer evaluation criteria.

---

## 🔮 Future Enhancements
1. Integration of vector databases (ChromaDB / FAISS) for dense chunk-level vector search.

2. Multi-PDF document merging and citation highlighting.

3. Support for voice input and audio flashcard generation.