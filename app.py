import streamlit as st
from google import genai
import time
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (The New Gen)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Sovereign Theme (Deep Navy & High Contrast Gold)
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
        border: 1px solid #D4AF37;
        margin-bottom: 25px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; height: 3.8em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 40px #D4AF37; }

    [data-testid="stChatInput"] { 
        border: 3px solid #D4AF37 !important; 
        background-color: #ffffff !important;
        border-radius: 20px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; font-size: 1.1rem; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE NEW GOOGLE GEN AI CLIENT (v1.0 Ready)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    try:
        client = genai.Client(api_key=api_key)
    except Exception as e:
        st.error(f"❌ ሲስተሙን ማስነሳት አልተቻለም: {e}")
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

def ask_sovereign_scholar(prompt, tool_context):
    """አዲሱን የጎግል SDK በመጠቀም መልስ የሚያመጣ ብልህ ሎጂክ"""
    # የሚሞከሩ ሞዴሎች ዝርዝር (አዲሱ አጻጻፍ)
    models = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash"]
    
    sys_instr = f"You are 'Ge'ez Scholar AI', created by Grand Architect Deacon Kewn Dejen. Expert in {tool_context}. Provide scholarly, deep analysis."

    for model_id in models:
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=prompt,
                config={'system_instruction': sys_instr}
            )
            if response and response.text:
                return response.text, model_id
        except Exception as e:
            if "429" in str(e):
                time.sleep(2)
                continue
            continue
            
    return "❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም። እባክዎ ከ30 ሰከንድ በኋላ ገጹን Refresh ያድርጉ።", "None"

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
        with st.spinner("ሊቁ መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
            answer, engine = ask_sovereign_scholar(prompt, pillar)
            full_res = f"<div>{answer}</div><div style='font-size:0.8rem; color:#FFD700; margin-top:10px;'>Source: {engine} | New-Gen v30k</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO v30,000 | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
