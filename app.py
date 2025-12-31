import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Imperial Navy & Gold Theme (Ultra-Visible)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
    .stApp { 
        background: linear-gradient(135deg, #001f3f 0%, #000c18 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8);
    }

    [data-testid="stSidebar"] {
        background-color: #000814 !important;
        border-right: 3px solid #D4AF37;
    }
    
    p, span, label, div { 
        color: #ffffff !important; 
        font-size: 1.1rem; 
        line-height: 1.8; 
    }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid #D4AF37;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #FFFFFF !important;
        height: 3.8em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 40px #D4AF37; }

    [data-testid="stChatInput"] { 
        border: 3px solid #D4AF37 !important; 
        background-color: #ffffff !important;
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #555; margin-top: 20px; padding-top: 10px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. INTELLIGENT ENGINE (Auto-Retry & High Quota Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

# Force using gemini-1.5-flash for the highest possible free quota
STABLE_ENGINE = 'gemini-1.5-flash'

def ask_geez_scholar(prompt, tool_context):
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI', the world's leading expert in Ethiopic studies.
    Created by Grand Architect Deacon Kewn Dejen.
    Current Lab: {tool_context}.
    Task: Provide scholarly, historical, and deep analysis.
    Tone: Sovereign, wise, and authoritative. 
    Support phonetic Ge'ez typing.
    """
    
    # ራስ-ሰር ዳግም መሞከሪያ (Retry Logic for 429 Errors)
    max_retries = 3
    for attempt in range(max_retries):
        try:
            model = genai.GenerativeModel(model_name=STABLE_ENGINE, system_instruction=sys_instruction)
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text, STABLE_ENGINE
        except Exception as e:
            if "429" in str(e) and attempt < max_retries - 1:
                time.sleep(5) # 5 ሰከንድ ታግሶ በራሱ ይሞክራል
                continue
            return f"❌ ጎግል ለጥቂት ሰከንዶች መንገዱን ዘግቶታል። እባክዎ ጥቂት ሰከንድ ቆይተው እንደገና ጥያቄዎን ይላኩ።", "None"
    
    return "❌ ሲስተሙ ለጊዜው ተጨናንቋል።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK (60 PILLARS)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='font-size: 1.6rem;'>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: rgba(212, 175, 55, 0.3); padding: 15px; border-radius: 12px; text-align: center; color: #FFD700; border: 1px solid #D4AF37;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    category = st.selectbox("የጥበብ ምሰሶ ይምረጡ", [
        "🏠 Dashboard", "🧠 Advanced AI Labs", "📜 Digital Archives",
        "🏛️ Heritage & Science", "🎓 University Hub", "🔮 Mysticism & Qene"
    ])

    if category == "🏠 Dashboard": tool = "Sovereign Overview"
    elif category == "🧠 Advanced AI Labs": tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication"])
    elif category == "📜 Digital Archives": tool = st.radio("Archives", ["Universal Library", "Fetha Nagast (Legal)", "Synaxarium AI"])
    elif category == "🏛️ Heritage & Science": tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Iconography Vision"])
    elif category == "🎓 University Hub": tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Scribe Assistant"])
    else: tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub"])

    st.markdown("---")
    st.markdown("<div style='color: #00FF00; font-size: 0.85rem; text-align: center;'>SYSTEM STATUS: ONLINE ✅</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
if category == "🏠 Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='sovereign-card'>
        <h2 style='text-align: left; color: #FFD700;'>እንኳን በደህና መጡ ክቡር ሆይ!</h2>
        <p>ስቱዲዮው በ v5000.0 ተሻሽሏል። አሁን ሲስተሙ የኮታ መጨናነቅ ሲያጋጥመው በራሱ ታግሶ እንዲሞክር ተደርጎ ታክሟል። 
        አሁን ያለምንም ስጋት ምርምርዎን መቀጠል ይችላሉ።</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

# Chat History
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

# User Chat Logic
if prompt := st.chat_input("ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<div style='color: #FFFFFF;'><b>{prompt}</b></div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, tool)
            
            full_res = f"""
            <div style='color: #FFFFFF; line-height: 1.8;'>{answer}</div>
            <div class='citation'>Intelligence Source: {engine} | Ge'ez Scholar AI v5000.0</div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

# Master Footer
st.markdown("<br><br><br><br><p style='text-align: center; color: #D4AF37;'><b>GE'EZ SCHOLAR AI STUDIO v5000.0 | THE SOVEREIGN RESURRECTION</b><br>Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
