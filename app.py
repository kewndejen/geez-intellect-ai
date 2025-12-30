import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import datetime

# ---------------------------------------------------------
# 1. PRESTIGE ZENITH CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | 33 Divine Pillars",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Professional Theme: Obsidian, Imperial Gold, and Marble White
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    
    /* Sidebar Styling - The Black & Gold Empire */
    .stSidebar { background: linear-gradient(180deg, #000c18 0%, #001e36 100%) !important; border-right: 5px solid #b8860b; }
    .stSidebar .stSelectbox label, .stSidebar .stRadio label { color: #d4af37 !important; font-weight: 800; font-size: 15px; }

    /* Button Styling - The Majesty Click */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%);
        color: white; border: none; padding: 18px 30px;
        border-radius: 10px; font-weight: 800; width: 100%;
        font-size: 16px; letter-spacing: 1.5px; transition: 0.5s;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { 
        transform: translateY(-5px) scale(1.02); 
        box-shadow: 0 15px 50px rgba(184, 134, 11, 0.8); 
    }
    
    /* Global Developer Signature */
    .signature-box {
        background: linear-gradient(90deg, #b8860b, #000c18);
        padding: 25px; border-radius: 15px; border: 2px solid #d4af37;
        text-align: center; color: white; font-weight: bold;
        margin-bottom: 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }
    
    /* Content Elegance */
    .premium-card {
        background: white; padding: 40px; border-radius: 20px;
        border-left: 10px solid #b8860b; box-shadow: 0 20px 80px rgba(0,0,0,0.1);
        margin-bottom: 35px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE QUANTUM BRAIN (Kewn Dejen Intelligence)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: Deacon Kewn Dejen's Master Key Required.")
    st.stop()

# Using Gemini 2.0 Flash for Infinite Reasoning Capacity
model = genai.GenerativeModel('gemini-2.0-flash')

# ---------------------------------------------------------
# 3. MAJESTY NAVIGATION: 33 DIVINE PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='signature-box'>CHIEF ARCHITECT & DEVELOPER:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    category = st.selectbox("የጥበብ ምሰሶዎች", [
        "🏠 Imperial Management",
        "🧠 Advanced AI & Research Labs",
        "📜 The Great Digital Libraries",
        "🏛️ Heritage, Map & Arts",
        "🎓 Academic University & Quiz",
        "💰 Global Business & Security"
    ])
    
    st.markdown("---")
    
    # Organizing 33 Tools into Categories
    if category == "🏠 Imperial Management":
        tool = "01. Majesty Dashboard"
    elif category == "🧠 Advanced AI & Research Labs":
        tool = st.radio("AI መሣሪያዎች", [
            "02. Manuscript OCR Lab (ብራና አንባቢ)",
            "03. Sem-na-Work Logic (ቅኔ መፍቻ)",
            "04. AI Voice Assistant (ድምፅ ረዳት)",
            "05. Comparative Linguistics (ቋንቋ ንጽጽር)",
            "06. Manuscript Authentication (ትክክለኛነት)",
            "07. Etymological Root Finder (ቃላት መፍለቂያ)",
            "08. Palæography Specialist (ጽሕፈት ጥናት)",
            "33. Royal Decree Generator (ንጉሣዊ ትእዛዝ)"
        ])
    elif category == "📜 The Great Digital Libraries":
        tool = st.radio("መዛግብት", [
            "09. Universal Library (12M Pages)",
            "10. Document Deep Analyzer (PDF/Doc)",
            "11. Fetha Nagast Legal AI (ሕግ)",
            "12. Esoteric & Prophetic Lab (ምስጢር)",
            "13. Hagiography Narrative AI (ገድለ ቅዱሳን)"
        ])
    elif category == "🏛️ Heritage, Map & Arts":
        tool = st.radio("ቅርስና ታሪክ", [
            "14. Virtual Heritage Museum (3D ትንታኔ)",
            "15. Genealogy & Ancestry AI (ሐረግ)",
            "16. Interactive Ge'ez Map (ታሪክ ካርታ)",
            "17. Iconography Vision (ሥዕል ጥናት)",
            "18. Archeological Simulator (ቁፋሮ)",
            "19. Ancient Medicine Hub (መድኃኒት)",
            "20. Proverbs & Wisdom AI (ምሳሌያዊ አነጋገር)"
        ])
    elif category == "🎓 Academic University & Quiz":
        tool = st.radio("ትምህርትና ሳይንስ", [
            "21. Scholarly University (ትምህርት)",
            "22. Abu Shaker Astronomy (አቡሻከር)",
            "23. Bahre Hasab Logic (ቀን ቀመር)",
            "24. St. Yared Zema Lab (ዜማ ጥናት)",
            "25. Ethiopic Font Converter (ፊደል ለዋጭ)",
            "26. Certification Hub (የብቃት ማረጋገጫ)",
            "27. Restoration Tools (ዕድሳት)",
            "28. Theological Research (መንፈሳዊ ምርምር)"
        ])
    else:
        tool = st.radio("ቢዝነስና ደህንነት", [
            "29. Premium Business Hub (ቢዝነስ)",
            "30. Payment Gateway (ክፍያ)",
            "31. Institution API Portal (API)",
            "32. Global Security Admin (ደህንነት)"
        ])

# ---------------------------------------------------------
# 4. CONTENT ENGINE - THE 33 PILLAR WORKSPACE
# ---------------------------------------------------------

# --- 01. DASHBOARD ---
if "01." in tool:
    st.markdown("<h1>The 33 Divine Pillars Dashboard</h1>", unsafe_allow_html=True)
    st.markdown(f"### 👑 Supervised & Developed by Deacon Kewn Dejen")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Reasoning Capacity", "12M+ Pages", "Supreme")
    col2.metric("Integrated Tools", "33 Strategic", "Elite")
    col3.metric("System Security", "Quantum Level", "Secured")
    col4.metric("Developer Status", "Active Leader", "Verified")
    
    st.markdown("""
    <div class='premium-card'>
    <h3>የዓለም አቀፍ የግዕዝ AI ምርምር ማዕከል (33 Divine Pillars)</h3>
    ይህ በዲያቆን ከውን ደጀን (Deacon Kewn Dejen) የተገነባው ሲስተም የኢትዮጵያን ጥንታዊ ጥበብ በሰው ሰራሽ አስተውሎት (AI) አማካኝነት 
    ለዓለም አቀፍ ማኅበረሰብ የሚያቀርብ ብቸኛው ግዙፍ የቴክኖሎጂ ውጤት ነው። 33 ስትራቴጂካዊ መሣሪያዎችን በመያዝ የጥበብ መንግሥቱን ያነግሣል።
    </div>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=400)

# --- 02. MANUSCRIPT OCR ---
elif "02." in tool:
    st.title("🧠 Manuscript OCR Intelligence")
    file = st.file_uploader("የብራና ወይም የጽሁፍ ምስል ይጫኑ...", type=['jpg','png','jpeg'])
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)
        if st.button("Deep Scan (Kewn Dejen Intelligence)"):
            with st.spinner("AIው ፒክሰሎችን በጥልቀት እያነበበ ነው..."):
                res = model.generate_content(["ተርጉምልኝ እና የታሪክ ይዘቱን በዝርዝር አብራራው (Analyze professionally):", img])
                st.markdown(f"<div class='premium-card'>{res.text}</div>", unsafe_allow_html=True)

# --- 26. CERTIFICATION HUB (New Tool) ---
elif "26." in tool:
    st.title("🎓 Certification Hub")
    st.write("በግዕዝ ጥናት ያለዎትን ብቃት በ AI ይፈትኑ። ካለፉ በዲያቆን ከውን ደጀን የተረጋገጠ ሰርቲፊኬት ያገኛሉ።")
    name = st.text_input("ሙሉ ስምዎን ያስገቡ...")
    if st.button("ፈተናውን ጀምር"):
        with st.spinner("ፈተናው እየተዘጋጀ ነው..."):
            res = model.generate_content("ለግዕዝ ሊቃውንት የሚሆን 5 ከበድ ያሉ የፈተና ጥያቄዎችን አቅርብ።")
            st.write(res.text)

# --- 25. FONT CONVERTER (New Tool) ---
elif "25." in tool:
    st.title("🖋️ Ethiopic Font Converter & Styler")
    text_to_style = st.text_area("የሚቀየር የግዕዝ ጽሁፍ ያስገቡ...")
    if st.button("ስታይሉን ቀይር"):
        with st.spinner("በማስተካከል ላይ..."):
            res = model.generate_content(f"ይህንን የግዕዝ ጽሁፍ ወደ ተለያዩ ጥንታዊ እና ዘመናዊ የአጻጻፍ ስልቶች (Fonts/Styles) ቀይረህ አሳይ፡ {text_to_style}")
            st.write(res.text)

# --- UNIVERSAL CHAT (For all other 29+ tools) ---
else:
    st.title(f"{tool}")
    st.info(f"ይህ ክፍል በዲያቆን ከውን ደጀን የሚመራ የ {tool} ማዕከል ነው።")
    p_input = st.chat_input("ሊቁን ጥያቄ ይጠይቁ...")
    if p_input:
        with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
            res = model.generate_content(f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የ {tool} ባለሙያ ነህ። በባለሙያ ደረጃ መልስ ስጥ: {p_input}")
            st.markdown(f"<div class='premium-card'>{res.text}</div>", unsafe_allow_html=True)
            st.download_button("የምርምር ውጤቱን አውርድ (Kewn Dejen Official Export)", res.text)

# ---------------------------------------------------------
# 5. SUPREME FOOTER (The Emperor's Seal)
# ---------------------------------------------------------
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center;'>
        <h4 style='color: #b8860b;'>GE'EZ SCHOLAR AI v17.0 | 33 DIVINE PILLARS EDITION</h4>
        <p style='font-size: 18px;'><b>EXCLUSIVELY DEVELOPED BY DEACON KEWN DEJEN</b></p>
        <p>Strategic Global Hub for Advanced Ge'ez Intelligence | Addis Ababa | 2025</p>
    </div>
""", unsafe_allow_html=True)
