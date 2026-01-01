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
    layout="wide"
)

# Sovereign UI (Emerald & Gold)
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
# 2. SESSION STATE (Auth, History, Storage)
# ---------------------------------------------------------
if 'users' not in st.session_state: st.session_state.users = {"deaconkewn": "AB12@#cdamdegeez"}
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'username' not in st.session_state: st.session_state.username = ""
if 'history' not in st.session_state: st.session_state.history = {} # User history

# ---------------------------------------------------------
# 3. AI SOVEREIGN ENGINE (Auto-Fix for 404 Error)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key Missing in Secrets!")
    st.stop()

@st.cache_resource
def get_working_model():
    """የ 404 ስህተትን ለመከላከል የሚሰራ ሞዴል በራስ-ሰር ይመርጣል"""
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # ቅድሚያ የምንሰጣቸው ሞዴሎች
        priority = ["models/gemini-2.0-flash", "models/gemini-1.5-flash", "models/gemini-pro"]
        for p in priority:
            if p in available_models: return p
        return available_models[0]
    except:
        return "models/gemini-1.5-flash"

WORKING_MODEL_NAME = get_working_model()

def ask_ai_master(prompt, context="", file_data=None, mime=None):
    model = genai.GenerativeModel(model_name=WORKING_MODEL_NAME)
    full_prompt = f"System: You are the 'Ge'ez Scholar AI' created by Grand Architect Deacon Kewn Dejen. Knowledge context: {context}\n\nUser Question: {prompt}"
    
    try:
        if file_data and mime:
            response = model.generate_content([full_prompt, {'mime_type': mime, 'data': file_data}])
        else:
            response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"ሊቁ ጥያቄዎን ሊመልሱ አልቻሉም። ስህተት: {str(e)}"

# ---------------------------------------------------------
# 4. FILE PROCESSING (PDF, DOCX)
# ---------------------------------------------------------
def extract_text(uploaded_file):
    name = uploaded_file.name.lower()
    try:
        if name.endswith('.pdf'):
            reader = PyPDF2.PdfReader(uploaded_file)
            return " ".join([page.extract_text() for page in reader.pages])
        elif name.endswith('.docx'):
            doc = Document(uploaded_file)
            return " ".join([p.text for p in doc.paragraphs])
    except:
        return ""
    return ""

# ---------------------------------------------------------
# 5. SIDEBAR: AUTH & PORTALS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>")
    
    if not st.session_state.logged_in:
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
        mode = st.radio("Access Control", ["Login", "Register"])
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if mode == "Login" and st.button("Sign In"):
            if u in st.session_state.users and st.session_state.users[u] == p:
                st.session_state.logged_in, st.session_state.username = True, u
                st.rerun()
            else: st.error("Wrong Username or Password")
        if mode == "Register" and st.button("Create Account"):
            if u and p:
                st.session_state.users[u] = p
                st.success("Account Created! Please Login.")
            else: st.error("Fill all fields")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()
    else:
        st.write(f"👑 Welcome, **{st.session_state.username}**")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("---")
    pillar = st.selectbox("Wisdom Pillar", ["🧠 AI Labs", "📜 Digital Archives", "🎓 University"])
    tool = st.radio("System Tools", ["Document Analyzer", "Manuscript OCR", "Voice Assistant"])

# ---------------------------------------------------------
# 6. MAIN WORKSPACE (Storage, Chat, Voice, History)
# ---------------------------------------------------------
if st.session_state.logged_in:
    st.title(f"{tool} Center")

    # 1. FILE STORAGE & LOADING
    with st.expander("📁 Imperial Storage (Upload PDF, DOCX, Image, Video)"):
        up_file = st.file_uploader("Upload document for AI analysis", type=['pdf', 'docx', 'png', 'jpg', 'jpeg', 'mp4'])
        doc_context, f_bytes, f_mime = "", None, None
        
        if up_file:
            if up_file.type in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                doc_context = extract_text(up_file)
                st.success(f"Document '{up_file.name}' stored in AI context.")
            else:
                f_bytes = up_file.read()
                f_mime = up_file.type
                st.info(f"Media file '{up_file.name}' ready for visual analysis.")

    # 2. CHAT HISTORY (Persistent for current session)
    if st.session_state.username not in st.session_state.history:
        st.session_state.history[st.session_state.username] = []

    # Display Conversation History
    for chat in st.session_state.history[st.session_state.username]:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    # 3. INTERACTION (Text & Voice Input)
    voice_enabled = st.checkbox("🎙️ Enable Voice Response (TTS)")
    
    if prompt := st.chat_input("Ask the Sovereign AI..."):
        # User Message
        st.session_state.history[st.session_state.username].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # AI Message
        with st.chat_message("assistant"):
            with st.spinner("ሊቁ መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
                answer = ask_ai_master(prompt, doc_context, f_bytes, f_mime)
                st.markdown(answer)
                
                # Voice Response (TTS)
                if voice_enabled:
                    try:
                        tts = gTTS(text=answer, lang='en') # Amharic support is partial in gTTS
                        audio_io = io.BytesIO()
                        tts.write_to_fp(audio_io)
                        st.audio(audio_io, format='audio/mp3')
                    except: pass
                
                st.session_state.history[st.session_state.username].append({"role": "assistant", "content": answer})

# ---------------------------------------------------------
# 7. SOVEREIGN FOOTER
# ---------------------------------------------------------
st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b><br>© 2026 Sovereign Edition | Engine: "+WORKING_MODEL_NAME+"</p>", unsafe_allow_html=True)
