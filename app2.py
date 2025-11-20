import streamlit as st
import os
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from gtts import gTTS
import tempfile


# -------------------- SETUP --------------------
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# LangChain pipeline
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly and helpful AI assistant."),
    ("user", "Question: {question}")
])
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # change to 0 for male, 1 for female



def speak(text):
    try:
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            tts.save(tmpfile.name)
            st.audio(tmpfile.name, format="audio/mp3", autoplay=True)
    except Exception as e:
        st.error(f"Voice generation failed: {e}")



# Speech recognition
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.toast("🎤 Listening...", icon="🎧")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        st.toast(f"✅ You said: {text}", icon="💬")
        return text
    except sr.UnknownValueError:
        st.toast("❌ Sorry, I couldn't understand you.", icon="⚠️")
        return None
    except sr.RequestError:
        st.toast("⚠️ Network error. Try again later.", icon="🌐")
        return None

# -------------------- UI --------------------
st.set_page_config(page_title="Voice Chatbot", page_icon="🎙️", layout="centered")

st.markdown("""
    <style>
    .chat-bubble-user {
        background-color: #DCF8C6;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 50px 5px 100px;
        text-align: right;
        font-size: 1rem;
    }
    .chat-bubble-bot {
        background-color: #F1F0F0;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 100px 5px 50px;
        text-align: left;
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎙️ Voice Chatbot (LangChain + Streamlit)")
st.caption("Ask by typing or speaking — and hear the bot reply!")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show chat history
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-bot'>{msg['content']}</div>", unsafe_allow_html=True)

# Input area
col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    voice_button = st.button("🎙️", help="Speak your question")
with col2:
    user_input = st.chat_input("Type your message...")
with col3:
    speak_button = st.button("🔊", help="Replay last bot reply")

# Handle input
if voice_button:
    text = listen()
    if text:
        user_input = text

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = chain.invoke({'question': user_input})
    st.session_state.chat_history.append({"role": "bot", "content": response})
    st.rerun()

# Handle speak output
if speak_button and st.session_state.chat_history:
    last_msg = st.session_state.chat_history[-1]
    if last_msg["role"] == "bot":
        speak(last_msg["content"])
