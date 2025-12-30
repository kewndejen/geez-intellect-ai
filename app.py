import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL PRESTIGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Sovereign Search Edition",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Professional Imperial CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background-color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    
    .stSidebar { 
        background: linear-gradient(180deg, #000c18 0%, #300000 100%) !important; 
        border-right: 5px solid #b8860b; 
    }
    .stSidebar [data-testid="stMarkdownContainer"] p { color: #d4af37 !important; font-weight: bold; }

    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%);
        color: white; border: none; padding: 18px 30px;
        border-radius: 12px; font-weight: 800; width: 100%;
        font-size: 16px; letter-spacing: 1px; transition: 0.5s;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    [data-testid="stChatInput"] {
        position: fixed; bottom: 30px; z-index: 1000;
        background: white !important; border: 2px solid #b8860b !important;
        border-radius: 15px !important;
    }
    
    .sovereign-card {
        background: white; padding: 40px; border-radius: 20px;
        border-left: 15px solid #b8860b; box-shadow: 0 20px 80px rgba(0,0,0,0.1);
        margin-bottom: 35px; border-top: 1px solid #f0f0f0;
    }
    
    .dev-signature {
        background: linear-gradient(90deg, #b8860b, #000c18);
        padding: 25px; border-radius: 15px; border: 2px solid #d4af37;
        text-align: center; color: white; font-weight: bold; margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. DYNAMIC AI CORE WITH GOOGLE SEARCH (Kewn Dejen Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: System Credentials Missing. Contact Deacon Kewn Dejen.")
    st.stop()

@st.cache_resource
def get_best_working_model():
    try:
        working_model = ""
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                if "gemini-2.0-flash" in m.name or "gemini-1.5-pro" in m.name:
                    working_model = m.name
                    break
        if not working_model:
            working_model = 'models/gemini-1.5-flash'
        return working_model
    except:
        return 'models/gemini-1.5-flash'

SELECTED_MODEL = get_best_working_model()

# 🔥 GOOGLE SEARCH TOOL ን እዚህ ጋር እናገናኘዋለን
# ይህ AIው ቀጥታ ከጎግል መረጃ እንዲያመጣ ያደርገዋል
tools_config = [
    {"google_search": {}}
]

model = genai.GenerativeModel(
    model_name=SELECTED_MODEL,
    tools=tools_config
)

# ---------------------------------------------------------
# 3. GLOBAL NAVIGATION - 60+ PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='dev-signature'>GRAND ARCHITECT & DEVELOPER:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    main_portal = st.selectbox("የእውቀት ምድብ", [
        "🏠 Imperial Dashboard",
        "🧠 Advanced AI Research Labs",
        "📜 Digital Libraries & Archives",
        "🏛️ Heritage, Map & Material Science",
        "🎓 Imperial University & Science",
        "🔮 Mysticism, Poetry & Prophecy",
        "💰 Strategic Business & Security"
    ])
    
    st.markdown("---")
    st.info(f"Active Model: {SELECTED_MODEL}")
    st.success("Google Search Grounding: ENABLED ✅")

# ---------------------------------------------------------
# 4. CONTENT ENGINE
# ---------------------------------------------------------

if main_portal == "🏠 Imperial Dashboard":
    st.title("The Absolute Emperor Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Reasoning Depth", "12M+ Pages", "Infinite")
    col2.metric("Search Mode", "Live Google Search", "Online")
    col3.metric("Lead Architect", "Kewn Dejen", "Verified")
    
    st.markdown(f"""
    <div class='sovereign-card'>
    <h3>እንኳን ወደ ዲያቆን ከውን ደጀን የጥበብ መንግሥት በደህና መጡ።</h3>
    ይህ ሲስተም አሁን <b>ከጎግል (Google Search)</b> ጋር የተገናኘ በመሆኑ ማንኛውንም ወቅታዊ ጥያቄ መመለስ ይችላል። 
    AIው መልስ ሲሰጥ መረጃውን ከኢንተርኔት ላይ በማመሳከር እጅግ አስተማማኝ ያደርገዋል።
    </div>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=350)

# (OCR and other tools stay here...)
elif "OCR" in str(main_portal) or "Research" in str(main_portal):
    st.title("🧠 Neural Manuscript Analysis")
    file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)
        if st.button("Start Deep Scan"):
            with st.spinner("Analyzing..."):
                res = model.generate_content(["ይህንን ምስል ተንትነህ ተርጉመው፡", img])
                st.write(res.text)

# ---------------------------------------------------------
# 5. THE ULTIMATE CHAT WITH GOOGLE SEARCH
# ---------------------------------------------------------
st.markdown("---")
st.subheader("💬 የ AI ሊቁን ውይይት (ከጎግል ፍለጋ ጋር)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("ወቅታዊ ወይም የታሪክ ጥያቄ እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ ጎግልን እያመሳከረ ነው..."):
            try:
                # በዲያቆን ከውን ደጀን ማንነት እንዲመልስ መመሪያ
                full_instruct = f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የግዕዝ ሊቅ ነህ። አስፈላጊ ከሆነ መረጃውን ከጎግል (Google Search) ፈልገህ አቅርብ። ጥያቄው፡ {prompt}"
                response = model.generate_content(full_instruct)
                
                # መልሱን ማሳየት
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
                # ጎግል ላይ የተጠቀመባቸውን ሊንኮች (Sources) ካሉ ማሳየት ይቻላል
            except Exception as e:
                if "429" in str(e):
                    st.warning("⚠️ ሲስተሙ ለጊዜው ተጨናንቋል። እባክህ 20 ሰከንድ ታግሰህ ድገመኝ።")
                else:
                    st.error(f"ያልታወቀ ስህተት ተፈጠረ፡ {e}")

# ---------------------------------------------------------
# 6. SOVEREIGN MASTER FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center; color: #b8860b;'>
        <h4>GE'EZ SCHOLAR AI v150.0 | GOOGLE SEARCH ENABLED</h4>
        <p style='font-size: 18px;'><b>PROUDLY DEVELOPED BY THE VISIONARY DEACON KEWN DEJEN</b></p>
    </div>
""", unsafe_allow_html=True)
