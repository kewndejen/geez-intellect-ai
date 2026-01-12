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
    
    p, span, label, div, .stMarkdown { color: #f8f9fa !important; font-size: 1.1rem; line-height: 1.8; }

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
        border-radius: 20px !important; 
        padding: 8px !important;
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.2rem !important; }
    
    .wait-msg { color: #FFD700; font-style: italic; font-size: 1rem; text-align: center; font-weight: bold; background: rgba(0,0,0,0.3); padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. INDESTRUCTIBLE ENGINE (Fail-Safe Retry Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም!")
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
    sys_instr = f"""
    You are 'Ge'ez Scholar AI Master', the ultimate expert created by Grand Architect Deacon Kewn Dejen.
    Expertise Area: {tool_context}. Knowledge: 60 Pillars of Wisdom.
    Context from Doc: {document_text[:15000]}
    Task: Provide scholarly, direct, and deep analysis. Support Ge'ez/Amharic.
    Tone: Sovereign, authoritative, and ancient. 
    """
    
    status_placeholder = st.empty()
    
    # ተስፋ የማይቆርጥ ሎጂክ (Retry Loop for 429 Errors)
    for model_name in ACTIVE_MODELS:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instr)
            
            # ለእያንዳንዱ ሞዴል 3 ጊዜ የመሞከር ዕድል ይሰጣል
            for attempt in range(1, 4):
                try:
                    response = model.generate_content(prompt)
                    if response and response.text:
                        status_placeholder.empty()
                        return response.text, model_name
                except Exception as e:
                    if "429" in str(e):
                        # መንገዱ ከተዘጋ ለጥቂት ሰከንዶች ይቆያል
                        wait = (attempt * 7) + random.random()
                        status_placeholder.markdown(f"<div class='wait-msg'>⏳ ሊቁ በጥልቅ ምርምር ላይ ናቸው... (ሙከራ {attempt}/3 - {model_name})</div>", unsafe_allow_html=True)
                        time.sleep(wait)
                        continue
                    break # ሌሎች ስህተቶች ካሉ ወደ ቀጣዩ ሞዴል ይዞራል
        except:
            continue
            
    status_placeholder.empty()
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም (ኮታ አልቋል)። እባክዎ ከ1 ደቂቃ በኋላ ገጹን Refresh አድርገው ይሞክሩ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60 PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:900;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("Select Wisdom Pillar", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    
    tools_map = {
        "Advanced AI Labs": ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Neural Translation"],
        "Archives & Law": ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees"],
        "Heritage & Science": ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"],
        "University Hub": ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"],
        "Mysticism & Qene": ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub"]
    }
    tool = st.radio("Labs", tools_map[pillar])

    if st.button("🔄 REBOOT SYSTEM"):
        st.cache_resource.clear()
        st.rerun()

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
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
        answer, engine = ask_sovereign_scholar(prompt, tool)
        
        full_res = f"""
        <div>{answer}</div>
        <div style='font-size:0.8rem; color:#FFD700; border-top:1px solid #ffffff33; margin-top:15px; padding-top:10px;'>
            Source: {engine} | v5.0 Sovereign Zenith
        </div>
        """
        st.markdown(full_res, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
