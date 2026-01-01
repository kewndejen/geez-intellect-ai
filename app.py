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
# 1. IMPERIAL PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Sovereign UI (Emerald, Gold & White Text)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    
    .stApp { background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); }

    /* Force ALL text to be White or Gold for perfect visibility */
    p, span, label, div, .stMarkdown, .stChatMessage p, .stSelectbox label { 
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

    /* Sovereign Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #FFFFFF !important;
        height: 3.5em; width: 100%; transition: 0.4s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px #FFD700; }

    /* Chat Input Fix */
    [data-testid="stChatInput"] { background-color: #ffffff !important; border-radius: 15px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; }

    .auth-box { background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; border: 1px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SESSION STATE (Storage & Auth)
# ---------------------------------------------------------
if 'users' not in st.session_state: st.session_state.users = {"admin": "kewn123"}
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'username' not in st.session_state: st.session_state.username = ""
if 'chat_history' not in st.session_state: st.session_state.chat_history = {}

# ---------------------------------------------------------
# 3. AI SOVEREIGN ENGINE (Ultra-Resilient Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም!")
    st.stop()

def ask_ai_master(prompt, context="", file_data=None, mime=None):
    # የሚሰሩ ሞዴሎች በቅደም ተከተል (Fallback list)
    models = ["gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"]
    full_prompt = f"System: You are 'Ge'ez Scholar AI' created by Deacon Kewn Dejen. Context: {context}\n\nQuestion: {prompt}"
    
    for m_name in models:
        try:
            model = genai.GenerativeModel(model_name=m_name)
            # 429 ገደብ ቢመጣ 3 ጊዜ ደጋግሞ ይሞክራል (Wait and Retry)
            for attempt in range(3):
                try:
                    if file_data and mime:
                        response = model.generate_content([full_prompt, {'mime_type': mime, 'data': file_data}])
                    else:
                        response = model.generate_content(full_prompt)
                    return response.text
                except Exception as e:
                    if "429" in str(e):
                        time.sleep(7) # 7 ሰከንድ ታግሶ ይደግማል
                        continue
                    raise e
        except:
            continue
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን መክፈት አልቻሉም። እባክዎ ጥቂት ሰከንዶች ቆይተው ገጹን Refresh ያድርጉ።"

# ---------------------------------------------------------
# 4. FILE PARSERS
# ---------------------------------------------------------
def parse_doc(file):
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
        st.markdown("<div class='auth-box'>", unsafe_allow_html=True)
        mode = st.radio("Access Control", ["Login", "Register"])
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Enter Portal"):
            if mode == "Login":
                if u in st.session_state.users and st.session_state.users[u] == p:
                    st.session_state.logged_in, st.session_state.username = True, u
                    st.rerun()
                else: st.error("ስህተት!")
            else:
                st.session_state.users[u] = p
                st.success("Registered! Now Login.")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()
    else:
        st.write(f"👑 Welcome: **{st.session_state.username}**")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("---")
    tool = st.radio("Imperial Tools", ["Document Intelligence", "Visual OCR Lab", "Voice Assistant"])

# ---------------------------------------------------------
# 6. MAIN SYSTEM
# ---------------------------------------------------------
if st.session_state.logged_in:
    st.title(f"{tool} Center")

    # Storage & File Context
    with st.expander("📁 Imperial Vault (PDF, DOCX, Image, Video)"):
        up_file = st.file_uploader("Upload to AI Memory", type=['pdf', 'docx', 'html', 'png', 'jpg', 'jpeg', 'mp4'])
        doc_context, f_bytes, f_mime = "", None, None
        if up_file:
            if up_file.type in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/html"]:
                doc_context = parse_doc(up_file)
                st.success("Document Memorized by AI.")
            else:
                f_bytes, f_mime = up_file.read(), up_file.type
                st.info("Media Ready for Analysis.")

    # History Logic
    user_key = st.session_state.username
    if user_key not in st.session_state.chat_history: st.session_state.chat_history[user_key] = []

    for chat in st.session_state.chat_history[user_key]:
        with st.chat_message(chat["role"]): st.markdown(chat["content"])

    voice_on = st.checkbox("🎙️ Enable Voice Response")
    
    if prompt := st.chat_input("ለሊቁ ጥያቄዎን ያቅርቡ..."):
        st.session_state.chat_history[user_key].append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("ሊቁ መዛግብቱን እያመሳከሩ ነው..."):
                answer = ask_ai_master(prompt, doc_context, f_bytes, f_mime)
                st.markdown(answer)
                
                if voice_on:
                    try:
                        tts = gTTS(text=answer[:300], lang='am')
                        audio_fp = io.BytesIO()
                        tts.write_to_fp(audio_fp)
                        st.audio(audio_fp, format='audio/mp3')
                    except: pass
                
                st.session_state.chat_history[user_key].append({"role": "assistant", "content": answer})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b></p>", unsafe_allow_html=True)
