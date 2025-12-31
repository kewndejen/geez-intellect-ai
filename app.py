import streamlit as st
import google.generativeai as genai
from PIL import Image
import time

# 1. IMPERIAL PAGE CONFIG
st.set_page_config(page_title="Ge'ez Scholar AI | Deacon Kewn Dejen", page_icon="🔱", layout="wide")

# 2. SOVEREIGN BLACK & GOLD CSS
st.markdown("""
    <style>
    .stApp { background-color: #00050a; color: #ffffff; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'Cinzel Decorative', serif; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #010c17 0%, #1a0000 100%) !important; border-right: 2px solid #d4af37; }
    .stButton>button { background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important; color: #000 !important; font-weight: bold; width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. ROBUST AI ENGINE (Quota-Aware)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Streamlit Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

def ask_scholar_ai(prompt, tool_name):
    instruction = f"You are 'Ge'ez Scholar AI', an expert in {tool_name}, created by Deacon Kewn Dejen. Provide a deep response."
    
    # የሞዴሎች ቅደም ተከተል (Flash መጀመሪያ - ምክንያቱም ኮታው ሰፊ ነው)
    models_to_try = ["gemini-1.5-flash", "gemini-2.0-flash-exp", "gemini-1.5-pro", "gemini-pro"]
    
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=instruction)
            response = model.generate_content(prompt)
            return response.text, model_name
        except Exception as e:
            if "429" in str(e): # ኮታው ካለቀ ወደ ቀጣዩ ሞዴል ይለፋል
                continue
            else:
                return f"❌ ስህተት ተከስቷል: {str(e)}", "None"
    
    return "ሊቁ በአሁኑ ሰዓት እጅግ ተጨናንቀዋል። እባክዎ ከ30 ሰከንድ በኋላ በድጋሚ ይሞክሩ።", "None"

# 4. SIDEBAR - THE 60 PILLARS OF WISDOM
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center; color:#d4af37;'>GRAND ARCHITECT: DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("የጥበብ ምሰሶ ይምረጡ", [
        "🧠 Advanced AI Labs", "📜 Digital Archives & Law", "🏛️ Heritage & Ancient Science",
        "🎓 Imperial University Hub", "🔮 Mysticism & Qene Lab", "💰 Strategic Wealth & Security"
    ])

    if pillar == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom"])
    elif pillar == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees"])
    elif pillar == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"])
    elif pillar == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"])
    elif pillar == "🔮 Mysticism & Qene Lab":
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema", "Theology Hub", "Scholar Roleplay"])
    else:
        tool = st.radio("Strategic", ["Business Hub", "API Portal", "Security Admin", "Wealth Strategy"])

# 5. MAIN WORKSPACE
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን እያመሳከረ ነው..."):
            res, engine = ask_scholar_ai(prompt, tool)
            st.markdown(res)
            st.caption(f"Intelligence Source: {engine}")
            st.session_state.messages.append({"role": "assistant", "content": res})

st.markdown("<br><hr><p style='text-align:center; color:#d4af37;'>GE'EZ SCHOLAR AI STUDIO v110.0 | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
