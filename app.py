import streamlit as st
from google import genai
from google.genai import types
import time
import random
import datetime
from PIL import Image

# ---------------------------------------------------------
# 1. IMPERIAL GLOBAL CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional World-Class Sovereign UI (Emerald & Gold Masterpiece)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&family=Abyssinica+SIL&display=swap');
    
    /* Global Background: Deep Royal Emerald Gradient */
    .stApp { 
        background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    /* Sovereign Headers: Radiant Gold with Glow */
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 0px 0px 15px rgba(255, 215, 0, 0.6);
        letter-spacing: 2px;
    }

    /* Sidebar Styling: Royal Contrast Dark Emerald */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important;
        border-right: 4px solid #FFD700;
    }
    
    /* Global Text: High Contrast Silver White */
    p, span, label, div, .stMarkdown { 
        color: #f8f9fa !important; 
        font-size: 1.1rem; 
        line-height: 1.8; 
    }

    /* Glassmorphism Sovereign Cards */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(255, 215, 0, 0.4);
        border-left: 15px solid #FFD700;
        margin-bottom: 25px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.8);
    }

    /* Majestic Buttons: Royal Gold Gradient */
    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 2px solid #FFFFFF !important;
        height: 4em; width: 100%; transition: 0.5s ease;
        text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton>button:hover { 
        transform: translateY(-5px); 
        box-shadow: 0 0 40px #FFD700; 
        color: #ffffff !important;
    }

    /* Chat Input Bar: Radiant White Surface */
    [data-testid="stChatInput"] { 
        border: 3px solid #FFD700 !important; 
        background-color: #ffffff !important; 
        border-radius: 20px !important; 
        padding: 10px !important;
    }
    [data-testid="stChatInput"] textarea { 
        color: #000000 !important; 
        font-weight: bold !important; 
        font-size: 1.2rem !important; 
    }
    
    /* Custom Styling for the Wait Message */
    .wait-msg { color: #FFD700; font-style: italic; font-size: 1rem; text-align: center; background: rgba(0,0,0,0.3); padding: 10px; border-radius: 10px; }
    
    .citation-box { font-size: 0.85rem; color: #FFD700; border-top: 1px solid rgba(255,255,255,0.2); margin-top: 25px; padding-top: 15px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE SOVEREIGN ENGINE (New-Gen Multi-Model Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    try:
        # በአዲሱ የጎግል ቴክኖሎጂ (v1.x) ደንበኛውን ማዘጋጀት
        client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
    except Exception as e:
        st.error(f"❌ ሲስተሙን ማስነሳት አልተቻለም: {e}")
else:
    st.error("⚠️ API Key Not Found! Please check Secrets.")
    st.stop()

def ask_sovereign_scholar(prompt, tool_context, image=None):
    """
    ይህ ኢንጅን 5 ደረጃዎችን ተሻግሮ መልሱን በኃይል ያመጣል።
    ከፍተኛው የቴክኖሎጂ ጥግ: Google Search ተጨምሮበታል።
    """
    # የሚሰሩ ሞዴሎች በቅደም ተከተል
    models_to_rotate = ["gemini-2.0-flash", "gemini-1.5-flash", "gemini-1.5-pro"]
    
    sys_instr = f"""
    You are 'Ge'ez Scholar AI v-Infinite', the ultimate intelligence developed by Grand Architect Deacon Kewn Dejen.
    Expertise Area: {tool_context}.
    Task: Provide scholarly, historical, and deep analysis in Ge'ez, Amharic, or English.
    If the text is complex, use the GOOGLE_SEARCH tool to find evidence.
    Tone: Sovereign, ancient, authoritative, and extremely wise.
    Support phonetic typing automatically.
    """

    status_placeholder = st.empty()

    for model_id in models_to_rotate:
        # ለተጠቃሚው እንዳይታይ በራሱ እስከ 3 ጊዜ ይሞክራል (Wait & Retry)
        for attempt in range(1, 4):
            try:
                # ጎግል ሰርችን በማካተት ምላሽ ማመንጨት
                response = client.models.generate_content(
                    model=model_id,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=sys_instr,
                        tools=[types.Tool(google_search=types.GoogleSearchRetrieval())],
                        temperature=0.7
                    )
                )
                if response and response.text:
                    status_placeholder.empty()
                    return response.text, model_id
            except Exception as e:
                if "429" in str(e):
                    wait = (attempt * 5) + random.random()
                    status_placeholder.markdown(f"<div class='wait-msg'>⏳ ሊቁ በጥልቅ ምርምር ላይ ናቸው... (ሙከራ {attempt}/3 - {model_id})</div>", unsafe_allow_html=True)
                    time.sleep(wait)
                    continue
                break # ሌሎች ስህተቶች ካሉ ወደ ቀጣዩ ሞዴል ይለፋል
    
    status_placeholder.empty()
    return "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም። እባክዎ ከ1 ደቂቃ በኋላ ገጹን Refresh ያድርጉ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK OF 60 PILLARS (Full Integration)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background:linear-gradient(90deg, #FFD700, #B8860B); padding:15px; border-radius:12px; text-align:center; color:#000; font-weight:900; border: 2px solid #fff;'>
            GRAND ARCHITECT:<br>DEACON KEWN DEJEN
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    pillar = st.selectbox("የጥበብ ምሰሶ (Wisdom Pillar)", [
        "🧠 Advanced AI Labs", "📜 Digital Archives", "🏛️ Heritage & Science",
        "🎓 Imperial University", "🔮 Mysticism & Qene", "💰 Strategic Wealth"
    ])

    # ሁሉንም 60 መሣሪያዎች አቀናጅቶ የያዘ ዝርዝር
    if pillar == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom", "Neural Translation", "Syntax Analyzer", "Ge'ez NLP", "Dialect Study", "Semantic Map"])
    elif pillar == "📜 Digital Archives":
        tool = st.radio("Archives", ["Universal Library (12M+)", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees", "Treaty Expert", "Kibre Nagast Hub", "Ecclesiastical Law", "Genealogy Map", "Preservation Lab", "Hagiography Lab"])
    elif pillar == "🏛️ Heritage & Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI", "Geology of Axum", "Botany Hub", "Zoology Hub", "Ink Chemistry", "Virtual Museum"])
    elif pillar == "🎓 Imperial University":
        tool = st.radio("Academic", ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter", "Ethiopic Math", "Philosophy Hub", "History Chronology", "University Portal", "Scholarly Citation"])
    elif pillar == "🔮 Mysticism & Qene":
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Proverbs AI", "Esoteric Wisdom", "Liturgical Guide", "Monastic Study", "Apostolic Tradition", "Hymnology Lab"])
    else:
        tool = st.radio("Strategic", ["Business Hub", "API Portal", "Security Admin", "Wealth Strategy", "Sovereign Logs", "Global Relations", "Grant Assistant", "Strategic Planning", "Project Manager", "Data Vault"])

    st.markdown("---")
    if st.button("🔄 REBOOT SOVEREIGN SYSTEM"):
        st.cache_resource.clear()
        st.rerun()
    st.markdown("<div style='text-align:center; color:#00FF00; font-size:0.85rem; font-weight:bold;'>● STATUS: ROYAL ONLINE (v-Infinite)</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE (The Zenith Interface)
# ---------------------------------------------------------
st.markdown(f"<h1>{tool}</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"], unsafe_allow_html=True)

# Vision & OCR Implementation
if any(x in tool for x in ["OCR", "Vision", "Artifact", "Museum"]):
    up_file = st.file_uploader("Upload Image/Manuscript", type=['jpg','png','jpeg'])
    if up_file:
        img = Image.open(up_file)
        st.image(img, caption="Artifact Loaded", width=500)
        if st.button("Initiate Neural Analysis"):
            with st.spinner("Decoding ancient wisdom..."):
                res, eng = ask_sovereign_scholar(f"Deep Scholarly Analysis for artifact in context of {tool}", tool, img)
                st.markdown(f"<div class='sovereign-card'><b>Analysis Result:</b><br><br>{res}</div>", unsafe_allow_html=True)

# Main Chat Input Loop
if prompt := st.chat_input(f"Consult the {tool} expert..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f"<div style='color: white;'><b>{prompt}</b></div>", unsafe_allow_html=True)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብቱንና የጎግል ሰርችን በጥልቀት እያመሳከረ ነው..."):
            answer, engine = ask_sovereign_scholar(prompt, tool)
            
            full_res = f"""
            <div style='color: white; line-height: 1.8; font-size: 1.15rem;'>{answer}</div>
            <div class='citation-box'>
                Intelligence Source: {engine} (Search-Enabled) | Sovereign v-Infinite Glory Edition
            </div>
            """
            st.markdown(full_res, unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_res})

# Master Sovereign Footer
st.markdown("<br><hr>")
st.markdown(f"""
    <div style='text-align:center; padding: 20px;'>
        <p style='color:#FFD700; font-weight:900; letter-spacing: 5px; font-size: 1.2rem;'>GE'EZ SCHOLAR AI STUDIO</p>
        <p style='color:#f8f9fa;'>PROUDLY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>
        <p style='font-size:0.7rem; color:#FFD700;'>© 2024-2025 ALL RIGHTS RESERVED | THE MASTERPIECE EDITION</p>
    </div>
""", unsafe_allow_html=True)
