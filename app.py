import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime

# 1. IMPERIAL PAGE SETUP
st.set_page_config(page_title="Ge'ez Scholar AI | Deacon Kewn Dejen", page_icon="🔱", layout="wide")

# 2. SOVEREIGN BLACK & GOLD CSS
st.markdown("""
    <style>
    .stApp { background-color: #00050a; color: #ffffff; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'Cinzel Decorative', serif; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #010c17 0%, #1a0000 100%) !important; border-right: 2px solid #d4af37; }
    .stButton>button { background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important; color: #000 !important; font-weight: bold; width: 100%; border-radius: 10px; }
    .stChatInput input { background-color: #001220 !important; color: white !important; border: 1px solid #d4af37 !important; }
    .sovereign-card { background: rgba(255, 255, 255, 0.03); padding: 20px; border-radius: 15px; border-left: 8px solid #d4af37; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 3. SMART API & MODEL DISCOVERY
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    # የሚሰሩ ሞዴሎችን በራስ-ሰር መፈለግ
    @st.cache_resource
    def find_best_model():
        try:
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            # ቅደም ተከተል፡ 1.5 Flash -> 1.5 Pro -> 1.0 Pro -> Gemini Pro
            for target in ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-1.0-pro", "gemini-pro"]:
                for available in available_models:
                    if target in available:
                        return available
            return available_models[0] if available_models else "models/gemini-pro"
        except:
            return "models/gemini-pro"

    SELECTED_MODEL = find_best_model()
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Streamlit Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

# 4. RESPONSE ENGINE
def ask_scholar_ai(prompt, tool_name):
    instruction = f"You are 'Ge'ez Scholar AI', an expert in {tool_name}, created by Deacon Kewn Dejen. Provide a deep, scholarly response."
    try:
        model = genai.GenerativeModel(model_name=SELECTED_MODEL, system_instruction=instruction)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # 404 ስህተት ከመጣ ወደ መሠረታዊው ሞዴል መመለስ
        try:
            fallback_model = genai.GenerativeModel(model_name="gemini-pro")
            response = fallback_model.generate_content(f"Expert on {tool_name}: {prompt}")
            return response.text
        except:
            return f"❌ ስህተት ተከስቷል: {str(e)}"

# 5. SIDEBAR - THE 60 PILLARS OF WISDOM
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center; color:#d4af37;'>GRAND ARCHITECT: DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("የጥበብ ምሰሶ ይምረጡ", [
        "🧠 Advanced AI Labs",
        "📜 Digital Archives & Law",
        "🏛️ Heritage & Ancient Science",
        "🎓 Imperial University Hub",
        "🔮 Mysticism & Qene Lab",
        "💰 Strategic Wealth & Security"
    ])

    # 60 መሣሪያዎች በዝርዝር
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

    st.markdown("---")
    st.caption(f"Active Engine: {SELECTED_MODEL}")

# 6. MAIN WORKSPACE
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን እያመሳከረ ነው..."):
            res = ask_scholar_ai(prompt, tool)
            st.markdown(res)
            st.session_state.messages.append({"role": "assistant", "content": res})

# 7. FOOTER
st.markdown("<br><hr><p style='text-align:center; color:#d4af37;'>GE'EZ SCHOLAR AI STUDIO v90.0 | DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>", unsafe_allow_html=True)
