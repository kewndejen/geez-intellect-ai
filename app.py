import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL GLOBAL CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Sovereign CSS (The Zenith Standard for Public Access)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background-color: #000a12; color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #d4af37 !important; }

    /* Sidebar - The Ark */
    .stSidebar { 
        background: linear-gradient(180deg, #011627 0%, #1a0000 100%) !important; 
        border-right: 2px solid #d4af37; 
    }

    /* Sovereign Cards */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-left: 10px solid #d4af37;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        margin-bottom: 25px;
        backdrop-filter: blur(15px);
    }

    /* Buttons - Majestic */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important;
        color: #000 !important; font-weight: 800 !important;
        border-radius: 12px !important; border: none !important;
        height: 3.5em; transition: 0.5s;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 0 30px #d4af37; }

    /* Chat Input */
    [data-testid="stChatInput"] { border: 2px solid #d4af37 !important; border-radius: 20px !important; }
    
    .dev-signature {
        background: linear-gradient(90deg, #d4af37, #001627);
        padding: 15px; border-radius: 10px; text-align: center;
        color: #000; font-weight: bold; margin-bottom: 20px;
    }
    
    .hero-text { font-size: 1.2rem; line-height: 1.8; color: #e0e0e0; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE INTELLECT ENGINE (Scholarly Core)
# ---------------------------------------------------------
if "messages" not in st.session_state: st.session_state.messages = []

# API Verification from Streamlit Secrets
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("System Configuration Error: API Key missing in Secrets.")
    st.stop()

@st.cache_resource
def get_available_models():
    try:
        working = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        targets = ['gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-2.0-flash']
        ordered = [t for t in targets if any(t in w for w in working)]
        return ordered if ordered else ['models/gemini-pro']
    except:
        return ['models/gemini-1.5-flash']

MODELS = get_available_models()

def scholarly_ai_response(prompt, tool_name, creativity=0.7):
    # ዓለም አቀፍ ተመራማሪዎችን ታሳቢ ያደረገ መመሪያ
    sys_prompt = f"""
    You are 'Ge'ez Scholar AI', the world's leading artificial intelligence for Ethiopic studies.
    Created by Grand Architect Deacon Kewn Dejen (GE'EZ STUDIO).
    Context: You are operating the '{tool_name}' module for a global audience of researchers and scholars.
    - Provide deep, academic, and well-structured insights.
    - Support Ge'ez, Amharic, and English fluently.
    - If phonetic Ge'ez (Latin letters) is used, automatically interpret it as Ge'ez/Amharic.
    - Explain complex concepts like 'Sem-na-Worq' (Wax and Gold) for international users.
    - Maintain a tone of wisdom, authority, and extreme respect.
    """
    
    for m in MODELS:
        try:
            model = genai.GenerativeModel(model_name=m, system_instruction=sys_prompt)
            # Google Search Retrieval ማካተት (ከተቻለ)
            response = model.generate_content(prompt, generation_config={"temperature": creativity})
            return response.text, m
        except: continue
    return "The Scholar is currently in deep meditation. Please retry in a moment.", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF KNOWLEDGE
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<div class='dev-signature'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    portal = st.selectbox("Explore Research Pillars", [
        "🏛️ Heritage & Science Hub",
        "🧠 AI Research Labs",
        "📜 Digital Archives",
        "🎓 Imperial University",
        "🔮 Mysticism & Poetry",
        "💼 Strategic Gateway"
    ])

    # Dynamic Tool Selection
    if portal == "🏛️ Heritage & Science Hub":
        tool = st.radio("Sectors", ["Global Heritage Map", "Ancient Medicine", "Architecture AI", "Virtual Museum"])
    elif portal == "🧠 AI Research Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder"])
    elif portal == "📜 Digital Archives":
        tool = st.radio("Archives", ["Universal Library", "Legal AI (Fetha Nagast)", "Synaxarium AI", "Royal Decrees"])
    elif portal == "🎓 Imperial University":
        tool = st.radio("Academic", ["Bahre Hasab Logic", "Astronomy Lab", "Numerology", "Scribe Assistant"])
    elif portal == "🔮 Mysticism & Poetry":
        tool = st.radio("Arts", ["Sem-na-Work (Qene)", "Zema Lab", "Theology Hub", "Scholar Roleplay"])
    else:
        tool = st.radio("Gateway", ["API Portal", "Strategic Business Hub", "Developer Logs"])

    st.markdown("---")
    creativity = st.slider("AI Insight Depth", 0.0, 1.0, 0.7)
    st.info(f"Active Pillar: {portal}")

# ---------------------------------------------------------
# 4. MAIN INTERFACE (PUBLIC ACCESS)
# ---------------------------------------------------------
# Hero Section
st.markdown("<h1 style='text-align: center;'>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='hero-text'>Welcome to the World's First AI Gateway to Ancient Wisdom.<br>Operating under the vision of <b>Deacon Kewn Dejen</b>.</p>", unsafe_allow_html=True)

# Pillar Description
st.markdown(f"""
<div class='sovereign-card'>
    <h3>Current Pillar: {tool}</h3>
    <p>Explore the depths of Ethiopian wisdom through our advanced AI models. 
    Select a tool from the sidebar to begin your research journey.</p>
</div>
""", unsafe_allow_html=True)

# Special Tool: Manuscript OCR (Sample Functionality)
if "OCR" in tool:
    st.subheader("📸 Manuscript Neural Scanner")
    uploaded_file = st.file_uploader("Upload an image of a manuscript or text", type=['jpg', 'png', 'jpeg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, width=500, caption="Uploaded Artifact")
        if st.button("Initiate Scholarly Scan"):
            with st.spinner("The AI is analyzing the ancient script..."):
                res, eng = scholarly_ai_response("Analyze and translate this manuscript image in detail.", tool, creativity)
                st.markdown(f"<div class='sovereign-card'>{res}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. THE GLOBAL CHAT INTERFACE
# ---------------------------------------------------------
st.markdown("---")
st.subheader(f"💬 Consult the Scholar ({tool} Expert)")

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input Logic
if prompt := st.chat_input("Ask the Scholar... (e.g., 'Explain the grammar of this Qene...')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("The Scholar is consulting the archives..."):
            response, engine = scholarly_ai_response(prompt, tool, creativity)
            st.markdown(response)
            st.caption(f"Intelligence Source: {engine} | Ge'ez Studio v21.0")
            st.session_state.messages.append({"role": "assistant", "content": response})

# ---------------------------------------------------------
# 6. FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><p style='text-align: center; color: #d4af37;'><b>GE'EZ SCHOLAR AI STUDIO | THE ETERNAL ZENITH</b><br>PROUDLY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>", unsafe_allow_html=True)
