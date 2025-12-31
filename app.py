import streamlit as st
import google.generativeai as genai
from PIL import Image
import time
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

# Professional Imperial Navy & Gold Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    .stApp { background: radial-gradient(circle at center, #001f3f 0%, #000814 100%); color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; text-shadow: 2px 2px 8px #000; }
    [data-testid="stSidebar"] { background-color: #000b1a !important; border-right: 3px solid #D4AF37; }
    p, span, label, div { color: #ffffff !important; font-size: 1.1rem; line-height: 1.7; }
    .sovereign-card { background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(15px); padding: 30px; border-radius: 20px; border: 1px solid #D4AF37; margin-bottom: 25px; }
    .stButton>button { background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important; color: #000 !important; font-weight: 900 !important; border-radius: 10px; height: 3.8em; width: 100%; transition: 0.5s ease; text-transform: uppercase; }
    [data-testid="stChatInput"] { border: 3px solid #D4AF37 !important; background-color: #ffffff !important; border-radius: 15px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.1rem !important; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. DYNAMIC ENGINE DISCOVERY (Fail-Safe Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    @st.cache_resource
    def get_stable_model():
        try:
            available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            priority = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]
            for target in priority:
                for actual in available:
                    if target in actual: return actual
            return available[0]
        except:
            return "models/gemini-1.5-flash"

    SELECTED_MODEL = get_stable_model()
else:
    st.error("API Key missing! Please check Secrets.")
    st.stop()

def ask_geez_scholar(prompt, tool_context, image=None):
    # This function is now guaranteed to always return 2 values (tuple)
    sys_instr = f"You are 'Ge'ez Scholar AI Master', an expert in {tool_context}, created by Deacon Kewn Dejen. Provide scholarly depth."
    try:
        model = genai.GenerativeModel(model_name=SELECTED_MODEL, system_instruction=sys_instr)
        # Attempt content generation with 429 Retry logic
        for i in range(2):
            try:
                if image:
                    response = model.generate_content([prompt, image])
                else:
                    response = model.generate_content(prompt)
                
                if response and response.text:
                    return response.text, SELECTED_MODEL
            except Exception as e:
                if "429" in str(e):
                    time.sleep(5)
                    continue
                break
        return "❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም (ኮታ አልቋል)። እባክዎ ከ30 ሰከንድ በኋላ በድጋሚ ይሞክሩ።", "None"
    except Exception as e:
        return f"❌ የቴክኒክ ስህተት፦ {str(e)}", "Error"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60 PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:10px; border-radius:12px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene", "Strategic Wealth"])

    if pillar == "Advanced AI Labs": tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Voice of Wisdom", "Neural Translation"])
    elif pillar == "Archives & Law": tool = st.radio("Archives", ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees"])
    elif pillar == "Heritage & Science": tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"])
    elif pillar == "University Hub": tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"])
    elif pillar == "Mysticism & Qene": tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub"])
    else: tool = st.radio("Strategic", ["Premium Business Hub", "API Portal", "Security Admin", "Wealth Strategy"])

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
            # Fixed Unpacking: Always returns 2 values
            answer, engine = ask_geez_scholar(prompt, tool)
            
            full_res = f"<div>{answer}</div><div style='font-size:0.8rem; color:#FFD700; margin-top:20px; border-top:1px solid #555; padding-top:10px;'>Intelligence Source: {engine} | Glory Edition</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
