import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
import time
import random
import datetime
import re
from PIL import Image

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION & SESSION STATE
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State (Suggestion 3)
if "messages" not in st.session_state: st.session_state.messages = []
if "global_memory" not in st.session_state: st.session_state.global_memory = ""
if "file_names" not in st.session_state: st.session_state.file_names = []
if "usage_count" not in st.session_state: st.session_state.usage_count = 0

# Majestic Sovereign UI (Suggestion 1 & 8 Theme)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    .stApp { background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; text-shadow: 2px 2px 8px #000; }
    [data-testid="stSidebar"] { background-color: #001a0d !important; border-right: 4px solid #FFD700; }
    .sovereign-card { background: rgba(255, 255, 255, 0.12); padding: 25px; border-radius: 15px; border: 1px solid #FFD700; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    .stButton>button { background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important; color: #000 !important; font-weight: 900 !important; border-radius: 10px; height: 3.5em; width: 100%; text-transform: uppercase; border: 2px solid #fff; }
    [data-testid="stChatInput"] { border: 3px solid #FFD700 !important; background-color: #ffffff !important; border-radius: 15px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. ENHANCED SECURITY & ENGINE DISCOVERY (Suggestion 1 & 6)
# ---------------------------------------------------------
def setup_api():
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        # Side input fallback if secrets not set
        user_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")
        if user_key:
            genai.configure(api_key=user_key)
        else:
            st.sidebar.warning("🔐 Master Key Required to Access Archive.")
            st.stop()

setup_api()

@st.cache_resource
def get_engines():
    try:
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        priority = ["models/gemini-1.5-flash", "models/gemini-1.5-pro", "models/gemini-pro"]
        return [p for p in priority if p in available] or [available[0]]
    except: return ["models/gemini-1.5-flash"]

ACTIVE_MODELS = get_engines()

# ---------------------------------------------------------
# 3. ADVANCED LOADING & PROCESSING (Suggestion 2, 7 & 8)
# ---------------------------------------------------------
def show_geez_spinner(message):
    """Themed loading state with Ge'ez numerals"""
    symbols = ["፩", "፪", "፫", "፬", "፭", "፮", "፯", "፰", "፱", "፲"]
    placeholder = st.empty()
    for sym in symbols:
        placeholder.markdown(f"<div style='text-align:center; color:#FFD700; font-size:20px;'>{sym} {message}...</div>", unsafe_allow_html=True)
        time.sleep(0.1)
    placeholder.empty()

def extract_enhanced_text(uploaded_file):
    ext = uploaded_file.name.split('.')[-1].lower()
    text = ""
    try:
        if ext == 'pdf':
            reader = PdfReader(uploaded_file)
            for i, page in enumerate(reader.pages):
                text += f"\n[PAGE {i+1}]\n{page.extract_text()}\n"
        elif ext in ['docx', 'doc']:
            doc = Document(uploaded_file)
            for para in doc.paragraphs: text += para.text + "\n"
        return text if text.strip() else "No extractable text found."
    except Exception as e:
        st.error(f"Processing Error: {e}")
        return ""

# ---------------------------------------------------------
# 4. RESILIENT SCHOLAR LOGIC (Suggestion 6 & 10)
# ---------------------------------------------------------
def ask_sovereign_scholar(prompt, tool_context, doc_context=""):
    # Choose optimal model based on input length
    model_id = ACTIVE_MODELS[0]
    if len(prompt) > 1000 or len(doc_context) > 10000:
        model_id = "models/gemini-1.5-pro" if "models/gemini-1.5-pro" in ACTIVE_MODELS else ACTIVE_MODELS[0]

    sys_instr = f"""
    You are 'Ge'ez Scholar AI Master', created by Deacon Kewn Dejen.
    Current Expertise: {tool_context}.
    Knowledge Base: 60 Pillars of Wisdom and the provided document.
    DOCUMENT CONTENT: {doc_context[:20000]}
    
    Task: Provide scholarly, direct analysis. If the answer is in the document, cite it. 
    Support Ge'ez/Amharic. Tone: Sovereign and Ancient.
    """
    
    # Enhanced error recovery with exponential backoff (Suggestion 10)
    for attempt in range(3):
        try:
            model = genai.GenerativeModel(model_name=model_id, system_instruction=sys_instr)
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text, model_id
        except Exception as e:
            if "429" in str(e):
                time.sleep(5 * (attempt + 1))
                continue
            return f"Error: {e}", "None"
    return "❌ ሊቁ ተጨናንቀዋል። እባክዎ ገጹን Refresh አድርገው ይሞክሩ።", "None"

# ---------------------------------------------------------
# 5. SIDEBAR: NAVIGATION, EXPORT & TOOLS (Suggestion 4)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:10px; border-radius:12px; text-align:center; color:#000; font-weight:900;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Pillar & Tool Selection
    pillar = st.selectbox("Wisdom Pillar", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    tools = {
        "Advanced AI Labs": ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom"],
        "Archives & Law": ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees"],
        "Heritage & Science": ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"],
        "University Hub": ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"],
        "Mysticism & Qene": ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay"]
    }
    tool = st.radio("Labs", tools[pillar])

    st.markdown("---")
    # File Uploader
    uploaded_file = st.file_uploader("📚 Load Document (PDF/Word)", type=['pdf', 'docx'])
    if uploaded_file and uploaded_file.name not in st.session_state.file_names:
        show_geez_spinner("ሰነዱን በማንበብ ላይ")
        st.session_state.global_memory = extract_enhanced_text(uploaded_file)
        st.session_state.file_names.append(uploaded_file.name)
        st.success(f"✅ {uploaded_file.name} Loaded")

    # Export & Clear Chat (Suggestion 4)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Export Chat"):
            chat_text = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
            st.download_button("Download", chat_text, "geez_research.txt")
    with col2:
        if st.button("📊 Clear Chat"):
            st.session_state.messages = []
            st.rerun()

# ---------------------------------------------------------
# 6. MAIN WORKSPACE (Suggestion 9 & 5)
# ---------------------------------------------------------
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

# Preview Feature (Suggestion 9)
if st.session_state.global_memory:
    with st.expander("🔍 Preview Document Content", expanded=False):
        st.text_area("Extracted Context", st.session_state.global_memory[:2000] + "...", height=150)

# Message History
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

# Chat Input
if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        show_geez_spinner("ሊቁ መዛግብቱን እያመሳከረ ነው")
        answer, engine = ask_sovereign_scholar(prompt, tool, st.session_state.global_memory)
        
        # Celebrate usage (Suggestion 5)
        st.session_state.usage_count += 1
        if st.session_state.usage_count % 10 == 0: st.balloons()

        full_res = f"<div>{answer}</div><div style='font-size:0.8rem; color:#FFD700; border-top:1px solid #ffffff33; margin-top:15px; padding-top:10px;'>Source: {engine} | Sovereign Zenith v4.0</div>"
        st.markdown(full_res, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b></p>", unsafe_allow_html=True)
