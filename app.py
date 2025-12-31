import streamlit as st
import google.generativeai as genai
import time
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Sovereign Theme (Navy & Gold - High Visibility)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    .stApp { background: radial-gradient(circle at center, #001a33 0%, #00050a 100%); color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; }
    [data-testid="stSidebar"] { background-color: #000814 !important; border-right: 3px solid #D4AF37; }
    .sovereign-card { background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 15px; border-left: 8px solid #D4AF37; margin-bottom: 20px; }
    .stButton>button { background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important; color: #000; font-weight: 900; border-radius: 10px; height: 3.5em; width: 100%; text-transform: uppercase; }
    [data-testid="stChatInput"] { border: 2px solid #D4AF37 !important; background-color: #ffffff !important; border-radius: 15px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. STABLE API CORE (Lightweight Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም!")
    st.stop()

def ask_geez_scholar(prompt, tool_context):
    # ሰፊ ኮታ ያለውን gemini-1.5-flash ብቻ እንጠቀማለን (ለመረጋጋት)
    try:
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=f"You are 'Ge'ez Scholar AI', created by Grand Architect Deacon Kewn Dejen. Expert in {tool_context}. Provide scholarly analysis."
        )
        response = model.generate_content(prompt)
        return response.text, "gemini-1.5-flash"
    except Exception as e:
        if "429" in str(e):
            return "⚠️ ጎግል መንገዱን ለጥቂት ደቂቃዎች ዘግቶታል። እባክዎ ለ10 ደቂቃ ፋታ ሰጥተው ገጹን Refresh ያድርጉ።", "None"
        return f"❌ ስህተት፦ {str(e)}", "None"

# ---------------------------------------------------------
# 3. SIDEBAR & TOOLS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:10px; border-radius:10px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    if st.button("🔄 REBOOT SYSTEM"):
        st.cache_resource.clear()
        st.rerun()

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input("ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, pillar)
            full_res = f"<div>{answer}</div><div style='font-size:0.8rem; color:#FFD700; margin-top:10px;'>Source: {engine} | Sovereign Eternal</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
