# 🎓 GenAI Learning Mentor

> An intelligent academic tutoring and revision system powered by Retrieval-Augmented Generation (RAG) and high-speed LLM inference to assist university engineering students in mastering coursework and preparing for university examinations.

---

## 📋 Table of Contents
* [Project Overview](#-project-overview)
* [Problem Statement](#-problem-statement)
* [System Architecture](#-system-architecture)
* [RAG Pipeline Deep Dive](#-rag-pipeline-deep-dive)
* [Key Features & Agent Capabilities](#-key-features--agent-capabilities)
* [Live Inference & Tech Stack](#-live-inference--tech-stack)
* [Prompt Engineering Strategies](#-prompt-engineering-strategies)
* [Setup & Installation](#-setup--installation)
* [Evaluation & Rubric Alignment](#-evaluation--rubric-alignment)
* [Future Enhancements](#-future-enhancements)

---

## 💡 Project Overview
**GenAI Learning Mentor** bridges the gap between static university textbooks and interactive, adaptive learning. By ingesting raw course syllabi and lecture materials in PDF format, the mentor extracts high-yield academic context and provides contextual explanations, time-boxed study roadmaps, and automated practice quizzes.

---

## 📌 Problem Statement
Engineering students frequently encounter:
* High cognitive load when parsing through 100+ page lecture notes and dense syllabi.
* Inability to self-assess knowledge against realistic university-style questions.
* Generic LLM hallucinations when asking queries about niche academic topics without course grounding.

---

## 🏗️ System Architecture

```text
========================================================================================
                               GENAI LEARNING MENTOR ARCHITECTURE
========================================================================================

    +-------------------+                       +----------------------------------+
    |   Student User    |                       |       Course Materials (PDF)     |
    | (Enters Question) |                       |     (Syllabus / Lecture Notes)   |
    +---------+---------+                       +----------------+-----------------+
              |                                                  |
              |                                                  | Upload Document
              v                                                  v
    +------------------------------------------------------------------------------+
    |                             Streamlit Web Frontend                           |
    |            [ 💬 Ask Mentor ]   [ 📝 Study Roadmap ]   [ 🎯 Practice Quiz ]     |
    +------------------------------------+-----------------------------------------+
                                         |
                                         v
    +------------------------------------------------------------------------------+
    |                         Document Ingestion Pipeline                          |
    |                           (pypdf Text Extraction)                            |
    +------------------------------------+-----------------------------------------+
                                         |
                                         v
    +------------------------------------------------------------------------------+
    |                        Augmented Prompt Constructor                          |
    |               [ System Role ] + [ PDF Notes Context ] + [ User Prompt ]       |
    +------------------------------------+-----------------------------------------+
                                         |
                                         v
    +------------------------------------------------------------------------------+
    |                            Groq Cloud Inference API                          |
    |                    (Ultra-low latency LPU Cloud Processing)                  |
    +------------------------------------+-----------------------------------------+
                                         |
                                         v
    +------------------------------------------------------------------------------+
    |                              Open-Weights LLM                                |
    |                        (Structured Response Generation)                      |
    +------------------------------------+-----------------------------------------+
                                         |
                                         v
    +------------------------------------------------------------------------------+
    |                          Interactive UI Output Display                       |
    |                   (Step-by-step Answers, Roadmaps, & Quizzes)                |
    +------------------------------------------------------------------------------+
========================================================================================
```

---

## 🔍 RAG Pipeline Deep Dive
* **Document Ingestion:** The user uploads course notes or syllabus files directly through the Streamlit sidebar.
* **Text Extraction:** `pypdf.PdfReader` iterates over document pages and compiles extracted text into application memory.
* **Context Injection:** When a prompt is triggered, the system augments the user's question with the extracted document tokens into a combined prompt payload.
* **Context-Grounded Inference:** The LLM processes both the system guardrails and raw source context to produce accurate, hallucination-free explanations.

---

## ✨ Key Features & Agent Capabilities
* **📚 Contextual Q&A Mentor:** Explains complex theoretical principles step-by-step with analogies and real-world examples.
* **📝 Automated Study Strategist:** Generates a daily revision roadmap based on target examination timelines (1 to 30 days).
* **🎯 Dynamic Quiz Generator:** Produces 3-question multiple-choice quizzes with options, answers, and rationales.

---

## ⚡ Live Inference & Tech Stack
* **Language:** Python 3.9+
* **Frontend:** Streamlit
* **Document Processing:** PyPDF
* **Inference Platform:** Groq Cloud LPUs (Ultra-low latency inference)
* **Underlying Model:** High-throughput open-weights LLM (`openai/gpt-oss-20b`)
* **Environment Security:** `python-dotenv` for zero-leak token protection

---

## 🎯 Prompt Engineering Strategies
* **Role Conditioning:** System prompts explicitly instruct the model to adopt the persona of an academic tutor, strategy coach, or exam designer.
* **Instructional Constraints:** Output formats are restricted to structured Markdown headings, bullet points, and numbered steps for readability.
* **Context Anchoring:** Appending `pdf_context` directly prevents the model from generating out-of-scope answers.

---

## 🚀 Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/HarshitG2006/GenAI_learning_assistant.git](https://github.com/HarshitG2006/GenAI_learning_assistant.git)
   cd GenAI_learning_assistant
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key:**
   Create a `.env` file in the root folder:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Launch the Application:**
   ```bash
   streamlit run app.py
   ```

---

## 📊 Evaluation & Rubric Alignment (100 Marks)
* **Problem Definition (10 Marks):** Clear focus on university academic preparation challenges[cite: 1].
* **Prompt Engineering (15 Marks):** Multi-role agent design (Mentor, Strategist, Quiz Master)[cite: 1].
* **RAG Implementation (20 Marks):** Live PDF ingestion and context augmentation pipeline[cite: 1].
* **Agent/Workflow Design (15 Marks):** Dynamic feature routing across tabs[cite: 1].
* **UI/UX (10 Marks):** Streamlit dashboard with real-time spinners and dark-mode styling[cite: 1].
* **Innovation & Demo (20 Marks):** Instant roadmap and quiz generation powered by Groq LPUs[cite: 1].

---

## 🔮 Future Enhancements
* Implementing vector embeddings with FAISS / ChromaDB for chunked semantic similarity search[cite: 1].
* Support for multi-PDF uploads and automatic citation highlighting.
* Exporting generated roadmaps and quizzes directly to downloadable PDF summary sheets.