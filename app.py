import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
import time
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Majestic Emerald Green & Royal Gold Sovereign UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; text-shadow: 2px 2px 10px #000; }
    
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important; border-right: 4px solid #FFD700; }
    
    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 25px; border-radius: 15px;
        border: 1px solid #FFD700;
        margin-bottom: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }

    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 10px !important; border: 2px solid #fff !important;
        height: 3.5em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase;
    }

    [data-testid="stChatInput"] { 
        border: 3px solid #FFD700 !important; 
        background-color: #ffffff !important; 
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; font-size: 1.1rem; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #ffffff; margin-top: 15px; padding-top: 10px; font-family: monospace; }
    .doc-status { background: rgba(0, 255, 0, 0.1); border: 1px solid #00ff00; padding: 10px; border-radius: 10px; font-size: 0.9rem; margin-bottom: 20px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. DOCUMENT & ENGINE LOGIC
# ---------------------------------------------------------
def extract_text(uploaded_file):
    ext = uploaded_file.name.split('.')[-1].lower()
    text = ""
    try:
        if ext == 'pdf':
            reader = PdfReader(uploaded_file)
            for page in reader.pages: text += page.extract_text()
        elif ext in ['docx', 'doc']:
            doc = Document(uploaded_file)
            for p in doc.paragraphs: text += p.text + "\n"
        return text
    except Exception as e:
        return f"Error: {e}"

if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    @st.cache_resource
    def get_sovereign_model():
        try:
            available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            priority = ["models/gemini-2.0-flash-exp", "models/gemini-1.5-flash", "models/gemini-pro"]
            for target in priority:
                for actual in available:
                    if target in actual: return actual
            return available[0]
        except: return "models/gemini-1.5-flash"

    SELECTED_MODEL = get_sovereign_model()
else:
    st.error("API Key missing!")
    st.stop()

def ask_geez_expert(prompt, tool_context, document_memory=""):
    # ጀሚኒ ሰነዱን እንዲያነብና እንዲያስቀምጥ የሚያደርግ ጥብቅ መመሪያ
    sys_instr = f"""
    You are 'Ge'ez Scholar AI Master', created by Deacon Kewn Dejen.
    Expertise: {tool_context}.
    
    CRITICAL CONTEXT:
    The user has uploaded a document. You must treat the following text as your primary knowledge source:
    ---
    {document_memory[:25000]} 
    ---
    
    Instructions:
    1. If the answer is in the document, start with "እንደተሰጠው ሰነድ መሠረት..." (Based on the provided document...).
    2. If not, use your general wisdom but clarify: "ይህ መረጃ ከጠቅላላው መዛግብት የተገኘ ነው."
    3. Be direct, scholarly, and wise. Avoid fluff. Support Ge'ez/Amharic.
    """
    try:
        model = genai.GenerativeModel(model_name=SELECTED_MODEL, system_instruction=sys_instr)
        # 429 Retry Logic
        for attempt in range(1, 4):
            try:
                response = model.generate_content(prompt)
                return response.text, SELECTED_MODEL
            except Exception as e:
                if "429" in str(e):
                    time.sleep(attempt * 8)
                    continue
                raise e
    except Exception as e:
        return f"❌ የቴክኒክ ስህተት፦ {str(e)}", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK & DOCUMENT MANAGEMENT
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:10px; border-radius:8px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 📚 The Sovereign Document Uploader
    st.subheader("📜 ሰነድ ይጫኑ (Upload Document)")
    uploaded_file = st.file_uploader("PDF ወይም Word ፋይል ይጫኑ", type=['pdf', 'docx'])
    
    if "doc_memory" not in st.session_state: st.session_state.doc_memory = ""
    if "file_name" not in st.session_state: st.session_state.file_name = ""

    if uploaded_file:
        if st.session_state.file_name != uploaded_file.name:
            with st.spinner("ሰነዱን በማንበብ ላይ..."):
                st.session_state.doc_memory = extract_text(uploaded_file)
                st.session_state.file_name = uploaded_file.name
                st.success(f"✅ '{uploaded_file.name}' ተነቧል!")

    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ", [
        "Advanced AI Labs", "Archives & Law", "Heritage & Science",
        "Imperial University", "Mysticism & Qene", "Strategic Wealth"
    ])

    # Mapping Tools
    tools_map = {
        "Advanced AI Labs": ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom"],
        "Archives & Law": ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees"],
        "Heritage & Science": ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"],
        "Imperial University": ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"],
        "Mysticism & Qene": ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub"],
        "Strategic Wealth": ["Business Hub", "API Portal", "Security Admin", "Wealth Strategy"]
    }
    tool = st.radio("Labs", tools_map[pillar])

    if st.button("🔄 REBOOT SYSTEM"):
        st.session_state.doc_memory = ""
        st.session_state.messages = []
        st.cache_resource.clear()
        st.rerun()

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if st.session_state.doc_memory:
    st.markdown(f"<div class='doc-status'>📂 በንባብ ላይ ያለ ሰነድ፦ <b>{st.session_state.file_name}</b></div>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ ሰነዱንና መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
            answer, engine = ask_geez_expert(prompt, tool, st.session_state.doc_memory)
            full_res = f"<div>{answer}</div><div class='citation'>Source: {engine} | Sovereign Archivist v-Final</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
