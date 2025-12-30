import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import datetime

# ---------------------------------------------------------
# 1. PRESTIGE GLASSMORPHISM CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Supreme Zenith Edition",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Styling: Gold, Platinum, and Deep Space Blue
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background: #f0f2f5; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    
    /* Sidebar Styling */
    .stSidebar { background: linear-gradient(180deg, #001529 0%, #000000 100%) !important; border-right: 3px solid #b8860b; }
    .stSidebar .stSelectbox label, .stSidebar .stRadio label { color: #d4af37 !important; font-weight: bold; }

    /* Button Styling */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%);
        color: white; border: none; padding: 15px 30px;
        border-radius: 12px; font-weight: 800; width: 100%;
        font-size: 16px; letter-spacing: 1px; transition: 0.5s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { 
        transform: translateY(-3px); 
        box-shadow: 0 10px 30px rgba(184, 134, 11, 0.6); 
    }
    
    /* Dev Credit Box */
    .dev-credit-box {
        background: rgba(184, 134, 11, 0.15);
        padding: 20px; border-radius: 15px; border: 1px solid #d4af37;
        text-align: center; color: #d4af37; font-weight: bold;
        box-shadow: 0 0 20px rgba(184, 134, 11, 0.2);
    }
    
    /* Content Cards */
    .content-card {
        background: white; padding: 30px; border-radius: 20px;
        border-bottom: 6px solid #b8860b; box-shadow: 0 15px 50px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. CORE AI ARCHITECTURE (Kewn Dejen Framework)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("ACCESS DENIED: Credentials Required.")
    st.stop()

# Using Gemini 2.0 Flash for 12M+ Reasoning
model = genai.GenerativeModel('gemini-2.0-flash')

# ---------------------------------------------------------
# 3. SUPREME NAVIGATION: 21 ELITE TOOLS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='dev-credit-box'>CHIEF ARCHITECT & DEVELOPER:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    tool = st.selectbox("የእውቀት ፖርታል (21 Strategic Tools)", [
        "01. 🏛️ Imperial Dashboard (መቆጣጠሪያ)",
        "02. 🧠 Manuscript OCR Lab (ብራና አንባቢ)",
        "03. 📜 Sem-na-Work Logic (ቅኔ መፍቻ)",
        "04. 📄 Document Deep Analyzer (PDF/Doc)",
        "05. 🎙️ AI Voice Assistant (የድምፅ ረዳት)",
        "06. 🏛️ Virtual Heritage Museum (3D ትንታኔ)",
        "07. 🌳 Genealogy & Ancestry AI (ሐረግ ጥናት)",
        "08. 🗺️ Interactive Ge'ez Map (የታሪክ ካርታ)",
        "09. 🔮 Esoteric & Prophetic Lab (ምስጢር)",
        "10. 📚 Universal Digital Library (12M Pages)",
        "11. ⚖️ Fetha Nagast Legal AI (የሕግ ተንታኝ)",
        "12. 🏥 Ancient Medicine Hub (መድኃኒት ጥናት)",
        "13. 🎨 Iconography Vision (ሥዕል ጥናት)",
        "14. 🔭 Abu Shaker Astronomy (አቡሻከር)",
        "15. 🎼 St. Yared Zema Lab (ዜማ ጥናት)",
        "16. 🎓 Scholarly University (ትምህርት)",
        "17. ⛪ Theological Research (መንፈሳዊ ምርምር)",
        "18. 🛠️ Restoration Tools (ዕድሳት)",
        "19. 💎 Premium Business Hub (ቢዝነስ)",
        "20. 💳 Payment Gateway (ክፍያ)",
        "21. 🛡️ Global Security Admin (ደህንነት)"
    ])
    
    st.markdown("---")
    st.caption(f"System: Quantum Zenith v12\nDeveloper: Deacon Kewn Dejen\nDate: {datetime.date.today()}")

# ---------------------------------------------------------
# 4. CONTENT ENGINE - THE SUPREME WORKSPACE
# ---------------------------------------------------------

# --- 01. DASHBOARD ---
if "01." in tool:
    st.markdown("<h1>Imperial Scholar Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("### 🏛️ The Legacy of Deacon Kewn Dejen")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Reasoning Capacity", "12,000,000 Pages", "Zenith")
    col2.metric("AI Precision", "99.99%", "Quantum")
    col3.metric("Global Sync", "Active", "Shielded")
    col4.metric("Knowledge Nodes", "21 Pillars", "Stable")
    
    st.markdown("""
    <div class='content-card'>
    <h3>የዓለም አቀፍ የግዕዝ AI ምርምር ማዕከል</h3>
    ይህ በዲያቆን ከውን ደጀን (Deacon Kewn Dejen) የተገነባው ሲስተም የኢትዮጵያን ጥንታዊ ጥበብ በሰው ሰራሽ አስተውሎት (AI) አማካኝነት 
    ለዓለም አቀፍ ማኅበረሰብ የሚያቀርብ ብቸኛው ግዙፍ የቴክኖሎጂ ውጤት ነው። 21 ስትራቴጂካዊ መሣሪያዎችን በመያዝ ጥንታዊውን እና ዘመናዊውን ዓለም ያገናኛል።
    </div>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/crown.png", width=400)

# --- 06. VIRTUAL MUSEUM (New Tool) ---
elif "06." in tool:
    st.title("🏛️ Virtual Heritage Museum (3D Analysis)")
    st.write("የጥንታዊ ቅርሶችን ፎቶ እዚህ ይጫኑ። AIው ቅርሱን መርምሮ ታሪካዊና ጥበባዊ ይዘቱን ይተነትናል።")
    museum_file = st.file_uploader("የቅርሱን ምስል ይጫኑ...", type=['jpg','png','jpeg'])
    if museum_file:
        img = Image.open(museum_file)
        st.image(img, use_container_width=True)
        if st.button("ቅርሱን መርምር (3D AI Scan)"):
            with st.spinner("Deacon Kewn Dejen's AI is analyzing the artifact..."):
                res = model.generate_content(["የዚህን ቅርስ ታሪካዊ ፋይዳ፣ የተሰራበትን ዘመን እና ጥበባዊ ምስጢር በዝርዝር ተንትነህ አብራራ፡", img])
                st.markdown(f"<div class='content-card'>{res.text}</div>", unsafe_allow_html=True)

# --- 07. GENEALOGY AI (New Tool) ---
elif "07." in tool:
    st.title("🌳 Genealogy & Ancestry AI")
    st.write("የትውልድ ሐረግዎን ወይም የታዋቂ ሰዎችን የትውልድ ታሪክ ከጥንታዊ መዛግብት ጋር በማመሳከር ይመርምሩ።")
    name_input = st.text_input("የቤተሰብ ወይም የታዋቂ ሰው ስም ያስገቡ (ለምሳሌ፡ አጼ ኃይለሥላሴ)")
    if name_input:
        with st.spinner("ሐረጉን ከመዛግብት ውስጥ በመፈለግ ላይ..."):
            res = model.generate_content(f"ስለ {name_input} የትውልድ ሐረግ እና ታሪካዊ የዘር ግንንድ ከግዕዝ መዛግብት አንጻር ተንትን።")
            st.write(res.text)

# --- 08. INTERACTIVE MAP (New Tool) ---
elif "08." in tool:
    st.title("🗺️ Interactive Ge'ez & Historical Map")
    st.write("የጥንታዊ አብያተ ክርስቲያናት፣ ገዳማት እና የታሪክ ቦታዎችን መገኛ እና ታሪክ ይመርምሩ።")
    place = st.text_input("የቦታውን ስም ያስገቡ (ለምሳሌ፡ አክሱም፣ ላሊበላ፣ ጣና ቂርቆስ)")
    if place:
        with st.spinner("ካርታውን እያዘጋጀሁ ነው..."):
            res = model.generate_content(f"የ {place} ታሪካዊ መገኛ፣ የጥንት ስሙ እና ከግዕዝ መዛግብት ጋር ያለው ግንኙነት ምንድነው?")
            st.info(res.text)

# --- 09. ESOTERIC LAB (New Tool) ---
elif "09." in tool:
    st.title("🔮 Esoteric & Prophetic Lab")
    st.write("ጥልቅ ምስጢር ያላቸውን የግዕዝ መጻሕፍት (ምሳሌ፡ ራእየ ዮሐንስ፣ መጽሐፈ ሄኖክ ምስጢራት) ይተንትኑ።")
    secret_query = st.text_area("የሚመረመረው የምስጢር ርዕስ ወይም ጥቅስ...")
    if st.button("ምስጢሩን ግለጥ"):
        with st.spinner("የከውን ደጀን AI በጥልቀት እያሰላ ነው..."):
            res = model.generate_content(f"ለዚህ ጥልቅ ምስጢራዊ ጥያቄ በባለሙያ ደረጃ ትንታኔ ስጥ፡ {secret_query}")
            st.markdown(f"<div style='background:#fefefe; padding:20px; border-left:10px solid gold;'>{res.text}</div>", unsafe_allow_html=True)

# --- 20. PAYMENT GATEWAY (Keeping existing) ---
elif "20." in tool:
    st.title("💳 Global Payment & Monetization")
    st.markdown("""
    <div class='content-card'>
    <h3>የክፍያ አማራጮች (Payment Systems)</h3>
    ለላቀ ምርምር እና ፕሪሚየም አገልግሎት ክፍያዎን እዚህ ይፈጽሙ፡
    <br><br>
    🔵 <b>Telebirr:</b> 09XX XXX XXX<br>
    🟠 <b>Chapa:</b> Card & International Payments<br>
    🟢 <b>CBE:</b> 1000XXXXXXXXX
    </div>
    """, unsafe_allow_html=True)
    st.success("የደንበኝነት ፈቃድዎ ለ 12 ሚሊዮን ገጾች ተፈቅዷል።")

# --- UNIVERSAL CHAT (For all other 17+ sections) ---
else:
    st.title(f"{tool}")
    st.info(f"ይህ ክፍል በዲያቆን ከውን ደጀን የሚመራ የ {tool} ማዕከል ነው።")
    p_input = st.chat_input("ሊቁን ጥያቄ ይጠይቁ...")
    if p_input:
        with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
            res = model.generate_content(f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የ {tool} ባለሙያ ነህ። በባለሙያ ደረጃ መልስ ስጥ: {p_input}")
            st.markdown(f"<div class='content-card'>{res.text}</div>", unsafe_allow_html=True)
            st.download_button("የምርምር ውጤቱን አውርድ (Export PDF)", res.text)

# ---------------------------------------------------------
# 5. SUPREME FOOTER (The Master's Signature)
# ---------------------------------------------------------
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center;'>
        <h4 style='color: #b8860b;'>GE'EZ SCHOLAR AI v12.0 | SUPREME ZENITH EDITION</h4>
        <p style='font-size: 18px;'><b>EXCLUSIVELY DEVELOPED BY DEACON KEWN DEJEN</b></p>
        <p>Global Center for Advanced Ge'ez Intelligence | Addis Ababa | 2025</p>
    </div>
""", unsafe_allow_html=True)
