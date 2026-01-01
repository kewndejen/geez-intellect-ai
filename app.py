import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import datetime

# ---------------------------------------------------------
# 1. ULTIMATE IMPERIAL CONFIGURATION (Deacon Kewn Dejen Standard)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Grand Architect Deacon Kewn Dejen",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sovereign Aesthetics (Gold, Midnight Blue, Crimson)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@400;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    
    .stSidebar { background: linear-gradient(180deg, #000c18 0%, #300000 100%) !important; border-right: 5px solid #b8860b; }
    .stSidebar [data-testid="stMarkdownContainer"] p { color: #d4af37 !important; font-weight: bold; }

    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%);
        color: white; border: none; padding: 18px 30px;
        border-radius: 12px; font-weight: 800; width: 100%;
        font-size: 16px; letter-spacing: 1.5px; transition: 0.5s;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { 
        transform: translateY(-5px) scale(1.02); 
        box-shadow: 0 15px 50px rgba(184, 134, 11, 0.8); 
    }
    
    .signature-card {
        background: linear-gradient(90deg, #b8860b, #000c18);
        padding: 25px; border-radius: 15px; border: 2px solid #d4af37;
        text-align: center; color: white; font-weight: bold;
        margin-bottom: 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.6);
    }
    
    .premium-card {
        background: white; padding: 40px; border-radius: 20px;
        border-left: 15px solid #b8860b; box-shadow: 0 25px 90px rgba(0,0,0,0.12);
        margin-bottom: 35px;
    }

    .payment-box {
        background: #fffdf5; padding: 30px; border-radius: 20px;
        border: 3px solid #d4af37; text-align: center;
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE QUANTUM ENGINE (Master Authorization)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: Master Key Required. Contact Deacon Kewn Dejen.")
    st.stop()

model = genai.GenerativeModel('gemini-2.0-flash')

# ---------------------------------------------------------
# 3. GLOBAL NAVIGATION: THE 60+ PILLAR HUB
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='signature-card'>GRAND ARCHITECT & CEO:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    category = st.selectbox("የጥበብ ምሰሶዎች", [
        "🏠 Imperial Dashboard",
        "🧠 AI Research & OCR Labs",
        "📜 The Great Digital Vaults",
        "🏛️ Heritage, Map & Material Science",
        "🎓 Academic University",
        "🔮 Mysticism, Poetry & Prophecy",
        "💰 Global Business & Wealth Hub"
    ])
    
    st.markdown("---")
    st.success("System: Online")
    st.info(f"Capacity: 12M+ Reasoning Nodes")

# ---------------------------------------------------------
# 4. CONTENT ENGINE - DYNAMIC PORTALS
# ---------------------------------------------------------

# --- PORTAL I: DASHBOARD ---
if category == "🏠 Imperial Dashboard":
    st.markdown("<h1>The Absolute Sovereign Dashboard</h1>", unsafe_allow_html=True)
    st.markdown(f"### 👑 Designed & Developed by Deacon Kewn Dejen")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Reasoning Depth", "12M+ Data Points", "Supreme")
    col2.metric("Integrated Tools", "60+ Strategic", "Maximized")
    col3.metric("Developer Status", "Deacon Kewn Dejen", "Active")
    col4.metric("Security Level", "Quantum Tier", "Shielded")
    
    st.markdown("""
    <div class='premium-card'>
    <h3>የዓለም አቀፍ የግዕዝ AI ምርምር ማዕከል (Global Center)</h3>
    እንኳን ወደ ዲያቆን ከውን ደጀን የጥበብ መንግሥት በደህና መጡ። ይህ ሲስተም የኢትዮጵያን ጥንታዊ ጥበብ በሰው ሰራሽ አስተውሎት (AI) አማካኝነት 
    ለዓለም አቀፍ ማኅበረሰብ የሚያቀርብ ብቸኛው ግዙፍ የቴክኖሎጂ ውጤት ነው። 60 ስትራቴጂካዊ ምሰሶዎችን በመያዝ የጥበብ መንግሥቱን ያነግሣል።
    </div>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=400)

# --- PORTAL II: AI RESEARCH & OCR ---
elif category == "🧠 AI Research & OCR Labs":
    st.title("🧠 Neural Manuscript Analysis & OCR")
    st.write("የብራና ወይም የጥንታዊ ጽሁፍ ምስል እዚህ ይጫኑ። ሲስተሙ ጽሁፉን አንብቦ በጥልቀት ይተረጉመዋል።")
    file = st.file_uploader("የምስል ፋይል ይጫኑ (Manuscript/Artifact)", type=['jpg','png','jpeg'])
    if file:
        img = Image.open(file)
        st.image(img, use_container_width=True)
        if st.button("Deep Neural Scan (Kewn Dejen Intelligence)"):
            with st.spinner("AI Engine is scanning with Master Precision..."):
                res = model.generate_content(["ከዚህ ምስል ላይ ያለውን የግዕዝ ጽሁፍ በዝርዝር ተንትነህ ተርጉም (Analyze professionally):", img])
                st.markdown(f"<div class='premium-card'>{res.text}</div>", unsafe_allow_html=True)

# --- PORTAL III: LIBRARY ---
elif category == "📜 The Great Digital Vaults":
    st.title("📜 The Universal Digital Library (12M Volumes)")
    st.write("ከ12 ሚሊዮን መዛግብት ውስጥ የፈለጉትን መጽሐፍ ወይም ርዕስ ይጠይቁ።")
    search = st.text_input("መጽሐፍ ወይም ጥቅስ ፈልግ (ለምሳሌ፡ ሄኖክ፣ ፍትሐ ነገሥት...)")
    if search:
        with st.spinner("ሊቁ ሰነዶችን እያመሳከረ ነው..."):
            res = model.generate_content(f"አንተ የአለም አቀፍ የግዕዝ ሊቅ ነህ። ስለዚህ ጉዳይ እጅግ ጥልቅ መረጃ ስጥ፡ {search}")
            st.write(res.text)

# --- PORTAL VII: BUSINESS & WEALTH ---
elif category == "💰 Global Business & Wealth Hub":
    st.title("💰 Global Business & Monetization Center")
    st.markdown(f"""
    <div class='payment-box'>
        <h3 style='color: #8b6b00;'>የክቡር ዲያቆን ከውን ደጀን የጥበብ ማዕከልን ይደግፉ</h3>
        <p>ይህንን ጥንታዊ ጥበብ ለዓለም ለማድረስ በምናደርገው ጉዞ የእርስዎ ድጋፍ ወሳኝ ነው።</p>
        <p><b>የቴሌብር ቁጥር:</b> 09XX XXX XXX (Deacon Kewn Dejen)</p>
        <p><b>የባንክ አካውንት (CBE):</b> 1000XXXXXXXXX</p>
        <p style='font-style: italic; color: #b8860b;'>ለፕሪሚየም አገልግሎት እና ለጥልቅ ምርምር የደንበኝነት ክፍያዎን እዚህ ይፈጽሙ።</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("---")
    st.subheader("የደንበኝነት ፈቃዶች")
    colA, colB = st.columns(2)
    colA.info("Standard (ተማሪ): 100 ETB/mo")
    colB.success("Elite (ተመራማሪ): 500 ETB/mo")

# --- OTHER CATEGORIES (Dynamic Chat) ---
else:
    st.title(f"{category}")
    st.info(f"ይህ ክፍል በዲያቆን ከውን ደጀን የሚመራ የ {category} ማዕከል ነው።")
    st.write("በዚህ ዘርፍ የሚፈልጉትን ጥያቄ ከታች ባለው የቻት ሳጥን ይጠይቁ።")

# ---------------------------------------------------------
# 5. UNIVERSAL CHAT INTERFACE (ALWAYS VISIBLE)
# ---------------------------------------------------------
st.markdown("---")
st.subheader("💬 የ AI ሊቁን ውይይት")

if "messages" not in st.session_state: st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

if prompt := st.chat_input("የሊቅ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
            try:
                # በዲያቆን ከውን ደጀን ማንነት እንዲመልስ መመሪያ
                full_instruct = f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የግዕዝ ሊቅ ነህ። ለዚህ ጥያቄ እጅግ ጥልቅና ፕሮፌሽናል መልስ ስጥ፡ {prompt}"
                response = model.generate_content(full_instruct)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except: st.warning("እባክህ 20 ሰከንድ ቆይተህ ድገመው።")

# ---------------------------------------------------------
# 6. SUPREME MASTER SIGNATURE (Footer)
# ---------------------------------------------------------
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center;'>
        <h4 style='color: #b8860b;'>GE'EZ SCHOLAR AI v70.0 | ABSOLUTE SOVEREIGN EDITION</h4>
        <p style='font-size: 18px;'><b>EXCLUSIVELY DEVELOPED BY THE GRAND ARCHITECT DEACON KEWN DEJEN</b></p>
        <p>Strategic Global Hub for Advanced Ge'ez Intelligence | Addis Ababa | 2026</p>
    </div>
""", unsafe_allow_html=True)
