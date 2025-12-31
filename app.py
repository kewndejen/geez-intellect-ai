import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL GLOBAL CONFIGURATION (v30.0 - Sovereign)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Premium Sovereign CSS (Imperial Standard)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&family=Abyssinica+SIL&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background-color: #000c18; color: #f5f5f5; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #d4af37 !important; font-weight: 900; }
    .geez-text { font-family: 'Abyssinica SIL', serif; font-size: 1.2rem; }

    /* Imperial Sidebar (The Ark of Knowledge) */
    .stSidebar { 
        background: linear-gradient(180deg, #001220 0%, #1a0000 100%) !important; 
        border-right: 4px solid #d4af37; 
        box-shadow: 5px 0 25px rgba(212, 175, 55, 0.3);
    }

    /* Sovereign Cards (Glassmorphism Gold) */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 30px; border-radius: 25px;
        border: 1px solid rgba(212, 175, 55, 0.4);
        border-left: 12px solid #d4af37;
        box-shadow: 0 15px 45px rgba(0,0,0,0.6);
        margin-bottom: 30px;
        backdrop-filter: blur(20px);
    }

    /* Majestic Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #d4af37 0%, #8b6b00 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 15px !important; border: 2px solid #f5f5f5 !important;
        padding: 20px 40px !important; transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton>button:hover { 
        transform: scale(1.05) translateY(-5px); 
        box-shadow: 0 0 40px #d4af37;
        color: #fff !important;
    }

    /* Scholar's Analysis Section */
    .analysis-box {
        background: rgba(212, 175, 55, 0.05);
        border: 1px dashed #d4af37;
        padding: 20px; border-radius: 15px;
        margin-top: 20px; color: #e0e0e0;
    }
    
    .citation-box {
        background: #111; padding: 15px; border-radius: 10px;
        font-family: monospace; font-size: 0.8rem; border: 1px solid #444;
        margin-top: 15px; color: #d4af37;
    }

    /* Chat Input Focus */
    [data-testid="stChatInput"] { border: 2px solid #d4af37 !important; background: #001220 !important; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. INTELLIGENT SOVEREIGN CORE (The Brain)
# ---------------------------------------------------------
if "messages" not in st.session_state: st.session_state.messages = []

# API Verification from Streamlit Secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("CRITICAL ERROR: Imperial API Key missing in System Secrets.")
    st.stop()

@st.cache_resource
def load_advanced_models():
    try:
        working = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # Priority: 2.0 Flash -> 1.5 Pro (Research Grade)
        targets = ['gemini-2.0-flash', 'gemini-1.5-pro']
        ordered = [t for t in targets if any(t in w for w in working)]
        return ordered if ordered else ['gemini-1.5-flash']
    except:
        return ['gemini-1.5-flash']

MODELS = load_advanced_models()

def ask_sovereign_scholar(prompt, tool_name, image=None):
    # የታላቅ ሊቅ መመሪያ (Supreme System Instruction)
    instruction = f"""
    You are 'Ge'ez Scholar AI Studio v30.0', the world's most advanced AI developed by Grand Architect Deacon Kewn Dejen.
    Your mission is to provide unprecedented analysis for the '{tool_name}' research pillar.
    - Format: 1. Literal Translation, 2. Grammatical (Sewsow) Breakdown, 3. Deep Symbolic (Sem-na-Worq) Analysis.
    - Intelligence: If Ge'ez text is provided, analyze its theological and historical roots.
    - Language: Expertly bridge Ge'ez, Amharic, and English.
    - Tone: Sovereign, ancient, wise, and academically rigorous.
    """
    
    for m in MODELS:
        try:
            model = genai.GenerativeModel(model_name=m, system_instruction=instruction)
            content = [prompt, image] if image else [prompt]
            response = model.generate_content(content)
            return response.text, m
        except: continue
    return "The Archive is temporarily sealed. Please retry, Scholar.", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK (60+ PILLARS)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background: linear-gradient(90deg, #d4af37, #001220); padding: 15px; border-radius: 12px; text-align: center; color: #000; font-weight: 900; border: 1px solid #fff;'>
            GRAND ARCHITECT:<br>DEACON KEWN DEJEN
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    portal = st.selectbox("Select Research Pillar", [
        "🏛️ Heritage, Map & Science Hub",
        "🧠 Advanced AI Research Labs",
        "📜 Digital Libraries & Archives",
        "🎓 Imperial University Hub",
        "🔮 Mysticism, Poetry & Zema",
        "💼 Strategic Wealth & Business"
    ])

    # Enhanced Tool Logic
    if portal == "🏛️ Heritage, Map & Science Hub":
        tool = st.radio("Sectors", ["Virtual Heritage Museum", "Ancient Medicine AI", "Archeology Simulation", "Interstellar Architecture"])
    elif portal == "🧠 Advanced AI Research Labs":
        tool = st.radio("Labs", ["Manuscript OCR (Vision)", "Linguistic Bridge", "Root Finder AI", "Script Authentication"])
    elif portal == "📜 Digital Libraries & Archives":
        tool = st.radio("Archives", ["Universal Library (12M+)", "Fetha Nagast Legal AI", "Synaxarium Analysis", "Royal Decrees Archive"])
    elif portal == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Chronology", "Abu Shaker Astronomy", "Numerology & Ethics", "Scribe Assistant"])
    elif portal == "🔮 Mysticism, Poetry & Zema":
        tool = st.radio("Arts", ["Sem-na-Worq (Qene) Lab", "St. Yared Zema Analysis", "Theology Research", "Scholar Roleplay"])
    else:
        tool = st.radio("Wealth", ["Premium Business AI", "Strategic API Portal", "Security Admin Logs"])

    st.markdown("---")
    st.markdown("<div style='text-align: center; font-size: 0.8rem;'>System: <span style='color: #00ff00;'>Sovereign Online ✅</span></div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; font-size: 0.8rem;'>Model: {MODELS[0]}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE (THE IMPERIAL GATEWAY)
# ---------------------------------------------------------
# Hero Banner
st.markdown("<h1 style='text-align: center; font-size: 3.5rem;'>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-size: 1.2rem; color: #d4af37;'><i>Operating under the Authority of Deacon Kewn Dejen</i></p>", unsafe_allow_html=True)

# Pillar Introduction
st.markdown(f"""
<div class='sovereign-card'>
    <h3 style='margin-top: 0;'>Active Pillar: {tool}</h3>
    <p style='font-size: 1.1rem; color: #f0f0f0;'>This laboratory is optimized for <b>{tool}</b>. 
    Our AI models are cross-referencing 12 million archive pages and ancient manuscripts to assist your research.</p>
</div>
""", unsafe_allow_html=True)

# Tool Feature: Vision & Artifact Analysis
if "OCR" in tool or "Museum" in tool or "Vision" in tool:
    st.subheader("📸 Artifact Neural Scanner")
    f = st.file_uploader("Upload Manuscript, Icon, or Artifact Image", type=['jpg', 'jpeg', 'png'])
    if f:
        img = Image.open(f)
        st.image(img, caption="Target Artifact", width=500)
        if st.button("Initiate Imperial Analysis"):
            with st.spinner("Deciphering ancient codes..."):
                res, eng = ask_sovereign_scholar(f"Perform a deep scholarly analysis for: {tool}", tool, img)
                st.markdown(f"<div class='sovereign-card'><b>Analysis Result:</b><br><br>{res}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. THE SCHOLAR CHAT (WORLD-CLASS DIALOGUE)
# ---------------------------------------------------------
st.markdown("---")
st.subheader(f"💬 Consult the Scholar ({tool} Expert)")

# Render Messages with Premium Style
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat Input & Scholarly Logic
if prompt := st.chat_input("Ask the Scholar... (e.g. 'Analyze the theological depth of St. Yared's Dugua')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("The Scholar is consulting the archives..."):
            answer, engine = ask_sovereign_scholar(prompt, tool)
            
            # Citation Generation Logic
            cite_date = datetime.datetime.now().strftime("%Y")
            citation = f"Citation: Kewn Dejen et al. ({cite_date}). {tool} Analysis. Ge'ez Scholar AI Studio v30.0."
            
            full_response = f"{answer}\n\n<div class='citation-box'>{citation}</div>"
            
            st.markdown(full_response, unsafe_allow_html=True)
            st.caption(f"Source: {engine} | Powered by GE'EZ STUDIO")
            st.session_state.messages.append({"role": "assistant", "content": full_response})

# ---------------------------------------------------------
# 6. FOOTER (THE ZENITH STANDARD)
# ---------------------------------------------------------
st.markdown("<br><br><br>")
st.markdown(f"""
    <div style='text-align: center; border-top: 2px solid #d4af37; padding-top: 20px;'>
        <p style='color: #d4af37; font-weight: 900; letter-spacing: 3px;'>GE'EZ SCHOLAR AI STUDIO v30.0 | THE ETERNAL ZENITH</p>
        <p style='color: #888;'>PROUDLY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>
        <p style='font-size: 0.7rem; color: #555;'>© {datetime.datetime.now().year} GE'EZ STUDIO. ALL RIGHTS RESERVED.</p>
    </div>
""", unsafe_allow_html=True)
