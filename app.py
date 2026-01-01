import streamlit as st
import google.generativeai as genai
import time
import os
import json
import datetime
from PIL import Image
import PyPDF2
from docx import Document
from gtts import gTTS
import io

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION & STYLING
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Emerald & Gold UI Logic
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    
    .stApp { background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important; border-right: 4px solid #FFD700; }
    
    /* Sovereign Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important; border-radius: 12px !important;
        height: 3em; width: 100%; border: 1px solid #fff !important;
    }
    
    /* Login Box */
    .auth-container { background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; border: 1px solid #FFD700; }
    
    /* Chat Input */
    [data-testid="stChatInput"] { border: 2px solid #FFD700 !important; border-radius: 20px !important; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #ffffff44; margin-top: 10px; padding-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SESSION & ACCOUNT MANAGEMENT
# ---------------------------------------------------------
if 'users' not in st.session_state: st.session_state.users = {"admin": "kewn123"}
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'user' not in st.session_state: st.session_state.user = ""
if 'history' not in st.session_state: st.session_state.history = {}

def handle_login(u, p):
    if u in st.session_state.users and st.session_state.users[u] == p:
        st.session_state.logged_in = True
        st.session_state.user = u
        return True
    return False

# ---------------------------------------------------------
# 3. FILE PROCESSING (PDF, DOCX, HTML)
# ---------------------------------------------------------
def read_document(file):
    name = file.name.lower()
    content = ""
    try:
        if name.endswith('.pdf'):
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages: content += page.extract_text()
        elif name.endswith('.docx'):
            doc = Document(file)
            for para in doc.paragraphs: content += para.text + "\n"
        elif name.endswith('.html'):
            content = file.read().decode("utf-8")
    except Exception as e:
        st.error(f"Error reading file: {e}")
    return content

# ---------------------------------------------------------
# 4. AI SOVEREIGN ENGINE
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም!")

@st.cache_resource
def get_model():
    return genai.GenerativeModel("gemini-1.5-flash")

def ask_scholar_master(prompt, doc_context="", files=[]):
    model = get_model()
    # Adding instructions for the Master Expert
    system_prompt = f"You are Ge'ez Scholar AI Master, developed by Deacon Kewn Dejen. Context from uploaded files: {doc_context}. Answer the user with deep wisdom."
    
    inputs = [system_prompt, prompt]
    # Handle multimodal (images/video) if provided
    for f in files:
        if f['type'].startswith('image') or f['type'].startswith('video'):
            inputs.append({'mime_type': f['type'], 'data': f['data']})
            
    try:
        response = model.generate_content(inputs)
        return response.text
    except Exception as e:
        return f"ሊቁ ስህተት ገጠማቸው: {e}"

# ---------------------------------------------------------
# 5. SIDEBAR: ACCOUNT & TOOLS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    
    if not st.session_state.logged_in:
        st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
        mode = st.radio("Account Access", ["Login", "Register"])
        user_in = st.text_input("Username")
        pass_in = st.text_input("Password", type="password")
        if mode == "Login":
            if st.button("Enter Studio"):
                if handle_login(user_in, pass_in): st.rerun()
                else: st.error("ተሳስተዋል!")
        else:
            if st.button("Create Account"):
                st.session_state.users[user_in] = pass_in
                st.success("ተመዝግበዋል! አሁን Login ያድርጉ።")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()
    else:
        st.markdown(f"<p style='text-align:center;'>👑 Emperor: <b>{st.session_state.user}</b></p>", unsafe_allow_html=True)
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ", ["Advanced AI Labs", "Digital Archives", "Heritage & Science", "Imperial University", "Mysticism & Qene", "Strategic Wealth"])
    tool = st.radio("Tool Select", ["Document Master", "Voice Assistant", "Manuscript OCR", "History Vault"])

# ---------------------------------------------------------
# 6. MAIN WORKSPACE: FILE STORAGE & INTERACTION
# ---------------------------------------------------------
if st.session_state.logged_in:
    st.markdown(f"<h2>{tool} Hub</h2>", unsafe_allow_html=True)

    # File Upload & Storage Section
    with st.expander("📁 Upload Documents to AI Brain (PDF, DOCX, Media)"):
        uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True, type=['pdf', 'docx', 'png', 'jpg', 'jpeg', 'mp4', 'html'])
        
        doc_context = ""
        media_files = []
        
        if uploaded_files:
            for f in uploaded_files:
                if f.type in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/html"]:
                    doc_context += f"\n--- Content from {f.name} ---\n" + read_document(f)
                else:
                    media_files.append({"type": f.type, "data": f.read()})
            st.success(f"{len(uploaded_files)} ፋይሎች ወደ AI አእምሮ ተጭነዋል።")

    # Chat History
    if st.session_state.user not in st.session_state.history:
        st.session_state.history[st.session_state.user] = []

    # Display History
    for chat in st.session_state.history[st.session_state.user]:
        with st.chat_message(chat["role"]): st.markdown(chat["content"])

    # Input Section
    col_chat, col_voice = st.columns([0.8, 0.2])
    
    with col_chat:
        prompt = st.chat_input("Ask the Scholar...")
    
    with col_voice:
        voice_active = st.toggle("🎙️ Voice Out")

    if prompt:
        # Save User History
        st.session_state.history[st.session_state.user].append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
                # The AI looks at the text from PDFs/Docs AND the images/videos
                answer = ask_scholar_master(prompt, doc_context, media_files)
                st.markdown(answer)
                
                # Text-to-Speech Output
                if voice_active:
                    try:
                        tts = gTTS(text=answer[:500], lang='en') # gTTS works best with English/Standard text
                        audio_fp = io.BytesIO()
                        tts.write_to_fp(audio_fp)
                        st.audio(audio_fp, format='audio/mp3')
                    except:
                        st.warning("ድምፅ ማመንጨት አልተቻለም።")
                
                # Save Assistant History
                st.session_state.history[st.session_state.user].append({"role": "assistant", "content": answer})

# Master Footer
st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b><br>© 2026 Sovereign Edition | Verified & Secured</p>", unsafe_allow_html=True)
