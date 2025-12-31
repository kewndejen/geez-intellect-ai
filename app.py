import streamlit as st
import google.generativeai as genai
import time
import datetime
import random

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (v15,000)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Majestic Sovereign Theme (Navy, Gold & High Readability White)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #001f3f 0%, #000814 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.5);
    }

    [data-testid="stSidebar"] {
        background-color: #000b1a !important;
        border-right: 3px solid #D4AF37;
    }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
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
        height: 4em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase; letter-spacing: 3px;
    }
    .stButton>button:hover { transform: scale(1.03); box-shadow: 0 0 50px rgba(255, 215, 0, 0.6); }

    [data-testid="stChatInput"] { 
        border: 3px solid #D4AF37 !important; 
        background-color: #ffffff !important;
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.2rem !important; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid rgba(255,255,255,0.2); margin-top: 25px; padding-top: 15px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. INDESTRUCTIBLE ENGINE (5-Tier Failover Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key missing! Please add GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

def ask_sovereign_scholar(prompt, tool_context):
    """
    ይህ ኢንጅን 5 የተለያዩ ሞዴሎችን በየተራ ይሞክራል። አንዱ ከተዘጋ ወዲያውኑ ወደ ሌላኛው ይዞራል።
    """
    # ሞዴሎች በቅደም ተከተል (Flash-8b እጅግ ሰፊ ኮታ ያለው ነው)
    models_to_rotate = [
        "gemini-1.5-flash-8b", 
        "gemini-1.5-flash", 
        "gemini-1.5-pro", 
        "gemini-pro"
    ]
    
    sys_instr = f"You are 'Ge'ez Scholar AI v15,000', created by Grand Architect Deacon Kewn Dejen. Expert in {tool_context}. Provide scholarly, historical, and deep analysis."

    for model_name in models_to_rotate:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instr)
            
            # ለእያንዳንዱ ሞዴል 3 ጊዜ የመሞከር ዕድል ይሰጣል
            for attempt in range(3):
                try:
                    response = model.generate_content(prompt)
                    if response and response.text:
                        return response.text, model_name
                except Exception as e:
                    if "429" in str(e):
                        time.sleep(random.randint(3, 7)) # ከ3-7 ሰከንድ ታግሶ ይሞክራል
                        continue
                    break # ሌሎች ስህተቶች ካሉ ወደ ቀጣዩ ሞዴል ይለፋል
        except:
            continue
            
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም (ከፍተኛ መጨናነቅ)። እባክዎ ከ1 ደቂቃ በኋላ ገጹን Refresh ያድርጉ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR & NAVIGATION
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
    st.markdown("<div style='text-align:center; color:#00FF00; font-size:0.8rem;'>● ROYAL ONLINE</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input("ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<div style='color: white;'>{prompt}</div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን እያመሳከረ ነው..."):
            answer, engine = ask_sovereign_scholar(prompt, pillar)
            
            full_res = f"""
            <div style='color: white; line-height: 1.8; font-size: 1.15rem;'>{answer}</div>
            <div class='citation'>Intelligence Source: {engine} | Sovereign Zenith v15,000</div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO v15,000 | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
