🎙️ Voice Chatbot (Streamlit + LangChain)

A simple and interactive voice-enabled chatbot built using Streamlit, LangChain, OpenAI, speech recognition, and text-to-speech.
You can talk to the bot using your microphone and hear responses using gTTS audio.

🚀 Features

🎤 Voice Input using Google Speech Recognition

🤖 AI Responses using LangChain + OpenAI

🔊 Voice Output using gTTS

💬 Chat-style Interface with user & bot bubbles

🌐 Streamlit Web App with clean UI

🔁 Press a button to replay the bot's last answer

🧠 Stores full chat history

📦 Tech Stack

Python

Streamlit

LangChain

OpenAI API

SpeechRecognition

pyttsx3 / gTTS

dotenv

🛠️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Princekr-coder/streamlit-voice-chatbot.git
cd streamlit-voice-chatbot

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

3️⃣ Install Dependencies

Create a file requirements.txt (if not already made):

streamlit
speechrecognition
gtts
pyttsx3
python-dotenv
langchain
langchain-openai
openai


Then install:

pip install -r requirements.txt

4️⃣ Add Your OpenAI API Key

Create a .env file:

OPENAI_API_KEY=your_api_key_here

▶️ Running the App
streamlit run app2.py


Then open the local URL in your browser.

📁 Project Structure
├── app.py
├── README.md
├── requirements.txt
└── .env

🧩 How It Works

User clicks the mic → app records audio

Google Speech Recognition converts audio → text

Text sent to LangChain → OpenAI model

AI generates response

Response shown in chat bubble

gTTS converts text → audio

Streamlit plays the audio

🙌 Author

Prince Kumar
Voice-enabled AI assistant built using Streamlit + LangChain.
