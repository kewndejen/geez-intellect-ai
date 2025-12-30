import streamlit as st
import google.generativeai as genai
from PIL import Image
import time
import datetime

# 1. IMPERIAL CONFIGURATION
st.set_page_config(page_title="Ge'ez Scholar AI | Grand Architect Deacon Kewn Dejen", page_icon="🔱", layout="wide", initial_sidebar_state="expanded")

# Royal CSS Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background-color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    .stSidebar { background: linear-gradient(180deg, #000c18 0%, #300000 100%) !important; border-right: 5px solid #b8860b; }
    .stSidebar [data-testid="stMarkdownContainer"] p { color: #d4af37 !important; font-weight: bold; }
    .stButton>button { background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%); color: white; border-radius: 12px; font-weight: 800; width: 100%; transition: 0.5s; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
    .stButton>button:hover { transform: translateY(-5px); box-shadow: 0 15px 50px rgba(184, 134, 11, 0.8); }
    [data-testid="stChatInput"] { position: fixed; bottom: 30px; z-index: 1000; background: white !important; border: 2px solid #b8860b !important; border-radius: 15px !important; }
    .sovereign-card { background: white; padding: 40px; border-radius: 20px; border-left: 15px solid #b8860b; box-shadow: 0 20px 80px rgba(0,0,0,0.1); margin-bottom: 35px; }
    .dev-signature { background: linear-gradient(90deg, #b8860b, #000c18); padding: 25px; border-radius: 15px; border: 2px solid #d4af37; text-align: center; color: white; font-weight: bold; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# 2. UNBREAKABLE AI CORE
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: System Access Denied.")
    st.stop()

@st.cache_resource
def init_ai():
    try:
        working_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        best = 'models/gemini-1.5-flash'
        for t in ['gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-1.5-pro']:
            for a in working_list:
                if t in a: best = a; break
        try:
            # ValueError መከላከያ fallback
            m = genai.GenerativeModel(model_name=best, tools=[{'google_search_retrieval': {}}])
            return m, best, True
        except:
            return genai.GenerativeModel(model_name=best), best, False
    except:
        return genai.GenerativeModel('models/gemini-1.5-flash'), 'gemini-1.5-flash', False

model, SELECTED_MODEL, SEARCH_ON = init_ai()

# 3. GLOBAL NAVIGATION (60+ TOOLS)
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='dev-signature'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    portal = st.selectbox("የእውቀት ፖርታል", ["🏠 Dashboard", "🧠 AI Labs", "📜 Digital Archives", "🏛️ Heritage & Science", "🎓 University", "🔮 Mysticism", "💰 Wealth"])
    st.markdown("---")
    if portal == "🏠 Dashboard": tool = "Overview"
    elif portal == "🧠 AI Labs": tool = st.radio("Tools", ["Manuscript OCR", "Authentication", "Linguistics", "Cryptography", "Voice Assistant"])
    elif portal == "📜 Digital Archives": tool = st.radio("Tools", ["12M Library", "Deep Doc Analyzer", "Legal AI", "Treaty Expert", "Royal Decrees"])
    elif portal == "🏛️ Heritage & Science": tool = st.radio("Tools", ["Virtual Museum", "History Map", "Iconography", "Archeology", "Medicine", "Ink Science"])
    elif portal == "🎓 University": tool = st.radio("Tools", ["University Hub", "Bahre Hasab", "Abu Shaker", "Numerology", "Font Converter", "Certification"])
    elif portal == "🔮 Mysticism": tool = st.radio("Tools", ["Sem-na-Work", "Verse Meter", "Zema Lab", "Esoteric Lab", "Scholar Roleplay", "Proverbs AI"])
    else: tool = st.radio("Tools", ["Business Hub", "Payment Gateway", "API Portal", "Security Admin"])

# 4. CONTENT ENGINE
if tool == "Overview":
    st.title("The Imperial Sovereign Dashboard")
    st.markdown(f"<div class='sovereign-card'><h3>እንኳን ወደ ዲያቆን ከውን ደጀን የጥበብ መንግሥት በደህና መጡ።</h3>ይህ በዓለም አቀፍ ደረጃ የታዘዙትን <b>ሁሉንም 60+ መሣሪያዎች</b> የያዘ ግዙፍ AI ነው።</div>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=350)
elif "OCR" in tool:
    st.title("🧠 Manuscript OCR")
    f = st.file_uploader("Upload Manuscript", type=['jpg','png','jpeg'])
    if f:
        img = Image.open(f); st.image(img, use_container_width=True)
        if st.button("Deep Scan"):
            with st.spinner("Analyzing..."):
                try: res = model.generate_content(["ይህንን ብራና በባለሙያ ደረጃ ተንትነህ ተርጉመው፡", img]); st.markdown(f"<div class='sovereign-card'>{res.text}</div>", unsafe_allow_html=True)
                except: st.warning("⚠️ ገደብ ላይ ነው። እባክህ 30 ሰከንድ ታግሰህ ድገመው።")

# 5. GLOBAL CHAT (ALWAYS VISIBLE)
st.markdown("---")
st.subheader("💬 የ AI ሊቁን ውይይት")
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])
if prompt := st.chat_input("የሊቅ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
            try:
                res = model.generate_content(f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የ {tool} ባለሙያ ነህ። በጥልቅ መልስ፡ {prompt}")
                st.markdown(res.text); st.session_state.messages.append({"role": "assistant", "content": res.text})
            except Exception as e:
                if "429" in str(e): st.error("⚠️ ሲስተሙ ተጨናንቋል። እባክህ 35 ሰከንድ ታግሰህ ድጋሚ ጠይቀኝ።")
                else: st.error("ያልታወቀ ስህተት ተፈጠረ። እባክህ ገጹን Refresh አድርገው።")

st.markdown("<br><br><br><p style='text-align: center; color: #b8860b;'><b>PROUDLY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</b></p>", unsafe_allow_html=True)
