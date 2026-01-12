import streamlit as st
import google.generativeai as genai
import time
import os
from PIL import Image
import PyPDF2import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ge’ez Scholar AI Studio",
    page_icon="🔱",
    layout="wide",
)

# --- CUSTOM CSS (Emerald & Gold Theme) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Fauna+One&display=swap');

    :root {
        --emerald: #043927;
        --gold: #D4AF37;
        --dark-bg: #021a12;
    }

    /* Main Background */
    .stApp {
        background-color: var(--dark-bg);
        color: #e0e0e0;
    }

    /* Headers */
    h1, h2, h3 {
        font-family: 'Cinzel', serif !important;
        color: var(--gold) !important;
        text-align: center;
    }

    /* Buttons */
    .stButton>button {
        background-color: var(--emerald);
        color: var(--gold);
        border: 2px solid var(--gold);
        border-radius: 0px;
        font-family: 'Cinzel', serif;
        width: 100%;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: var(--gold);
        color: var(--emerald);
    }

    /* Cards/Sections */
    .feature-card {
        background: rgba(4, 57, 39, 0.3);
        padding: 30px;
        border-radius: 10px;
        border-left: 5px solid var(--gold);
        height: 100%;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 50px;
        font-family: 'Fauna One', serif;
        color: #888;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.sidebar.image("https://img.icons8.com/ios-filled/100/D4AF37/pillar.png") # Placeholder for Logo
st.sidebar.title("Ge'ez Navigation")
menu = st.sidebar.radio("Go to", ["Home", "Studio Access", "About the Scholar", "Contact"])

# --- HOME SECTION ---
if menu == "Home":
    # Hero Section
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1>🔱 GE’EZ SCHOLAR AI STUDIO 🔱</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: white !important;'>Sovereign Intelligence. Ancient Wisdom.</h3>", unsafe_allow_html=True)
    st.write("<p style='text-align: center; font-size: 1.2em;'>A sovereign-grade AI research hub empowering scholars with document intelligence, visual cognition, and divine reasoning.</p>", unsafe_allow_html=True)
    
    st.markdown("---")

    # Features Section
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📚 Document Knowledge</h3>
            <p>Deep semantic querying of PDF and DOCX archives using multi-modal Gemini architecture.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>👁 Visual OCR Lab</h3>
            <p>Advanced image and video processing for visual intelligence and script deciphering.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>🔊 Voice of Wisdom</h3>
            <p>Immersive text-to-speech interaction in English and Amharic for an oral tradition experience.</p>
        </div>
        """, unsafe_allow_html=True)

# --- STUDIO ACCESS (Login Mockup) ---
elif menu == "Studio Access":
    st.markdown("<h2>🛡 Portal Authentication</h2>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        st.text_input("Scholar ID")
        st.text_input("Access Key", type="password")
        if st.button("Enter the Sanctum"):
            st.success("Welcome, Scholar. Initializing Ge'ez Environment...")

    with tab2:
        st.text_input("Full Name")
        st.text_input("Email Address")
        st.text_input("Create Access Key", type="password")
        st.button("Request Membership")

# --- CONTACT SECTION ---
elif menu == "Contact":
    st.markdown("<h2>📜 Reach the Council</h2>", unsafe_allow_html=True)
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### Digital Coordinates")
        st.write("📧 **Email:** contact@geezscholar.ai")
        st.write("📍 **Location:** Digital Diaspora / Addis Ababa")
        st.write("🌐 **Socials:** [LinkedIn](#) | [GitHub](#) | [Twitter](#)")

    with col_b:
        st.write("### Send a Message")
        st.text_input("Name")
        st.text_area("Your Inquiry")
        st.button("Send Dispatch")

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        <hr style="border: 0.5px solid #D4AF37;">
        <p>© 2024 Ge’ez Scholar AI Studio. All Rights Reserved. <br> 
        <i>"Knowledge is the light of the soul."</i></p>
    </div>
    """, unsafe_allow_html=True)
from docx import Document
from gtts import gTTS
import io

# ---------------------------------------------------------
# 1. PRESTIGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide"
)

# Professional Sovereign UI (Emerald, Gold & High Visibility)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    .stApp { background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); }
    p, span, label, div, .stMarkdown, .stChatMessage p, .stSelectbox label, .stRadio label { 
        color: #ffffff !important; font-family: 'Montserrat', sans-serif; font-size: 1.1rem;
    }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; text-shadow: 2px 2px 10px rgba(0,0,0,0.8); }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important; border-right: 5px solid #FFD700; }
    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important; border-radius: 12px !important;
        height: 3.5em; width: 100%; transition: 0.5s; border: 2px solid #FFFFFF !important;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 10px 30px #FFD700; }
    [data-testid="stChatInput"] { background-color: #ffffff !important; border-radius: 20px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; }
    .auth-box { background: rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 20px; border: 2px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SESSION & AUTH
# ---------------------------------------------------------
if 'users' not in st.session_state: st.session_state.users = {"admin": "kewn123"}
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'username' not in st.session_state: st.session_state.username = ""
if 'history' not in st.session_state: st.session_state.history = {}

# ---------------------------------------------------------
# 3. INFINITE BRAIN ENGINE (Multi-Key & Auto-Retry Logic)
# ---------------------------------------------------------
# Secrets ውስጥ GOOGLE_API_KEY, GOOGLE_API_KEY_2 ወዘተ ብለው ቢጨምሩ ሲስተሙ ሁሉንም ይጠቀማል
keys = [st.secrets.get("GOOGLE_API_KEY"), st.secrets.get("GOOGLE_API_KEY_2"), st.secrets.get("GOOGLE_API_KEY_3")]
keys = [k for k in keys if k] # የሚሰሩትን ብቻ መውሰድ

@st.cache_resource
def get_model(api_key):
    genai.configure(api_key=api_key)
    try:
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        for target in ["models/gemini-2.0-flash", "models/gemini-1.5-flash", "models/gemini-pro"]:
            if target in available: return target
        return available[0]
    except: return "gemini-pro"

def ask_sovereign_ai(prompt, context="", file_data=None, mime=None):
    full_prompt = f"System: You are 'Ge'ez Scholar AI' created by Deacon Kewn Dejen. Knowledge Context: {context}\n\nQuestion: {prompt}"
    
    # በየቁልፎቹ (Keys) መዞር (Infinite Hack)
    for api_key in keys:
        genai.configure(api_key=api_key)
        model_name = get_model(api_key)
        model = genai.GenerativeModel(model_name=model_name)
        
        # ገደብ ሲመጣ 3 ጊዜ ደጋግሞ መሞከር
        for attempt in range(3):
            try:
                if file_data and mime:
                    response = model.generate_content([full_prompt, {'mime_type': mime, 'data': file_data}])
                else:
                    response = model.generate_content(full_prompt)
                return response.text, model_name
            except Exception as e:
                if "429" in str(e):
                    time.sleep(5) # 5 ሰከንድ ዝም ብሎ መታገስ
                    continue
                break # ወደ ቀጣዩ ቁልፍ መሸጋገር
    
    return "❌ ሊቁ በአሁኑ ሰዓት እጅግ ተጨናንቀዋል። እባክዎ ጥቂት ሰከንዶች ታግሰው Refresh ያድርጉ ወይም ሌላ API Key በ Secrets ውስጥ ይጨምሩ።", "None"

# ---------------------------------------------------------
# 4. FILE SYSTEM
# ---------------------------------------------------------
def parse_file(file):
    name = file.name.lower()
    try:
        if name.endswith('.pdf'):
            return " ".join([p.extract_text() for p in PyPDF2.PdfReader(file).pages])
        elif name.endswith('.docx'):
            return " ".join([p.text for p in Document(file).paragraphs])
        return file.read().decode("utf-8")
    except: return ""

# ---------------------------------------------------------
# 5. SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>")
    if not st.session_state.logged_in:
        st.markdown("<div class='auth-box'>", unsafe_allow_html=True)
        mode = st.radio("Access Control", ["Login", "Register"])
        u, p = st.text_input("User"), st.text_input("Pass", type="password")
        if st.button("Enter Sovereign Portal"):
            if mode == "Login" and u in st.session_state.users and st.session_state.users[u] == p:
                st.session_state.logged_in, st.session_state.username = True, u
                st.rerun()
            elif mode == "Register" and u and p:
                st.session_state.users[u] = p
                st.success("Registered!")
            else: st.error("ስህተት!")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()
    else:
        st.write(f"👑 Welcome: **{st.session_state.username}**")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
    st.markdown("---")
    tool = st.radio("Sovereign Tools", ["Document Knowledge", "Visual OCR Lab", "Voice of Wisdom"])

# ---------------------------------------------------------
# 6. MAIN SYSTEM
# ---------------------------------------------------------
if st.session_state.logged_in:
    st.title(f"{tool} Center")
    with st.expander("📁 Imperial Storage (PDF, DOCX, Image, Video)"):
        up_file = st.file_uploader("Upload to AI Memory", type=['pdf', 'docx', 'png', 'jpg', 'mp4'])
        doc_context, f_bytes, f_mime = "", None, None
        if up_file:
            if up_file.type in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                doc_context = parse_file(up_file)
                st.success("Memorized.")
            else:
                f_bytes, f_mime = up_file.read(), up_file.type
                st.info("Visual/Audio Ready.")

    user_key = st.session_state.username
    if user_key not in st.session_state.history: st.session_state.history[user_key] = []
    for chat in st.session_state.history[user_key]:
        with st.chat_message(chat["role"]): st.markdown(chat["content"])

    voice_on = st.checkbox("🎙️ Enable Voice Response")
    if prompt := st.chat_input("Consult the Sovereign Scholar..."):
        st.session_state.history[user_key].append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        with st.chat_message("assistant"):
            with st.spinner("ሊቁ መዛግብቱን እየመረመሩ ነው..."):
                answer, engine = ask_sovereign_ai(prompt, doc_context, f_bytes, f_mime)
                st.markdown(answer)
                if voice_on:
                    try:
                        tts = gTTS(text=answer[:300], lang='en')
                        audio_io = io.BytesIO()
                        tts.write_to_fp(audio_io)
                        st.audio(audio_io, format='audio/mp3')
                    except: pass
                st.session_state.history[user_key].append({"role": "assistant", "content": answer})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b></p>", unsafe_allow_html=True)
