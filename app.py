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

# Professional World-Class Sovereign Theme (High Readability)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&family=Abyssinica+SIL&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at top, #001f3f 0%, #000814 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 0px 4px 10px rgba(255, 215, 0, 0.4);
    }

    [data-testid="stSidebar"] {
        background-color: #000b1a !important;
        border-right: 2px solid #D4AF37;
    }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.5);
        border-left: 15px solid #D4AF37;
        margin-bottom: 25px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }

    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #fff !important;
        height: 3.8em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 40px rgba(255, 215, 0, 0.5); }

    [data-testid="stChatInput"] { 
        border: 3px solid #D4AF37 !important; 
        background-color: #ffffff !important;
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.1rem !important; }
    
    .citation { font-size: 0.9rem; color: #FFD700; border-top: 1px solid rgba(255,255,255,0.2); margin-top: 25px; padding-top: 15px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE INDESTRUCTIBLE ENGINE (Advanced Retry Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

# የሚሞከሩ ሞዴሎች ዝርዝር
MODELS_TO_TRY = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]

def ask_geez_scholar(prompt, tool_context):
    sys_instr = f"You are 'Ge'ez Scholar AI Master', created by Grand Architect Deacon Kewn Dejen. Expert in {tool_context}. Provide scholarly, deep analysis."
    
    for model_name in MODELS_TO_TRY:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instr)
            
            # ራስ-ሰር የፈውስ ዑደት (Retry Loop for 429)
            attempts = 0
            while attempts < 3: # ሦስት ጊዜ በራሱ ይሞክራል
                try:
                    response = model.generate_content(prompt)
                    if response and response.text:
                        return response.text, model_name
                except Exception as e:
                    if "429" in str(e):
                        attempts += 1
                        time.sleep(5) # 5 ሰከንድ ታግሶ ይሞክራል
                        continue
                    break # ሌሎች ስህተቶች ካሉ ወደ ቀጣዩ ሞዴል ይዞራል
        except:
            continue
            
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም። ጎግል መንገዱን በኃይል ዘግቶታል። እባክዎ ከ1 ደቂቃ በኋላ ገጹን Refresh ያድርጉ።", "None"

# ---------------------------------------------------------
# 3. UI: THE ARK OF KNOWLEDGE
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='font-size: 1.6rem;'>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    st.markdown("---")
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
        with st.spinner("ሊቁ መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, pillar)
            
            full_res = f"""
            <div style='color: white; line-height: 1.8; font-size: 1.1rem;'>{answer}</div>
            <div class='citation'>Source: {engine} | Ge'ez Scholar AI v9000.0 Sovereign</div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO v9000.0 | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
