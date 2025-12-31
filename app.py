import streamlit as st
import google.generativeai as genai
import time
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (v6000.0)
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
    .stApp { background: linear-gradient(135deg, #001f3f 0%, #000c18 100%); color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; text-shadow: 2px 2px 5px #000; }
    [data-testid="stSidebar"] { background-color: #000814 !important; border-right: 3px solid #D4AF37; }
    .sovereign-card { background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); padding: 30px; border-radius: 20px; border: 1px solid #D4AF37; margin-bottom: 25px; }
    .stButton>button { background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important; color: #000; font-weight: 900; border-radius: 12px; height: 3.8em; width: 100%; transition: 0.5s; text-transform: uppercase; border: 2px solid #fff; }
    [data-testid="stChatInput"] { border: 3px solid #D4AF37 !important; background-color: #ffffff !important; border-radius: 15px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE ORACLE ENGINE (Smart Multi-Model Discovery)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ የ API ቁልፍ (Key) አልተገኘም!")
    st.stop()

@st.cache_resource
def get_available_engine():
    """የእርስዎ ቁልፍ የሚፈቅደውን ማንኛውንም የሚሰራ ሞዴል ይፈልጋል"""
    try:
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # 2.0-exp ኮታ ስለሌለው ከዝርዝሩ እናስወግደዋለን
        safe_priority = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]
        for target in safe_priority:
            for actual in available_models:
                if target in actual and "experimental" not in actual:
                    return actual
        return available_models[0]
    except:
        return "models/gemini-1.5-flash"

ACTIVE_MODEL = get_available_engine()

def ask_oracle(prompt, context):
    sys_instr = f"You are 'Ge'ez Scholar AI', created by Deacon Kewn Dejen. Expert in {context}."
    try:
        model = genai.GenerativeModel(model_name=ACTIVE_MODEL, system_instruction=sys_instr)
        # አጭር መቆራረጥ ካለ ራስ-ሰር ዳግም መሞከሪያ
        for i in range(2):
            try:
                response = model.generate_content(prompt)
                return response.text, ACTIVE_MODEL
            except Exception as e:
                if "429" in str(e):
                    time.sleep(3)
                    continue
                raise e
    except Exception as e:
        return f"❌ የጎግል ሲስተም ምላሽ አልሰጠም። ምክንያት፦ {str(e)}", "None"

# ---------------------------------------------------------
# 3. UI & SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:10px; border-radius:10px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    tool = st.selectbox("Select Tool", ["General Scholar", "Qene Lab", "Manuscript OCR", "Bahre Hasab"])
    st.info(f"Engine: {ACTIVE_MODEL}")
    if st.button("🔄 Reboot Engine"):
        st.cache_resource.clear()
        st.rerun()

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን እያመሳከረ ነው..."):
            answer, engine = ask_oracle(prompt, tool)
            st.markdown(answer)
            st.caption(f"Source: {engine} | v6000.0")
            st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO v6000.0 | Deacon Kewn Dejen</p>", unsafe_allow_html=True)
