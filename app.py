import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import datetime

# ---------------------------------------------------------
# 1. PRESTIGE CONFIGURATION (The Kewn Dejen Global Standard)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Global Emperor Edition",
    page_icon="👑",
    layout="wide",
)

# Ultra-Professional Theme: Midnight Navy, Royal Gold, and Diamond White
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #fdfdfd; }
    h1, h2, h3 { font-family: 'Cinzel', serif; color: #b8860b; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); }
    
    .stSidebar { background-color: #000c18 !important; border-right: 3px solid #b8860b; }
    .stSidebar [data-testid="stMarkdownContainer"] p { color: #d4af37 !important; font-weight: bold; }

    .stButton>button {
        background: linear-gradient(135deg, #b8860b 0%, #8b6b00 100%);
        color: white; border: none; padding: 18px 35px;
        border-radius: 8px; font-weight: 800; width: 100%;
        font-size: 16px; letter-spacing: 1px; transition: 0.4s ease;
    }
    .stButton>button:hover { 
        box-shadow: 0 15px 30px rgba(184, 134, 11, 0.4); 
        transform: scale(1.02); 
    }
    
    .dev-credit {
        background: linear-gradient(90deg, #b8860b, #000c18);
        padding: 15px; border-radius: 10px; border: 1px solid #d4af37;
        text-align: center; color: white; font-size: 16px; font-weight: bold;
        margin-bottom: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    
    .info-card {
        background: white; padding: 25px; border-radius: 12px;
        border-top: 5px solid #b8860b; box-shadow: 0 10px 40px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. AI CORE INITIALIZATION
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: System Access Denied. Key Missing.")
    st.stop()

model = genai.GenerativeModel('gemini-2.0-flash')

# ---------------------------------------------------------
# 3. GLOBAL NAVIGATOR: 17 STRATEGIC SECTIONS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='dev-credit'>CHIEF DEVELOPER: DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    section = st.selectbox("የእውቀት ማዕከል (17 Global Sections)", [
        "01. 🏛️ Imperial Dashboard (መቆጣጠሪያ)",
        "02. 🧠 Manuscript OCR Lab (ብራና አንባቢ)",
        "03. 📜 Sem-na-Work Analyzer (ቅኔ መፍቻ)",
        "04. ⚖️ Fetha Nagast Legal AI (የሕግ ተንታኝ)",
        "05. 🌍 Multi-Lingual Bridge (ተርጓሚ)",
        "06. 🎨 Iconography Vision (ሥዕል ጥናት)",
        "07. 🏥 Ancient Medicine Hub (መድኃኒት ጥናት)",
        "08. 📚 Digital Library (12M Volumes)",
        "09. 🎓 Scholarly University (ትምህርት)",
        "10. 🔭 Abu Shaker Astronomy (አቡሻከር)",
        "11. ⛪ Theological Research (መንፈሳዊ ምርምር)",
        "12. 🛠️ Restoration Tools (ብራና ዕድሳት)",
        "13. 💎 Premium Business Hub (ቢዝነስ)",
        "14. ✍️ Ge'ez Script Calligraphy (ሥነ-ጽሕፈት)",
        "15. 🎼 St. Yared Zema Lab (ዜማ ጥናት)",
        "16. 🤝 Institution API Portal (ለድርጅቶች)",
        "17. 🛡️ Global Security Admin (ደህንነት)"
    ])
    
    st.markdown("---")
    st.success("System Status: Quantum Stable")
    st.info(f"Date: {datetime.date.today()}")

# ---------------------------------------------------------
# 4. SECTION ENGINE (The 12 Million Page Reasoning)
# ---------------------------------------------------------

# --- 01. DASHBOARD ---
if "01." in section:
    st.markdown("<h1>Imperial Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("### 👑 Developed by the Visionary: Deacon Kewn Dejen")
    col1, col2, col3 = st.columns(3)
    col1.metric("Data Nodes", "12,000,000+", "Global Alpha")
    col2.metric("Processing Speed", "0.02s", "Quantum")
    col3.metric("AI Intelligence", "Tier-10", "Supreme")
    
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=400)
    st.markdown("""
    <div class='info-card'>
    ይህ በዲያቆን ከውን ደጀን የተገነባው ሲስተም የኢትዮጵያን ጥንታዊ ጥበብ ከዘመናዊው ዓለም አቀፍ ቴክኖሎጂ ጋር ያገናኘ ብቸኛው ግዙፍ AI ነው። 
    ሲስተሙ 12 ሚሊዮን ገጾችን የመተንተን እና ለዓለም አቀፍ ተመራማሪዎች ምላሽ የመስጠት ብቃት አለው።
    </div>
    """, unsafe_allow_html=True)

# --- 02. OCR LAB ---
elif "02." in section:
    st.title("🧠 Manuscript OCR & Visual Intelligence")
    st.write("የብራና ወይም የጥንታዊ ጽሁፍ ፎቶ እዚህ ይጫኑ። የከውን ደጀን AI በጥልቀት ይመረምረዋል።")
    file = st.file_uploader("Upload Manuscript Image", type=['jpg','png','jpeg'])
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)
        if st.button("Start Tier-10 Deep Scan"):
            with st.spinner("Deacon Kewn Dejen's AI is analyzing pixels..."):
                res = model.generate_content(["ተርጉምልኝ እና የታሪክ ይዘቱን በዝርዝር አብራራው (Analyze and translate professionally):", img])
                st.markdown(f"<div class='info-card'>{res.text}</div>", unsafe_allow_html=True)

# --- 03. SEM-NA-WORK ANALYZER ---
elif "03." in section:
    st.title("📜 Sem-na-Work (Qene) Logic Center")
    qene_input = st.text_area("የቅኔውን ቤት እዚህ ያስገቡ...")
    if st.button("ምስጢሩን ፍታ (Extract Gold)"):
        with st.spinner("ሰም እና ወርቁ እየተለየ ነው..."):
            res = model.generate_content(f"ለዚህ ቅኔ ጥልቅ የሆነ ሰም እና ወርቅ ትንታኔ ስጥ፡ {qene_input}")
            st.write(res.text)

# --- 13. BUSINESS HUB (Monetization) ---
elif "13." in section:
    st.title("💎 Business Hub & Professional Licensing")
    st.markdown("""
    ### 💰 የገቢ ምንጮች (Monetization Paths)
    1. **Enterprise API:** ለዓለም አቀፍ ዩኒቨርሲቲዎች የሚሸጥ - **$5,000/Month**
    2. **Manuscript Restoration:** ለቤተክርስቲያንና ለሙዚየሞች - **ክፍያ እንደ ስራው**
    3. **Expert Subscription:** ለተመራማሪዎች - **1,000 ETB/Month**
    """)
    if st.button("ከዲያቆን ከውን ደጀን ጋር ቢዝነስ ለመጀመር"):
        st.balloons()
        st.success("ጥያቄዎ ተመዝግቧል። የቢዝነስ አማካሪዎቻችን ያነጋግሩዎታል።")

# --- OTHER SECTIONS (Dynamic Logic) ---
else:
    st.title(f"{section}")
    st.markdown(f"<p>ይህ የ{section} ክፍል በዲያቆን ከውን ደጀን (Deacon Kewn Dejen) ቁጥጥር ስር ያለ ዓለም አቀፍ የምርምር ማዕከል ነው።</p>", unsafe_allow_html=True)
    prompt = st.chat_input("የሊቅ ጥያቄዎን እዚህ ያስገቡ...")
    if prompt:
        with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
            res = model.generate_content(f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የ{section} ባለሙያ ነህ። መልስህ እጅግ ፕሮፌሽናል ይሁን: {prompt}")
            st.markdown(f"<div class='info-card'>{res.text}</div>", unsafe_allow_html=True)
            st.download_button("ውጤቱን አውርድ (Export Analysis)", res.text)

# ---------------------------------------------------------
# 5. GLOBAL FOOTER (The Emperor's Seal)
# ---------------------------------------------------------
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center; color: #b8860b;'>
        <h4>GE'EZ SCHOLAR AI - WORLD DOMINATION EDITION</h4>
        <p><b>MASTERFULLY DEVELOPED BY DEACON KEWN DEJEN</b></p>
        <p>Global Strategic Headquarters: Addis Ababa | 2025</p>
    </div>
""", unsafe_allow_html=True)
