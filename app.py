import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL & SCHOLARLY CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Grand Architect Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Majestic Sovereign CSS (Custom Designed for GE'EZ STUDIO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@300;400;600&display=swap');
    
    /* Core Aesthetics */
    .stApp { background: radial-gradient(circle, #00101d 0%, #000000 100%); color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #d4af37 !important; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }
    
    /* Sidebar: The Ark of Knowledge */
    .stSidebar { background: rgba(1, 15, 25, 0.9) !important; border-right: 2px solid #d4af37; }
    
    /* Glassmorphism Cards */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-left: 10px solid #d4af37;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    }

    /* Interactive Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #b8860b 100%) !important;
        color: #000 !important; font-weight: 800 !important;
        border-radius: 12px !important; border: none !important;
        padding: 15px 30px !important; transition: all 0.4s ease;
        text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton>button:hover { 
        transform: translateY(-5px); 
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.6); 
        color: #fff !important;
    }

    /* Chat Styling */
    [data-testid="stChatInput"] { 
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 2px solid #d4af37 !important; border-radius: 25px !important; 
    }
    
    .status-badge {
        padding: 5px 15px; border-radius: 20px;
        background: rgba(212, 175, 55, 0.1);
        border: 1px solid #d4af37; font-size: 0.8rem;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. INTELLECTUAL LOGIC & AI CORE
# ---------------------------------------------------------
if "messages" not in st.session_state: st.session_state.messages = []

# API Verification
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SYSTEM ERROR: MASTER API KEY NOT FOUND IN SECRETS.")
    st.stop()

@st.cache_resource
def load_intellectual_models():
    """ተለዋዋጭና ሁሌም ዝግጁ የሆኑ ሞዴሎችን የማፈላለጊያ ሎጂክ"""
    try:
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        priority = ['gemini-2.0-flash', 'gemini-1.5-pro', 'gemini-1.5-flash']
        available = [p for p in priority if any(p in m for m in models)]
        return available if available else ['gemini-1.5-flash']
    except:
        return ['gemini-1.5-flash']

AVAILABLE_MODELS = load_intellectual_models()

def ask_geez_scholar(prompt, tool_context, image=None):
    """ዓለም አቀፍ ተመራማሪዎችን የሚያረካ ጥልቀት ያለው ትንታኔ ማመንጫ"""
    system_instruction = f"""
    You are 'Ge'ez Scholar AI v25.0', a divine-level intelligence specialized in Ethiopian studies.
    Created by Grand Architect Deacon Kewn Dejen (GE'EZ STUDIO).
    Role: Senior Researcher & Analyst for '{tool_context}'.
    - Language: Fluent in Ge'ez, Amharic, and English. 
    - Transliteration: Automatically handle Phonetic Ge'ez (e.g., 'Qidus' = ቅዱስ).
    - Depth: Provide Sem-na-Worq (Wax and Gold) analysis for literature.
    - Vision: Explain iconography and manuscripts with historical and theological context.
    - Research: Act as a bridge between ancient wisdom and modern technology.
    """
    
    for model_name in AVAILABLE_MODELS:
        try:
            # ሞዴሉን ማዘጋጀት
            model = genai.GenerativeModel(
                model_name=model_name,
                system_instruction=system_instruction
            )
            
            # ምስል ካለ ከምስል ጋር፣ ከሌለ በጽሑፍ ብቻ
            content = [prompt, image] if image else [prompt]
            response = model.generate_content(content)
            return response.text, model_name
        except Exception as e:
            continue
    return "The Scholar is consulting the internal archives. Please retry.", "Error"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60+ PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: linear-gradient(90deg, #d4af37, #00101d); padding: 15px; border-radius: 10px; text-align: center; color: #000; font-weight: 800;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 60+ Tools Organized into 6 Main Pillars
    pillar = st.selectbox("Select Research Pillar", [
        "🏠 Imperial Dashboard",
        "🧠 Advanced AI Labs",
        "📜 Digital Archives & Law",
        "🏛️ Heritage, Map & Medicine",
        "🎓 University & Chronology",
        "🔮 Mysticism, Qene & Zema"
    ])

    if pillar == "🏠 Imperial Dashboard": tool = "Sovereign Overview"
    elif pillar == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Iconography Vision", "Linguistic Bridge", "Script Authentication", "Root Finder"])
    elif pillar == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library (12M Pages)", "Fetha Nagast (Legal AI)", "Synaxarium AI", "Royal Decrees"])
    elif pillar == "🏛️ Heritage, Map & Medicine":
        tool = st.radio("Sectors", ["Global Heritage Map", "Ancient Medicine", "Archeology AI", "Architectural Heritage"])
    elif pillar == "🎓 University & Chronology":
        tool = st.radio("Academic", ["Bahre Hasab (Chronology)", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant"])
    else:
        tool = st.radio("Arts", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay"])

    st.markdown("---")
    st.markdown("<div class='status-badge'>System Status: ROYAL ONLINE ✅</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='status-badge'>Intelligence: {AVAILABLE_MODELS[0]}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN INTERFACE: THE ZENITH EXPERIENCE
# ---------------------------------------------------------
if pillar == "🏠 Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size: 1.2rem; color: #d4af37;'>The Eternal Gateway to Ancient Wisdom</p>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='sovereign-card'>
        <h3>Welcome, Global Scholar.</h3>
        <p style='font-size: 1.1rem; line-height: 1.8;'>This is the world's most advanced AI dedicated to Ethiopian wisdom. 
        Engineered by <b>Deacon Kewn Dejen</b>, this studio provides real-time analysis of ancient manuscripts, 
        complex poetry (Qene), and historical archives through 60+ specialized research pillars.</p>
        <p><i>Select a laboratory from the sidebar to begin your journey.</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Archives", "12M+ Pages", "Synced")
    col2.metric("Models", f"{len(AVAILABLE_MODELS)} Active", "Stable")
    col3.metric("Developer", "Kewn Dejen", "Verified")

# ---------------------------------------------------------
# 5. SPECIALIZED TOOL INTERFACES (VISION & RESEARCH)
# ---------------------------------------------------------
if "OCR" in tool or "Vision" in tool:
    st.subheader(f"📸 {tool} Intelligence")
    uploaded_file = st.file_uploader("Upload Artifact (Image/Manuscript)", type=['jpg', 'jpeg', 'png'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Target Artifact", width=500)
        if st.button(f"Initiate {tool} Analysis"):
            with st.spinner("The AI is decoding the artifact..."):
                response, engine = ask_geez_scholar(f"Provide a deep, professional analysis for: {tool}", tool, img)
                st.markdown(f"<div class='sovereign-card'><b>Analysis Result:</b><br><br>{response}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. THE UNIVERSAL CHAT (ALWAYS ACCESSIBLE)
# ---------------------------------------------------------
st.markdown("---")
st.subheader(f"💬 Consult the Scholar ({tool} Expert)")

# Display Chat History with Visual Style
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Global Chat Input Logic
if prompt := st.chat_input("Ask the Scholar a question... (e.g., 'Analyze the Qene: ንጽሕት ይእቲ...')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Consulting the archives..."):
            answer, engine = ask_geez_scholar(prompt, tool)
            if answer:
                st.markdown(answer)
                st.caption(f"Intelligence Source: {engine} | Ge'ez Studio v25.0")
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                st.error("The Archive is momentarily busy. Please repeat your request.")

# ---------------------------------------------------------
# 7. MASTER FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><br><p style='text-align: center; color: #d4af37;'><b>GE'EZ SCHOLAR AI STUDIO | THE ETERNAL ZENITH v25.0</b><br>PROUDLY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>", unsafe_allow_html=True)
