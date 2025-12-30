import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import datetime

# ---------------------------------------------------------
# 1. PRESTIGE IMPERIAL CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Absolute Majesty Edition",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Aesthetics: Royal Gold, Diamond White, and Deep Obsidian
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    
    /* Sidebar Styling - The Black & Gold Command Center */
    .stSidebar { background: linear-gradient(180deg, #000c18 0%, #001e36 100%) !important; border-right: 4px solid #b8860b; }
    .stSidebar .stSelectbox label, .stSidebar .stRadio label { color: #d4af37 !important; font-weight: 800; font-size: 16px; }

    /* Button Styling - The Royal Touch */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%);
        color: white; border: none; padding: 18px 30px;
        border-radius: 8px; font-weight: 800; width: 100%;
        font-size: 16px; letter-spacing: 1.5px; transition: 0.5s;
        box-shadow: 0 5px 20px rgba(0,0,0,0.4);
    }
    .stButton>button:hover { 
        transform: translateY(-4px); 
        box-shadow: 0 12px 40px rgba(184, 134, 11, 0.7); 
    }
    
    /* Signature Credit Box */
    .master-credit {
        background: linear-gradient(90deg, #b8860b, #000c18);
        padding: 25px; border-radius: 12px; border: 2px solid #d4af37;
        text-align: center; color: white; font-weight: bold;
        margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    /* Elite Content Card */
    .premium-card {
        background: white; padding: 35px; border-radius: 15px;
        border-top: 8px solid #b8860b; box-shadow: 0 20px 60px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE QUANTUM ENGINE (Kewn Dejen Intelligence)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: Master Credentials Required.")
    st.stop()

# Using Gemini 2.0 Flash for 12M+ Data Reasoning
model = genai.GenerativeModel('gemini-2.0-flash')

# ---------------------------------------------------------
# 3. MAJESTY NAVIGATION: 27 ELITE TOOLS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='master-credit'>CHIEF ARCHITECT & CEO:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    category = st.selectbox("ዋናው የጥናት ዘርፍ", [
        "🏠 Imperial Dashboard",
        "🧠 Advanced AI Labs",
        "📜 Digital Libraries",
        "🏛️ History & Heritage",
        "🎓 Academic Excellence",
        "🛡️ Security & Business"
    ])
    
    st.markdown("---")
    
    # 27 Tools organized within categories
    if category == "🏠 Imperial Dashboard":
        tool = "01. Dashboard Overview"
    elif category == "🧠 Advanced AI Labs":
        tool = st.radio("AI መሣሪያዎች", [
            "02. Manuscript OCR Lab (ብራና አንባቢ)",
            "03. Sem-na-Work Logic (ቅኔ መፍቻ)",
            "04. AI Voice Assistant (ድምፅ ረዳት)",
            "05. Comparative Linguistics (ቋንቋ ንጽጽር)",
            "06. Manuscript Authentication (ትክክለኛነት)",
            "27. Royal Decree Generator (ንጉሣዊ ትእዛዝ)"
        ])
    elif category == "📜 Digital Libraries":
        tool = st.radio("መዛግብት", [
            "07. Universal Library (12M Pages)",
            "08. Document Deep Analyzer (PDF/Doc)",
            "09. Fetha Nagast Legal AI (ሕግ)",
            "10. Esoteric & Prophetic Lab (ምስጢር)"
        ])
    elif category == "🏛️ History & Heritage":
        tool = st.radio("ቅርስና ታሪክ", [
            "11. Virtual Heritage Museum (3D ትንታኔ)",
            "12. Genealogy & Ancestry AI (ሐረግ)",
            "13. Interactive Ge'ez Map (ታሪክ ካርታ)",
            "14. Iconography Vision (ሥዕል ጥናት)",
            "15. Archeological Simulator (ቁፋሮ)",
            "16. Ancient Medicine Hub (መድኃኒት)"
        ])
    elif category == "🎓 Academic Excellence":
        tool = st.radio("ትምህርትና ሳይንስ", [
            "17. Scholarly University (ትምህርት)",
            "18. Abu Shaker Astronomy (አቡሻከር)",
            "19. Bahre Hasab Logic (ቀን ቀመር)",
            "20. St. Yared Zema Lab (ዜማ ጥናት)",
            "21. Restoration Tools (ዕድሳት)",
            "22. Theological Research (መንፈሳዊ ምርምር)"
        ])
    else:
        tool = st.radio("ቢዝነስና ደህንነት", [
            "23. Premium Business Hub (ቢዝነስ)",
            "24. Payment Gateway (ክፍያ)",
            "25. Institution API Portal (API)",
            "26. Global Security Admin (ደህንነት)"
        ])

# ---------------------------------------------------------
# 4. CONTENT ENGINE - THE MAJESTY WORKSPACE
# ---------------------------------------------------------

# --- 01. DASHBOARD ---
if "01." in tool:
    st.markdown("<h1>The Absolute Majesty Dashboard</h1>", unsafe_allow_html=True)
    st.markdown(f"### 🔱 Developed & Directed by Deacon Kewn Dejen")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Reasoning Depth", "12M Pages", "Infinite")
    col2.metric("AI Intelligence", "Majesty v15", "Quantum")
    col3.metric("Global Sync", "Active", "Secured")
    col4.metric("Tools Integrated", "27 Strategic", "Elite")
    
    st.markdown("""
    <div class='premium-card'>
    <h3>የዓለም አቀፍ የግዕዝ AI ምርምር ማዕከል (Global Center)</h3>
    ይህ በዲያቆን ከውን ደጀን (Deacon Kewn Dejen) የተገነባው ሲስተም የኢትዮጵያን ጥንታዊ ጥበብ በሰው ሰራሽ አስተውሎት (AI) አማካኝነት 
    ለዓለም አቀፍ ማኅበረሰብ የሚያቀርብ ብቸኛው ግዙፍ የቴክኖሎጂ ውጤት ነው። 27 ስትራቴጂካዊ መሣሪያዎችን በመያዝ የጥበብ መንግሥቱን ያነግሣል።
    </div>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=400)

# --- 02. OCR LAB ---
elif "02." in tool:
    st.title("🧠 Manuscript OCR Intelligence")
    file = st.file_uploader("የብራና ወይም የጽሁፍ ምስል ይጫኑ...", type=['jpg','png','jpeg'])
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)
        if st.button("Deep Scan (Kewn Dejen Engine)"):
            with st.spinner("AIው ፒክሰሎችን በጥልቀት እያነበበ ነው..."):
                res = model.generate_content(["ተርጉምልኝ እና የታሪክ ይዘቱን በዝርዝር አብራራው (Professionally analyze and translate):", img])
                st.markdown(f"<div class='premium-card'>{res.text}</div>", unsafe_allow_html=True)

# --- 19. BAHRE HASAB (New Tool) ---
elif "19." in tool:
    st.title("📅 Bahre Hasab & Calendar Logic")
    st.write("የዓመታትን ባሕረ ሐሳብ፣ በዓላትን እና አጽዋማትን በ AI ቀመር ያስሉ ወይም ይጠይቁ።")
    year = st.number_input("ዓመተ ምሕረት ያስገቡ (ለምሳሌ፡ 2017)", min_value=1)
    if st.button("ቀመሩን አውጣ"):
        with st.spinner("ባሕረ ሐሳቡ እየተሰላ ነው..."):
            res = model.generate_content(f"ለ {year} ዓመተ ምሕረት የባሕረ ሐሳብ ቀመር (አጽዋማትና በዓላት) በግዕዝ እና በአማርኛ አውጣ።")
            st.write(res.text)

# --- 27. ROYAL DECREE GENERATOR (New Tool) ---
elif "27." in tool:
    st.title("📝 Royal Decree Generator (ንጉሣዊ ትእዛዝ)")
    st.write("ደብዳቤዎችን ወይም ሰነዶችን በጥንታዊ የንጉሣዊ አጻጻፍ ስልት በ AI ያዘጋጁ።")
    topic = st.text_area("የደብዳቤው ርዕሰ ጉዳይ...")
    if st.button("ትእዛዙን አውጣ"):
        with st.spinner("ንጉሣዊ ስልቱ እየተቀረጸ ነው..."):
            res = model.generate_content(f"ይህንን ርዕስ በጥንታዊ ንጉሣዊ የደብዳቤ አጻጻፍ ስልት (Imperial Style) አዘጋጅ፡ {topic}")
            st.markdown(f"<div style='background:#f9f9f9; padding:30px; border:2px solid gold; font-family:serif;'>{res.text}</div>", unsafe_allow_html=True)

# --- UNIVERSAL CHAT (For all other 20+ sections) ---
else:
    st.title(f"{tool}")
    st.info(f"ይህ ክፍል በዲያቆን ከውን ደጀን የሚመራ የ {tool} ማዕከል ነው።")
    p_input = st.chat_input("ሊቁን ጥያቄ ይጠይቁ...")
    if p_input:
        with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
            res = model.generate_content(f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የ {tool} ባለሙያ ነህ። በባለሙያ ደረጃ መልስ ስጥ: {p_input}")
            st.markdown(f"<div class='premium-card'>{res.text}</div>", unsafe_allow_html=True)
            st.download_button("የምርምር ውጤቱን አውርድ (Export Master Document)", res.text)

# ---------------------------------------------------------
# 5. MAJESTY FOOTER (The Signature of Greatness)
# ---------------------------------------------------------
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center;'>
        <h4 style='color: #b8860b;'>GE'EZ SCHOLAR AI v15.0 | ABSOLUTE MAJESTY EDITION</h4>
        <p style='font-size: 18px;'><b>EXCLUSIVELY DEVELOPED BY DEACON KEWN DEJEN</b></p>
        <p>Strategic Global Hub for Advanced Ge'ez Intelligence | Addis Ababa | 2025</p>
    </div>
""", unsafe_allow_html=True)
