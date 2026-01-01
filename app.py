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

# Professional UI: Emerald, Gold & Crystal White Visibility
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    
    .stApp { background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); }

    /* Force Crystal White Text for 100% Visibility */
    p, span, label, div, .stMarkdown, .stChatMessage p, .stSelectbox label, .stRadio label { 
        color: #ffffff !important; 
        font-family: 'Montserrat', sans-serif;
        font-size: 1.1rem;
        font-weight: 500;
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
        border-right: 5px solid #FFD700;
    }

    /* Sovereign Majesty Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #FFFFFF !important;
        height: 3.5em; width: 100%; transition: 0.5s;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 10px 30px #FFD700; }

    /* Chat Input Bar Fix */
    [data-testid="stChatInput"] { background-color: #ffffff !important; border-radius: 20px !important; padding: 5px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; }

    .auth-box { background: rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 20px; border: 2px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SESSION MANAGEMENT (Auth, History, Storage)
# ---------------------------------------------------------
if 'users' not in st.session_state: st.session_state.users = {"admin": "kewn123"}
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'username' not in st.session_state: st.session_state.username = ""
if 'history' not in st.session_state: st.session_state.history = {}

# ---------------------------------------------------------
# 3. THE UNBREAKABLE ENGINE (Auto-Model Discovery)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: Master Key Missing!")
    st.stop()

@st.cache_resource
def find_sovereign_model():
    """የ 404 ስህተትን ለመከላከል የሚሰራውን ሞዴል በራሱ ፈልጎ ያገኘዋል"""
    try:
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # ቅድሚያ የሚሰጣቸው ሞዴሎች
        for target in ["models/gemini-2.0-flash", "models/gemini-1.5-flash", "models/gemini-1.5-pro", "models/gemini-pro"]:
            if target in available: return target
        return available[0] if available else "models/gemini-pro"
    except:
        return "gemini-pro" # Fallback

WORKING_MODEL = find_sovereign_model()

def ask_sovereign_ai(prompt, context="", file_data=None, mime=None):
    model = genai.GenerativeModel(model_name=WORKING_MODEL)
    full_prompt = f"System: You are 'Ge'ez Scholar AI' created by Deacon Kewn Dejen. Context: {context}\n\nQuestion: {prompt}"
    
    # Retry logic for 429
    for attempt in range(3):
        try:
            if file_data and mime:
                response = model.generate_content([full_prompt, {'mime_type': mime, 'data': file_data}])
            else:
                response = model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            if "429" in str(e):
                time.sleep(8)
                continue
            return f"ሊቁ ስህተት ገጠማቸው: {str(e)}"
    return "❌ ገደብዎ አልቋል። እባክዎ ጥቂት ደቂቃ ቆይተው ገጹን Refresh ያድርጉ።"

# ---------------------------------------------------------
# 4. FILE SYSTEM (PDF, DOCX, HTML)
# ---------------------------------------------------------
def parse_file(file):
    name = file.name.lower()
    try:
        if name.endswith('.pdf'):
            reader = PyPDF2.PdfReader(file)
            return " ".join([p.extract_text() for p in reader.pages])
        elif name.endswith('.docx'):
            doc = Document(file)
            return " ".join([p.text for p in doc.paragraphs])
        elif name.endswith('.html'):
            return file.read().decode("utf-8")
    except: return ""
    return ""

# ---------------------------------------------------------
# 5. SIDEBAR: THE COMMAND CENTER
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>")
    
    if not st.session_state.logged_in:
        st.markdown("<div class='auth-box'>", unsafe_allow_html=True)
        mode = st.radio("Access Control", ["Login", "Register"])
        u = st.text_input("Username")
        p = st.text_input("Password", type="password")
        if st.button("Enter Sovereign Portal"):
            if mode == "Login":
                if u in st.session_state.users and st.session_state.users[u] == p:
                    st.session_state.logged_in, st.session_state.username = True, u
                    st.rerun()
                else: st.error("ስህተት!")
            else:
                if u and p:
                    st.session_state.users[u] = p
                    st.success("አካውንት ተፈጥሯል። አሁን Login ያድርጉ።")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()
    else:
        st.markdown(f"<div style='text-align:center;'>👑 <b>Emperor {st.session_state.username}</b></div>", unsafe_allow_html=True)
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown("---")
    tool = st.radio("Sovereign Tools", ["Document Knowledge", "Visual OCR Lab", "Voice of Wisdom"])

# ---------------------------------------------------------
# 6. MAIN WORKSPACE
# ---------------------------------------------------------
if st.session_state.logged_in:
    st.title(f"{tool} Center")

    # Storage & Upload Area
    with st.expander("📁 Imperial Storage (Upload PDF, DOCX, Image, Video)"):
        up_file = st.file_uploader("Upload to AI Memory", type=['pdf', 'docx', 'html', 'png', 'jpg', 'jpeg', 'mp4'])
        doc_context, f_bytes, f_mime = "", None, None
        if up_file:
            if up_file.type in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/html"]:
                doc_context = parse_file(up_file)
                st.success(f"ሰነድ '{up_file.name}' በሊቁ አእምሮ ተቀምጧል።")
            else:
                f_bytes, f_mime = up_file.read(), up_file.type
                st.info(f"ፋይል '{up_file.name}' ለምስል ምርመራ ዝግጁ ነው።")

    # History Display
    user_key = st.session_state.username
    if user_key not in st.session_state.history: st.session_state.history[user_key] = []

    for chat in st.session_state.history[user_key]:
        with st.chat_message(chat["role"]): st.markdown(chat["content"])

    # Interaction
    voice_on = st.checkbox("🎙️ Enable Voice AI")
    
    if prompt := st.chat_input("Consult the Sovereign Scholar..."):
        st.session_state.history[user_key].append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("ሊቁ መዛግብቱን እየመረመሩ ነው..."):
                answer = ask_sovereign_ai(prompt, doc_context, f_bytes, f_mime)
                st.markdown(answer)
                
                if voice_on:
                    try:
                        tts = gTTS(text=answer[:350], lang='en')
                        audio_io = io.BytesIO()
                        tts.write_to_fp(audio_io)
                        st.audio(audio_io, format='audio/mp3')
                    except: pass
                
                st.session_state.history[user_key].append({"role": "assistant", "content": answer})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b><br>© 2026 Sovereign Edition | Engine: "+WORKING_MODEL+"</p>", unsafe_allow_html=True)
