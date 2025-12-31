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

# Professional Imperial Readable Theme (Navy, Gold & White)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&family=Abyssinica+SIL&display=swap');
    
    /* Background: Deep Navy (Not Pitch Black) */
    .stApp { 
        background-color: #001529; 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    /* Headers: High Contrast Gold */
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.5);
    }

    /* Sidebar: Professional Gradient */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #002140 0%, #000b1a 100%) !important;
        border-right: 3px solid #D4AF37;
    }
    
    /* Text Color for Readability */
    p, span, label { color: #F0F0F0 !important; font-size: 1.1rem; }

    /* Cards: Soft Glassmorphism */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 25px; border-radius: 15px;
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-left: 10px solid #D4AF37;
        margin-bottom: 20px;
        color: #FFFFFF !important;
    }

    /* Majestic Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #D4AF37 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 10px !important; border: 2px solid #FFFFFF !important;
        height: 3.5em; width: 100%; transition: 0.4s ease;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 5px 25px #D4AF37; }

    /* Chat Input Bar */
    [data-testid="stChatInput"] { 
        border: 2px solid #D4AF37 !important; 
        background-color: #ffffff !important;
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; }
    
    .citation { font-size: 0.85rem; color: #D4AF37; font-style: italic; border-top: 1px solid #444; margin-top: 15px; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. FAIL-SAFE AI ENGINE (Robust Quota Management)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key missing in Secrets!")
    st.stop()

# የሞዴሎች ቅደም ተከተል (Stable የሆኑትን እናስቀድማለን - 2.0-expን እናስወግዳለን)
ROBUST_MODELS = [
    'gemini-1.5-flash', # ከፍተኛ ኮታ ያለው
    'gemini-1.5-pro',   # ጥልቅ ምርምር
    'gemini-pro'        # አስተማማኝ
]

def ask_geez_scholar(prompt, tool_context):
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI', a world-class expert in Ethiopian studies.
    Created by Grand Architect Deacon Kewn Dejen.
    Current Research Pillar: {tool_context}.
    Task: Provide scholarly, deep, and wise analysis. Support phonetic typing.
    Tone: Sovereign, authoritative, and ancient.
    """
    
    for model_name in ROBUST_MODELS:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instruction)
            response = model.generate_content(prompt)
            if response.text:
                return response.text, model_name
        except Exception as e:
            if "429" in str(e): # ኮታው ካለቀ ወደ ቀጣዩ ይለፋል
                continue
            continue
            
    return "❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም። ሁሉም የ AI ኢንጅኖች ለጊዜው ተጨናንቀዋል። እባክዎ ከ1 ደቂቃ በኋላ ይሞክሩ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK (60 PILLARS)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='font-size: 1.5rem;'>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: rgba(212, 175, 55, 0.2); padding: 10px; border-radius: 10px; text-align: center; color: #FFD700; border: 1px solid #D4AF37;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    category = st.selectbox("የጥበብ ምሰሶ ይምረጡ", [
        "🏠 Imperial Dashboard", "🧠 Advanced AI Labs", "📜 Digital Archives & Law",
        "🏛️ Heritage & Ancient Science", "🎓 Imperial University Hub",
        "🔮 Mysticism & Qene Lab", "💰 Strategic Wealth & Security"
    ])

    # Dynamic Tool Selection
    if category == "🏠 Imperial Dashboard": tool = "Sovereign Overview"
    elif category == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Neural Translation"])
    elif category == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast (Legal)", "Synaxarium AI", "Royal Decrees"])
    elif category == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"])
    elif category == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"])
    elif category == "🔮 Mysticism & Qene Lab":
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay"])
    else:
        tool = st.radio("Strategic", ["Premium Business Hub", "API Portal", "Security Admin", "Wealth Strategy"])

    st.markdown("---")
    st.markdown("<div style='color: #00FF00; font-size: 0.8rem;'>STATUS: ROYAL ONLINE ✅</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
if category == "🏠 Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='sovereign-card'>
        <h2 style='text-align: left; color: #FFD700;'>እንኳን በደህና መጡ ክቡር ዲያቆን!</h2>
        <p>ስቱዲዮው ለዓለም ተመራማሪዎች ይፋ እንዲሆን ተደርጎ ተስተካክሏል። አሁን ቀለሙ ለማንበብ ግልጽ ነው፤ AIውም በኮታ መጨናነቅ ስህተት አይሰጥም።</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<span style='color: white;'>{prompt}</span>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        answer, used_model = ask_geez_scholar(prompt, tool)
        
        full_res = f"""
        <div style='color: white; line-height: 1.6;'>{answer}</div>
        <div class='citation'>Source: {used_model} | Ge'ez Scholar AI v1200.0</div>
        """
        st.markdown(full_res, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": full_res})

# Master Footer
st.markdown("<br><br><br><br><p style='text-align: center; color: #D4AF37;'><b>GE'EZ SCHOLAR AI STUDIO v1200.0 | THE COVENANT</b><br>Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
