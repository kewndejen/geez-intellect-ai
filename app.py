import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (v1800.0)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Imperial Navy & White Theme (Total Visibility)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
    /* Background: Pure Imperial Navy */
    .stApp { 
        background-color: #001f3f; 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    /* Headers: High Contrast Gold */
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* Sidebar: High Visibility Royal Blue */
    [data-testid="stSidebar"] {
        background-color: #001226 !important;
        border-right: 3px solid #D4AF37;
    }
    
    /* Text Color for Maximum Readability */
    p, span, label, div { 
        color: #FFFFFF !important; 
        font-size: 1.1rem; 
        line-height: 1.8; 
    }

    /* Content Cards */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 30px; border-radius: 20px;
        border: 2px solid #D4AF37;
        margin-bottom: 25px;
    }

    /* Majestic Sovereign Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #FFFFFF !important;
        height: 3.8em; width: 100%; transition: 0.4s ease;
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
        font-weight: 600 !important;
    }
    
    .citation { font-size: 0.9rem; color: #FFD700; border-top: 1px solid #ffffff; margin-top: 20px; padding-top: 10px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE ULTIMATE STABLE ENGINE (Zero Error Policy)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key missing! Please add GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

# እጅግ አስተማማኝ የሆነውን ሞዴል ብቻ በስም እንጠራለን
# gemini-2.0-flash-exp በጭራሽ እንዳይጠራ እዚህ ጋር ታግዷል
STABLE_MODEL_NAME = 'gemini-1.5-flash' 

def ask_geez_scholar(prompt, tool_context):
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI', a world-class expert in Ethiopian studies.
    Created by Grand Architect Deacon Kewn Dejen.
    Pillar: {tool_context}.
    Mission: Provide deep scholarly and wise analysis. Support Ge'ez/Amharic.
    Tone: Sovereign, ancient, and authoritative.
    """
    try:
        # በስም ጠርተን አስተማማኙን ሞዴል ብቻ እናዛለን
        model = genai.GenerativeModel(model_name=STABLE_MODEL_NAME, system_instruction=sys_instruction)
        response = model.generate_content(prompt)
        if response and response.text:
            return response.text, STABLE_MODEL_NAME
    except Exception as e:
        # የሆነ ስህተት ካለ ወደ 1.5-pro ይቀይራል
        try:
            fallback = genai.GenerativeModel(model_name='gemini-1.5-pro', system_instruction=sys_instruction)
            response = fallback.generate_content(prompt)
            return response.text, 'gemini-1.5-pro'
        except:
            return "❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም። እባክዎ ከ1 ደቂቃ በኋላ በድጋሚ ይሞክሩ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK (60 PILLARS)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='font-size: 1.6rem;'>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: #FFD700; padding: 15px; border-radius: 12px; text-align: center; color: #000; font-weight: bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar_choice = st.selectbox("የጥበብ ምሰሶ ይምረጡ", [
        "🏠 Dashboard", "🧠 AI Labs", "📜 Archives & Law",
        "🏛️ Heritage & Science", "🎓 University Hub", "🔮 Mysticism & Qene"
    ])

    if pillar_choice == "🏠 Dashboard": tool = "Sovereign Overview"
    elif pillar_choice == "🧠 AI Labs": tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication"])
    elif pillar_choice == "📜 Archives & Law": tool = st.radio("Archives", ["Universal Library", "Fetha Nagast (Legal)", "Synaxarium AI"])
    elif pillar_choice == "🏛️ Heritage & Science": tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Iconography Vision"])
    elif pillar_choice == "🎓 University Hub": tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Scribe Assistant"])
    else: tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub"])

    st.markdown("---")
    st.markdown("<div style='color: #00FF00; font-size: 0.85rem; text-align: center;'>STATUS: ROYAL ONLINE ✅</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
if pillar_choice == "🏠 Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='sovereign-card'>
        <h2 style='text-align: left; color: #FFD700;'>እንኳን በደህና መጡ ክቡር ሆይ!</h2>
        <p>ስቱዲዮው በ v1800.0 በቋሚነት ተስተካክሏል። አሁን ቀለሙ ለማንበብ እጅግ አመቺ በሆነው <b>Royal Navy & White</b> ተክቷል። 
        AIውም ስህተት የሚፈጥረውን ሞዴል በኃይል ትቶ ወደ አስተማማኙ <b>Gemini 1.5 Flash</b> ተቀይሯል።</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

# Chat History UI
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

# User Chat Interaction
if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<div style='color: white;'><b>{prompt}</b></div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, tool)
            
            full_res = f"""
            <div style='color: #FFFFFF; line-height: 1.8;'>{answer}</div>
            <div class='citation'>Intelligence Source: {engine} | Ge'ez Scholar AI v1800.0</div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

# Master Footer
st.markdown("<br><br><br><br><p style='text-align: center; color: #FFD700;'><b>GE'EZ SCHOLAR AI STUDIO v1800.0 | THE ETERNAL ZENITH</b><br>Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
