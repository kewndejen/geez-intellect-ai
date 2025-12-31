import streamlit as st
import google.generativeai as genai
from PIL import Image
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

# Professional High-Contrast Imperial Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
    .stApp { background-color: #001f3f; color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; text-shadow: 2px 2px 4px #000; }
    [data-testid="stSidebar"] { background-color: #001226 !important; border-right: 3px solid #D4AF37; }
    p, span, label, div { color: #ffffff !important; font-size: 1.1rem; line-height: 1.7; }
    
    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 25px; border-radius: 15px;
        border: 1px solid #D4AF37;
        margin-bottom: 20px;
    }

    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 10px !important; border: 2px solid #fff !important;
        height: 3.5em; width: 100%; transition: 0.3s ease;
    }

    [data-testid="stChatInput"] { border: 2px solid #D4AF37 !important; background-color: #ffffff !important; border-radius: 15px !important; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.1rem !important; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #ffffff; margin-top: 15px; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. STABLE ENGINE SELECTION (The 429 Killer Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key missing! Please add GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

@st.cache_resource
def get_safe_model():
    try:
        # የሚሰሩ ሞዴሎችን ዝርዝር ማምጣት
        all_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # ቃል ኪዳን፡- ስህተት የሚፈጥረውን gemini-2.5-pro በጭራሽ እንዳይጠቀም መከልከል
        # እጅግ አስተማማኝ የሆኑትን በቅደም ተከተል ማስቀመጥ
        safe_priority = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]
        
        for target in safe_priority:
            for actual in all_models:
                if target in actual and "2.5" not in actual: # 2.5-proን በኃይል ያግዳል
                    return actual
        return "models/gemini-1.5-flash"
    except:
        return "models/gemini-1.5-flash"

SELECTED_MODEL = get_safe_model()

def ask_geez_scholar(prompt, tool_context, image=None):
    # 429 ስህተት እንዳይመጣ ጥልቅ መመሪያ
    sys_instruction = f"You are 'Ge'ez Scholar AI', an expert in {tool_context}, created by Deacon Kewn Dejen. Respond with deep scholarly wisdom. Support Ge'ez/Amharic."
    try:
        model = genai.GenerativeModel(model_name=SELECTED_MODEL, system_instruction=sys_instruction)
        if image:
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # 429 ስህተት ከመጣ ወደ ቀጣዩ አስተማማኝ ሞዴል ይዞራል
        try:
            fallback = genai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_instruction)
            res = fallback.generate_content(prompt)
            return res.text
        except:
            return f"❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም (ኮታ አልቋል)። እባክዎ ከ30 ሰከንድ በኋላ ይሞክሩ።"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60 PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:10px; border-radius:8px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("የጥበብ ምሰሶ", [
        "🧠 Advanced AI Labs", "📜 Digital Archives & Law", "🏛️ Heritage & Science Hub",
        "🎓 Imperial University Hub", "🔮 Mysticism & Qene Lab", "💰 Strategic Wealth & Security"
    ])

    if pillar == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom", "Ge'ez NLP"])
    elif pillar == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast (Legal AI)", "Synaxarium Analysis", "Royal Decrees"])
    elif pillar == "🏛️ Heritage & Science Hub":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"])
    elif pillar == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"])
    elif pillar == "🔮 Mysticism & Qene Lab":
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema", "Theology Hub", "Scholar Roleplay"])
    else:
        tool = st.radio("Strategic", ["Business Hub", "API Portal", "Security Admin", "Wealth Strategy"])

    st.markdown("---")
    st.caption(f"Active Engine: {SELECTED_MODEL}")
    st.markdown("<div style='color:#00ff00; font-size:0.8rem; text-align:center;'>STATUS: ROYAL ONLINE ✅</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        answer = ask_geez_scholar(prompt, tool)
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO v4000.0 | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
