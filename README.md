EduMind 📚🤖
EduMind is an AI-powered learning application that helps students understand and study academic content more effectively. It uses Python, Streamlit, and Generative AI to provide interactive learning features such as question answering, summarization, quizzes, and concept explanations.
🚀 Features
💬 AI Question & Answer – Ask questions and get AI-generated explanations.
📄 PDF Summarization – Upload study material and generate concise summaries.
📝 Text Summarization – Convert lengthy notes into easy-to-understand summaries.
🧠 Concept Explanation – Get simple explanations for difficult topics.
❓ Quiz Generation – Generate questions to test your understanding.
✨ Prompt-Based Learning – Interact with the AI using customized prompts.
🎓 Student-Friendly Interface – Simple and interactive Streamlit interface.
🛠️ Technologies Used
Python
Streamlit
Google Gemini API
Generative AI / LLM
PyPDF2
python-dotenv
📂 Project Structure
EduMind/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

Note: The .env file should not be uploaded to GitHub because it contains the API key.
⚙️ Installation and Setup
1. Clone the Repository
git clone https://github.com/your-username/EduMind.git

2. Open the Project
cd EduMind

3. Create a Virtual Environment
python -m venv venv

4. Activate the Virtual Environment
Windows:
venv\Scripts\activate

5. Install Required Packages
pip install -r requirements.txt

6. Configure the API Key
Create a .env file in the project folder:
GEMINI_API_KEY=your_api_key_here

Replace your_api_key_here with your actual API key.
7. Run the Application
streamlit run app.py

The application will open in your browser.
🔐 Environment Variables
The project uses environment variables to keep API credentials secure.
Example:
GEMINI_API_KEY=your_api_key_here

📌 Example Use Cases
Students can use EduMind to:
Understand difficult concepts
Summarize lengthy study materials
Generate quizzes for practice
Ask questions about academic topics
Create quick revision notes
Learn topics through interactive AI explanations
🎯 Project Objective
The main objective of EduMind is to build an interactive AI-based study companion that makes learning easier by providing personalized explanations, summaries, and practice materials using Generative AI.
🔮 Future Enhancements
User login and authentication
Chat history
Subject-wise organization
Personalized study plans
Voice-based interaction
Multiple document support
Progress tracking
Question-answering directly from uploaded PDFs
👩‍💻 Author
Vattikuti Deepika
B.Tech – Artificial Intelligence and Machine Learning
CMR Engineering College
