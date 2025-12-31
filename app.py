import streamlit as st
from google import genai
from google.genai import types
import time
import random
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (The Ultimate Zenith)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Majestic Sovereign UI (Navy Blue, Gold & High-Contrast White)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #001f3f 0%, #000814 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.5); }
    
    [data-testid="stSidebar"] { background-color: #000b1a !important; border-right: 3px solid #D4AF37; }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.5);
        border-left: 12px solid #D4AF37;
        margin-bottom: 25px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.8);
    }

    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; height: 4em; width: 100%; transition: 0.5s;
        text-transform: uppercase; letter-spacing: 3px; border: 2px solid #fff !important;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 50px rgba(255, 215, 0, 0.7); }

    [data-testid="stChatInput"] { border: 3px solid #D4AF37 !important; background-color: #ffffff !important; border-radius: 20px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.2rem !important; }
    
    .thinking-box { background: rgba(212, 175, 55, 0.1); border-left: 5px solid #FFD700; padding: 15px; font-style: italic; color: #FFD700; margin-bottom: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE UNIVERSAL SOVEREIGN ENGINE (New-Gen API v1.1)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    try:
        # በአዲሱ ቴክኖሎጂ ደንበኛውን ማዘጋጀት
        client = genai.Client(api_key=api_key)
    except Exception as e:
        st.error(f"❌ ሲስተሙን ማስነሳት አልተቻለም: {e}")
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

def ask_sovereign_scholar(prompt, tool_context):
    """
    ይህ ኢንጅን 5 ደረጃዎችን አልፎ መልሱን በኃይል ያመጣል።
    ከፍተኛው የቴክኖሎጂ ጥግ: Google Search ተጨምሮበታል።
    """
    # የሚሞከሩ ሞዴሎች በቅደም ተከተል (Flash-8b እጅግ ሰፊ ኮታ ያለው ነው)
    models = ["gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-flash-8b", "gemini-1.5-pro"]
    
    sys_instr = f"""
    You are 'Ge'ez Scholar AI v50,000', the ultimate intelligence developed by Grand Architect Deacon Kewn Dejen.
    Expertise: {tool_context}.
    Your knowledge spans 3,000 years of Ethiopian wisdom.
    Task: Provide scholarly, historical, and deep analysis.
    If information is not in your training, use the GOOGLE_SEARCH tool.
    Tone: Sovereign, ancient, authoritative, and wise.
    """

    for model_id in models:
        # ለተጠቃሚው እንዳይታይ በራሱ እስከ 3 ጊዜ ይሞክራል (Exponential Backoff)
        wait_time = 3
        for attempt in range(3):
            try:
                # ጎግል ሰርችን በማካተት ምላሽ ማመንጨት
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
                    return response.text, model_id
            except Exception as e:
                if "429" in str(e):
                    time.sleep(wait_time + random.uniform(0, 1))
                    wait_time *= 2 # መጠበቂያውን ጊዜ እጥፍ ያደርገዋል
                    continue
                break
    
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም። ይህ የሚሆነው ጎግል ለነፃ ተጠቃሚዎች የሰጠው መንገድ ለጊዜው ስለተዘጋ ነው። እባክዎ ከ1 ደቂቃ በኋላ ገጹን Refresh ያድርጉ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR & BRANDING
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background:linear-gradient(90deg, #FFD700, #B8860B); padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:900; border: 2px solid #fff;'>
            GRAND ARCHITECT:<br>DEACON KEWN DEJEN
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    pillar = st.selectbox("የጥበብ ምሰሶ (Wisdom Pillar)", [
        "Advanced AI Labs", "Digital Archives", "Heritage & Science", "Imperial University", "Mysticism & Qene"
    ])
    st.markdown("---")
    if st.button("🔄 REBOOT SOVEREIGN SYSTEM"):
        st.cache_resource.clear()
        st.rerun()
    st.markdown("<div style='text-align:center; color:#00FF00; font-size:0.8rem;'>● SYSTEM STATUS: ROYAL ONLINE (v50k)</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE (The Public Gateway)
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
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown("<div class='thinking-box'>ሊቁ የዓለም መዛግብትንና የጎግል ሰርችን እያመሳከረ ነው...</div>", unsafe_allow_html=True)
        
        answer, engine = ask_sovereign_scholar(prompt, pillar)
        thinking_placeholder.empty()
        
        full_res = f"""
        <div style='color: white; line-height: 1.8; font-size: 1.15rem;'>{answer}</div>
        <div style='font-size: 0.8rem; color: #FFD700; border-top: 1px solid rgba(255,255,255,0.2); margin-top: 20px; padding-top: 10px;'>
            Intelligence Source: {engine} (Search-Enabled) | Universal Zenith v50,000
        </div>
        """
        st.markdown(full_res, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO v50,000 | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
