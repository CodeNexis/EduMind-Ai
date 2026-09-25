import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import PyPDF2

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title(" EduMind AI")

# Chatbot
question = st.text_input("Ask a question")

if st.button("Ask"):
    if question:
        response = model.generate_content(question)
        st.write(response.text)

# Notes Summarizer
st.header("Notes Summarizer")

notes = st.text_area("Paste your notes here")

if st.button("Generate Summary"):

    prompt = f"""
    Summarize the following notes into short bullet points:

    {notes}
    """

    response = model.generate_content(prompt)

    st.write(response.text)
# Quiz Generator

st.header("Quiz Generator")

quiz_topic = st.text_input("Enter Quiz Topic")

if st.button("Generate Quiz"):

    prompt = f"""
    Create 5 multiple-choice questions on {quiz_topic}.

    Requirements:
    - 4 options for each question
    - Show the correct answer
    - Beginner friendly
    """

    response = model.generate_content(prompt)

    st.write(response.text)
st.header("Concept Explainer")

topic = st.text_input("Enter a Concept")

if st.button("Explain Concept"):

    prompt = f"""
    Explain {topic} in simple language.
    Give examples and important points.
    """

    response = model.generate_content(prompt)

    st.write(response.text)
st.header("PDF Summarizer")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    if st.button("Summarize PDF"):

        prompt = f"""
        Summarize the following PDF notes.
        Use bullet points.
        Highlight important concepts.

        {text[:5000]}
        """

        response = model.generate_content(prompt)

        st.write(response.text)