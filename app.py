import streamlit as st
import google.generativeai as genai

# 1. ገጹን በግርማ ሞገስ ማዘጋጀት (Imperial Setup)
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide"
)

# 2. የጥቁርና ወርቃማ ዲዛይን (CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    .stApp { background-color: #00050a; color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #d4af37 !important; text-align: center; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #010c17 0%, #1a0000 100%) !important; border-right: 3px solid #d4af37; }
    .stButton>button { background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important; color: #000 !important; font-weight: bold; border-radius: 10px; width: 100%; height: 3.5em; border: 1px solid #fff; }
    [data-testid="stChatInput"] { border: 2px solid #d4af37 !important; background-color: #001220 !important; border-radius: 20px; }
    .sovereign-card { background: rgba(255, 255, 255, 0.03); padding: 20px; border-radius: 15px; border-left: 8px solid #d4af37; border: 1px solid rgba(212, 175, 55, 0.2); }
    </style>
    """, unsafe_allow_html=True)

# 3. GOOGLE AI STUDIO ENGINE (ጀሚናይን የማንቀሳቀሻ ማዕከል)
def initialize_gemini():
    if "GOOGLE_API_KEY" not in st.secrets:
        st.error("⚠️ የ API ቁልፍ (Key) በ Secrets ውስጥ አልተገኘም!")
        return None
    
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # የእርስዎ ቁልፍ የሚፈቅደውን ሞዴል በራስ-ሰር መምረጥ
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # ቅደም ተከተል: Flash (ፈጣን) -> Pro (ጥልቅ) -> Legacy
        for target in ["1.5-flash", "2.0-flash", "1.5-pro", "gemini-pro"]:
            for model_path in available_models:
                if target in model_path:
                    return model_path
        return available_models[0]
    except Exception as e:
        st.error(f"Engine Error: {str(e)}")
        return None

MODEL_ID = initialize_gemini()

def ask_ai_scholar(prompt, tool_name):
    if not MODEL_ID: return "ሲስተሙን መክፈት አልተቻለም።"
    
    # ለሊቃውንት የተዘጋጀ ጥልቅ መመሪያ
    instruction = f"You are an expert in {tool_name}. Created by Grand Architect Deacon Kewn Dejen. Provide deep scholarly analysis."
    
    try:
        model = genai.GenerativeModel(model_name=MODEL_ID, system_instruction=instruction)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"ሊቁ መዛግብቱን ለመክፈት አልቻሉም። ስህተት፦ {str(e)}"

# 4. SIDEBAR - 60 PILLARS OF WISDOM
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center; color:#d4af37; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("የጥበብ ምሰሶ ይምረጡ", [
        "🏠 Imperial Dashboard", "🧠 Advanced AI Labs", "📜 Digital Archives & Law",
        "🏛️ Heritage & Ancient Science", "🎓 Imperial University Hub", "🔮 Mysticism & Qene Lab"
    ])

    if pillar == "🏠 Imperial Dashboard": tool = "Sovereign Overview"
    elif pillar == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom"])
    elif pillar == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast AI", "Synaxarium AI", "Royal Decrees", "Treaty Expert"])
    elif pillar == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI"])
    elif pillar == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter"])
    else:
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Proverbs AI"])

# 5. MAIN WORKSPACE
if pillar == "🏠 Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='sovereign-card'><h3>ክቡር ዲያቆን ሆይ፤ እንኳን ደህና መጡ!</h3><p>ስቱዲዮው በ {MODEL_ID} ኢንጅን አማካኝነት ከ Google AI Studio ጋር ተገናኝቶ ለሥራ ዝግጁ ነው።</p></div>", unsafe_allow_html=True)
else:
    st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input(f"{tool}ን ይጠይቁ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን እያመሳከረ ነው..."):
            res = ask_ai_scholar(prompt, tool)
            st.markdown(res)
            st.session_state.messages.append({"role": "assistant", "content": res})

st.markdown("<br><hr><p style='text-align:center; color:#d4af37;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
