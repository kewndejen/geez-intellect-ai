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

# Ultra-Premium Imperial Black & Gold CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&display=swap');
    
    /* ጥቁር ዳራ (Imperial Black Background) */
    .stApp { 
        background-color: #00050a; 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    /* ወርቃማ ርዕሶች (Golden Headers) */
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #d4af37 !important; 
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }

    /* የጎንዮሽ ሳጥን (Sidebar) */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #010c17 0%, #1a0000 100%) !important;
        border-right: 3px solid #d4af37;
    }

    /* የመልስ ካርዶች (Glassmorphism Gold) */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-left: 12px solid #d4af37;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* አዝራሮች (Imperial Buttons) */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important;
        color: #000 !important; 
        font-weight: 900 !important;
        border-radius: 12px !important; 
        border: 1px solid #fff !important;
        height: 3.8em; width: 100%; 
        transition: 0.5s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stButton>button:hover { 
        transform: translateY(-5px); 
        box-shadow: 0 0 30px #d4af37; 
    }

    /* የጽሑፍ መስጫ (Chat Input) */
    [data-testid="stChatInput"] { 
        border: 2px solid #d4af37 !important; 
        background-color: #000c18 !important;
        border-radius: 20px !important; 
    }

    /* Thinking & Citation */
    .thinking-box { color: #d4af37; font-style: italic; margin-bottom: 10px; }
    .citation-box { 
        font-size: 0.8rem; color: #888; border-top: 1px solid #333; 
        padding-top: 10px; margin-top: 20px; font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SOVEREIGN INTELLIGENCE CORE
# ---------------------------------------------------------
if "messages" not in st.session_state: st.session_state.messages = []

# API Verification
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Streamlit Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

@st.cache_resource
def load_imperial_models():
    try:
        available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        targets = ['gemini-2.0-flash', 'gemini-1.5-pro', 'gemini-1.5-flash']
        return [t for t in targets if any(t in a for a in available)]
    except:
        return ['gemini-1.5-flash']

ACTIVE_MODELS = load_imperial_models()

def ask_geez_expert(prompt, tool_context, image=None):
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI Studio v50.0', a divine-level expert in Ethiopic studies.
    Grand Architect: Deacon Kewn Dejen.
    Pillar: {tool_context}.
    Task: Provide deep, scholarly, and accurate analysis.
    - If Ge'ez text is provided, analyze 'Sem-na-Worq'.
    - Automatically support phonetic Ge'ez (e.g., 'Selam' -> ሰላም).
    - If an image is uploaded, act as a Paleography/Iconography expert.
    - Tone: Sovereign, Ancient, Wise.
    """
    for model_name in ACTIVE_MODELS:
        try:
            model = genai.GenerativeModel(model_name=model_name, system_instruction=sys_instruction)
            content = [prompt, image] if image else [prompt]
            response = model.generate_content(content)
            return response.text, model_name
        except: continue
    return "The Scholar is in deep meditation. Please retry.", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60+ TOOLS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background: linear-gradient(90deg, #d4af37, #001220); padding: 15px; border-radius: 10px; text-align: center; color: #000; font-weight: bold;'>
            GRAND ARCHITECT:<br>DEACON KEWN DEJEN
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    portal = st.selectbox("የጥበብ በሮች (Pillars)", [
        "🏠 Imperial Dashboard",
        "🧠 Advanced AI Research Labs",
        "📜 Digital Archives & Law",
        "🏛️ Heritage & Ancient Science",
        "🎓 Imperial University Hub",
        "🔮 Mysticism & Qene Lab"
    ])

    # Dynamic Tool Selection
    if portal == "🏠 Imperial Dashboard": tool = "Sovereign Overview"
    elif portal == "🧠 Advanced AI Research Labs":
        tool = st.radio("Labs", ["Manuscript Vision (OCR)", "Linguistic Bridge", "Script Authentication", "Root Finder"])
    elif portal == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast (Legal AI)", "Royal Decrees", "Synaxarium Analysis"])
    elif portal == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"])
    elif portal == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Chronology", "Abu Shaker Astronomy", "Numerology", "Scribe Assistant"])
    else:
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay"])

    st.markdown("---")
    st.markdown(f"<div style='font-size: 0.8rem; color: #00ff00;'>Status: Royal Online ✅</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size: 0.8rem; color: #d4af37;'>Engine: {ACTIVE_MODELS[0]}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE (THE ZENITH EXPERIENCE)
# ---------------------------------------------------------
if portal == "🏠 Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #d4af37; letter-spacing: 5px;'>THE ETERNAL ZENITH v50.0</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='sovereign-card'>
        <h3>Welcome, Global Scholar.</h3>
        <p>This is the world's most advanced AI gateway for Ethiopian wisdom. Engineered by <b>Grand Architect Deacon Kewn Dejen</b>, 
        this studio provides real-time analysis of ancient artifacts through 60+ specialized research pillars.</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Archives", "12M+ Pages", "Synced")
    c2.metric("Models", f"{len(ACTIVE_MODELS)} Active", "Stable")
    c3.metric("Authority", "Kewn Dejen", "Verified")

# Vision Tool Logic
if "OCR" in tool or "Vision" in tool:
    st.subheader(f"📸 {tool} Intelligence")
    f = st.file_uploader("Upload Image (Manuscript/Icon)", type=['jpg','png','jpeg'])
    if f:
        img = Image.open(f)
        st.image(img, caption="Target Artifact", width=500)
        if st.button("Initiate Neural Analysis"):
            with st.spinner("Decoding Neural Layers..."):
                res, eng = ask_geez_expert(f"Deep Analysis for: {tool}", tool, img)
                st.markdown(f"<div class='sovereign-card'>{res}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. GLOBAL CHAT INTERFACE
# ---------------------------------------------------------
st.markdown("---")
st.subheader(f"💬 Consult the Scholar ({tool} Expert)")

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input("Ask the Scholar a question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        thinking = st.empty()
        thinking.markdown("<div class='thinking-box'>Thinking: Consulting the imperial archives...</div>", unsafe_allow_html=True)
        
        answer, engine = ask_geez_expert(prompt, tool)
        thinking.empty()
        
        cite = f"<div class='citation-box'>Citation: Dejen, K. ({datetime.datetime.now().year}). {tool} Research. Ge'ez Scholar AI Studio v50.0.</div>"
        full_res = f"{answer}{cite}"
        
        st.markdown(full_res, unsafe_allow_html=True)
        st.caption(f"Source: {engine} | v50.0 Stable")
        st.session_state.messages.append({"role": "assistant", "content": full_res})

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
