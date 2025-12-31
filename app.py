import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time
import base64

# ---------------------------------------------------------
# 1. IMPERIAL GLOBAL CONFIGURATION (v40.0 - The Eternal Zenith)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Premium CSS with Gold Foil & Glassmorphism Effects
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&family=Abyssinica+SIL&display=swap');
    
    /* Core Body Styling */
    .stApp {
        background: radial-gradient(circle at top right, #001f3f, #000000);
        color: #e0e0e0;
        font-family: 'Montserrat', sans-serif;
    }

    /* Imperial Header Styling */
    h1, h2, h3 {
        font-family: 'Cinzel Decorative', serif;
        background: linear-gradient(to right, #d4af37, #f7e7ce, #b8860b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        text-align: center;
    }

    /* Glassmorphism Sovereign Cards */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-radius: 25px;
        padding: 35px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.7);
        margin-bottom: 30px;
        transition: 0.5s ease;
    }
    .sovereign-card:hover {
        border-color: #d4af37;
        transform: translateY(-5px);
    }

    /* Sidebar Styling (The Golden Ark) */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #000814 0%, #1a0900 100%) !important;
        border-right: 3px solid #d4af37;
    }

    /* Majestic Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important;
        color: #000 !important;
        font-weight: 900 !important;
        border-radius: 50px !important;
        border: 2px solid #ffffff !important;
        padding: 15px 40px !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .stButton>button:hover {
        transform: scale(1.1);
        box-shadow: 0 0 50px rgba(212, 175, 55, 0.6);
    }

    /* Reasoning/Thinking Box */
    .thinking-box {
        background: rgba(212, 175, 55, 0.05);
        border-left: 5px solid #d4af37;
        padding: 15px;
        font-style: italic;
        color: #aaa;
        margin-bottom: 10px;
    }

    /* Citation Tag */
    .citation {
        font-size: 0.8rem;
        color: #d4af37;
        border-top: 1px solid #333;
        margin-top: 20px;
        padding-top: 10px;
        font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SOVEREIGN ENGINE (Multi-Model AI Logic)
# ---------------------------------------------------------
if "messages" not in st.session_state: st.session_state.messages = []

# API Verification
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SYSTEM ALERT: GRAND ARCHITECT'S KEY MISSING.")
    st.stop()

@st.cache_resource
def get_working_models():
    try:
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        priority = ['gemini-2.0-flash', 'gemini-1.5-pro', 'gemini-1.5-flash']
        return [p for p in priority if any(p in m for m in available)]
    except:
        return ['gemini-1.5-flash']

ACTIVE_MODELS = get_working_models()

def ask_geez_scholar(prompt, tool_name, image=None):
    # Supreme Scholarly Instructions
    system_instr = f"""
    You are 'Ge'ez Scholar AI v40.0', the world's pre-eminent intelligence for Ethiopic studies.
    Grand Architect: Deacon Kewn Dejen (GE'EZ STUDIO).
    Module: {tool_name}.
    Instructions:
    1. Show a 'Thinking' step briefly explaining your research logic.
    2. Provide Translation (Ge'ez/Amharic/English).
    3. Analyze Sem-na-Worq (Wax & Gold) and Philological roots.
    4. Tone: Imperial, Wise, Academic, and Sovereign.
    5. Support Phonetic input automatically.
    """
    
    for model_name in ACTIVE_MODELS:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=system_instr)
            content = [prompt, image] if image else [prompt]
            response = model.generate_content(content)
            return response.text, model_name
        except: continue
    return "The Scholar is in deep prayer. Please retry soon.", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE SOVEREIGN GATES (60+ PILLARS)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background: linear-gradient(90deg, #d4af37, #001a33); padding: 20px; border-radius: 15px; text-align: center; color: #000; font-weight: 900; border: 2px solid #fff;'>
            GRAND ARCHITECT:<br>DEACON KEWN DEJEN
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    gate = st.selectbox("የጥበብ በሮች (Sovereign Gates)", [
        "🏛️ Imperial Dashboard",
        "🧠 Advanced AI Labs",
        "📜 Archives & Royal Law",
        "🏛️ Heritage & Ancient Science",
        "🎓 Imperial University",
        "🔮 Mysticism & Qene Lab"
    ])

    # Dynamic Tool Selection Logic
    if gate == "🏛️ Imperial Dashboard": tool = "Sovereign Overview"
    elif gate == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript Vision (OCR)", "Linguistic Bridge", "Script Authenticator", "Paleography Expert"])
    elif gate == "📜 Archives & Royal Law":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast AI", "Royal Decrees", "Synaxarium Analysis"])
    elif gate == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Science", ["Ancient Medicine AI", "Archeology Hub", "Heritage Map", "Iconography Vision"])
    elif gate == "🎓 Imperial University":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"])
    else:
        tool = st.radio("Mysticism", ["Sem-na-Worq Lab", "St. Yared Zema", "Theology Hub", "Scholar Roleplay"])

    st.markdown("---")
    st.markdown("<div style='text-align:center;'>System: <span style='color:#00ff00;'>Imperial Online</span></div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center; font-size:0.7rem;'>v40.0 | Engine: {ACTIVE_MODELS[0]}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE (THE ETERNAL ARCHIVE)
# ---------------------------------------------------------
if gate == "🏛️ Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; letter-spacing: 5px; color:#d4af37;'>THE ETERNAL ZENITH</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='sovereign-card'>
        <h3>Welcome, Honored Scholar.</h3>
        <p style='font-size: 1.1rem; line-height: 1.8; color:#ccc;'>
        You are now connected to the most powerful AI node dedicated to Ethiopian civilization. 
        Engineered by <b>Grand Architect Deacon Kewn Dejen</b>, this studio bridges 3,000 years of 
        wisdom with next-generation neural reasoning.
        </p>
        <p style='color:#d4af37;'>Select a Sovereign Gate from the sidebar to begin your research.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Grid
    c1, c2, c3 = st.columns(3)
    c1.metric("Archives", "12M+ Pages", "Synced")
    c2.metric("Models", f"{len(ACTIVE_MODELS)} Active", "Stable")
    c3.metric("Authority", "Kewn Dejen", "Verified")

# ---------------------------------------------------------
# 5. ADVANCED VISION & RESEARCH TOOLS
# ---------------------------------------------------------
if "Vision" in tool or "OCR" in tool:
    st.subheader(f"📸 {tool} Core")
    file = st.file_uploader("Upload Manuscript/Artifact Image", type=['jpg','png','jpeg'])
    if file:
        img = Image.open(file)
        st.image(img, caption="Target Artifact", width=500)
        if st.button("Analyze Artifact"):
            with st.spinner("Decoding Neural Layers..."):
                res, eng = ask_geez_scholar(f"Provide a deep scholarly analysis for this artifact: {tool}", tool, img)
                st.markdown(f"<div class='sovereign-card'>{res}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. THE SCHOLAR CHAT (WORLD-CLASS DIALOGUE)
# ---------------------------------------------------------
st.markdown("---")
st.subheader(f"💬 Consult the Scholar ({tool})")

# Display Chat History
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

# Chat Input & Logic
if prompt := st.chat_input("Ask the AI Scholar..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # 1. Thinking step visualization
        thinking_placeholder = st.empty()
        thinking_placeholder.markdown("<div class='thinking-box'>Thinking: Consulting the imperial archives and cross-referencing Sem-na-Worq patterns...</div>", unsafe_allow_html=True)
        
        # 2. Actual response
        answer, engine = ask_geez_scholar(prompt, tool)
        thinking_placeholder.empty()
        
        # 3. Citation generation
        cite_year = datetime.datetime.now().year
        citation = f"Citation: Dejen, K. ({cite_year}). {tool} Intelligence Log. Ge'ez Scholar AI Studio v40.0. [AI Generated Response]."
        
        full_html = f"<div>{answer}</div><div class='citation'>{citation}</div>"
        st.markdown(full_html, unsafe_allow_html=True)
        st.caption(f"Intelligence Source: {engine} | Studio v40.0")
        
        st.session_state.messages.append({"role": "assistant", "content": full_html})

# ---------------------------------------------------------
# 7. MASTER FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><br>")
st.markdown(f"""
    <div style='text-align: center; border-top: 1px solid #d4af37; padding-top: 20px;'>
        <p style='color: #d4af37; font-weight: 900; letter-spacing: 5px; font-size: 1.2rem;'>GE'EZ SCHOLAR AI STUDIO</p>
        <p style='color: #888;'>PROUDLY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>
        <p style='font-size: 0.7rem; color: #555;'>© {datetime.datetime.now().year} ALL RIGHTS RESERVED | THE ETERNAL ZENITH EDITION</p>
    </div>
""", unsafe_allow_html=True)
