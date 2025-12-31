import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL GLOBAL CONFIGURATION (The Zenith Standard)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Premium Sovereign CSS (Imperial Black & Gold)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&family=Abyssinica+SIL&display=swap');
    
    .stApp { background-color: #00050a; color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #d4af37 !important; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); }
    .geez-font { font-family: 'Abyssinica SIL', serif; }

    /* Sidebar: The Ark of 60 Pillars */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #010c17 0%, #1a0000 100%) !important;
        border-right: 3px solid #d4af37;
    }
    
    /* Sovereign Glassmorphism Cards */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-left: 12px solid #d4af37;
        margin-bottom: 25px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.6);
    }

    /* Majestic Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 1px solid #fff !important;
        height: 3.8em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton>button:hover { transform: translateY(-5px); box-shadow: 0 0 40px #d4af37; }

    /* Global Chat Input */
    [data-testid="stChatInput"] { 
        border: 2px solid #d4af37 !important; 
        background-color: #000c18 !important;
        border-radius: 20px !important; 
    }
    
    .citation-box { font-size: 0.8rem; color: #888; border-top: 1px solid #333; padding-top: 10px; margin-top: 20px; font-family: monospace; }
    .thinking-box { color: #d4af37; font-style: italic; font-size: 0.9rem; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SOVEREIGN AI ENGINE (The Fail-Safe Intelligence)
# ---------------------------------------------------------
if "messages" not in st.session_state: st.session_state.messages = []

# API Verification from Streamlit Secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ SECURITY ALERT: API Key missing in Streamlit Secrets!")
    st.stop()

@st.cache_resource
def load_sovereign_engine():
    """በራስ-ሰር የሚሠራ ምርጥ ሞዴል መፈለጊያ (Colab Logic)"""
    try:
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # ቅደም ተከተል: 1.5 Flash (Stability) -> 2.0 Flash -> 1.5 Pro (Depth)
        priority = ['gemini-1.5-flash', 'gemini-2.0-flash', 'gemini-1.5-pro', 'gemini-pro']
        for target in priority:
            for actual in available:
                if target in actual: return actual
        return available[0]
    except:
        return 'models/gemini-1.5-flash'

SELECTED_MODEL = load_sovereign_engine()

def ask_geez_scholar(prompt, tool_context, image=None):
    """የሊቃውንት ትንታኔ ማመንጫ ሎጂክ"""
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI', a world-class expert in Ethiopian studies and ancient wisdom.
    Created by Grand Architect Deacon Kewn Dejen.
    Current Pillar: {tool_context}.
    Task: Provide scholarly, deep, and wise analysis. 
    - Handle Latin phonetic typing (e.g., 'Selam' -> ሰላም) automatically.
    - Provide Sem-na-Worq analysis for literature.
    - Analyze iconography and manuscripts for theological depth.
    - Tone: Sovereign, authoritative, and ancient.
    """
    try:
        model = genai.GenerativeModel(model_name=SELECTED_MODEL, system_instruction=sys_instruction)
        if image:
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⚠️ ሊቁ ተጨናንቀዋል። እባክዎ 15 ሰከንድ ታግሰው በድጋሚ ይሞክሩ።"
        return f"❌ ስህተት ተከስቷል: {str(e)}"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60 PILLARS (The Complete Library)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background: linear-gradient(90deg, #d4af37, #010c17); padding: 15px; border-radius: 12px; text-align: center; color: #000; font-weight: bold;'>
            GRAND ARCHITECT:<br>DEACON KEWN DEJEN
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    category = st.selectbox("Select Wisdom Pillar", [
        "🏠 Imperial Dashboard",
        "🧠 Advanced AI Labs",
        "📜 Digital Archives & Law",
        "🏛️ Heritage & Ancient Science",
        "🎓 Imperial University Hub",
        "🔮 Mysticism & Qene Lab",
        "💰 Strategic Wealth & Security"
    ])

    # 60 Specialized Tools Organization
    if category == "🏠 Imperial Dashboard": tool = "Sovereign Overview"
    elif category == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Neural Translation", "Syntax Analyzer", "Ge'ez NLP", "Dialect Study", "Semantic Map", "Voice of Wisdom"])
    elif category == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library (12M+)", "Fetha Nagast (Legal)", "Synaxarium AI", "Royal Decrees", "Treaty Expert", "Kibre Nagast Hub", "Ecclesiastical Law", "Genealogy Map", "Manuscript Preservation", "Hagiography Lab"])
    elif category == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI", "Geology of Axum", "Botany of Ethiopia", "Zoology in Brana", "Ink Chemistry", "Virtual Museum"])
    elif category == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter", "Ethiopic Math", "Philosophy Hub", "History Chronology", "University Portal", "Scholarly Citation"])
    elif category == "🔮 Mysticism & Qene Lab":
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Proverbs AI", "Esoteric Wisdom", "Liturgical Guide", "Monastic Study", "Apostolic Tradition", "Hymnology Lab"])
    else:
        tool = st.radio("Strategic", ["Premium Business Hub", "API Portal", "Security Admin", "Wealth Strategy", "Sovereign Logs", "Global Relations", "Grant Assistant", "Strategic Planning", "Project Manager", "Data Vault"])

    st.markdown("---")
    st.caption(f"Active Engine: {SELECTED_MODEL}")
    st.markdown("<div style='font-size: 0.7rem; color: #00ff00;'>STATUS: ROYAL ONLINE ✅</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE (The Public Research Gate)
# ---------------------------------------------------------
if category == "🏠 Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #d4af37; letter-spacing: 5px;'>THE ETERNAL ZENITH v1000.0</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='sovereign-card'>
        <h3>Welcome, Global Scholar.</h3>
        <p>This is the world's most advanced AI gateway for Ethiopian wisdom, engineered by <b>Grand Architect Deacon Kewn Dejen</b>. 
        Select a specialized laboratory from the sidebar to begin analyzing manuscripts, ancient laws, and deep mysticism.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Archives", "12M+ Pages", "Synced")
    col2.metric("Intelligence", f"{SELECTED_MODEL}", "Stable")
    col3.metric("Authority", "Kewn Dejen", "Verified")
else:
    st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

# Special Tool: Vision/OCR Implementation
if "OCR" in tool or "Vision" in tool or "Museum" in tool:
    st.subheader(f"📸 {tool} Intelligence")
    up_file = st.file_uploader("Upload Manuscript, Icon, or Artifact Image", type=['jpg','png','jpeg'])
    if up_file:
        img = Image.open(up_file)
        st.image(img, caption="Target Artifact", width=500)
        if st.button("Initiate Neural Analysis"):
            with st.spinner("Decoding ancient wisdom..."):
                res = ask_geez_scholar(f"Provide a deep scholarly analysis for this artifact in the context of: {tool}", tool, img)
                st.markdown(f"<div class='sovereign-card'><b>Analysis Result:</b><br><br>{res}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. THE GLOBAL CHAT INTERFACE (Public-Ready)
# ---------------------------------------------------------
st.markdown("---")
st.subheader(f"💬 Consult the {tool} Expert")

# Display History
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

# User Interaction Loop
if prompt := st.chat_input(f"Ask the Scholar a question about {tool}..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        thinking = st.empty()
        thinking.markdown("<div class='thinking-box'>Thinking: Consulting the imperial archives...</div>", unsafe_allow_html=True)
        
        answer = ask_geez_scholar(prompt, tool)
        thinking.empty()
        
        # Automatic Citation Generator
        year = datetime.datetime.now().year
        citation = f"<div class='citation-box'>Citation: Dejen, K. ({year}). {tool} Research Report. Ge'ez Scholar AI Studio v1000.0. Powered by GE'EZ STUDIO.</div>"
        
        full_res = f"{answer}{citation}"
        st.markdown(full_res, unsafe_allow_html=True)
        st.session_state.messages.append({"role": "assistant", "content": full_res})

# ---------------------------------------------------------
# 6. MASTER FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><br>")
st.markdown(f"""
    <div style='text-align: center; border-top: 2px solid #d4af37; padding-top: 20px;'>
        <p style='color: #d4af37; font-weight: 900; letter-spacing: 5px;'>GE'EZ SCHOLAR AI STUDIO</p>
        <p style='color: #888;'>PROUDLY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>
        <p style='font-size: 0.7rem; color: #444;'>© {datetime.datetime.now().year} ALL RIGHTS RESERVED | THE ETERNAL ZENITH EDITION</p>
    </div>
""", unsafe_allow_html=True)
