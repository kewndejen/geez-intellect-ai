import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
import time
import random
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
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
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
        border: 1px solid #FFD700;
        margin-bottom: 25px;
        box-shadow: 0 15px 45px rgba(0,0,0,0.6);
    }

    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #FFFFFF !important;
        height: 3.8em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 0 35px #FFD700; }

    [data-testid="stChatInput"] { 
        border: 3px solid #FFD700 !important; 
        background-color: #ffffff !important; 
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.2rem !important; }
    
    .wait-msg { color: #FFD700; font-style: italic; font-size: 1rem; text-align: center; font-weight: bold; }
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #ffffff; margin-top: 25px; padding-top: 15px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. FILE PROCESSING ENGINE
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
# 3. INDESTRUCTIBLE AI ENGINE (Auto-Retry Failover)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም!")
    st.stop()

# የተረጋጉ ሞዴሎች ቅደም ተከተል (Flash መጀመሪያ - ለሰፊ ኮታ)
STABLE_MODELS = ['gemini-1.5-flash', 'gemini-2.0-flash-exp', 'gemini-1.5-pro']

def ask_sovereign_scholar(prompt, tool_context, document_text=""):
    sys_instr = f"""
    You are 'Ge'ez Scholar AI Master', the ultimate expert created by Grand Architect Deacon Kewn Dejen.
    Current Specialized Pillar: {tool_context}.
    Task: Provide scholarly, historical, and deep analysis in Ge'ez/Amharic.
    Primary Reference Document: {document_text[:12000]}
    Instructions:
    1. If the info is in the document, use it. 2. Support phonetic Ge'ez typing. 3. Be wise and authoritative.
    """
    
    status_placeholder = st.empty()
    
    # ተስፋ የማይቆርጥ ሎጂክ (Auto-Retry across models)
    for model_name in STABLE_MODELS:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instr)
            # ለእያንዳንዱ ሞዴል 3 ጊዜ በራሱ ይሞክራል (429 ካጋጠመው)
            for attempt in range(1, 4):
                try:
                    response = model.generate_content(prompt)
                    if response and response.text:
                        status_placeholder.empty()
                        return response.text, model_name
                except Exception as e:
                    if "429" in str(e):
                        wait = (attempt * 5) + random.random()
                        status_placeholder.markdown(f"<div class='wait-msg'>⏳ ሊቁ በጥልቅ ምርምር ላይ ናቸው... (ሙከራ {attempt}/3 - {model_name})</div>", unsafe_allow_html=True)
                        time.sleep(wait) # ራሱ ታግሶ እንዲሞክር ያደርጋል
                        continue
                    break # ሌሎች ስህተቶች ካሉ ወደ ቀጣዩ ሞዴል ይዞራል
        except:
            continue
            
    status_placeholder.empty()
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም (ኮታ አልቋል)። እባክዎ ከ1 ደቂቃ በኋላ ገጹን Refresh አድርገው ይሞክሩ።", "None"

# ---------------------------------------------------------
# 4. SIDEBAR: THE ARK OF 60 PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:900; border: 2px solid #fff;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("የጥበብ ምሰሶ", [
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
    uploaded_file = st.file_uploader("📚 የመረጃ ምንጭ (PDF/Word)", type=['pdf', 'docx'])
    source_text = ""
    if uploaded_file:
        source_text = extract_text_from_file(uploaded_file)
        st.success("መጽሐፉ ተነቧል!")

# ---------------------------------------------------------
# 5. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
            answer, engine = ask_sovereign_scholar(prompt, tool, source_text)
            full_res = f"<div>{answer}</div><div class='citation'>Source: {engine} | v3.0 Masterpiece</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b></p>", unsafe_allow_html=True)
