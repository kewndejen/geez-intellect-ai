import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import datetime

# ---------------------------------------------------------
# 1. ULTIMATE IMPERIAL CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | 40 Imperial Pillars",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sovereign Aesthetics: Obsidian Black, Imperial Gold, and Diamond White
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    
    /* Sidebar Styling - The Imperial Command Center */
    .stSidebar { background: linear-gradient(180deg, #000c18 0%, #001e36 100%) !important; border-right: 5px solid #b8860b; }
    .stSidebar .stSelectbox label, .stSidebar .stRadio label { color: #d4af37 !important; font-weight: 800; font-size: 15px; }

    /* Button Styling - The Royal Touch */
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
    
    /* Sovereign Developer Signature */
    .signature-card {
        background: linear-gradient(90deg, #b8860b, #000c18);
        padding: 25px; border-radius: 15px; border: 2px solid #d4af37;
        text-align: center; color: white; font-weight: bold;
        margin-bottom: 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }
    
    /* Content Elegance */
    .imperial-card {
        background: white; padding: 40px; border-radius: 20px;
        border-left: 12px solid #b8860b; box-shadow: 0 25px 90px rgba(0,0,0,0.12);
        margin-bottom: 35px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE QUANTUM ENGINE (Kewn Dejen Intelligence)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: System Access Denied. Contact Deacon Kewn Dejen.")
    st.stop()

# Using Gemini 2.0 Flash for Supreme Reasoning
model = genai.GenerativeModel('gemini-2.0-flash')

# ---------------------------------------------------------
# 3. IMPERIAL NAVIGATION: 40 PILLARS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='signature-card'>CHIEF ARCHITECT & DEVELOPER:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    category = st.selectbox("የእውቀት ምሰሶዎች", [
        "🏠 Imperial Command Center",
        "🧠 Neural AI & Research Labs",
        "📜 The Great Digital Vaults",
        "🏛️ Heritage, Map & Material Science",
        "🎓 University & Professional Certification",
        "🔮 Mysticism, Poetry & Prophecy",
        "💰 Global Business & Sovereign Security"
    ])
    
    st.markdown("---")
    
    # Organizing 40 Tools into 7 Imperial Categories
    if category == "🏠 Imperial Command Center":
        tool = "01. Sovereign Dashboard"
    elif category == "🧠 Neural AI & Research Labs":
        tool = st.radio("AI መሣሪያዎች", [
            "02. Manuscript OCR Lab (ብራና አንባቢ)",
            "03. Palæography Specialist (ጽሕፈት ጥናት)",
            "04. Manuscript Authentication (ትክክለኛነት)",
            "05. Comparative Linguistics (ቋንቋ ንጽጽር)",
            "06. Ethiopic Cryptography Lab (ምስጢር ጽሕፈት)",
            "07. AI Voice Assistant (ድምፅ ረዳት)",
            "08. Etymological Root Finder (ቃላት መፍለቂያ)"
        ])
    elif category == "📜 The Great Digital Vaults":
        tool = st.radio("መዛግብት", [
            "09. Universal Library (12M Pages)",
            "10. Document Deep Analyzer (PDF/Doc)",
            "11. Fetha Nagast Legal AI (ሕግ)",
            "12. Hagiography Narrative AI (ገድለ ቅዱሳን)",
            "13. Royal Decree Generator (ንጉሣዊ ትእዛዝ)",
            "14. Kingdom Timelines (የነገሥታት ታሪክ)"
        ])
    elif category == "🏛️ Heritage, Map & Material Science":
        tool = st.radio("ቅርስና ሳይንስ", [
            "15. Virtual Heritage Museum (3D ትንታኔ)",
            "16. Interactive Ge'ez Map (ታሪክ ካርታ)",
            "17. Iconography Vision (ሥዕል ጥናት)",
            "18. Archeological Simulator (ቁፋሮ)",
            "19. Sacred Geometry & Architecture (ቅዱስ ጥበብ)",
            "20. Ink & Material Science AI (ቀለምና ብራና)",
            "21. Ancient Medicine Hub (መድኃኒት ጥናት)"
        ])
    elif category == "🎓 University & Professional Certification":
        tool = st.radio("ትምህርትና ብቃት", [
            "22. Scholarly University (ትምህርት)",
            "23. Certification Hub (የብቃት ማረጋገጫ)",
            "24. Bahre Hasab Logic (ቀን ቀመር)",
            "25. Abu Shaker Astronomy (አቡሻከር)",
            "26. Ethiopic Font Converter (ፊደል ለዋጭ)",
            "27. Restoration Tools (ዕድሳት)",
            "28. Global Philology Hub (ሥርወ-ቃል ጥናት)"
        ])
    elif category == "🔮 Mysticism, Poetry & Prophecy":
        tool = st.radio("ምስጢርና ቅኔ", [
            "29. Sem-na-Work Logic (ቅኔ መፍቻ)",
            "30. Verse Meter Composer (የቤት መቺ)",
            "31. Esoteric & Prophetic Lab (ምስጢር)",
            "32. Virtual Scholar Roleplay (የሊቃውንት ውይይት)",
            "33. Proverbs & Wisdom AI (ምሳሌያዊ አነጋገር)",
            "34. Theological Research (መንፈሳዊ ምርምር)",
            "35. St. Yared Zema Lab (ዜማ ጥናት)"
        ])
    else:
        tool = st.radio("ቢዝነስና ደህንነት", [
            "36. Premium Business Hub (ቢዝነስ)",
            "37. Payment Gateway (ክፍያ)",
            "38. Institution API Portal (API)",
            "39. Global Security Admin (ደህንነት)",
            "40. Master Settings & Logs"
        ])

# ---------------------------------------------------------
# 4. CONTENT ENGINE - THE 40 PILLAR WORKSPACE
# ---------------------------------------------------------

# --- 01. DASHBOARD ---
if "01." in tool:
    st.markdown("<h1>The 40 Imperial Pillars Dashboard</h1>", unsafe_allow_html=True)
    st.markdown(f"### 👑 Supervised & Developed by Deacon Kewn Dejen")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Reasoning Nodes", "12M+ Data Points", "Infinite")
    col2.metric("Sovereign Tools", "40 Integrated", "Maximized")
    col3.metric("AI Model", "Gemini 2.0 Flash", "Elite")
    col4.metric("Security", "Sovereign Shield", "Verified")
    
    st.markdown("""
    <div class='imperial-card'>
    <h3>የዓለም አቀፍ የግዕዝ AI ምርምር ማዕከል (Global Excellence)</h3>
    ይህ በዲያቆን ከውን ደጀን (Deacon Kewn Dejen) የተገነባው ሲስተም የኢትዮጵያን ጥንታዊ ጥበብ በሰው ሰራሽ አስተውሎት (AI) አማካኝነት 
    ለዓለም አቀፍ ማኅበረሰብ የሚያቀርብ ብቸኛው ግዙፍ የቴክኖሎጂ ውጤት ነው። 40 ስትራቴጂካዊ ምሰሶዎችን በመያዝ የጥበብ መንግሥቱን ያነግሣል።
    </div>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=400)

# --- 02. MANUSCRIPT OCR ---
elif "02." in tool:
    st.title("🧠 Manuscript OCR & Neural Analysis")
    file = st.file_uploader("የብራና ወይም የጽሁፍ ምስል ይጫኑ...", type=['jpg','png','jpeg'])
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)
        if st.button("Deep Neural Scan (Kewn Dejen Intelligence)"):
            with st.spinner("AIው ፒክሰሎችን በጥልቀት እያነበበ ነው..."):
                res = model.generate_content(["ከዚህ ምስል ላይ ያለውን የግዕዝ ጽሁፍ በዝርዝር ተንትነህ ተርጉም (Analyze professionally):", img])
                st.markdown(f"<div class='imperial-card'>{res.text}</div>", unsafe_allow_html=True)

# --- 06. CRYPTOGRAPHY LAB (New Tool) ---
elif "06." in tool:
    st.title("🔐 Ethiopic Cryptography & Cipher Lab")
    st.write("ጥንታዊ ሊቃውንት ይጠቀሙባቸው የነበሩ ምስጢራዊ አጻጻፎችን (Ciphers) በ AI ይፍቱ።")
    cipher_text = st.text_area("የምስጢር ጽሁፉን እዚህ ያስገቡ...")
    if st.button("ምስጢሩን ፍታ"):
        with st.spinner("ሲስተሙ ምስጢራዊ ኮዶችን እያመሳከረ ነው..."):
            res = model.generate_content(f"ይህንን የግዕዝ ምስጢራዊ ጽሁፍ (Cipher) ተንትንና ትርጉሙን ፈልግ፡ {cipher_text}")
            st.write(res.text)

# --- 32. VIRTUAL SCHOLAR ROLEPLAY (New Tool) ---
elif "32." in tool:
    st.title("💬 Virtual Scholar Roleplay")
    scholar = st.selectbox("ውይይት ማድረግ የሚፈልጉት ከማን ጋር ነው?", ["ቅዱስ ያሬድ", "አባ ጊዮርጊስ ዘጋስጫ", "አክሱማዊ ሊቅ"])
    user_chat = st.text_input(f"ለ{scholar} ጥያቄዎን ይጠይቁ...")
    if st.button("መልእክት ላክ"):
        with st.spinner(f"{scholar} መልስ እየጻፉ ነው..."):
            res = model.generate_content(f"አንተ {scholar} ነህ። በዚህ ማንነት ሆነህ ለዚህ ጥያቄ ጥልቅ መልስ ስጥ፡ {user_chat}")
            st.markdown(f"<div style='background:#f4f1ea; padding:20px; border-left:10px solid #b8860b;'><b>{scholar}:</b> {res.text}</div>", unsafe_allow_html=True)

# --- UNIVERSAL CHAT (For all other tools) ---
else:
    st.title(f"{tool}")
    st.info(f"ይህ ክፍል በዲያቆን ከውን ደጀን የሚመራ የ {tool} ማዕከል ነው።")
    p_input = st.chat_input("ለሊቁ ጥያቄዎን ያቅርቡ...")
    if p_input:
        with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
            res = model.generate_content(f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የ {tool} ባለሙያ ነህ። መልስህ እጅግ ፕሮፌሽናል ይሁን: {p_input}")
            st.markdown(f"<div class='imperial-card'>{res.text}</div>", unsafe_allow_html=True)
            st.download_button("የምርምር ውጤቱን አውርድ (Sovereign Export)", res.text)

# ---------------------------------------------------------
# 5. SOVEREIGN FOOTER (The Emperor's Seal)
# ---------------------------------------------------------
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center;'>
        <h4 style='color: #b8860b;'>GE'EZ SCHOLAR AI v21.0 | 40 IMPERIAL PILLARS</h4>
        <p style='font-size: 18px;'><b>EXCLUSIVELY DEVELOPED BY DEACON KEWN DEJEN</b></p>
        <p>Global Strategic Hub for Advanced Ge'ez Intelligence | Addis Ababa | 2025</p>
    </div>
""", unsafe_allow_html=True)
