import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
import time
import random
import datetime
from PIL import Image
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

# Majestic Emerald Green & Royal Gold Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&family=Abyssinica+SIL&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important;
        border-right: 4px solid #FFD700;
    }
    
    p, span, label, div, .stMarkdown { 
        color: #f8f9fa !important; 
        font-size: 1.1rem; 
        line-height: 1.8; 
    }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(255, 215, 0, 0.4);
        border-left: 15px solid #FFD700;
        margin-bottom: 25px;
        box-shadow: 0 15px 45px rgba(0,0,0,0.6);
    }

    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #FFFFFF !important;
        height: 3.8em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton>button:hover { 
        transform: translateY(-3px); 
        box-shadow: 0 0 35px #FFD700; 
        color: #ffffff !important;
    }

    [data-testid="stChatInput"] { 
        border: 3px solid #FFD700 !important; 
        background-color: #ffffff !important; 
        border-radius: 20px !important; 
        padding: 8px !important;
    }
    [data-testid="stChatInput"] textarea { 
        color: #000000 !important; 
        font-weight: bold !important; 
        font-size: 1.2rem !important; 
    }
    
    .wait-msg { color: #FFD700; font-style: italic; font-size: 1rem; text-align: center; font-weight: bold; background: rgba(0,0,0,0.3); padding: 10px; border-radius: 10px; }
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid rgba(255,255,255,0.2); margin-top: 25px; padding-top: 15px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. FILE PROCESSING ENGINE (PDF & DOCX)
# ---------------------------------------------------------
def extract_text_from_file(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    text = ""
    try:
        if file_extension == 'pdf':
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text()
        elif file_extension in ['docx', 'doc']:
            doc = Document(uploaded_file)
            for para in doc.paragraphs:
                text += para.text + "\n"
        return text
    except Exception as e:
        return f"Error reading file: {e}"

# ---------------------------------------------------------
# 3. INDESTRUCTIBLE ENGINE (Source-Based Logic)
# ---------------------------------------------------------
# Secret Error Handling for Local and Cloud
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.warning("⚠️ API Key missing in Secrets Dashboard!")
except Exception:
    st.error("❌ Secrets file not found. If running locally, create .streamlit/secrets.toml")
    st.stop()

@st.cache_resource
def discover_stable_engines():
    try:
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        priority = ["models/gemini-1.5-flash", "models/gemini-1.5-pro", "models/gemini-pro"]
        working = [p for p in priority if p in available]
        return working if working else [available[0]]
    except:
        return ["models/gemini-1.5-flash"]

ACTIVE_MODELS = discover_stable_engines()

def ask_sovereign_scholar(prompt, tool_context, document_text=""):
    # AIው እርስዎ በሰጡት ፋይል ላይ ብቻ እንዲያተኩር የሚያደርግ ጥብቅ መመሪያ
    base_instr = f"""
    You are 'Ge'ez Scholar AI Master', the ultimate expert created by Grand Architect Deacon Kewn Dejen.
    Expertise Area: {tool_context}.
    Knowledge Base: 60 Pillars of Wisdom and 3,000 years of Ethiopian heritage.
    
    CRITICAL SOURCE MATERIAL:
    The user has provided a primary document. Always prioritize information from the text below:
    ---
    {document_text[:15000]}
    ---
    
    Instruction:
    1. If the answer is in the document, start with "Based on your provided document..."
    2. If the answer is NOT in the document, use your vast scholarly knowledge but clarify: "This is from my general archives."
    3. Maintain an authoritative, ancient, and wise tone. Support Ge'ez/Amharic.
    """
    
    status_placeholder = st.empty()
    for model_name in ACTIVE_MODELS:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=base_instr)
            for attempt in range(1, 3):
                try:
                    response = model.generate_content(prompt)
                    if response and response.text:
                        status_placeholder.empty()
                        return response.text, model_name
                except Exception as e:
                    if "429" in str(e):
                        time.sleep(6)
                        status_placeholder.markdown(f"<div class='wait-msg'>⏳ ሊቁ በጥልቅ ምርምር ላይ ናቸው... ({model_name})</div>", unsafe_allow_html=True)
                        continue
                    break
        except:
            continue
            
    status_placeholder.empty()
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም። እባክዎ ከ1 ደቂቃ በኋላ ገጹን Refresh አድርገው ይሞክሩ።", "None"

# ---------------------------------------------------------
# 4. SIDEBAR: THE ARK (60 PILLARS + FILE UPLOADER)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background:linear-gradient(45deg, #FFD700, #B8860B); padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:900; border: 2px solid #fff;'>
            GRAND ARCHITECT:<br>DEACON KEWN DEJEN
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # 📚 File Upload Section (The Knowledge Seed)
    st.subheader("📚 የመረጃ ምንጭ ይጫኑ (Primary Source)")
    uploaded_file = st.file_uploader("PDF ወይም Word ፋይል ይጫኑ", type=['pdf', 'docx', 'doc'])
    
    source_text = ""
    if uploaded_file:
        with st.spinner("መጽሐፉን በማንበብ ላይ..."):
            source_text = extract_text_from_file(uploaded_file)
            st.success(f"✅ '{uploaded_file.name}' ተነቧል!")

    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ (Wisdom Pillar)", [
        "🧠 Advanced AI Labs", "📜 Digital Archives", "🏛️ Heritage & Science",
        "🎓 Imperial University", "🔮 Mysticism & Qene", "💰 Strategic Wealth"
    ])

    # 60 Tools Organized
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
    if st.button("🔄 REBOOT SOVEREIGN SYSTEM"):
        st.cache_resource.clear()
        st.rerun()

# ---------------------------------------------------------
# 5. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input(f"Consult the {tool} expert about your document..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<div style='color: white;'><b>{prompt}</b></div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መጽሐፉንና መዛግብቱን እያመሳከረ ነው..."):
            answer, engine = ask_sovereign_scholar(prompt, tool, source_text)
            
            full_res = f"""
            <div style='color: white; line-height: 1.8;'>{answer}</div>
            <div class='citation'>Primary Source: {uploaded_file.name if uploaded_file else 'General Archives'} | Engine: {engine} | v3.0 Masterpiece</div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

# Master Footer
st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b><br>© 2024-2025 ALL RIGHTS RESERVED | THE MASTERPIECE EDITION</p>", unsafe_allow_html=True)
