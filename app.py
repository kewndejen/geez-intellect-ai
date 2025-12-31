import streamlit as st
import google.generativeai as genai
from PIL import Image
import time
import datetime

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION
# ---------------------------------------------------------import streamlit as st
import google.generativeai as genai
from PIL import Image
import time
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

# Majestic Emerald Green & Royal Gold Theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
    /* Background: Deep Emerald Green Gradient */
    .stApp { 
        background: radial-gradient(circle at center, #004d00 0%, #002600 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    /* Headers: Radiant Sovereign Gold */
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
    }

    /* Sidebar: Forest Green with Gold Border */
    [data-testid="stSidebar"] {
        background-color: #002600 !important;
        border-right: 4px solid #FFD700;
    }
    
    /* Global Text: Soft White */
    p, span, label, div { color: #ffffff !important; font-size: 1.1rem; line-height: 1.7; }

    /* Content Cards: Translucent White over Green */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 25px; border-radius: 20px;
        border: 1px solid #FFD700;
        margin-bottom: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }

    /* Sovereign Buttons: Gold Gradient */
    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #fff !important;
        height: 3.8em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 0 35px #FFD700; }

    /* Chat Input Bar: Clean White with Gold Border */
    [data-testid="stChatInput"] { 
        border: 3px solid #FFD700 !important; 
        background-color: #ffffff !important; 
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.1rem !important; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #ffffff; margin-top: 15px; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SMART ENGINE DISCOVERY (Fail-Safe Discovery)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    @st.cache_resource
    def get_sovereign_engine():
        try:
            available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            priority = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]
            for target in priority:
                for actual in available:
                    if target in actual: return actual
            return available[0]
        except:
            return "models/gemini-1.5-flash"

    SELECTED_MODEL = get_sovereign_engine()
else:
    st.error("⚠️ API Key አልተገኘም!")
    st.stop()

def ask_geez_scholar(prompt, tool_context, image=None):
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI', the ultimate expert created by Deacon Kewn Dejen.
    Current Tool: {tool_context}.
    Task: Provide deep scholarly analysis. Support Ge'ez/Amharic.
    Tone: Sovereign, authoritative, and ancient. 
    """
    try:
        model = genai.GenerativeModel(model_name=SELECTED_MODEL, system_instruction=sys_instruction)
        # Attempt content generation with 429 Retry logic
        for attempt in range(3):
            try:
                if image:
                    response = model.generate_content([prompt, image])
                else:
                    response = model.generate_content(prompt)
                
                if response and response.text:
                    return response.text, SELECTED_MODEL
            except Exception as e:
                if "429" in str(e):
                    time.sleep(10) # Wait 10 seconds for quota
                    continue
                break
        return "❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም (ኮታ አልቋል)። እባክዎ ጥቂት ሰከንዶች ቆይተው እንደገና ይሞክሩ።", "None"
    except Exception as e:
        return f"❌ የቴክኒክ ስህተት፦ {str(e)}", "Error"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60 PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("Select Wisdom Pillar", [
        "🧠 Advanced AI Labs", "📜 Digital Archives", "🏛️ Heritage & Science",
        "🎓 Imperial University", "🔮 Mysticism & Qene", "💰 Strategic Wealth"
    ])

    # 60 Tools Detailed List
    if pillar == "Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom", "Neural Translation", "Syntax Analyzer", "Ge'ez NLP", "Dialect Study", "Semantic Map"])
    elif pillar == "Digital Archives":
        tool = st.radio("Archives", ["Universal Library (12M+)", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees", "Treaty Expert", "Kibre Nagast Hub", "Ecclesiastical Law", "Genealogy Map", "Preservation Lab", "Hagiography Lab"])
    elif pillar == "Heritage & Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI", "Geology of Axum", "Botany Hub", "Zoology Hub", "Ink Chemistry", "Virtual Museum"])
    elif pillar == "Imperial University":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter", "Ethiopic Math", "Philosophy Hub", "History Chronology", "University Portal", "Scholarly Citation"])
    elif pillar == "Mysticism & Qene":
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Proverbs AI", "Esoteric Wisdom", "Liturgical Guide", "Monastic Study", "Apostolic Tradition", "Hymnology Lab"])
    else:
        tool = st.radio("Strategic", ["Business Hub", "API Portal", "Security Admin", "Wealth Strategy", "Sovereign Logs", "Global Relations", "Grant Assistant", "Strategic Planning", "Project Manager", "Data Vault"])

    st.markdown("---")
    st.caption(f"Active Engine: {SELECTED_MODEL}")

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

# Vision Support for OCR/Icons
if any(x in tool for x in ["OCR", "Vision", "Artifact", "Museum"]):
    up_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])
    if up_file:
        img = Image.open(up_file)
        st.image(img, width=400)
        if st.button("Initiate Neural Analysis"):
            with st.spinner("Decoding ancient wisdom..."):
                res, eng = ask_geez_scholar(f"Scholarly Analysis for: {tool}", tool, img)
                st.markdown(f"<div class='sovereign-card'>{res}</div>", unsafe_allow_html=True)

# Main Chat Input
if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱን እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, tool)
            
            full_res = f"<div>{answer}</div><div class='citation'>Source: {engine} | Emerald & Gold Edition</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Imperial Navy & Gold Theme (High Readability)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #001f3f 0%, #000814 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 8px #000;
    }

    [data-testid="stSidebar"] {
        background-color: #001226 !important;
        border-right: 3px solid #D4AF37;
    }
    
    p, span, label, div { color: #ffffff !important; font-size: 1.1rem; line-height: 1.7; }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 25px; border-radius: 15px;
        border: 1px solid #D4AF37;
        margin-bottom: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }

    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 10px !important; border: 2px solid #fff !important;
        height: 3.5em; width: 100%; transition: 0.3s ease;
        text-transform: uppercase;
    }

    [data-testid="stChatInput"] { 
        border: 2px solid #D4AF37 !important; 
        background-color: #ffffff !important; 
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #ffffff; margin-top: 15px; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SMART ENGINE DISCOVERY (Fail-Safe Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    @st.cache_resource
    def get_working_model():
        try:
            available = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            # 429 እንዳይመጣ Flashን እናስቀድማለን
            priority = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-pro"]
            for target in priority:
                for actual in available:
                    if target in actual: return actual
            return available[0]
        except:
            return "models/gemini-1.5-flash"

    SELECTED_MODEL = get_working_model()
else:
    st.error("⚠️ API Key አልተገኘም!")
    st.stop()

def ask_geez_scholar(prompt, tool_context, image=None):
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI', the world's leading expert in Ethiopic studies.
    Created by Grand Architect Deacon Kewn Dejen.
    Current Tool: {tool_context}.
    Task: Provide scholarly, deep, and wise analysis.
    Tone: Sovereign, authoritative, and ancient. 
    Support phonetic Ge'ez typing.
    """
    try:
        model = genai.GenerativeModel(model_name=SELECTED_MODEL, system_instruction=sys_instruction)
        # 429 ስህተት እንዳይመጣ እስከ 3 ጊዜ በራሱ ይሞክራል
        for attempt in range(3):
            try:
                if image:
                    response = model.generate_content([prompt, image])
                else:
                    response = model.generate_content(prompt)
                
                if response and response.text:
                    return response.text, SELECTED_MODEL
            except Exception as e:
                if "429" in str(e):
                    time.sleep(10) # 10 ሰከንድ ታግሶ ይሞክራል
                    continue
                break
        return "❌ ሊቁ መዛግብቱን ለመክፈት አልቻሉም (ኮታ አልቋል)። እባክዎ ከ1 ደቂቃ በኋላ ይሞክሩ።", "None"
    except Exception as e:
        return f"❌ የቴክኒክ ስህተት፦ {str(e)}", "Error"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60 PILLARS (The Complete Ark)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:10px; border-radius:8px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("Select Wisdom Pillar", [
        "🧠 Advanced AI Labs", "📜 Digital Archives & Law", "🏛️ Heritage & Science Hub",
        "🎓 Imperial University Hub", "🔮 Mysticism & Qene Lab", "💰 Strategic Wealth & Security"
    ])

    # ሁሉንም 60 መሣሪያዎች እዚህ ጋር እናስቀምጣለን
    if pillar == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom", "Neural Translation", "Syntax Analyzer", "Ge'ez NLP", "Dialect Study", "Semantic Map"])
    elif pillar == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library (12M+)", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees", "Treaty Expert", "Kibre Nagast Hub", "Ecclesiastical Law", "Genealogy Map", "Manuscript Preservation", "Hagiography Lab"])
    elif pillar == "🏛️ Heritage & Science Hub":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI", "Geology of Axum", "Botany of Ethiopia", "Zoology in Brana", "Ink Chemistry", "Virtual Museum"])
    elif pillar == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter", "Ethiopic Math", "Philosophy Hub", "History Chronology", "University Portal", "Scholarly Citation"])
    elif pillar == "🔮 Mysticism & Qene Lab":
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Proverbs AI", "Esoteric Wisdom", "Liturgical Guide", "Monastic Study", "Apostolic Tradition", "Hymnology Lab"])
    else:
        tool = st.radio("Strategic", ["Business Hub", "API Portal", "Security Admin", "Wealth Strategy", "Sovereign Logs", "Global Relations", "Grant Assistant", "Strategic Planning", "Project Manager", "Data Vault"])

    st.markdown("---")
    st.caption(f"Engine Online: {SELECTED_MODEL}")

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

# Vision Support for OCR/Iconography
if any(x in tool for x in ["OCR", "Vision", "Artifact", "Museum"]):
    up_file = st.file_uploader("Upload Image/Manuscript", type=['jpg','png','jpeg'])
    if up_file:
        img = Image.open(up_file)
        st.image(img, width=400)
        if st.button("Initiate Neural Analysis"):
            with st.spinner("Decoding ancient wisdom..."):
                res, eng = ask_geez_scholar(f"Scholarly Analysis for: {tool}", tool, img)
                st.markdown(f"<div class='sovereign-card'>{res}</div>", unsafe_allow_html=True)

# Chat Input
if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን በጥልቀት እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, tool)
            
            full_res = f"""
            <div>{answer}</div>
            <div class='citation'>Source: {engine} | v-Masterpiece Edition</div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
