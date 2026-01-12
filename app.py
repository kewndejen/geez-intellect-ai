import streamlit as st
import google.generativeai as genai
from google.api_core import exceptions
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

# Professional World-Class Sovereign UI (Emerald & Gold)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Fauna+One&family=Abyssinica+SIL&display=swap');
    
    /* Global Styles */
    .stApp { 
        background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); 
        color: #ffffff; 
        font-family: 'Fauna One', sans-serif; 
    }
    
    /* Headers */
    h1, h2, h3 { 
        font-family: 'Cinzel', serif !important; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important;
        border-right: 4px solid #FFD700;
    }
    
    /* Content Cards */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid #FFD700;
        margin-bottom: 25px;
        box-shadow: 0 15px 45px rgba(0,0,0,0.6);
    }

    /* Majestic Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 5px !important; border: 2px solid #FFFFFF !important;
        height: 3.5em; width: 100%; transition: 0.4s ease;
        text-transform: uppercase; font-family: 'Cinzel', serif;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 0 35px #FFD700; }

    /* Chat Input Bar */
    [data-testid="stChatInput"] { 
        border: 2px solid #FFD700 !important; 
        background-color: #ffffff !important; 
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; }
    
    /* Custom Scrollbar for Ge'ez feeling */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #001a0d; }
    ::-webkit-scrollbar-thumb { background: #FFD700; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. CORE UTILITIES (File Processing)
# ---------------------------------------------------------
def extract_text_from_file(uploaded_file):
    ext = uploaded_file.name.split('.')[-1].lower()
    text = ""
    try:
        if ext == 'pdf':
            reader = PdfReader(uploaded_file)
            for page in reader.pages: text += page.extract_text()
        elif ext in ['docx', 'doc']:
            doc = Document(uploaded_file)
            for para in doc.paragraphs: text += para.text + "\n"
        return text
    except Exception as e:
        return f"Error reading file: {e}"

# ---------------------------------------------------------
# 3. THE SOVEREIGN AI ENGINE (Multi-API Failover)
# ---------------------------------------------------------
def get_api_keys():
    # በ Secrets ውስጥ ቁልፍ መኖሩን ማረጋገጥ
    if "GEMINI_KEYS" in st.secrets:
        return st.secrets["GEMINI_KEYS"]
    elif "GOOGLE_API_KEY" in st.secrets:
        return [st.secrets["GOOGLE_API_KEY"]]
    return []

def ask_sovereign_scholar(prompt, tool_context, document_text=""):
    keys = get_api_keys()
    if not keys:
        return "🔱 የሊቁ መግቢያ ቁልፍ (API Key) አልተገኘም። እባክዎ በ Secrets ውስጥ ያስገቡ።", "None"

    sys_instr = f"""
    You are 'Ge'ez Scholar AI', a world-class expert in Ethiopian studies, Ge'ez literature, and Qene.
    Created by Grand Architect Deacon Kewn Dejen.
    Current Specialized Pillar: {tool_context}.
    
    DOCUMENT CONTEXT:
    ---
    {document_text[:15000]}
    ---
    
    Instructions:
    1. If a document is provided, prioritize answering from it.
    2. Provide scholarly, deep, and wise analysis.
    3. If the quota is busy, the system will inform the user politely.
    4. Tone: Sovereign, authoritative, ancient, and wise.
    """

    for key in keys:
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel(model_name='gemini-2.0-flash', system_instruction=sys_instr)
            response = model.generate_content(prompt)
            return response.text, "Gemini 2.0 Flash"
        except exceptions.ResourceExhausted:
            continue # ወደ ቀጣዩ Key ይለፋል
        except Exception as e:
            continue
            
    return "⚠️ ሊቁ በአሁኑ ሰዓት እጅግ ተጨናንቀዋል። እባክዎ ጥቂት ሰከንዶች ታግሰው Refresh ያድርጉ ወይም ሌላ API Key በ Secrets ውስጥ ይጨምሩ።", "None"

# ---------------------------------------------------------
# 4. SIDEBAR: THE ARK OF 60 PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:900; border: 2px solid #fff;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("የጥበብ ምሰሶ (Wisdom Pillar)", [
        "🧠 Advanced AI Labs", "📜 Digital Archives", "🏛️ Heritage & Science",
        "🎓 Imperial University", "🔮 Mysticism & Qene", "💰 Strategic Wealth"
    ])

    # 60 Tools Organized in 6 Pillars
    tools_map = {
        "🧠 Advanced AI Labs": ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom", "Neural Translation", "Syntax Analyzer", "Ge'ez NLP", "Dialect Study", "Semantic Map"],
        "📜 Digital Archives": ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees", "Treaty Expert", "Kibre Nagast Hub", "Ecclesiastical Law", "Genealogy Map", "Preservation Lab", "Hagiography Lab"],
        "🏛️ Heritage & Science": ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI", "Geology of Axum", "Botany Hub", "Zoology Hub", "Ink Chemistry", "Virtual Museum"],
        "🎓 Imperial University": ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter", "Ethiopic Math", "Philosophy Hub", "History Chronology", "University Portal", "Scholarly Citation"],
        "🔮 Mysticism & Qene": ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Proverbs AI", "Esoteric Wisdom", "Liturgical Guide", "Monastic Study", "Apostolic Tradition", "Hymnology Lab"],
        "💰 Strategic Wealth": ["Business Hub", "API Portal", "Security Admin", "Wealth Strategy", "Sovereign Logs", "Global Relations", "Grant Assistant", "Strategic Planning", "Project Manager", "Data Vault"]
    }
    tool = st.radio("Labs", tools_map[pillar])

    st.markdown("---")
    uploaded_file = st.file_uploader("📚 ሰነድ ጭነው ለሊቁ ያሳዩ (PDF/Word)", type=['pdf', 'docx'])
    doc_text = ""
    if uploaded_file:
        doc_text = extract_text_from_file(uploaded_file)
        st.success(f"✅ '{uploaded_file.name}' ተነቧል!")

    if st.button("🔄 REBOOT STUDIO"):
        st.cache_resource.clear()
        st.rerun()

# ---------------------------------------------------------
# 5. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown(f"<h1>🔱 {tool} 🔱</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ በጥልቅ እያሰላሰሉ ነው..."):
            answer, engine = ask_sovereign_scholar(prompt, tool, doc_text)
            
            full_res = f"<div>{answer}</div><div style='font-size:0.8rem; color:#FFD700; margin-top:20px; border-top:1px solid #555; padding-top:10px;'>Intelligence: {engine} | Sovereign Zenith v-Final</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b><br>© 2024-2025 ALL RIGHTS RESERVED</p>", unsafe_allow_html=True)
