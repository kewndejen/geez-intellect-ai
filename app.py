import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Imperial Navy & Gold Theme (Extreme Contrast & Visibility)
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
        background-color: #000b1a !important;
        border-right: 3px solid #D4AF37;
    }
    
    p, span, label, div { color: #ffffff !important; font-size: 1.1rem; line-height: 1.8; }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid #D4AF37;
        margin-bottom: 25px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.7);
    }

    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 10px !important; border: 2px solid #fff !important;
        height: 3.8em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase;
    }

    /* Ultra-Visible Chat Input */
    [data-testid="stChatInput"] { 
        border: 3px solid #D4AF37 !important; 
        background-color: #ffffff !important;
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold !important; font-size: 1.2rem !important; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE DYNAMIC SOVEREIGN ENGINE (No-Error Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    @st.cache_resource
    def discover_sovereign_model():
        """በእርስዎ ቁልፍ የሚሰራውን ሞዴል በራስ-ሰር ይፈልጋል (404 መከላከያ)"""
        try:
            # የሚሰሩ ሞዴሎችን ዝርዝር መጠየቅ
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            
            # ምርጥ የሆኑትን በቅደም ተከተል መምረጥ
            priority_list = ["gemini-1.5-flash", "gemini-1.5-pro", "gemini-2.0-flash", "gemini-pro"]
            for target in priority_list:
                for actual in available_models:
                    if target in actual:
                        return actual
            return available_models[0] # ምንም ካልተገኘ ዝርዝሩ ውስጥ ያለውን የመጀመሪያውን መጠቀም
        except:
            return "models/gemini-pro" # የመጨረሻ አማራጭ

    SELECTED_MODEL = discover_sovereign_model()
else:
    st.error("⚠️ API Key አልተገኘም!")
    st.stop()

def ask_geez_scholar(prompt, tool_context):
    sys_instr = f"You are 'Ge'ez Scholar AI', an expert in {tool_context}, created by Grand Architect Deacon Kewn Dejen. Provide deep scholarly analysis."
    try:
        model = genai.GenerativeModel(model_name=SELECTED_MODEL, system_instruction=sys_instr)
        
        # የኮታ መጨናነቅን (429) ለመከላከል እስከ 3 ጊዜ ይሞክራል
        for attempt in range(3):
            try:
                response = model.generate_content(prompt)
                if response and response.text:
                    return response.text, SELECTED_MODEL
            except Exception as e:
                if "429" in str(e):
                    time.sleep(5)
                    continue
                raise e
    except Exception as e:
        return f"❌ የቴክኒክ ስህተት፦ {str(e)}", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60 PILLARS (All Tools)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background:#FFD700; padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:bold;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("የጥበብ ምሰሶ", [
        "Advanced AI Labs", "Digital Archives", "Heritage & Science",
        "Imperial University", "Mysticism & Qene", "Strategic Wealth"
    ])

    if pillar == "Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Neural Translation", "Syntax Analyzer", "Ge'ez NLP", "Dialect Study", "Semantic Map", "Voice of Wisdom"])
    elif pillar == "Digital Archives":
        tool = st.radio("Archives", ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees", "Treaty Expert", "Kibre Nagast Hub", "Ecclesiastical Law", "Genealogy Map", "Preservation Lab", "Hagiography Lab"])
    elif pillar == "Heritage & Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI", "Geology of Axum", "Botany Hub", "Zoology in Brana", "Ink Chemistry", "Virtual Museum"])
    elif pillar == "Imperial University":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter", "Ethiopic Math", "Philosophy Hub", "History Chronology", "University Portal", "Scholarly Citation"])
    elif pillar == "Mysticism & Qene":
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Proverbs AI", "Esoteric Wisdom", "Liturgical Guide", "Monastic Study", "Apostolic Tradition", "Hymnology Lab"])
    else:
        tool = st.radio("Strategic", ["Business Hub", "API Portal", "Security Admin", "Wealth Strategy", "Sovereign Logs", "Global Relations", "Grant Assistant", "Strategic Planning", "Project Manager", "Data Vault"])

    st.markdown("---")
    st.caption(f"Engine Online: {SELECTED_MODEL}")

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትን በጥልቀት እያመሳከረ ነው..."):
            answer, engine = ask_geez_scholar(prompt, tool)
            full_res = f"<div>{answer}</div><div style='font-size:0.8rem; color:#FFD700; margin-top:20px; border-top:1px solid #555; padding-top:10px;'>Intelligence Source: {engine} | Sovereign v-Ultimate</div>"
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</p>", unsafe_allow_html=True)
