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

# Professional Imperial Navy Theme (Extreme Readability & Focus)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&family=Abyssinica+SIL&display=swap');
    
    /* Background: Pure Imperial Navy */
    .stApp { 
        background-color: #001f3f; 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    /* Headers: High Contrast Radiant Gold */
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.8);
    }

    /* Sidebar: Royal Dark Gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #001226 0%, #000814 100%) !important;
        border-right: 3px solid #D4AF37;
    }
    
    /* Text Color for High Readability */
    p, span, label, .stMarkdown { 
        color: #FFFFFF !important; 
        font-size: 1.1rem; 
        line-height: 1.8; 
    }

    /* Cards: Soft Glassmorphism Content Box */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.5);
        border-left: 15px solid #D4AF37;
        margin-bottom: 25px;
    }

    /* Sovereign Golden Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #D4AF37 0%, #B8860B 100%) !important;
        color: #000000 !important; 
        font-weight: 900 !important;
        border-radius: 12px !important; 
        border: 2px solid #FFFFFF !important;
        height: 3.8em; width: 100%; 
        transition: 0.5s ease;
        text-transform: uppercase;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 35px #D4AF37; }

    /* Ultra-Readable Chat Input (White Background) */
    [data-testid="stChatInput"] { 
        border: 3px solid #D4AF37 !important; 
        background-color: #ffffff !important;
        border-radius: 15px !important; 
        padding: 8px !important;
    }
    [data-testid="stChatInput"] textarea { 
        color: #000000 !important; 
        font-size: 1.2rem !important; 
        font-weight: 500 !important;
    }
    
    .citation { font-size: 0.9rem; color: #FFD700; border-top: 1px solid #555; margin-top: 20px; padding-top: 10px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. BULLETPROOF ENGINE (Silent Failover Strategy)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Streamlit Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

# list of stable models to try in sequence
# gemini-2.0-flash-exp is REMOVED because it causes the 429 error.
STABLE_MODELS = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']

def ask_geez_scholar(prompt, tool_context):
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI', a world-class expert in Ethiopian studies.
    Created by Grand Architect Deacon Kewn Dejen.
    Current Research Pillar: {tool_context}.
    Mission: Provide scholarly, deep, and wise analysis. Support phonetic Ge'ez typing.
    Tone: Sovereign, authoritative, and ancient. 
    """
    
    # ይህ ሎጂክ አንዱ ሞዴል ቢዘጋ ወደ ቀጣዩ በራሱ ይሸጋገራል
    for model_name in STABLE_MODELS:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instruction)
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text, model_name
        except Exception as e:
            # 429 ወይም ሌላ ስህተት ቢመጣ በዝምታ ወደ ቀጣዩ ይለፋል
            continue
            
    return "❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም። ሁሉም የ AI ኢንጅኖች ለጊዜው ተጨናንቀዋል። እባክዎ ከ1 ደቂቃ በኋላ ይሞክሩ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK (60 PILLARS)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='font-size: 1.6rem;'>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: rgba(212, 175, 55, 0.2); padding: 15px; border-radius: 12px; text-align: center; color: #FFD700; border: 1px solid #D4AF37;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar_choice = st.selectbox("የጥበብ ምሰሶ ይምረጡ", [
        "🏠 Imperial Dashboard", "🧠 Advanced AI Labs", "📜 Digital Archives & Law",
        "🏛️ Heritage & Ancient Science", "🎓 Imperial University Hub",
        "🔮 Mysticism & Qene Lab", "💰 Strategic Wealth & Security"
    ])

    if pillar_choice == "🏠 Imperial Dashboard": tool = "Sovereign Overview"
    elif pillar_choice == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Neural Translation"])
    elif pillar_choice == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast (Legal)", "Synaxarium AI", "Royal Decrees"])
    elif pillar_choice == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"])
    elif pillar_choice == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"])
    elif pillar_choice == "🔮 Mysticism & Qene Lab":
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay"])
    else:
        tool = st.radio("Strategic", ["Premium Business AI", "API Portal", "Security Admin", "Wealth Strategy"])

    st.markdown("---")
    st.markdown("<div style='color: #00FF00; font-size: 0.85rem; text-align: center;'>SYSTEM STATUS: ROYAL ONLINE ✅</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
if pillar_choice == "🏠 Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='sovereign-card'>
        <h2 style='text-align: left; color: #FFD700;'>እንኳን በደህና መጡ ክቡር ሆይ!</h2>
        <p>ስቱዲዮው በ v1600.0 ተሻሽሏል። አሁን ቀለሙ ለማንበብ እጅግ አመቺ ነው፤ AIውም በራሱ የተረጋጋውን ሞዴል በመምረጥ የኮታ መጨናነቅን (429 Error) ያልፋል። ምርምርዎን በሰላም መቀጠል ይችላሉ።</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

# Chat History UI
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

# Chat Logic with Silent Failover
if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<div style='color: #FFFFFF;'>{prompt}</div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, tool)
            
            full_res = f"""
            <div style='color: #FFFFFF; line-height: 1.8;'>{answer}</div>
            <div class='citation'>Intelligence Source: {engine} | Ge'ez Scholar AI v1600.0</div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

# Master Footer
st.markdown("<br><br><br><br><p style='text-align: center; color: #D4AF37;'><b>GE'EZ SCHOLAR AI STUDIO v1600.0 | THE SOVEREIGN HEALING</b><br>Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
