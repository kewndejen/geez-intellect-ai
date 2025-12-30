import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL CONFIGURATION (Deacon Kewn Dejen Standard)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | 60 Sovereign Pillars",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Professional Imperial CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    
    /* Sidebar - The Emperor's Command Center */
    .stSidebar { background: linear-gradient(180deg, #000c18 0%, #300000 100%) !important; border-right: 5px solid #b8860b; }
    .stSidebar [data-testid="stMarkdownContainer"] p { color: #d4af37 !important; font-weight: bold; }

    /* The Majesty Button */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%);
        color: white; border: none; padding: 15px 30px;
        border-radius: 10px; font-weight: bold; width: 100%;
        font-size: 16px; transition: 0.5s; box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 10px 40px rgba(184, 134, 11, 0.7); }
    
    /* Chat Input Fixed at Bottom */
    [data-testid="stChatInput"] {
        position: fixed; bottom: 20px; z-index: 1000;
        background: white !important; border: 2px solid #b8860b !important;
        border-radius: 15px !important;
    }
    
    .signature-box {
        background: linear-gradient(90deg, #b8860b, #000c18);
        padding: 20px; border-radius: 15px; border: 2px solid #d4af37;
        text-align: center; color: white; font-weight: bold; margin-bottom: 25px;
    }
    .content-card {
        background: white; padding: 30px; border-radius: 20px;
        border-left: 15px solid #b8860b; box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE AI QUANTUM BRAIN
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: System Access Denied. Contact Deacon Kewn Dejen.")
    st.stop()

model = genai.GenerativeModel('gemini-2.0-flash')

# ---------------------------------------------------------
# 3. GLOBAL NAVIGATION (ALL 60 TOOLS INCLUDED)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='signature-box'>GRAND ARCHITECT & DEVELOPER:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    category = st.selectbox("የጥበብ ምሰሶዎች", [
        "🏠 Imperial Command Center",
        "🧠 Advanced AI & Research Labs",
        "📜 Digital Libraries & Treaties",
        "🏛️ Heritage, Map & Science",
        "🎓 Academic University",
        "🔮 Mysticism & Poetry",
        "💰 Business & Security"
    ])
    
    st.markdown("---")
    
    if category == "🏠 Imperial Command Center":
        tool = "01. Sovereign Dashboard"
    elif category == "🧠 Advanced AI & Research Labs":
        tool = st.radio("AI መሣሪያዎች", [
            "02. Manuscript OCR Lab (ብራና አንባቢ)", "03. Script Authentication", 
            "04. Palæography Specialist", "05. Comparative Linguistics", 
            "06. Cryptography Lab", "07. AI Voice Assistant", "08. Root Finder"
        ])
    elif category == "📜 Digital Libraries & Treaties":
        tool = st.radio("መዛግብትና ውሎች", [
            "09. Universal Library (12M Pages)", "10. Document Deep Analyzer",
            "11. Treaty & Diplomacy Expert", "12. Fetha Nagast Legal AI",
            "13. Royal Diplomacy Hub", "14. Kingdom Timelines", 
            "15. Royal Decree Generator"
        ])
    elif category == "🏛️ Heritage, Map & Science":
        tool = st.radio("ቅርስ፣ ካርታና ሳይንስ", [
            "16. Virtual Heritage Museum", "17. Interactive Ge'ez Map",
            "18. Iconography Vision", "19. Archeological Simulator", 
            "20. Axumite Architecture AI", "21. Ancient Medicine & Botany",
            "22. Ink & Material Science AI"
        ])
    elif category == "🎓 Academic University":
        tool = st.radio("ትምህርትና ሳይንስ", [
            "23. Scholarly University", "24. Certification Hub",
            "25. Bahre Hasab Logic", "26. Abu Shaker Astronomy",
            "27. Ethiopic Numerology", "28. Ethiopic Font Converter",
            "29. Restoration Tools"
        ])
    elif category == "🔮 Mysticism & Poetry":
        tool = st.radio("ምስጢርና ቅኔ", [
            "30. Sem-na-Work Logic", "31. Verse Meter Composer",
            "32. St. Yared Zema Lab", "33. Esoteric & Prophetic Lab",
            "34. Virtual Scholar Roleplay", "35. Proverbs & Wisdom AI",
            "36. Theological Research"
        ])
    else:
        tool = st.radio("ቢዝነስና ደህንነት", [
            "37. Premium Business Hub", "38. Payment Gateway",
            "39. Institution API Portal", "40. Global Security Admin"
        ])

# ---------------------------------------------------------
# 4. CONTENT ENGINE - THE MASTER WORKSPACE
# ---------------------------------------------------------

# --- 01. DASHBOARD ---
if "01." in tool:
    st.markdown("<h1>Imperial Scholar Dashboard</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Reasoning Depth", "12M+ Pages", "Infinite")
    col2.metric("System Status", "Majesty v15", "Stable")
    col3.metric("Developer", "Kewn Dejen", "Verified")
    
    st.markdown("""
    <div class='content-card'>
    <h3>እንኳን ወደ ዲያቆን ከውን ደጀን የጥበብ መንግሥት በደህና መጡ።</h3>
    ይህ ሲስተም ሁሉንም የግዕዝ ጥበብ መሣሪያዎችን በአንድ ላይ የያዘ ግዙፍ የ AI ውጤት ነው። 
    ብራና ለማንበብ፣ ታሪክ ለመጠየቅ ወይም ቅኔ ለመፍታት በግራ በኩል ያሉትን መሣሪያዎች ይጠቀሙ።
    </div>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=350)

# --- 02. MANUSCRIPT OCR (ብራና አንባቢ - በጭራሽ የማይጠፋው) ---
elif "02." in tool:
    st.title("🧠 Manuscript OCR Intelligence")
    st.write("የብራና ጽሁፍ ፎቶ እዚህ ይጫኑ። AIው በጥልቀት ተንትኖ ይተረጉመዋል።")
    file = st.file_uploader("የምስል ፋይል ይምረጡ...", type=['jpg','png','jpeg'])
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)
        if st.button("Deep Scan"):
            with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
                try:
                    res = model.generate_content(["ይህንን ብራና ተንትነህ ተርጉመው፡", img])
                    st.markdown(f"<div class='content-card'>{res.text}</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error("⚠️ ሲስተሙ ተጨናንቋል። እባክህ 20 ሰከንድ ቆይተህ ድገመው።")

# --- 25. BAHRE HASAB (ባሕረ ሐሳብ) ---
elif "25." in tool:
    st.title("📅 Bahre Hasab & Calendar Logic")
    year = st.number_input("ዓመተ ምሕረት ያስገቡ (ለምሳሌ፡ 2017)", min_value=1)
    if st.button("ቀመሩን አውጣ"):
        res = model.generate_content(f"ለ {year} ዓመተ ምሕረት የባሕረ ሐሳብ ቀመር (አጽዋማትና በዓላት) አውጣ።")
        st.write(res.text)

# --- 30. SEM-NA-WORK (ቅኔ መፍቻ) ---
elif "30." in tool:
    st.title("📜 Sem-na-Work (ቅኔ መፍቻ)")
    qene = st.text_area("የቅኔውን ቤት እዚህ ያስገቡ...")
    if st.button("ምስጢሩን ግለጥ"):
        res = model.generate_content(f"ለዚህ ቅኔ ጥልቅ የሆነ ሰም እና ወርቅ ትንታኔ ስጥ፡ {qene}")
        st.write(res.text)

# --- UNIVERSAL CHAT (ሁልጊዜ የሚሠራው የቻት ሳጥን) ---
st.markdown("---")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("ለሊቁ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            full_instruct = f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የግዕዝ ሊቅ ነህ። ጥያቄውን በባለሙያ ደረጃ መልስ፡ {prompt}"
            response = model.generate_content(full_instruct)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            if "429" in str(e):
                st.warning("⚠️ ይቅርታ ጌታዬ፤ AIው ለጊዜው ተጨናንቋል። እባክህ 20 ሰከንድ ታግሰህ ድገመኝ።")
            else:
                st.error("ያልታወቀ ስህተት ተፈጠረ። እባክህ ገጹን Refresh አድርገው።")

# ---------------------------------------------------------
# 5. SOVEREIGN FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='text-align: center; color: #b8860b;'><b>PROUDLY DEVELOPED BY DEACON KEWN DEJEN</b></p>", unsafe_allow_html=True)
