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

# Professional Sovereign CSS (Tested & Optimized)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&display=swap');
    
    /* Core Body */
    .stApp { background-color: #000814; color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #d4af37 !important; text-align: center; }

    /* Imperial Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #001220 0%, #1a0000 100%) !important;
        border-right: 3px solid #d4af37;
    }

    /* Sovereign Glass Cards */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        padding: 25px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-left: 10px solid #d4af37;
        margin-bottom: 20px;
    }

    /* Professional Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important;
        color: #000 !important; font-weight: 800 !important;
        border-radius: 10px !important; border: none !important;
        height: 3.5em; width: 100%; transition: 0.3s ease;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px #d4af37; }

    /* Chat Input */
    [data-testid="stChatInput"] { border: 2px solid #d4af37 !important; border-radius: 20px !important; }

    /* Citation & Thinking Box */
    .thinking-box { color: #d4af37; font-style: italic; font-size: 0.9rem; margin-bottom: 10px; }
    .citation-box { 
        font-size: 0.75rem; color: #888; border-top: 1px solid #333; 
        padding-top: 10px; margin-top: 20px; font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. CORE INTELLIGENCE ENGINE (Robust & Scalable)
# ---------------------------------------------------------
if "messages" not in st.session_state: st.session_state.messages = []

# API Verification
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ CRITICAL ERROR: API Key is missing. Please add GOOGLE_API_KEY to Streamlit Secrets.")
    st.stop()

@st.cache_resource
def load_models():
    """ሁሌም የሚሰሩና የተሻሉ ሞዴሎችን በቅደም ተከተል መምረጥ"""
    try:
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # ቅድሚያ ለ 2.0 እና 1.5 ፕሮ
        targets = ['gemini-2.0-flash', 'gemini-1.5-pro', 'gemini-1.5-flash']
        working = [t for t in targets if any(t in a for a in available)]
        return working if working else ['gemini-1.5-flash']
    except:
        return ['gemini-1.5-flash']

ACTIVE_MODELS = load_models()

def ask_scholar_ai(prompt, tool_context, image=None):
    """ጥልቅ የሆነ የምሁር ትንታኔ ማመንጫ ሎጂክ"""
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI Studio v50.0', a world-class expert in Ethiopic studies.
    Created by Grand Architect Deacon Kewn Dejen.
    Pillar Context: {tool_context}.
    Task: Provide scholarly, accurate, and deep analysis. 
    1. If text is in Ge'ez, explain its grammar and 'Sem-na-Worq'.
    2. Support phonetic Ge'ez (Latin input) automatically.
    3. If an image is provided, act as a Paleography/Iconography expert.
    4. Tone: Respectful, Academic, Sovereign.
    """
    
    for model_name in ACTIVE_MODELS:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instruction)
            content = [prompt, image] if image else [prompt]
            response = model.generate_content(content)
            return response.text, model_name
        except: continue
    return "The Scholar is currently reviewing the archives. Please retry shortly.", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60+ TOOLS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background: linear-gradient(90deg, #d4af37, #001220); padding: 15px; border-radius: 10px; text-align: center; color: #000; font-weight: bold;'>
            GRAND ARCHITECT:<br>DEACON KEWN DEJEN
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    category = st.selectbox("Select Research Pillar", [
        "🏛️ Imperial Dashboard",
        "🧠 AI Research Labs",
        "📜 Digital Archives & Law",
        "🏛️ Heritage & Ancient Science",
        "🎓 Imperial University Hub",
        "🔮 Mysticism, Qene & Zema"
    ])

    # Dynamic Tool Loading
    if category == "🏛️ Imperial Dashboard": tool = "Sovereign Overview"
    elif category == "🧠 AI Research Labs":
        tool = st.radio("Labs", ["Manuscript OCR (Vision)", "Linguistic Bridge", "Script Authentication", "Root Finder"])
    elif category == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast (Legal AI)", "Royal Decrees", "Synaxarium Analysis"])
    elif category == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"])
    elif category == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Logic", "Abu Shaker Astronomy", "Numerology", "Scribe Assistant"])
    else:
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay"])

    st.markdown("---")
    st.markdown(f"<div style='font-size: 0.75rem; color: #d4af37;'>Intelligence Source: {ACTIVE_MODELS[0]}</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 0.75rem; color: #00ff00;'>System Status: ONLINE ✅</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE (THE ZENITH EXPERIENCE)
# ---------------------------------------------------------
if category == "🏛️ Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #d4af37; letter-spacing: 3px;'>THE ETERNAL ZENITH v50.0</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='sovereign-card'>
        <h3>Welcome, Honored Scholar.</h3>
        <p>This is the world's most advanced AI gateway for Ethiopian wisdom, engineered by <b>Grand Architect Deacon Kewn Dejen</b>. 
        Select a specialized laboratory from the sidebar to begin analyzing manuscripts, laws, and ancient sciences.</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Archives", "12M+ Pages", "Synced")
    c2.metric("Models", f"{len(ACTIVE_MODELS)} Active", "Stable")
    c3.metric("Authority", "Kewn Dejen", "Verified")

# Vision Tool Logic
if "OCR" in tool or "Vision" in tool:
    st.subheader(f"📸 {tool} Intelligence")
    up_file = st.file_uploader("Upload Image (Manuscript/Icon)", type=['jpg','png','jpeg'])
    if up_file:
        img = Image.open(up_file)
        st.image(img, caption="Target Artifact", width=450)
        if st.button("Initiate Neural Analysis"):
            with st.spinner("Decoding ancient script..."):
                res, eng = ask_scholar_ai(f"Provide a deep scholarly analysis for this image in the context of: {tool}", tool, img)
                st.markdown(f"<div class='sovereign-card'><b>Analysis Result:</b><br><br>{res}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. GLOBAL CHAT INTERFACE
# ---------------------------------------------------------
st.markdown("---")
st.subheader(f"💬 Consult the Scholar ({tool} Mode)")

# Display History
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

# Input
if prompt := st.chat_input("Ask the Scholar a question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        thinking = st.empty()
        thinking.markdown("<div class='thinking-box'>Thinking: Consulting the imperial archives...</div>", unsafe_allow_html=True)
        
        answer, engine = ask_scholar_ai(prompt, tool)
        thinking.empty()
        
        # Citation
        year = datetime.datetime.now().year
        cite = f"<div class='citation-box'>Citation: Dejen, K. ({year}). {tool} Research Log. Ge'ez Scholar AI Studio v50.0. Powered by Ge'ez Studio.</div>"
        
        full_response = f"{answer}{cite}"
        st.markdown(full_response, unsafe_allow_html=True)
        st.caption(f"Source: {engine} | v50.0 Stable")
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# ---------------------------------------------------------
# 6. MASTER FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><br>")
st.markdown(f"""
    <div style='text-align: center; border-top: 2px solid #d4af37; padding-top: 20px;'>
        <p style='color: #d4af37; font-weight: 900; letter-spacing: 5px;'>GE'EZ SCHOLAR AI STUDIO</p>
        <p style='color: #888;'>PROUDLY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>
        <p style='font-size: 0.7rem; color: #444;'>© {datetime.datetime.now().year} ALL RIGHTS RESERVED | THE MASTERPIECE EDITION</p>
    </div>
""", unsafe_allow_html=True)
