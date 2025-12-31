import streamlit as st
import google.generativeai as genai
import time
import random

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (Emerald & Gold Resurrection)
# ---------------------------------------------------------
st.set_page_config(page_title="Ge'ez Scholar AI | Deacon Kewn Dejen", page_icon="🔱", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    .stApp { background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; text-shadow: 2px 2px 10px #000; }
    [data-testid="stSidebar"] { background-color: #001a0d !important; border-right: 4px solid #FFD700; }
    .sovereign-card { background: rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 15px; border: 1px solid #FFD700; margin-bottom: 20px; }
    .stButton>button { background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important; color: #000; font-weight: 900; border-radius: 10px; height: 3.5em; width: 100%; text-transform: uppercase; border: 2px solid #fff; }
    [data-testid="stChatInput"] { border: 3px solid #FFD700 !important; background-color: #ffffff !important; border-radius: 15px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; }
    .wait-msg { color: #FFD700; font-style: italic; font-size: 0.9rem; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE RESILIENT ENGINE (Gemini 2.0 Flash Powered)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key missing!")
    st.stop()

def ask_geez_scholar(prompt, tool_context):
    # አዲሱና ሰፊው Gemini 2.0 Flash ሞዴል
    model_name = 'gemini-2.0-flash-exp' 
    sys_instr = f"You are 'Ge'ez Scholar AI Master', created by Grand Architect Deacon Kewn Dejen. Expert in {tool_context}. Provide deep scholarly analysis."
    
    status_placeholder = st.empty()
    
    # ተስፋ የማይቆርጥ የሙከራ ዑደት (Smart Retry)
    for attempt in range(1, 6):
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instr)
            response = model.generate_content(prompt)
            if response and response.text:
                status_placeholder.empty()
                return response.text, model_name
        except Exception as e:
            if "429" in str(e):
                wait = (attempt * 3) + random.random()
                status_placeholder.markdown(f"<div class='wait-msg'>⏳ ሊቁ በጥልቅ ማሰላሰል ላይ ናቸው... (ሙከራ {attempt}/5)</div>", unsafe_allow_html=True)
                time.sleep(wait)
                continue
            # ሞዴሉ ካልተገኘ ወደ 1.5 Flash ይዞራል
            model_name = 'gemini-1.5-flash'
            continue
            
    status_placeholder.empty()
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም። እባክዎ ከ1 ደቂቃ በኋላ ገጹን Refresh ያድርጉ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE 60 PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:10px; border-radius:10px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    pillar = st.selectbox("Select Wisdom Pillar", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    st.markdown("---")
    if st.button("🔄 Reboot Studio"):
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
    with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, pillar)
            full_res = f"<div>{answer}</div><div style='font-size:0.8rem; color:#FFD700; margin-top:20px; border-top:1px solid #ffffff;'>Source: {engine} | Master Sovereign v2.0</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
