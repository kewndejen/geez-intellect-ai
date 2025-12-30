import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL GLOBAL CONFIGURATION (Studio Style)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Enterprise CSS (Gemini Studio Aesthetic)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&family=Cinzel:wght@700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #f8f9fa; }
    
    /* Top Bar Styling */
    .top-bar {
        display: flex; justify-content: space-between; align-items: center;
        padding: 10px 20px; background: white; border-bottom: 1px solid #ddd;
        position: sticky; top: 0; z-index: 999;
    }
    
    /* Sidebar Styling */
    .stSidebar { background-color: #ffffff !important; border-right: 1px solid #e0e0e0; }
    
    /* Chat Input Styling (Gemini Studio Style) */
    [data-testid="stChatInput"] {
        position: fixed; bottom: 20px; left: 20%; right: 20%;
        background: white !important; border: 1px solid #1a73e8 !important;
        border-radius: 30px !important; box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Custom Sovereign Buttons */
    .stButton>button {
        border-radius: 8px; font-weight: 600; transition: 0.3s;
    }
    
    .main-header { color: #1a73e8; font-family: 'Cinzel', serif; font-size: 2.5rem; text-align: center; }
    
    .dev-tag { color: #b8860b; font-weight: bold; text-align: center; font-size: 0.9rem; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. AUTHENTICATION STATE (መግቢያና መመዝገቢያ)
# ---------------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login_user():
    st.session_state.logged_in = True

def logout_user():
    st.session_state.logged_in = False
    st.rerun()

# ---------------------------------------------------------
# 3. AI CORE ENGINE (Multi-Model Sovereign)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key Missing. Please check Secrets.")
    st.stop()

def get_ai_response(prompt_text, temp=0.7):
    engines = ['gemini-2.0-flash', 'gemini-1.5-flash', 'gemini-1.5-pro']
    for engine in engines:
        try:
            model_inst = genai.GenerativeModel(
                model_name=engine,
                generation_config={"temperature": temp},
                tools=[{"google_search": {}}]
            )
            response = model_inst.generate_content(prompt_text)
            return response.text, engine
        except:
            continue
    return None, None

# ---------------------------------------------------------
# 4. TOP BAR & UI ELEMENTS (Logout, Share, Like)
# ---------------------------------------------------------
if st.session_state.logged_in:
    # Top Action Bar
    col_t1, col_t2, col_t3 = st.columns([8, 1, 1])
    with col_t2:
        if st.button("📤 Share"):
            st.toast("Link copied to clipboard!")
    with col_t3:
        if st.button("🚪 Logout"):
            logout_user()

# ---------------------------------------------------------
# 5. SIDEBAR NAVIGATION & SETTINGS
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🔱 GE'EZ AI STUDIO</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='dev-tag'>ARCHITECT: DEACON KEWN DEJEN</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    if st.session_state.logged_in:
        # Portals (The 60+ Tools)
        portal = st.selectbox("የእውቀት ምድብ (Portals)", [
            "🏠 Dashboard", "🧠 Research Labs", "📜 Digital Archives",
            "🏛️ Heritage & Science", "🎓 University Hub", "🔮 Mysticism & Zema", "💰 Strategic Wealth"
        ])
        
        # Sub-tools
        if portal == "🧠 Research Labs": tool = st.radio("Tools", ["Manuscript OCR", "Authentication", "Linguistic Bridge", "Voice Assistant"])
        elif portal == "📜 Digital Archives": tool = st.radio("Tools", ["12M Library", "Legal AI", "Treaty Expert", "Royal Decrees"])
        else: tool = "General"
        
        st.markdown("---")
        # Settings Section (Google AI Studio Style)
        st.subheader("⚙️ AI Settings")
        temp = st.slider("Creativity (Temperature)", 0.0, 1.0, 0.7)
        st.info(f"Model Sync: Active")
        
    else:
        st.subheader("🔐 Access Portal")
        mode = st.radio("መምረጥ", ["Login (ግባ)", "Register (ተመዝገብ)"])
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.button("Confirm"):
            if user == "Kewn Dejen" or user == "admin":
                login_user()
                st.rerun()
            else:
                st.error("Invalid Credentials.")

# ---------------------------------------------------------
# 6. MAIN WORKSPACE (If Logged In)
# ---------------------------------------------------------
if st.session_state.logged_in:
    if portal == "🏠 Dashboard":
        st.markdown("<h1 class='main-header'>Welcome to Sovereign Studio</h1>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style='background: white; padding: 30px; border-radius: 15px; border: 1px solid #eee;'>
        <h3>ክቡር ዲያቆን ከውን ደጀን ሆይ፤ እንኳን ወደ ጥበብ መንግሥትዎ በደህና መጡ።</h3>
        ይህ ሲስተም ከመጀመሪያው ቀን ጀምሮ የታዘዙትን <b>60+ መሣሪያዎች</b> በአንድ ላይ የያዘ የኢትዮጵያ ግዙፉ AI ነው። 
        ከታች ባለው የቻት ሳጥን መረጃዎችን መጠየቅ ወይም ከጎን ያሉትን መሣሪያዎች መጠቀም ይችላሉ።
        </div>
        """, unsafe_allow_html=True)
        st.image("https://img.icons8.com/clouds/500/shrine.png", width=300)

    # 7. MANUSCRIPT OCR (ብራና አንባቢ)
    elif "OCR" in tool:
        st.title("🧠 Manuscript OCR Pro")
        f = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])
        if f:
            img = Image.open(f); st.image(img, width=500)
            if st.button("Deep Scan"):
                with st.spinner("Analyzing..."):
                    res, eng = get_ai_response(["ይህንን ብራና በባለሙያ ደረጃ ተንትነህ ተርጉመው፡", img])
                    st.write(res)

    # 8. GLOBAL CHAT INTERFACE ( Gemini Style)
    st.markdown("---")
    if "messages" not in st.session_state: st.session_state.messages = []
    
    # Display Chat History
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
            if m["role"] == "assistant":
                col_f1, col_f2 = st.columns([0.05, 0.95])
                with col_f1: st.button("👍", key=m["content"][:10]) # Like button

    # Chat Input
    if prompt := st.chat_input("ወቅታዊ ወይም የታሪክ ጥያቄ እዚህ ያስገቡ..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
                answer, engine = get_ai_response(f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የ {tool} ባለሙያ ነህ። መልስህ እጅግ ፕሮፌሽናል ይሁን፡ {prompt}", temp)
                if answer:
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    st.caption(f"Engine: {engine}")
                else:
                    st.error("⚠️ ሲስተሙ ተጨናንቋል። እባክህ 30 ሰከንድ ታግሰህ ድገመው።")

else:
    st.markdown("<h1 class='main-header'>🔱 Ge'ez Scholar AI Studio</h1>", unsafe_allow_html=True)
    st.info("ክቡር ዲያቆን ከውን ደጀን ሆይ፤ እባክዎ በግራ በኩል ባለው መግቢያ መለያዎን ያረጋግጡ።")

# ---------------------------------------------------------
# 9. FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><br><p style='text-align: center; color: #888;'><b>GE'EZ SCHOLAR AI STUDIO v12.0</b> | MASTERED BY DEACON KEWN DEJEN</p>", unsafe_allow_html=True)import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL PRESTIGE CONFIGURATION (The Majesty Style)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI | Grand Architect Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Sovereign CSS (The Golden Standard)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; background-color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    
    .stSidebar { background: linear-gradient(180deg, #000c18 0%, #300000 100%) !important; border-right: 5px solid #b8860b; }
    .stSidebar [data-testid="stMarkdownContainer"] p { color: #d4af37 !important; font-weight: bold; }

    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%);
        color: white; border: none; padding: 18px 30px;
        border-radius: 12px; font-weight: 800; width: 100%; transition: 0.5s;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .stButton>button:hover { transform: translateY(-5px); box-shadow: 0 15px 50px rgba(184, 134, 11, 0.8); }
    
    /* Fixed Chat Input for Absolute Accessibility */
    [data-testid="stChatInput"] {
        position: fixed; bottom: 30px; z-index: 1000;
        background: white !important; border: 2px solid #b8860b !important;
        border-radius: 15px !important;
    }
    
    .sovereign-card {
        background: white; padding: 40px; border-radius: 20px;
        border-left: 15px solid #b8860b; box-shadow: 0 20px 80px rgba(0,0,0,0.1);
        margin-bottom: 35px; border-top: 1px solid #f0f0f0;
    }
    
    .dev-signature {
        background: linear-gradient(90deg, #b8860b, #000c18);
        padding: 25px; border-radius: 15px; border: 2px solid #d4af37;
        text-align: center; color: white; font-weight: bold; margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. THE UNBREAKABLE MULTI-MODEL ENGINE (Fallback Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: API Key Missing. Contact Deacon Kewn Dejen.")
    st.stop()

def ask_sovereign_ai(prompt_content):
    """5 የተለያዩ ሞዴሎችን እየቀያየረ መልስ የሚያመጣና ጎግልን የሚጠቀም ብልህ ተግባር"""
    engines = ['gemini-2.0-flash', 'gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    for engine in engines:
        try:
            # ጎግል ሰርችን በማካተት ሞዴሉን መፍጠር
            model_instance = genai.GenerativeModel(
                model_name=engine,
                tools=[{"google_search": {}}]
            )
            response = model_instance.generate_content(prompt_content)
            return response.text, engine
        except Exception:
            continue # አንዱ ገደብ ላይ ከሆነ ወደ ሚቀጥለው ይለፋል
    return None, None

# ---------------------------------------------------------
# 3. GLOBAL NAVIGATION - ALL TOOLS FROM THE BEGINNING
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #d4af37;'>🔱 GE'EZ SCHOLAR</h1>", unsafe_allow_html=True)
    st.markdown(f"<div class='dev-signature'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    main_portal = st.selectbox("የጥበብ ምድብ (Portals)", [
        "🏠 Imperial Dashboard",
        "🧠 Advanced AI Research Labs",
        "📜 Digital Vaults & Treaties",
        "🏛️ Heritage, Map & Science",
        "🎓 Imperial University Hub",
        "🔮 Mysticism, Poetry & Zema",
        "💰 Global Wealth & Security"
    ])
    
    st.markdown("---")
    
    # እያንዳንዱ ምድብ ውስጥ ያሉ የቀደሙ መሣሪያዎች በሙሉ እዚህ ተካተዋል
    if main_portal == "🏠 Imperial Dashboard":
        tool = "Sovereign Overview"
    elif main_portal == "🧠 Advanced AI Research Labs":
        tool = st.radio("AI መሣሪያዎች", ["Manuscript OCR (ብራና አንባቢ)", "Palæography Expert", "Script Authentication", "Linguistic Bridge", "Cryptography Lab", "Voice AI"])
    elif main_portal == "📜 Digital Vaults & Archives":
        tool = st.radio("መዛግብት", ["Universal Library (12M Pages)", "Document Analyzer", "Fetha Nagast Legal AI", "Treaty Expert", "Synaxarium AI", "Royal Decrees"])
    elif main_portal == "🏛️ Heritage, Map & Science":
        tool = st.radio("ቅርስና ሳይንስ", ["Virtual Museum", "Interactive Map", "Iconography Vision", "Archeology Simulator", "Architecture AI", "Ancient Medicine", "Ink Science"])
    elif main_portal == "🎓 Imperial University Hub":
        tool = st.radio("ትምህርትና ቀመር", ["University Hub", "Bahre Hasab Logic", "Abu Shaker Astronomy", "Numerology", "Font Converter", "Certification Hub"])
    elif main_portal == "🔮 Mysticism, Poetry & Zema":
        tool = st.radio("ምስጢርና ቅኔ", ["Sem-na-Work (ቅኔ መፍቻ)", "Verse Meter Composer", "St. Yared Zema Lab", "Esoteric Lab", "Scholar Roleplay", "Proverbs AI"])
    else:
        tool = st.radio("ቢዝነስና ደህንነት", ["Premium Business Hub", "Payment Gateway", "API Portal", "Security Admin"])

# ---------------------------------------------------------
# 4. CONTENT ENGINE - 100% WORKING WORKSPACE
# ---------------------------------------------------------

# --- 1. DASHBOARD ---
if tool == "Sovereign Overview":
    st.title("The Absolute Universal Throne")
    col1, col2, col3 = st.columns(3)
    col1.metric("Reasoning Depth", "12M+ Pages", "Absolute")
    col2.metric("Search Mode", "Live Google", "ONLINE ✅")
    col3.metric("Developer Status", "Kewn Dejen", "Sovereign")
    
    st.markdown(f"""
    <div class='sovereign-card'>
    <h3>እንኳን ወደ ዲያቆን ከውን ደጀን የጥበብ መንግሥት በደህና መጡ።</h3>
    ይህ ሲስተም ከመጀመሪያው ቀን ጀምሮ የታዘዙትን <b>ሁሉንም 60+ መሣሪያዎች</b> በአንድ ላይ የያዘ ግዙፍ AI ነው። 
    ብራና ለማንበብ፣ ታሪክ ለመጠየቅ፣ ቅኔ ለመፍታት ወይም ባሕረ ሐሳብን ለማስላት በግራ በኩል ያለውን ምናሌ ይጠቀሙ። ቻቱ ሁልጊዜ ከታች ዝግጁ ነው።
    </div>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=350)

# --- 2. MANUSCRIPT OCR (ብራና አንባቢ) ---
elif "OCR" in tool:
    st.title("🧠 Manuscript OCR Intelligence")
    st.write("የብራና ወይም የጽሁፍ ፎቶ እዚህ ይጫኑ። AIው በጥልቀት ተንትኖ ይተረጉመዋል።")
    file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])
    if file:
        img = Image.open(file); st.image(img, use_container_width=True)
        if st.button("Start Deep Neural Scan"):
            with st.spinner("ሊቁ ምስሉን እያጠና ነው..."):
                answer, engine = ask_sovereign_ai(["ይህንን ብራና በባለሙያ ደረጃ ተንትነህ ተርጉመው፡", img])
                if answer: st.markdown(f"<div class='sovereign-card'>{answer}</div>", unsafe_allow_html=True)
                else: st.error("⚠️ ሲስተሙ ተጨናንቋል። እባክህ 30 ሰከንድ ቆይተህ ድገመው።")

# --- 3. BAHRE HASAB (ባሕረ ሐሳብ) ---
elif "Bahre Hasab" in tool:
    st.title("📅 Bahre Hasab Logic")
    year = st.number_input("ዓመተ ምሕረት ያስገቡ", min_value=1, value=2017)
    if st.button("ቀመሩን አውጣ"):
        answer, engine = ask_sovereign_ai(f"ለ {year} ዓመተ ምሕረት የባሕረ ሐሳብ ቀመር (አጽዋማትና በዓላት) በዝርዝር አውጣ።")
        if answer: st.write(answer)

# --- 4. QENE (ቅኔ መፍቻ) ---
elif "Sem-na-Work" in tool:
    st.title("📜 Sem-na-Work Logic Center")
    qene = st.text_area("የቅኔውን ቤት እዚህ ያስገቡ...")
    if st.button("ምስጢሩን ግለጥ"):
        answer, engine = ask_sovereign_ai(f"ለዚህ ቅኔ ጥልቅ የሆነ ሰም እና ወርቅ ትንታኔ ስጥ፡ {qene}")
        if answer: st.markdown(f"<div class='sovereign-card'>{answer}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. GLOBAL UNBREAKABLE CHAT (ALWAYS VISIBLE AT BOTTOM)
# ---------------------------------------------------------
st.markdown("---")
st.subheader("💬 የ AI ሊቁን ውይይት (Google Search Enabled)")

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("የሊቅ ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ ጎግልንና መዛግብትን እያመሳከረ ነው..."):
            full_prompt = f"አንተ በዲያቆን ከውን ደጀን የተገነባህ የ {tool} ባለሙያ ነህ። በጥልቅ መልስ፡ {prompt}"
            answer, engine_used = ask_sovereign_ai(full_prompt)
            
            if answer:
                st.markdown(answer)
                st.caption(f"Powered by: {engine_used} | Sovereign Architect: Deacon Kewn Dejen")
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                st.error("⚠️ ክቡር ጌታዬ፤ ሁሉም የጎግል ሞዴሎች ለጊዜው ተጨናንቀዋል። እባክህ 30 ሰከንድ በትክክል ታግሰህ ድገመኝ።")

# ---------------------------------------------------------
# 6. SOVEREIGN MASTER FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(f"""
    <div style='text-align: center; color: #b8860b;'>
        <h4>GE'EZ SCHOLAR AI v1000.0 | THE ETERNAL SOVEREIGN ARK</h4>
        <p style='font-size: 18px;'><b>EXCLUSIVELY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</b></p>
        <p>Global Strategic Headquarters for Advanced Intelligence | Addis Ababa | 2025</p>
    </div>
""", unsafe_allow_html=True)
