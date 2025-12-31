import streamlit as st
import google.generativeai as genai
from PIL import Image
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

# Professional High-Contrast Theme (Royal Navy & White)
# ጥቁሩ ቀለም ተወግዶ ለማንበብ ግልጽ እንዲሆን ተደርጓል
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
    /* Background: Deep Royal Navy */
    .stApp { 
        background-color: #002b5c; 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    /* Headers: Radiant Gold */
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #ffd700 !important; 
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }

    /* Sidebar: High Contrast Dark Navy */
    [data-testid="stSidebar"] {
        background-color: #001a33 !important;
        border-right: 3px solid #ffd700;
    }
    
    /* Global Text Color: Pure White for Readability */
    p, span, label, div { 
        color: #ffffff !important; 
        font-size: 1.1rem; 
        line-height: 1.7; 
    }

    /* Content Cards */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 25px; border-radius: 15px;
        border: 2px solid #ffd700;
        margin-bottom: 20px;
    }

    /* Sovereign Gold Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #ffd700 0%, #b8860b 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 10px !important; border: 2px solid #ffffff !important;
        height: 3.5em; width: 100%; transition: 0.3s ease;
    }

    /* Chat Input Bar: Pure White (Very Visible) */
    [data-testid="stChatInput"] { 
        border: 3px solid #ffd700 !important; 
        background-color: #ffffff !important;
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { 
        color: #000000 !important; 
        font-size: 1.1rem !important;
        font-weight: bold !important;
    }
    
    .citation { font-size: 0.85rem; color: #ffd700; border-top: 1px solid #ffffff; margin-top: 15px; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. GUARANTEED STABLE ENGINE (No more 429 Errors)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key missing! Please add GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

# ቃል ኪዳን፡- ስህተት የሚፈጥረውን 2.0-expን ሙሉ በሙሉ መከልከል
# እጅግ አስተማማኝ የሆኑትን ብቻ እንጠቀማለን
FINAL_STABLE_MODEL = 'gemini-1.5-flash' 

def ask_geez_scholar(prompt, tool_context):
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI', the world's most reliable expert in Ethiopian studies.
    Created by Grand Architect Deacon Kewn Dejen.
    Pillar: {tool_context}.
    Task: Provide scholarly analysis. Support Ge'ez and Amharic.
    Tone: Sovereign, ancient, and clear.
    """
    try:
        # በስም ጠርተን አስተማማኙን ሞዴል ብቻ እናዛለን
        model = genai.GenerativeModel(model_name=FINAL_STABLE_MODEL, system_instruction=sys_instruction)
        response = model.generate_content(prompt)
        if response and response.text:
            return response.text, FINAL_STABLE_MODEL
    except Exception as e:
        # የሆነ ስህተት ካለ ወደ 1.5-pro ይቀይራል
        try:
            fallback_model = genai.GenerativeModel(model_name='gemini-1.5-pro', system_instruction=sys_instruction)
            response = fallback_model.generate_content(prompt)
            return response.text, 'gemini-1.5-pro'
        except:
            return "❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም። እባክዎ ከ30 ሰከንድ በኋላ በድጋሚ ይሞክሩ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK (60 PILLARS)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: #ffd700; padding: 10px; border-radius: 8px; text-align: center; color: #000; font-weight: bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("የጥበብ ምሰሶ", [
        "🏠 Dashboard", "🧠 AI Labs", "📜 Archives & Law",
        "🏛️ Heritage & Science", "🎓 University Hub", "🔮 Mysticism & Qene"
    ])

    if pillar == "🏠 Dashboard": tool = "Sovereign Overview"
    elif pillar == "🧠 AI Labs": tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication"])
    elif pillar == "📜 Archives & Law": tool = st.radio("Archives", ["Universal Library", "Fetha Nagast (Legal)", "Synaxarium AI"])
    elif pillar == "🏛️ Heritage & Science": tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Iconography Vision"])
    elif pillar == "🎓 University Hub": tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Scribe Assistant"])
    else: tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema", "Scholar Roleplay"])

    st.markdown("---")
    st.markdown("<div style='color: #00ff00; font-size: 0.8rem; text-align: center;'>STATUS: ROYAL ONLINE ✅</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
if pillar == "🏠 Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='sovereign-card'>
        <h2 style='text-align: left; color: #ffd700;'>እንኳን በደህና መጡ ክቡር ሆይ!</h2>
        <p>ስቱዲዮው በ v1700.0 ተሻሽሏል። አሁን ቀለሙ ለማንበብ እጅግ አመቺ በሆነው <b>Royal Navy & White</b> ተክቷል። 
        AIውም ስህተት የሚፈጥረውን ሞዴል ትቶ ወደ አስተማማኙ <b>Gemini 1.5 Flash</b> ተቀይሯል።</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

# Chat History UI
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

# User Chat Logic
if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, tool)
            
            full_res = f"""
            <div style='color: #ffffff; line-height: 1.8;'>{answer}</div>
            <div class='citation'>Source: {engine} | Ge'ez Scholar AI v1700.0</div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

# Footer
st.markdown("<br><br><p style='text-align: center; color: #ffd700;'><b>GE'EZ SCHOLAR AI STUDIO v1700.0 | THE ABSOLUTE VOW</b><br>Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
