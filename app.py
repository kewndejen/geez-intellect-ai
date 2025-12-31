import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime

# 1. ገጹን ማስተካከያ (Imperial Setup)
st.set_page_config(page_title="Ge'ez Scholar AI | Deacon Kewn Dejen", page_icon="🔱", layout="wide")

# 2. የጥቁርና ወርቃማ ዲዛይን (Imperial CSS)
st.markdown("""
    <style>
    .stApp { background-color: #00050a; color: #ffffff; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'Cinzel Decorative', serif; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #010c17 0%, #1a0000 100%) !important; border-right: 2px solid #d4af37; }
    .stButton>button { background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important; color: #000 !important; font-weight: bold; width: 100%; border-radius: 10px; }
    .stChatInput input { background-color: #001220 !important; color: white !important; border: 1px solid #d4af37 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. የ AI ግንኙነት (API Connection)
if "GOOGLE_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    except Exception as e:
        st.error(f"API Configuration Error: {e}")
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Streamlit Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")

# 4. መልስ ማምጫ ተግባር (Response Function)
def get_ai_response(user_text, tool_name):
    instruction = f"You are an expert in {tool_name}, created by Deacon Kewn Dejen. Provide a deep, scholarly answer in the language the user speaks (Amharic/Ge'ez/English)."
    try:
        # gemini-1.5-flash እጅግ ፈጣንና አስተማማኝ ነው
        model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=instruction)
        response = model.generate_content(user_text)
        return response.text
    except Exception as e:
        return f"❌ ስህተት ተከስቷል: {str(e)}"

# 5. የጎንዮሽ ምሰሶዎች (60 Tools Organized in 6 Pillars)
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center; color:#d4af37;'>GRAND ARCHITECT: DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("የጥበብ ዘርፍ ይምረጡ", [
        "🧠 Advanced AI Labs",
        "📜 Digital Archives & Law",
        "🏛️ Heritage & Ancient Science",
        "🎓 Imperial University Hub",
        "🔮 Mysticism & Qene Lab",
        "💰 Strategic Wealth & Security"
    ])

    if pillar == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom", "Neural Translation", "Syntax Analyzer", "Ge'ez NLP", "Dialect Study", "Semantic Map"])
    elif pillar == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees", "Treaty Expert", "Kibre Nagast Hub", "Ecclesiastical Law", "Genealogy Map", "Manuscript Preservation", "Hagiography Lab"])
    elif pillar == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI", "Geology of Axum", "Botany of Ethiopia", "Zoology in Brana", "Ink Chemistry", "Virtual Museum"])
    elif pillar == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter", "Ethiopic Math", "Philosophy Hub", "History Chronology", "University Portal", "Scholarly Citation"])
    elif pillar == "🔮 Mysticism & Qene Lab":
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema", "Theology Hub", "Scholar Roleplay", "Proverbs AI", "Esoteric Wisdom", "Liturgical Guide", "Monastic Study", "Apostolic Tradition", "Hymnology Lab"])
    else:
        tool = st.radio("Strategic", ["Business Hub", "API Portal", "Security Admin", "Wealth Strategy", "Sovereign Logs", "Global Relations", "Grant Assistant", "Strategic Planning", "Project Manager", "Data Vault"])

# 6. ዋናው የሥራ ገጽ (Main Layout)
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# መልእክቶችን ማሳያ
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ጥያቄ መቀበያ
if prompt := st.chat_input(f"{tool}ን ይጠይቁ..."):
    # የተጠቃሚውን ጥያቄ መመዝገብ
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # የ AI መልስ ማምጣት
    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን እያመሳከረ ነው..."):
            answer = get_ai_response(prompt, tool)
            st.markdown(answer)
            st.session_state.chat_history.append({"role": "assistant", "content": answer})

# 7. መዝጊያ (Footer)
st.markdown("<br><hr><p style='text-align:center; color:#d4af37;'>GE'EZ SCHOLAR AI STUDIO v80.0 | DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>", unsafe_allow_html=True)
