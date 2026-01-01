import streamlit as st
import google.generativeai as genai
import time
import os
import datetime
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

# Professional World-Class UI (Emerald & Gold)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    .stApp { background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important; border-right: 4px solid #FFD700; }
    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important; border-radius: 12px !important;
    }
    .auth-card { background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; border: 1px solid #FFD700; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. AUTHENTICATION & STORAGE LOGIC
# ---------------------------------------------------------
if 'users' not in st.session_state: st.session_state.users = {"admin": "kewn123"}
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'username' not in st.session_state: st.session_state.username = ""
if 'chat_history' not in st.session_state: st.session_state.chat_history = {}

def login_user(u, p):
    if u in st.session_state.users and st.session_state.users[u] == p:
        st.session_state.logged_in = True
        st.session_state.username = u
        return True
    return False

def register_user(u, p):
    if u not in st.session_state.users:
        st.session_state.users[u] = p
        return True
    return False

# ---------------------------------------------------------
# 3. FILE PROCESSING (PDF, DOCX, HTML)
# ---------------------------------------------------------
def extract_text(file):
    fname = file.name.lower()
    if fname.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        return "".join([page.extract_text() for page in pdf_reader.pages])
    elif fname.endswith('.docx'):
        doc = Document(file)
        return "".join([p.text for p in doc.paragraphs])
    elif fname.endswith('.html'):
        return file.read().decode("utf-8")
    return ""

# ---------------------------------------------------------
# 4. AI ENGINE (FAIL-SAFE)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key Missing!")
    st.stop()

def ask_ai(prompt, context_text="", file_bytes=None, mime_type=None):
    model = genai.GenerativeModel("gemini-1.5-flash")
    full_prompt = f"Context from Document: {context_text}\n\nUser Question: {prompt}"
    
    if file_bytes and mime_type:
        response = model.generate_content([full_prompt, {'mime_type': mime_type, 'data': file_bytes}])
    else:
        response = model.generate_content(full_prompt)
    return response.text

# ---------------------------------------------------------
# 5. SIDEBAR: AUTH & PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>")
    
    if not st.session_state.logged_in:
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
        tab_login, tab_reg = st.tabs(["Login", "Register"])
        with tab_login:
            u = st.text_input("Username", key="l_u")
            p = st.text_input("Password", type="password", key="l_p")
            if st.button("Login"):
                if login_user(u, p): st.rerun()
                else: st.error("Invalid credentials")
        with tab_reg:
            nu = st.text_input("New Username", key="r_u")
            np = st.text_input("New Password", type="password", key="r_p")
            if st.button("Register"):
                if register_user(nu, np): st.success("Registered! Please Login.")
                else: st.error("User exists")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()
    else:
        st.write(f"👑 Welcome, **{st.session_state.username}**")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ", ["🧠 AI Labs", "📜 Archives", "🎓 University", "💰 Strategic"])
    tool = st.radio("Tools", ["Document Analyzer", "Voice Assistant", "Manuscript OCR", "History Vault"])

# ---------------------------------------------------------
# 6. MAIN CONTENT: FILE STORAGE & AI
# ---------------------------------------------------------
if st.session_state.logged_in:
    st.markdown(f"<h1>{tool} Center</h1>", unsafe_allow_html=True)

    # File Storage & Upload
    with st.expander("📁 Upload & Store Documents (PDF, DOCX, Images, Video)"):
        uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'html', 'png', 'jpg', 'jpeg', 'mp4'])
        doc_context = ""
        file_payload = None
        m_type = None

        if uploaded_file:
            if uploaded_file.type in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                doc_context = extract_text(uploaded_file)
                st.success(f"{uploaded_file.name} Loaded into AI Memory.")
            elif uploaded_file.type.startswith("image/"):
                file_payload = uploaded_file.read()
                m_type = uploaded_file.type
                st.image(uploaded_file, width=300)
            elif uploaded_file.type.startswith("video/"):
                file_payload = uploaded_file.read()
                m_type = uploaded_file.type
                st.video(uploaded_file)

    # Chat Interface
    if st.session_state.username not in st.session_state.chat_history:
        st.session_state.chat_history[st.session_state.username] = []

    # Display History
    for chat in st.session_state.chat_history[st.session_state.username]:
        with st.chat_message(chat["role"]): st.markdown(chat["content"])

    # Input (Text or Voice placeholder)
    prompt = st.chat_input("Ask the AI about your documents or Ge'ez wisdom...")
    
    # Voice Input Simulation
    voice_on = st.checkbox("🎙️ Enable Voice Mode (Read Aloud)")

    if prompt:
        st.session_state.chat_history[st.session_state.username].append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
                answer = ask_ai(prompt, doc_context, file_payload, m_type)
                st.markdown(answer)
                
                if voice_on:
                    tts = gTTS(text=answer, lang='en') # Amharic support can be added if gTTS updated
                    audio_fp = io.BytesIO()
                    tts.write_to_fp(audio_fp)
                    st.audio(audio_fp, format='audio/mp3')

                st.session_state.chat_history[st.session_state.username].append({"role": "assistant", "content": answer})

# Footer
st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Deacon Kewn Dejen</b><br>© 2026 Sovereign Edition</p>", unsafe_allow_html=True)
