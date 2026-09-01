import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader

# 1. Page Configuration & Theme
st.set_page_config(page_title="GenAI Learning Mentor", page_icon="🎓", layout="wide")
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 2. Sidebar: Document Upload (RAG Data Source)
st.sidebar.title("📚 Course Materials")
uploaded_file = st.sidebar.file_uploader("Upload Notes or Syllabus (PDF)", type=["pdf"])

pdf_context = ""
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_context += text + "\n"
    st.sidebar.success(f"Loaded: {uploaded_file.name}")

# 3. Main Dashboard UI
st.title("🎓 GenAI Learning Mentor")
st.caption("Your personalized exam coach powered by LLMs & RAG")

tab1, tab2, tab3 = st.tabs(["💬 Ask Mentor", "📝 Study Roadmap", "🎯 Practice Quiz"])

# Function to query LLM
def query_mentor(system_instruction, user_prompt):
    context_addon = f"\n\nContext from uploaded notes:\n{pdf_context[:4000]}" if pdf_context else ""
    full_prompt = user_prompt + context_addon
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": full_prompt}
        ]
    )
    return response.choices[0].message.content

# --- Tab 1: Q&A Mentor ---
with tab1:
    user_query = st.text_input("Ask any concept, question, or doubt:")
    if st.button("Get Answer", type="primary"):
        if user_query:
            with st.spinner("Analyzing and preparing explanation..."):
                ans = query_mentor(
                    "You are an expert academic tutor. Explain concepts clearly, step-by-step, with brief examples suitable for university exams.",
                    user_query
                )
                st.markdown(ans)
        else:
            st.warning("Please type a question first.")

# --- Tab 2: Study Roadmap ---
with tab2:
    subject = st.text_input("Enter subject or topics to cover:")
    days = st.slider("Exam preparation timeline (Days):", 1, 30, 7)
    if st.button("Generate Study Plan"):
        if subject:
            with st.spinner("Drafting roadmap..."):
                prompt = f"Create a structured {days}-day revision roadmap for the subject '{subject}'. Focus on high-weightage topics and daily goals."
                roadmap = query_mentor("You are an academic mentor specializing in exam strategy.", prompt)
                st.markdown(roadmap)
        else:
            st.warning("Please enter a subject name.")

# --- Tab 3: Quiz Generator ---
with tab3:
    quiz_topic = st.text_input("Enter topic for quick evaluation:")
    if st.button("Generate 3-Question Practice Quiz"):
        if quiz_topic:
            with st.spinner("Generating questions..."):
                prompt = f"Generate 3 multiple-choice practice questions on '{quiz_topic}' with 4 options each, followed by the correct answers and brief explanations at the end."
                quiz = query_mentor("You are an exam question paper designer.", prompt)
                st.markdown(quiz)
        else:
            st.warning("Please enter a quiz topic.")