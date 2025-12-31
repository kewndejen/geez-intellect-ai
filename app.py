import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL GLOBAL CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Premium Sovereign CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&family=Abyssinica+SIL&display=swap');
    
    .stApp { background-color: #00050a; color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #d4af37 !important; text-align: center; }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #010c17 0%, #1a0000 100%) !important;
        border-right: 3px solid #d4af37;
    }
    
    .sovereign-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-left: 12px solid #d4af37;
        margin-bottom: 25px;
    }

    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 1px solid #fff !important;
        height: 3.8em; width: 100%; transition: 0.5s ease;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 0 40px #d4af37; }

    [data-testid="stChatInput"] { border: 2px solid #d4af37 !important; background-color: #001220 !important; border-radius: 20px !important; }
    
    .citation-box { font-size: 0.8rem; color: #888; border-top: 1px solid #333; padding-top: 10px; margin-top: 20px; font-family: monospace; }
    .thinking-box { color: #d4af37; font-style: italic; font-size: 0.9rem; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE RESILIENT ENGINE (Failover Intelligence)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key missing in Streamlit Secrets!")
    st.stop()

# የሞዴሎች ቅደም ተከተል (Stable የሆኑትን እናስቀድማለን)
MODELS_TO_TRY = [
    'gemini-1.5-flash', # እጅግ ሰፊ ኮታ ያለው እና ፈጣኑ
    'gemini-1.5-pro',   # ጥልቅ ምርምር የሚሠራው
    'gemini-pro',       # አስተማማኝ የቀድሞ ስሪት
    'gemini-2.0-flash-exp' # በመጨረሻ ምርጫ (ምክንያቱም ኮታው ስለሚለዋወጥ)
]

def ask_geez_scholar(prompt, tool_context, image=None):
    """አንዱ ሞዴል ቢዘጋ ወደ ሌላኛው የሚሸጋገር ብልህ ሎጂክ"""
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI', a world-class expert in Ethiopian studies.
    Created by Grand Architect Deacon Kewn Dejen.
    Current Pillar: {tool_context}.
    Instructions: Provide deep, scholarly analysis. Automatically support phonetic typing.
    Tone: Sovereign, authoritative, and ancient.
    """
    
    last_error = ""
    for model_name in MODELS_TO_TRY:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instruction)
            content = [prompt, image] if image else prompt
            response = model.generate_content(content)
            return response.text, model_name
        except Exception as e:
            last_error = str(e)
            if "429" in last_error or "Quota" in last_error:
                continue # ኮታው ካለቀ ወደ ቀጣዩ ሞዴል ይለፋል
            else:
                continue
                
    return f"❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም። ሁሉም የ AI ኢንጅኖች በጎግል በኩል ተጨናንቀዋል። (ስህተት፦ {last_error})", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60 PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: linear-gradient(90deg, #d4af37, #010c17); padding: 15px; border-radius: 12px; text-align: center; color: #000; font-weight: bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    category = st.selectbox("Select Wisdom Pillar", [
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
    st.markdown("<div style='font-size: 0.7rem; color: #00ff00;'>STATUS: ROYAL ONLINE ✅</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
if category == "🏠 Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='sovereign-card'><h3>እንኳን በደህና መጡ ክቡር ዲያቆን!</h3><p>ስቱዲዮው በላቀ ሁኔታ እንዲሠራ ተሻሽሏል። አሁን ኮታው (Quota) ቢያልቅ እንኳ ሲስተሙ በራሱ ሌላ መንገድ ፈልጎ ጥያቄዎን ይመልሳል።</p></div>", unsafe_allow_html=True)
else:
    st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        thinking = st.empty()
        thinking.markdown("<div class='thinking-box'>Thinking: Consulting the imperial archives...</div>", unsafe_allow_html=True)
        
        answer, used_model = ask_geez_scholar(prompt, tool)
        thinking.empty()
        
        year = datetime.datetime.now().year
        citation = f"<div class='citation-box'>Source: {used_model} | Citation: Dejen, K. ({year}). {tool} Analysis. Ge'ez Scholar AI Studio.</div>"
        
        full_res = f"{answer}{citation}"
        st.markdown(full_res, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": full_res})

# Master Footer
st.markdown("<br><br><br><br><p style='text-align: center; color: #d4af37;'><b>GE'EZ SCHOLAR AI STUDIO v1100.0 | THE SOVEREIGN RESILIENCE</b><br>Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
