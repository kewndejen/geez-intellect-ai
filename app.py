import streamlit as st
import google.generativeai as genai
import time
import random

# ---------------------------------------------------------
# 1. IMPERIAL GLOBAL CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional World-Class Sovereign UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #001f3f 0%, #000814 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; }
    
    [data-testid="stSidebar"] { background-color: #000b1a !important; border-right: 3px solid #D4AF37; }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid #D4AF37;
        box-shadow: 0 10px 50px rgba(0,0,0,0.8);
        color: #ffffff !important;
    }

    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; height: 4em; width: 100%; transition: 0.5s;
        text-transform: uppercase; letter-spacing: 2px;
    }

    [data-testid="stChatInput"] { border: 3px solid #D4AF37 !important; background-color: #ffffff !important; border-radius: 20px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.1rem !important; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. INDESTRUCTIBLE ENGINE (The Fortress Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key Not Found! Please check Streamlit Secrets.")
    st.stop()

def ask_sovereign_scholar(prompt, tool_context):
    # ሰፊ ኮታ ያላቸው ሞዴሎች ዝርዝር
    models_to_try = ["gemini-1.5-flash", "gemini-1.5-flash-8b", "gemini-1.5-pro", "gemini-pro"]
    
    sys_instr = f"You are 'Ge'ez Scholar AI', created by Grand Architect Deacon Kewn Dejen. Expert in {tool_context}. Provide scholarly, deep analysis."

    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instr)
            # የዳግም ሙከራ ዑደት
            for attempt in range(2):
                try:
                    response = model.generate_content(prompt)
                    if response and response.text:
                        return response.text, model_name
                except Exception as e:
                    if "429" in str(e):
                        time.sleep(random.randint(2, 5))
                        continue
                    break
        except:
            continue
            
    return "❌ ጎግል መንገዱን በኃይል ዘግቶታል። ይህ የሚሆነው የ API ቁልፍዎ ስለታገደ ሊሆን ይችላል። እባክዎ አዲስ ቁልፍ ይፍጠሩ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR & TOOLS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:15px; border-radius:10px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    st.markdown("---")
    if st.button("🔄 REBOOT APP"):
        st.cache_resource.clear()
        st.rerun()

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን እያመሳከረ ነው..."):
            answer, engine = ask_sovereign_scholar(prompt, pillar)
            full_res = f"<div>{answer}</div><div style='font-size:0.8rem; color:#FFD700; margin-top:10px;'>Source: {engine} | Fortress v20k</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO v20,000 | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
