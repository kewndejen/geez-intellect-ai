import streamlit as st
import google.generativeai as genai
import time
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION (v11,000 Peace Edition)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide"
)

# Professional Navy & Gold Theme (High Readability)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    .stApp { background: radial-gradient(circle at center, #001f3f 0%, #000814 100%); color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; }
    [data-testid="stSidebar"] { background-color: #000b1a !important; border-right: 3px solid #D4AF37; }
    .stButton>button { background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important; color: #000; font-weight: 900; border-radius: 10px; height: 3.5em; width: 100%; transition: 0.5s ease; text-transform: uppercase; border: 2px solid #fff; }
    [data-testid="stChatInput"] { border: 3px solid #D4AF37 !important; background-color: #ffffff !important; border-radius: 10px; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE RESILIENT ENGINE (Anti-Quota Exhaustion Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

def ask_geez_scholar(prompt, tool_context):
    # ሰፊ ኮታ ያለውን gemini-1.5-flash ብቻ እንጠቀማለን (429ን ለመከላከል)
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=f"You are 'Ge'ez Scholar AI', created by Deacon Kewn Dejen for the people. Expert in {tool_context}."
    )
    
    # የዳግም ሙከራ ዑደት (Silent Retry Logic)
    for attempt in range(4): # እስከ 4 ጊዜ በራሱ ይታገላል
        try:
            response = model.generate_content(prompt)
            if response and response.text:
                return response.text
        except Exception as e:
            if "429" in str(e):
                # 429 ሲመጣ ለተጠቃሚው ከማሳየት ይልቅ ራሱ ለ10 ሰከንድ ይታገሳል
                time.sleep(10)
                continue
            return f"❌ የቴክኒክ ስህተት፦ {str(e)}"
    
    return "❌ ሊቁ በአሁኑ ሰዓት በጣም ተጨናንቀዋል። እባክዎ ለ5 ደቂቃ ፋታ ሰጥተው ገጹን Refresh ያድርጉ።"

# ---------------------------------------------------------
# 3. SIDEBAR & TOOLS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:10px; border-radius:10px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    tool = st.selectbox("የጥበብ ምሰሶ", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
    if st.button("🔄 Reboot System"):
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
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
            answer = ask_geez_scholar(prompt, tool)
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
