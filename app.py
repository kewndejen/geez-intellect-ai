import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# 1. IMPERIAL PRESTIGE CONFIGURATION
st.set_page_config(
    page_title="Ge'ez Scholar AI | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Sovereign CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background-color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    .stSidebar { background: linear-gradient(180deg, #000c18 0%, #300000 100%) !important; border-right: 5px solid #b8860b; }
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%);
        color: white; border: none; padding: 18px 30px;
        border-radius: 12px; font-weight: 800; width: 100%; transition: 0.5s;
    }
    .sovereign-card { background: white; padding: 40px; border-radius: 20px; border-left: 15px solid #b8860b; box-shadow: 0 20px 80px rgba(0,0,0,0.1); margin-bottom: 35px; }
    .dev-signature { background: linear-gradient(90deg, #b8860b, #000c18); padding: 20px; border-radius: 15px; border: 2px solid #d4af37; text-align: center; color: white; font-weight: bold; margin-bottom: 30px; }
    [data-testid="stChatInput"] { position: fixed; bottom: 30px; z-index: 1000; background: white !important; border: 2px solid #b8860b !important; border-radius: 15px !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. AI CORE WITH MULTI-ENGINE FALLBACK
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Security Alert: Key Missing.")
    st.stop()

def get_response_sovereign(prompt_content):
    """አንዱ ሞዴል ካልሰራ ወደ ሌላው የሚዘል ብልህ ተግባር"""
    # የሚሞከሩ ሞዴሎች ቅደም ተከተል (Hierarchy)
    model_names = ['gemini-2.0-flash', 'gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    
    for model_name in model_names:
        try:
            model_instance = genai.GenerativeModel(
                model_name=model_name,
                tools=[{"google_search": {}}] # ጎግል ሰርች እንዲሰራ
            )
            response = model_instance.generate_content(prompt_content)
            return response.text, model_name
        except Exception as e:
            # 429 ካጋጠመው ወደ ሚቀጥለው ሞዴል ይዘልላል
            if "429" in str(e) or "ResourceExhausted" in str(e):
                continue
            else:
                # ሌላ ስህተት ከሆነም ወደ ሚቀጥለው ይለፋል
                continue
    
    # ሁሉም ሞዴሎች እምቢ ካሉ (የመጨረሻው ሙከራ)
    return "⚠️ ክቡር ጌታዬ፤ ሁሉም የጎግል ሞዴሎች ለጊዜው ተጨናንቀዋል። እባክህ 30 ሰከንድ በትክክል ታግሰህ ድገመኝ።", "None"

# 3. SIDEBAR (60+ TOOLS)
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='dev-signature'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    portal = st.selectbox("የእውቀት ምድብ", ["🏠 Dashboard", "🧠 AI Labs", "📜 Archives", "🎓 University", "🔮 Mysticism", "💰 Wealth"])
    st.markdown("---")
    # Sub-tool selection logic
    if portal == "🏠 Dashboard": tool = "Overview"
    elif portal == "🧠 AI Labs": tool = st.radio("Tools", ["OCR", "Linguistics", "Voice"])
    else: tool = "General"

# 4. CONTENT AREA
if tool == "Overview":
    st.title("Imperial Sovereign Dashboard")
    st.markdown(f"<div class='sovereign-card'><h3>እንኳን በደህና መጡ ዲያቆን ከውን ደጀን።</h3>ሲስተሙ አሁን <b>Multi-Engine Logic</b> በመጠቀም ያለ መቆራረጥ እንዲሰራ ተደርጓል።</div>", unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=300)

# 5. THE UNBREAKABLE CHAT (ALWAYS VISIBLE)
st.markdown("---")
if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("የሊቅ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("ሊቁ በ 4 የተለያዩ ሞዴሎች እየፈለገ ነው..."):
            # ሎጂኩን እዚህ ጋር እንጠራዋለን
            answer, engine = get_response_sovereign(f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የግዕዝ ሊቅ ነህ። በጥልቅ መልስ፡ {prompt}")
            st.markdown(answer)
            st.caption(f"Engine used: {engine}")
            st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown("<br><br><br><p style='text-align: center; color: #b8860b;'><b>PROUDLY DEVELOPED BY DEACON KEWN DEJEN</b></p>", unsafe_allow_html=True)
