import streamlit as st
import google.generativeai as genai
import time

# 1. IMPERIAL PAGE CONFIGURATION
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide"
)

# 2. SOVEREIGN BLACK & GOLD THEME (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&display=swap');
    .stApp { background-color: #00050a; color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #d4af37 !important; text-align: center; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #010c17 0%, #1a0000 100%) !important; border-right: 3px solid #d4af37; }
    .stButton>button { background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important; color: #000 !important; font-weight: 900 !important; border-radius: 10px !important; border: 1px solid #fff !important; height: 3.5em; width: 100%; transition: 0.5s ease; }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 0 30px #d4af37; }
    [data-testid="stChatInput"] { border: 2px solid #d4af37 !important; background-color: #001220 !important; border-radius: 20px !important; }
    .sovereign-card { background: rgba(255, 255, 255, 0.03); padding: 25px; border-radius: 20px; border-left: 10px solid #d4af37; border: 1px solid rgba(212, 175, 55, 0.2); }
    </style>
    """, unsafe_allow_html=True)

# 3. PROFESSIONAL API CORE (THE ENGINE)
@st.cache_resource
def initialize_engine():
    if "GOOGLE_API_KEY" not in st.secrets:
        return None, "API Key Missing in Secrets"
    
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # የሚሰሩ ሞዴሎችን ዝርዝር ማረጋገጥ
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # ቅደም ተከተል: Flash (ፈጣን) -> Pro (ጥልቅ) -> Legacy (አስተማማኝ)
        for target in ["gemini-1.5-flash", "gemini-2.0-flash-exp", "gemini-1.5-pro", "gemini-pro"]:
            for model_name in available:
                if target in model_name:
                    return model_name, None
        return available[0], None
    except Exception as e:
        return None, str(e)

MODEL_NAME, ERROR = initialize_engine()

def ask_scholar(prompt, tool_context):
    if ERROR: return f"❌ System Error: {ERROR}"
    
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI Studio', a divine intelligence created by Deacon Kewn Dejen.
    Current Pillar: {tool_context}. 
    Your mission: Provide scholarly, historical, and theological analysis in Ge'ez, Amharic, or English.
    - Support phonetic Latin input (e.g. 'Selam' -> ሰላም).
    - Analyze Sem-na-Worq (Wax and Gold).
    - Tone: Sovereign, authoritative, and academic.
    """
    
    try:
        model = genai.GenerativeModel(model_name=MODEL_NAME, system_instruction=sys_instruction)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Retry logic with a secondary model if the primary fails
        try:
            fallback = genai.GenerativeModel("gemini-pro")
            res = fallback.generate_content(prompt)
            return res.text
        except:
            return f"ሊቁ መዛግብቱን ለመክፈት አልቻሉም። ስህተት፦ {str(e)}"

# 4. SIDEBAR: THE ARK OF 60 PILLARS
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: linear-gradient(90deg, #d4af37, #010c17); padding: 15px; border-radius: 10px; text-align: center; color: #000; font-weight: bold;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("Select Research Pillar", [
        "🏠 Imperial Dashboard", "🧠 Advanced AI Labs", "📜 Digital Archives & Law",
        "🏛️ Heritage & Ancient Science", "🎓 Imperial University Hub", "🔮 Mysticism & Qene Lab"
    ])

    if pillar == "🏠 Imperial Dashboard": tool = "Sovereign Overview"
    elif pillar == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Neural Translation"])
    elif pillar == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast AI", "Synaxarium AI", "Royal Decrees", "Treaty Expert"])
    elif pillar == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI"])
    elif pillar == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter"])
    else:
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Proverbs AI"])

    st.markdown("---")
    if MODEL_NAME: st.caption(f"Engine Online: {MODEL_NAME}")

# 5. MAIN WORKSPACE
if pillar == "🏠 Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='sovereign-card'><h3>እንኳን በደህና መጡ ክቡር ዲያቆን!</h3><p>ስቱዲዮው በ {MODEL_NAME} ኢንጅን አማካኝነት ለሥራ ዝግጁ ነው። በግራ በኩል መሣሪያ በመምረጥ ምርምርዎን ይጀምሩ።</p></div>", unsafe_allow_html=True)
else:
    st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን እያመሳከረ ነው..."):
            res = ask_scholar(prompt, tool)
            st.markdown(res)
            st.session_state.messages.append({"role": "assistant", "content": res})

st.markdown("<br><hr><p style='text-align:center; color:#d4af37;'>GE'EZ SCHOLAR AI STUDIO | DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>", unsafe_allow_html=True)
