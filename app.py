import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
import time
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL GEMINI 3 CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="GE'EZ STUDIO | Gemini 3 Sovereign",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Modern Sovereign UI (Emerald & Gold)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&family=Abyssinica+SIL&display=swap');
    
    /* Background: Deep Imperial Emerald Gradient */
    .stApp { 
        background: radial-gradient(circle at center, #003311 0%, #001a0d 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    /* Headers: High Contrast Radiant Gold */
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.5);
    }

    /* Modern Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important;
        border-right: 3px solid #FFD700;
    }
    
    /* Gemini 3 Style Message Bubbles */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.05) !important;
        border-radius: 15px !important;
        margin-bottom: 10px !important;
        border: 1px solid rgba(255, 215, 0, 0.1) !important;
    }

    /* Sovereign Document Display Box */
    .doc-vault {
        background: rgba(255, 215, 0, 0.1);
        border: 1px solid #FFD700;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 20px;
        text-align: center;
    }

    /* Majestic Sovereign Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 10px !important; height: 3.5em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 0 30px #FFD700; }

    /* Modern Chat Input */
    [data-testid="stChatInput"] { 
        border: 2px solid #FFD700 !important; 
        background-color: #ffffff !important; 
        border-radius: 20px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; font-size: 1.1rem; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #ffffff33; margin-top: 20px; padding-top: 10px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. DOCUMENT ARCHIVE LOGIC
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

# ---------------------------------------------------------
# 3. GEMINI 3 ENGINE (Fail-Safe Discovery)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    @st.cache_resource
    def load_sovereign_model():
        try:
            available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            # Gemini 3 Level Models: 2.0 Flash -> 1.5 Pro -> 1.5 Flash
            priority = ["models/gemini-2.0-flash-exp", "models/gemini-1.5-pro", "models/gemini-1.5-flash"]
            for target in priority:
                for actual in available:
                    if target in actual: return actual
            return available[0]
        except: return "models/gemini-1.5-flash"

    SELECTED_ENGINE = load_sovereign_model()
else:
    st.error("API Key አልተገኘም! እባክዎ በ Secrets ውስጥ ያስገቡ።")
    st.stop()

def ask_sovereign_expert(prompt, tool_context, document_archive=""):
    # Gemini 3 Logic: Deep Document Awareness
    sys_instr = f"""
    You are 'Ge'ez Scholar AI Master', the Gemini 3 standard intelligence created by Grand Architect Deacon Kewn Dejen.
    Current Specialized Module: {tool_context}.
    
    MANDATORY KNOWLEDGE SOURCE (DOCUMENT VAULT):
    The user has provided the following research material. You MUST prioritize this content for all answers:
    ---
    {document_archive[:30000]} 
    ---
    
    Rules:
    1. If information is in the document, start with "እንደተሰጠው ሰነድ መሠረት..." (Based on the document...).
    2. Cite specific sections if possible.
    3. If not in the document, use your vast Ge'ez/Historical database and state: "ይህ መረጃ ከመዛግብት የተገኘ ነው."
    4. Provide deep, scholarly, and wise analysis. Support Ge'ez/Amharic.
    """
    try:
        model = genai.GenerativeModel(model_name=SELECTED_ENGINE, system_instruction=sys_instr)
        # 429 Auto-Retry Loop
        for attempt in range(1, 4):
            try:
                response = model.generate_content(prompt)
                return response.text, SELECTED_ENGINE
            except Exception as e:
                if "429" in str(e):
                    time.sleep(attempt * 6)
                    continue
                raise e
    except Exception as e:
        return f"❌ የቴክኒክ ስህተት፦ {str(e)}", "None"

# ---------------------------------------------------------
# 4. SIDEBAR: THE ARK & DOCUMENT VAULT
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:linear-gradient(90deg, #FFD700, #B8860B); padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:900;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")

    # 📚 The Sovereign Document Vault
    st.subheader("📂 የሰነድ መዝገብ (Document Vault)")
    uploaded_files = st.file_uploader("PDF ወይም Word ፋይሎችን እዚህ ይደረድሩ", type=['pdf', 'docx'], accept_multiple_files=True)
    
    if "global_memory" not in st.session_state: st.session_state.global_memory = ""
    if "file_names" not in st.session_state: st.session_state.file_names = []

    if uploaded_files:
        combined_text = ""
        current_names = [f.name for f in uploaded_files]
        if current_names != st.session_state.file_names:
            with st.spinner("ጀሚኒ 3 ሰነዶቹን እየተነተነ ነው..."):
                for f in uploaded_files:
                    combined_text += f"\n[FILE: {f.name}]\n" + extract_text(f)
                st.session_state.global_memory = combined_text
                st.session_state.file_names = current_names
                st.success(f"✅ {len(uploaded_files)} ሰነዶች ወደ መዝገቡ ገብተዋል!")

    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ ይምረጡ", [
        "Advanced AI Labs", "Digital Archives", "Heritage & Science",
        "Imperial University", "Mysticism & Qene", "Strategic Wealth"
    ])

    # Mapping 60 Tools
    tools_map = {
        "Advanced AI Labs": ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom"],
        "Digital Archives": ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees", "Treaty Expert"],
        "Heritage & Science": ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI"],
        "Imperial University": ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter"],
        "Mysticism & Qene": ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Proverbs AI"],
        "Strategic Wealth": ["Business Hub", "API Portal", "Security Admin", "Wealth Strategy", "Sovereign Logs"]
    }
    tool = st.radio("Specialized Tools", tools_map[pillar])

    if st.button("🔄 REBOOT SOVEREIGN SYSTEM"):
        st.session_state.global_memory = ""
        st.session_state.messages = []
        st.cache_resource.clear()
        st.rerun()

# ---------------------------------------------------------
# 5. MAIN WORKSPACE (The Zenith Interface)
# ---------------------------------------------------------
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

# Display Document Status
if st.session_state.file_names:
    with st.expander("📝 በአሁኑ ሰዓት በመዝገብ ላይ ያሉ ሰነዶች"):
        for name in st.session_state.file_names:
            st.write(f"🔹 {name}")

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

# Chat Input & Gemini 3 Logic
if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<div style='color: white;'><b>{prompt}</b></div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ ሰነዶቹንና መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
            answer, engine = ask_sovereign_expert(prompt, tool, st.session_state.global_memory)
            
            full_res = f"""
            <div style='color: white; line-height: 1.8;'>{answer}</div>
            <div class='citation'>Source: {engine} | Gemini 3 Sovereign Edition</div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

# Master Footer
st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b><br>© 2024-2025 ALL RIGHTS RESERVED | GEMINI 3 STANDARD</p>", unsafe_allow_html=True)
