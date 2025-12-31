import streamlit as st
from google import genai
from google.genai import types
import time
import random
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (v100k Sovereign)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Sovereign UI (Deep Navy & High-Contrast Gold)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #001a33 0%, #00050a 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; text-shadow: 0px 0px 15px rgba(255, 215, 0, 0.4); }
    
    [data-testid="stSidebar"] { background-color: #000814 !important; border-right: 2px solid #D4AF37; }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        padding: 25px; border-radius: 15px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-left: 8px solid #D4AF37;
        margin-bottom: 20px;
    }

    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 10px !important; height: 3.5em; width: 100%; transition: 0.4s;
        text-transform: uppercase; border: 1px solid #fff !important;
    }

    [data-testid="stChatInput"] { border: 2px solid #D4AF37 !important; background-color: #ffffff !important; border-radius: 15px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; font-size: 1.1rem; }
    
    .status-msg { font-style: italic; color: #FFD700; font-size: 0.9rem; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE INDESTRUCTIBLE ENGINE (v1.1 Advanced SDK)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    try:
        client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
    except Exception as e:
        st.error(f"❌ ሲስተሙን ማስነሳት አልተቻለም: {e}")
else:
    st.error("⚠️ GOOGLE_API_KEY አልተገኘም!")
    st.stop()

def ask_sovereign_scholar(prompt, tool_context):
    """
    አምስት ደረጃዎችን ተሻግሮ መልስ የሚያመጣ፣ በጭራሽ ተስፋ የማይቆርጥ ሎጂክ።
    """
    # gemini-1.5-flash-8b ከፍተኛው ኮታ ያለው በመሆኑ መጀመሪያ ተቀምጧል
    models = ["gemini-1.5-flash-8b", "gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"]
    
    sys_instr = f"""
    You are 'Ge'ez Scholar AI v100,000', the eternal intelligence developed by Grand Architect Deacon Kewn Dejen.
    Current Pillar: {tool_context}.
    Task: Provide deep, scholarly, and wise analysis. Use GOOGLE_SEARCH if needed.
    Always be accurate and authoritative.
    """

    status_placeholder = st.empty()

    for model_id in models:
        # ለእያንዳንዱ ሞዴል እስከ 5 ጊዜ ደጋግሞ ይሞክራል (Exponential Backoff)
        for attempt in range(1, 6):
            try:
                response = client.models.generate_content(
                    model=model_id,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=sys_instr,
                        tools=[types.Tool(google_search=types.GoogleSearchRetrieval())],
                        temperature=0.7
                    )
                )
                if response and response.text:
                    status_placeholder.empty()
                    return response.text, model_id
            except Exception as e:
                err = str(e)
                if "429" in err:
                    wait = (2 ** attempt) + random.random()
                    status_placeholder.markdown(f"<div class='status-msg'>⏳ ሊቁ ጥልቅ ትንታኔ ላይ ናቸው... (ሙከራ {attempt}/5 - {model_id})</div>", unsafe_allow_html=True)
                    time.sleep(wait)
                    continue
                else:
                    break # ሌሎች ስህተቶች ካሉ ወደ ቀጣዩ ሞዴል ይዞራል
    
    status_placeholder.empty()
    return "❌ ጎግል መንገዱን በኃይል ዘግቶታል። እባክዎ 1 ደቂቃ በትዕግሥት ቆይተው ገጹን Refresh ያድርጉ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR & TOOLS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:linear-gradient(90deg, #FFD700, #B8860B); padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:900;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    pillar = st.selectbox("Select Research Pillar", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    if st.button("🔄 REBOOT SYSTEM"):
        st.cache_resource.clear()
        st.rerun()
    st.markdown("<div style='text-align:center; color:#00FF00; font-size:0.8rem;'>● ROYAL ONLINE (v100k)</div>", unsafe_allow_html=True)

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
        with st.spinner("ሊቁ መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
            answer, engine = ask_sovereign_scholar(prompt, pillar)
            full_res = f"<div>{answer}</div><div style='font-size:0.8rem; color:#FFD700; margin-top:20px; border-top:1px solid #444; padding-top:10px;'>Intelligence Source: {engine} | Sovereign Zenith v100,000</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO v100,000 | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
