import streamlit as st
import google.generativeai as genai
import time
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (Omega Masterpiece)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Majestic Imperial Theme (Extreme Contrast & Readability)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #001f3f 0%, #000814 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 8px #000;
    }

    [data-testid="stSidebar"] {
        background-color: #001226 !important;
        border-right: 3px solid #D4AF37;
    }
    
    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid #D4AF37;
        margin-bottom: 25px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; height: 3.8em; width: 100%; transition: 0.5s;
        text-transform: uppercase; border: 2px solid #fff;
    }

    [data-testid="stChatInput"] { 
        border: 3px solid #D4AF37 !important; 
        background-color: #ffffff !important;
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; font-size: 1.1rem; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #555; margin-top: 25px; padding-top: 15px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE OMEGA ENGINE (Indestructible Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Secrets ውስጥ ያስገቡ።")
    st.stop()

@st.cache_resource
def get_indestructible_model():
    """የሚሰራውን ሞዴል በራሱ ፈልጎ የሚያገኝ ሎጂክ"""
    try:
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        priority = ["models/gemini-1.5-flash", "models/gemini-1.5-pro", "models/gemini-pro"]
        for target in priority:
            for actual in available:
                if target in actual: return actual
        return available[0]
    except:
        return "models/gemini-1.5-flash"

ACTIVE_MODEL = get_indestructible_model()

def ask_geez_scholar(prompt, tool_context):
    """TypeError እንዳይመጣ ሁልጊዜም 2 እሴቶችን (tuple) እንደሚመልስ ዋስትና ይሰጣል"""
    sys_instr = f"You are 'Ge'ez Scholar AI Omega', an expert in {tool_context}, created by Deacon Kewn Dejen. Provide deep analysis."
    
    try:
        model = genai.GenerativeModel(model_name=ACTIVE_MODEL, system_instruction=sys_instr)
        # 429 ስህተት እንዳይመጣ በራሱ ደጋግሞ ይሞክራል
        for attempt in range(3):
            try:
                response = model.generate_content(prompt)
                if response and response.text:
                    return response.text, ACTIVE_MODEL
            except Exception as e:
                if "429" in str(e):
                    time.sleep(5)
                    continue
                break
        return "❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም። እባክዎ ገጹን Refresh አድርገው በድጋሚ ይሞክሩ።", "None"
    except Exception as e:
        return f"❌ የቴክኒክ ስህተት፦ {str(e)}", "Error"

# ---------------------------------------------------------
# 3. SIDEBAR: THE FULL ARK (60 PILLARS)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    
    if pillar == "Advanced AI Labs": tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Voice of Wisdom", "Ge'ez NLP"])
    elif pillar == "Archives & Law": tool = st.radio("Archives", ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees"])
    elif pillar == "Heritage & Science": tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"])
    elif pillar == "University Hub": tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"])
    else: tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub"])

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
            # Tuple Unpacking Fix: Guaranteed to work
            answer, engine = ask_geez_scholar(prompt, tool)
            
            full_res = f"<div>{answer}</div><div class='citation'>Source: {engine} | Omega Masterpiece v10k</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
