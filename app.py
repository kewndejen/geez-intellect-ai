import streamlit as st
import google.generativeai as genai
import time
import datetime
import random

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (v10,000)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Majestic Imperial Theme (Deep Navy, Gold & High Contrast White)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #001f3f 0%, #000814 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 0px 0px 15px rgba(255, 215, 0, 0.6);
    }

    [data-testid="stSidebar"] {
        background-color: #000b1a !important;
        border-right: 3px solid #D4AF37;
    }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(20px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.5);
        border-left: 15px solid #D4AF37;
        margin-bottom: 25px;
        box-shadow: 0 10px 50px rgba(0,0,0,0.8);
    }

    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #fff !important;
        height: 4em; width: 100%; transition: 0.5s;
        text-transform: uppercase; letter-spacing: 3px;
    }
    .stButton>button:hover { transform: scale(1.03); box-shadow: 0 0 50px rgba(255, 215, 0, 0.7); }

    [data-testid="stChatInput"] { 
        border: 3px solid #D4AF37 !important; 
        background-color: #ffffff !important;
        border-radius: 20px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.2rem !important; }
    
    .status-online { color: #00FF00; font-weight: bold; font-size: 0.8rem; text-align: center; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. INDESTRUCTIBLE AI ENGINE (Advanced Resilience Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

def ask_sovereign_scholar(prompt, tool_context):
    """
    ይህ ኢንጅን ጎግል 'ቆይ' ቢለው እንኳ በራሱ ሰከንዶችን እየቆጠረ ደጋግሞ በመሞከር መልሱን የግድ ያመጣል።
    """
    models = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]
    sys_instr = f"You are 'Ge'ez Scholar AI v10,000', created by Grand Architect Deacon Kewn Dejen. Expert in {tool_context}."
    
    for model_name in models:
        model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instr)
        
        # የዳግም ሙከራ ዑደት (Wait-and-Retry Algorithm)
        wait_time = 5 # የመጀመሪያው መጠበቂያ ሰከንድ
        for attempt in range(4): # እስከ 4 ጊዜ ይሞክራል
            try:
                response = model.generate_content(prompt)
                if response and response.text:
                    return response.text, model_name
            except Exception as e:
                error_msg = str(e)
                if "429" in error_msg:
                    # መንገዱ ከተዘጋ ለተወሰነ ሰከንድ ይቆያል
                    time.sleep(wait_time + random.uniform(0, 1))
                    wait_time *= 2 # መጠበቂያውን ጊዜ እጥፍ ያደርገዋል (Exponential)
                    continue
                break # ሌሎች ስህተቶች ካሉ ወደ ቀጣዩ ሞዴል ይለፋል
                
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም (ከፍተኛ መጨናነቅ)። እባክዎ 1 ደቂቃ በትዕግሥት ቆይተው ገጹን Refresh ያድርጉ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR & BRANDING
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background:linear-gradient(90deg, #FFD700, #B8860B); padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:900;'>
            GRAND ARCHITECT:<br>DEACON KEWN DEJEN
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    st.markdown("---")
    if st.button("🔄 REBOOT SYSTEM"):
        st.cache_resource.clear()
        st.rerun()
    st.markdown("<div class='status-online'>● SYSTEM STATUS: ROYAL ONLINE</div>", unsafe_allow_html=True)

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
    with st.chat_message("user"):
        st.markdown(f"<div style='color: white;'>{prompt}</div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን በጥልቀት እያመሳከረ ነው (ይህ ጥቂት ሰከንዶች ሊወስድ ይችላል)..."):
            answer, engine = ask_sovereign_scholar(prompt, pillar)
            
            full_res = f"""
            <div style='color: white; line-height: 1.8; font-size: 1.15rem;'>{answer}</div>
            <div style='font-size: 0.8rem; color: #FFD700; border-top: 1px solid #444; margin-top: 20px; padding-top: 10px;'>
                Intelligence Source: {engine} | Sovereign Zenith v10,000
            </div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO v10,000 | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
