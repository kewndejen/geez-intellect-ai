import streamlit as st
import google.generativeai as genai
import time
import os
from PIL import Image
import PyPDF2
from docx import Document
from gtts import gTTS
import io

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (Force Light/Dark Contrast)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional UI: Force Text Visibility (White/Gold on Dark Green)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    
    /* Background: Deep Emerald */
    .stApp { 
        background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); 
    }

    /* Force ALL text to be White or Gold */
    p, span, label, div, .stMarkdown, .stChatMessage p { 
        color: #ffffff !important; 
        font-family: 'Montserrat', sans-serif;
        font-size: 1.1rem;
    }

    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important;
        border-right: 4px solid #FFD700;
    }
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label {
        color: #FFD700 !important;
        font-weight: bold;
    }

    /* Sovereign Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; 
        font-weight: 900 !important;
        border-radius: 12px !important;
        border: 2px solid #FFFFFF !important;
        height: 3.5em; width: 100%;
    }
    
    /* Chat Input Fix (Black text on White background) */
    [data-testid="stChatInput"] { 
        background-color: #ffffff !important; 
        border: 3px solid #FFD700 !important;
        border-radius: 15px !important;
    }
    [data-testid="stChatInput"] textarea { 
        color: #000000 !important; 
        font-weight: bold !important;
    }

    /* Auth Cards */
    .auth-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px; border-radius: 15px;
        border: 1px solid #FFD700;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SESSION STATE (Auth, History, Storage)
# ---------------------------------------------------------
if 'users' not in st.session_state: st.session_state.users = {"admin": "kewn123"}
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'username' not in st.session_state: st.session_state.username = ""
if 'user_history' not in st.session_state: st.session_state.user_history = {}

# ---------------------------------------------------------
# 3. AI SOVEREIGN ENGINE (Resilient Model Switching)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም!")
    st.stop()

def ask_ai_master(prompt, context="", file_data=None, mime=None):
    # የሚሰሩ ሞዴሎች ቅደም ተከተል
    models_to_try = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash"]
    full_prompt = f"System: You are 'Ge'ez Scholar AI' created by Deacon Kewn Dejen. Knowledge Context: {context}\n\nUser Question: {prompt}"
    
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name=model_name)
            # 429 ስህተት ቢመጣ 2 ጊዜ ደጋግሞ ይሞክራል
            for attempt in range(2):
                try:
                    if file_data and mime:
                        response = model.generate_content([full_prompt, {'mime_type': mime, 'data': file_data}])
                    else:
                        response = model.generate_content(full_prompt)
                    return response.text
                except Exception as e:
                    if "429" in str(e):
                        time.sleep(6)
                        continue
                    raise e
        except:
            continue
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን መክፈት አልቻሉም። እባክዎ ጥቂት ሰከንዶች ቆይተው ገጹን Refresh ያድርጉ።"

# ---------------------------------------------------------
# 4. FILE PROCESSOR (PDF, DOCX, HTML)
# ---------------------------------------------------------
def process_uploaded_file(file):
    name = file.name.lower()
    try:
        if name.endswith('.pdf'):
            reader = PyPDF2.PdfReader(file)
            return " ".join([page.extract_text() for page in reader.pages])
        elif name.endswith('.docx'):
            doc = Document(file)
            return " ".join([p.text for p in doc.paragraphs])
        elif name.endswith('.html'):
            return file.read().decode("utf-8")
    except: return ""
    return ""

# ---------------------------------------------------------
# 5. SIDEBAR: AUTH & PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>")
    
    if not st.session_state.logged_in:
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
        auth_mode = st.radio("Account Access", ["Login", "Register"])
        u_input = st.text_input("Username")
        p_input = st.text_input("Password", type="password")
        
        if st.button("Enter Portal"):
            if auth_mode == "Login":
                if u_input in st.session_state.users and st.session_state.users[u_input] == p_input:
                    st.session_state.logged_in, st.session_state.username = True, u_input
                    st.rerun()
                else: st.error("ስህተት፡ የተሳሳተ መረጃ አስገብተዋል።")
            else:
                if u_input and p_input:
                    st.session_state.users[u_input] = p_input
                    st.success("አካውንት ተፈጥሯል! አሁን Login ያድርጉ።")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()
    else:
        st.markdown(f"<div style='color:#FFD700; text-align:center;'>👑 <b>Emperor {st.session_state.username}</b></div>", unsafe_allow_html=True)
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("---")
    tool = st.radio("System Tools", ["Document Intelligence", "Voice Assistant", "Manuscript OCR"])

# ---------------------------------------------------------
# 6. MAIN WORKSPACE (Storage, Chat, Voice, History)
# ---------------------------------------------------------
if st.session_state.logged_in:
    st.title(f"{tool} Center")

    # 1. File Storage & Multi-modal Input
    with st.expander("📁 Imperial Vault (PDF, DOCX, Image, Video)"):
        st.write("ፋይሎችን እዚህ ይጫኑ፤ AIው መላውን ሰነድ አጥንቶ ይመልሳል።")
        up_file = st.file_uploader("Upload to AI Memory", type=['pdf', 'docx', 'html', 'png', 'jpg', 'jpeg', 'mp4'])
        doc_context, f_bytes, f_mime = "", None, None
        
        if up_file:
            if up_file.type in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/html"]:
                doc_context = process_uploaded_file(up_file)
                st.success(f"ሰነድ '{up_file.name}' በሊቁ አእምሮ ውስጥ ተቀምጧል።")
            else:
                f_bytes, f_mime = up_file.read(), up_file.type
                st.info(f"ፋይል '{up_file.name}' ለምስል/ቪዲዮ ምርመራ ተዘጋጅቷል።")

    # 2. Chat History Logic
    user_key = st.session_state.username
    if user_key not in st.session_state.user_history:
        st.session_state.user_history[user_key] = []

    # Display History
    for chat in st.session_state.user_history[user_key]:
        with st.chat_message(chat["role"]):
            st.markdown(f"<div style='color: white;'>{chat['content']}</div>", unsafe_allow_html=True)

    # 3. Voice Logic
    voice_on = st.checkbox("🎙️ Enable Voice Response (TTS)")

    # 4. Interaction
    if prompt := st.chat_input("ለሊቁ ጥያቄዎን ያቅርቡ..."):
        # Store User Message
        st.session_state.user_history[user_key].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(f"<div style='color: white;'>{prompt}</div>", unsafe_allow_html=True)

        # AI Response
        with st.chat_message("assistant"):
            with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
                answer = ask_ai_master(prompt, doc_context, f_bytes, f_mime)
                st.markdown(f"<div style='color: #FFD700; font-weight: bold;'>{answer}</div>", unsafe_allow_html=True)
                
                # TTS (Voice)
                if voice_on:
                    try:
                        tts = gTTS(text=answer[:400], lang='en')
                        audio_io = io.BytesIO()
                        tts.write_to_fp(audio_io)
                        st.audio(audio_io, format='audio/mp3')
                    except: pass
                
                # Store AI History
                st.session_state.user_history[user_key].append({"role": "assistant", "content": answer})

# Sovereign Footer
st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b><br>© 2026 Sovereign Edition | 340 Trillion% Guaranteed</p>", unsafe_allow_html=True)
