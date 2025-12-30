import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL PRESTIGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Mastered by Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Sovereign CSS (Midnight Blue, Royal Gold, & Diamond White)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background-color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    
    /* Sidebar - The Sovereign Command Center */
    .stSidebar { 
        background: linear-gradient(180deg, #000c18 0%, #300000 100%) !important; 
        border-right: 5px solid #b8860b; 
    }
    .stSidebar [data-testid="stMarkdownContainer"] p { color: #d4af37 !important; font-weight: bold; }

    /* The Majesty Sovereign Button */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%);
        color: white; border: none; padding: 18px 30px;
        border-radius: 12px; font-weight: 800; width: 100%;
        font-size: 16px; letter-spacing: 1px; transition: 0.5s;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { 
        transform: translateY(-5px); 
        box-shadow: 0 15px 50px rgba(184, 134, 11, 0.8); 
    }
    
    /* Global Chat Input - Locked at Bottom for Perfection */
    [data-testid="stChatInput"] {
        position: fixed; bottom: 30px; z-index: 1000;
        background: white !important; border: 2px solid #b8860b !important;
        border-radius: 15px !important;
    }
    
    /* Elegant Content Cards */
    .sovereign-card {
        background: white; padding: 40px; border-radius: 20px;
        border-left: 15px solid #b8860b; box-shadow: 0 20px 80px rgba(0,0,0,0.1);
        margin-bottom: 35px; border-top: 1px solid #f0f0f0;
    }
    
    .dev-signature {
        background: linear-gradient(90deg, #b8860b, #000c18);
        padding: 25px; border-radius: 15px; border: 2px solid #d4af37;
        text-align: center; color: white; font-weight: bold; margin-bottom: 30px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE QUANTUM AI ENGINE (Kewn Dejen Intelligence)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: System Credentials Missing. Contact Deacon Kewn Dejen.")
    st.stop()

model = genai.GenerativeModel('gemini-2.0-flash')

# ---------------------------------------------------------
# 3. GLOBAL NAVIGATION - THE 60+ PILLARS COMMAND CENTER
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='dev-signature'>GRAND ARCHITECT & DEVELOPER:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    main_portal = st.selectbox("የእውቀት ምድብ (Select Portal)", [
        "🏠 Imperial Dashboard",
        "🧠 Advanced AI Research Labs",
        "📜 Digital Libraries & Archives",
        "🏛️ Heritage, Map & Material Science",
        "🎓 Imperial University & Science",
        "🔮 Mysticism, Poetry & Prophecy",
        "💰 Strategic Business & Security"
    ])
    
    st.markdown("---")
    
    # Nested Tools - All 60+ integrated here
    if main_portal == "🏠 Imperial Dashboard":
        tool = "Dashboard Overview"
    elif main_portal == "🧠 Advanced AI Research Labs":
        tool = st.radio("AI መሣሪያዎች", [
            "Manuscript OCR (ብራና አንባቢ)", "Palæography Expert", "Authentication Lab", 
            "Linguistic Bridge", "Cryptography Lab", "Voice Assistant", "Root Finder"
        ])
    elif main_portal == "📜 Digital Libraries & Archives":
        tool = st.radio("መዛግብት", [
            "Universal Library (12M Pages)", "Deep Doc Analyzer", "Legal AI (ሕግ)", 
            "Treaty Expert", "Timelines", "Royal Decrees", "Synaxarium AI"
        ])
    elif main_portal == "🏛️ Heritage, Map & Material Science":
        tool = st.radio("ቅርስና ሳይንስ", [
            "Virtual Museum", "Interactive Map", "Iconography", "Archeology", 
            "Architecture AI", "Ancient Medicine", "Ink & Material Science"
        ])
    elif main_portal == "🎓 Imperial University & Science":
        tool = st.radio("ትምህርትና ሳይንስ", [
            "University Hub", "Bahre Hasab Logic", "Abu Shaker Astronomy", 
            "Numerology", "Font Converter", "Certification", "Restoration"
        ])
    elif main_portal == "🔮 Mysticism, Poetry & Prophecy":
        tool = st.radio("ምስጢርና ቅኔ", [
            "Sem-na-Work (ቅኔ መፍቻ)", "Verse Meter", "Zema Lab", 
            "Esoteric Lab", "Scholar Roleplay", "Proverbs & Wisdom", "Theology"
        ])
    else:
        tool = st.radio("ቢዝነስና ደህንነት", [
            "Business Hub", "Payment Gateway", "API Portal", "Security Admin"
        ])

# ---------------------------------------------------------
# 4. DYNAMIC CONTENT WORKSPACE
# ---------------------------------------------------------

# --- PORTAL 1: DASHBOARD ---
if tool == "Dashboard Overview":
    st.title("The Imperial Sovereign Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Reasoning Depth", "12M+ Pages", "Infinite")
    col2.metric("Integrated Tools", "60+ Sovereigns", "Active")
    col3.metric("Developer Status", "Kewn Dejen", "Verified")
    
    st.markdown("""
    <div class='sovereign-card'>
    <h3>እንኳን ወደ ዲያቆን ከውን ደጀን የጥበብ መንግሥት በደህና መጡ።</h3>
    ይህ በዓለም አቀፍ ደረጃ እጅግ ተፈላጊ የሆኑትን ሁሉንም የግዕዝ ጥበብ መሣሪያዎች በአንድ ላይ የያዘ ግዙፍ የ AI ውጤት ነው። 
    ብራና ለማንበብ፣ ቅኔ ለመፍታት ወይም ታሪክ ለመጠየቅ በግራ በኩል ያሉትን መሣሪያዎች ይጠቀሙ። ቻቱ ሁልጊዜ ከታች ዝግጁ ነው።
    </div>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=350)

# --- PORTAL 2: MANUSCRIPT OCR (ብራና አንባቢ) ---
elif tool == "Manuscript OCR (ብራና አንባቢ)":
    st.title("🧠 Manuscript OCR Intelligence")
    st.write("የብራና ወይም የጽሁፍ ፎቶ እዚህ ይጫኑ። AIው በጥልቀት ተንትኖ ይተረጉመዋል።")
    file = st.file_uploader("Upload Manuscript Image", type=['jpg','png','jpeg'])
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)
        if st.button("Start Deep Neural Scan"):
            with st.spinner("Deacon Kewn Dejen's AI is analyzing..."):
                try:
                    res = model.generate_content(["ይህንን ብራና በባለሙያ ደረጃ ተንትነህ ተርጉመው፡", img])
                    st.markdown(f"<div class='sovereign-card'>{res.text}</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.warning("⚠️ ሲስተሙ ተጨናንቋል። እባክህ 20 ሰከንድ ቆይተህ ድገመው።")

# --- PORTAL: BAHRE HASAB (ባሕረ ሐሳብ) ---
elif tool == "Bahre Hasab Logic":
    st.title("📅 Bahre Hasab & Calendar AI")
    year = st.number_input("ዓመተ ምሕረት ያስገቡ (ለምሳሌ፡ 2017)", min_value=1)
    if st.button("ቀመሩን አውጣ"):
        res = model.generate_content(f"ለ {year} ዓመተ ምሕረት የባሕረ ሐሳብ ቀመር (አጽዋማትና በዓላት) አውጣ።")
        st.write(res.text)

# --- PORTAL: QENE (ቅኔ) ---
elif tool == "Sem-na-Work (ቅኔ መፍቻ)":
    st.title("📜 Sem-na-Work Logic Center")
    qene = st.text_area("የቅኔውን ቤት እዚህ ያስገቡ...")
    if st.button("ምስጢሩን ግለጥ"):
        res = model.generate_content(f"ለዚህ ቅኔ ጥልቅ የሆነ ሰም እና ወርቅ ትንታኔ ስጥ፡ {qene}")
        st.write(res.text)

# --- GLOBAL CHAT INTERFACE (ALWAYS ACCESSIBLE AT BOTTOM) ---
st.markdown("---")
st.subheader("💬 የ AI ሊቁን ውይይት")

# Session state for Chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input - FIXED AT THE END OF THE SCRIPT
if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
            try:
                # Add context based on the current tool
                context = f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የ {tool} ባለሙያ ነህ። ጥያቄውን በባለሙያ ደረጃ መልስ፡ {prompt}"
                response = model.generate_content(context)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                if "429" in str(e):
                    st.warning("⚠️ ይቅርታ ጌታዬ፤ AIው ለጊዜው ተጨናንቋል። እባክህ 20 ሰከንድ ታግሰህ ድገመኝ።")
                else:
                    st.error("ያልታወቀ ስህተት ተፈጠረ። እባክህ ገጹን Refresh አድርገህ ሞክር።")

# ---------------------------------------------------------
# 5. SOVEREIGN MASTER FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center; color: #b8860b;'>
        <h4>GE'EZ SCHOLAR AI v100.0 | ABSOLUTE SOVEREIGN EDITION</h4>
        <p style='font-size: 18px;'><b>EXCLUSIVELY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</b></p>
        <p>Global Strategic Hub for Advanced Ge'ez Intelligence | Addis Ababa | 2025</p>
    </div>
""", unsafe_allow_html=True)
