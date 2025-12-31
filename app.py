import streamlit as st
import google.generativeai as genai
import time
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Premium Readable Theme (Deep Navy, Gold & Silver White)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
    /* Background & Global Text */
    .stApp { 
        background: linear-gradient(135deg, #001f3f 0%, #000814 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    /* Golden Headers */
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 5px #000;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #000b1a !important;
        border-right: 3px solid #D4AF37;
    }

    /* High Visibility Cards */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.5);
        border-left: 10px solid #D4AF37;
        margin-bottom: 25px;
        color: #ffffff !important;
    }

    /* Sovereign Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #fff !important;
        height: 3.8em; width: 100%; transition: 0.4s ease;
        text-transform: uppercase;
    }

    /* Chat Input Fix */
    [data-testid="stChatInput"] { 
        border: 3px solid #D4AF37 !important; 
        background-color: #ffffff !important;
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #555; margin-top: 20px; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE INFINITE ENGINE (Multi-Model Resilient Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም!")
    st.stop()

# የሚሰሩ ሞዴሎች ዝርዝር (በቅደም ተከተል)
MODELS_TO_TRY = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]

def ask_geez_scholar(prompt, tool_context):
    sys_instr = f"You are 'Ge'ez Scholar AI', created by Deacon Kewn Dejen. Expert in {tool_context}. Provide deep scholarly analysis."
    
    # ሁሉንም ሞዴሎች በየተራ ይሞክራል
    for model_name in MODELS_TO_TRY:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instr)
            
            # መቆራረጥ ካለ እስከ 3 ጊዜ በራሱ ይሞክራል (Auto-Retry)
            for attempt in range(3):
                try:
                    response = model.generate_content(prompt)
                    if response and response.text:
                        return response.text, model_name
                except Exception as e:
                    if "429" in str(e): # ኮታው ካለቀ 3 ሰከንድ ጠብቆ ይሞክራል
                        time.sleep(3)
                        continue
                    break # ሌሎች ስህተቶች ካሉ ወደ ቀጣዩ ሞዴል ይዞራል
        except:
            continue
            
    return "❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም። እባክዎ ከ30 ሰከንድ በኋላ ገጹን Refresh አድርገው ይሞክሩ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:10px; border-radius:10px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    if st.button("🔄 Reboot System"):
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

if prompt := st.chat_input("ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<div style='color: white;'>{prompt}</div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, pillar)
            
            full_res = f"""
            <div style='color: white; line-height: 1.8;'>{answer}</div>
            <div class='citation'>Source: {engine} | v8000.0 Sovereign Infinite</div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO v8000.0 | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
