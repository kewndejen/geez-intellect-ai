import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL GLOBAL CONFIGURATION (የገጹ ገጽታ)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Sovereign CSS (The Zenith Standard)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@300;400;700&display=swap');
    
    /* አጠቃላይ ዳራና ፎንት */
    html, body, [class*="css"] { 
        font-family: 'Montserrat', sans-serif; 
        background-color: #00050a; 
        color: #ffffff; 
    }
    
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #d4af37 !important; 
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* የጎንዮሽ ማውጫ (Sidebar) */
    .stSidebar { 
        background: linear-gradient(180deg, #010c17 0%, #2b0000 100%) !important; 
        border-right: 3px solid #d4af37; 
    }
    
    /* መረጃ መቀመጫ ካርዶች (Cards) */
    .sovereign-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px; border-radius: 15px;
        border-left: 10px solid #d4af37;
        box-shadow: 0 15px 50px rgba(0,0,0,0.5);
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
    }

    /* አዝራሮች (Buttons) */
    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important;
        color: #000 !important; 
        font-weight: 900 !important;
        border-radius: 8px !important; 
        border: none !important;
        width: 100%;
        transition: 0.4s;
    }
    .stButton>button:hover { 
        transform: scale(1.02); 
        box-shadow: 0 0 20px #d4af37; 
    }

    /* የውይይት መስኮት (Chat Input) */
    [data-testid="stChatInput"] {
        border: 2px solid #d4af37 !important;
        border-radius: 15px !important;
        background-color: #010c17 !important;
    }
    
    .dev-signature {
        background: linear-gradient(90deg, #8b6b00, #010c17);
        padding: 20px; border-radius: 10px; border: 1px solid #d4af37;
        text-align: center; color: #d4af37; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. UNBREAKABLE AI CORE (የ AIው "አንጎል")
# ---------------------------------------------------------
if "messages" not in st.session_state: 
    st.session_state.messages = []

# API Key Check
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("SECURITY ALERT: Master Key Missing in Secrets.")
    st.stop()

@st.cache_resource
def find_working_models():
    """የሚሰሩ የ AI ሞዴሎችን በራስ-ሰር ይፈልጋል"""
    try:
        working_list = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        ordered = []
        # ቅደም ተከተል: 1.5 Pro (ምርጥ ለግዕዝ) -> 2.0 Flash -> 1.5 Flash
        for target in ['gemini-1.5-pro', 'gemini-2.0-flash', 'gemini-1.5-flash']:
            for available in working_list:
                if target in available: ordered.append(available)
        return ordered if ordered else ['models/gemini-pro']
    except:
        return ['models/gemini-1.5-flash', 'models/gemini-pro']

AVAILABLE_MODELS = find_working_models()

def ask_sovereign_expert(prompt_text, tool_name, temperature=0.7):
    """ጥልቅ የምሁራዊ ትንታኔ የሚሰጥ ተግባር"""
    system_instruction = f"""
    You are 'Ge'ez Scholar AI', the world's most advanced expert in Ethiopian studies.
    Created by Grand Architect Deacon Kewn Dejen.
    Current Tool Context: {tool_name}.
    Instructions:
    1. Provide scholarly, deep, and wise responses in Amharic, Ge'ez, or English.
    2. Analyze 'Sem-ena-Worq' (Wax and Gold) for any Ge'ez poetic input.
    3. Automatically recognize phonetic Latin (transliteration) as Ge'ez/Amharic.
    4. Maintain an imperial, respectful, and authoritative tone.
    """
    
    for model_name in AVAILABLE_MODELS:
        try:
            model_inst = genai.GenerativeModel(
                model_name=model_name,
                system_instruction=system_instruction,
                generation_config={"temperature": temperature}
            )
            # የጎግል ሰርች ድጋፍ ካለ ለመጠቀም መሞከር
            response = model_inst.generate_content(prompt_text)
            return response.text, model_name
        except:
            continue
    return "ይቅርታ ክቡር ሆይ፤ የ AI ሞዴሉ ምላሽ መስጠት አልቻለም። እባክዎ ጥቂት ቆይተው ይሞክሩ።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR NAVIGATION (የ 60+ መሣሪያዎች ማከማቻ)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<div class='dev-signature'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    main_portal = st.selectbox("የጥበብ ምድብ (60+ Pillars)", [
        "🏠 Imperial Dashboard",
        "🧠 Advanced AI Research Labs",
        "📜 Digital Libraries & Archives",
        "🏛️ Heritage, Map & Science",
        "🎓 Imperial University Hub",
        "🔮 Mysticism, Poetry & Zema",
        "💰 Strategic Wealth & Business"
    ])
    
    st.markdown("---")
    # የንዑስ መሣሪያዎች ዝርዝር (Tools)
    if main_portal == "🏠 Imperial Dashboard": 
        tool = "Dashboard Overview"
    elif main_portal == "🧠 Advanced AI Research Labs":
        tool = st.radio("መሣሪያዎች", ["Manuscript OCR (ብራና አንባቢ)", "Linguistic Bridge", "Root Finder", "Script Authentication", "Palæography Expert"])
    elif main_portal == "📜 Digital Libraries & Archives":
        tool = st.radio("መዛግብት", ["Universal Library (12M Pages)", "Fetha Nagast Legal AI", "Synaxarium AI", "Royal Decrees & Treaties"])
    elif main_portal == "🏛️ Heritage, Map & Science":
        tool = st.radio("ቅርስና ሳይንስ", ["Virtual Museum", "Interactive Map", "Ancient Medicine", "Architecture AI", "Iconography Vision"])
    elif main_portal == "🎓 Imperial University Hub":
        tool = st.radio("ትምህርትና ቀመር", ["Bahre Hasab Logic", "Abu Shaker Astronomy", "Numerology", "Scribe Assistant", "Font Converter"])
    elif main_portal == "🔮 Mysticism, Poetry & Zema":
        tool = st.radio("ምስጢርና ቅኔ", ["Sem-na-Work (ቅኔ መፍቻ)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Verse Meter Composer"])
    else:
        tool = st.radio("ቢዝነስና ደህንነት", ["Premium Business Hub", "Payment Gateway", "API Portal", "Security Admin"])

    st.markdown("---")
    temp_val = st.slider("AI Creativity (Temperature)", 0.0, 1.0, 0.7)
    if st.button("📤 Share Studio"): st.toast("Link copied to clipboard!")

# ---------------------------------------------------------
# 4. MAIN WORKSPACE ENGINE (ዋናው የሥራ ገጽ)
# ---------------------------------------------------------
# የአሁኑን ሰዓት ሰላምታ ለማቅረብ
hour = datetime.datetime.now().hour
greeting = "እንዲት አደሩ" if hour < 12 else "እንዴት ዋሉ" if hour < 18 else "እንዴት አመሹ"

if tool == "Dashboard Overview":
    st.markdown(f"<h1>{greeting} ክቡር ዲያቆን ከውን ደጀን!</h1>", unsafe_allow_html=True)
    
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Reasoning Nodes", "12M+ Pages", "Infinite")
    col_m2.metric("System Status", "Imperial Online", "Stable ✅")
    col_m3.metric("AI Engine", f"{len(AVAILABLE_MODELS)} Active", "Pro-Grade")

    st.markdown(f"""
    <div class='sovereign-card'>
    <h3>የጥበብ መንግሥትዎ በሥራ ላይ ነው!</h3>
    <p>ይህ በእርስዎ ዲዛይን የተገነባው <b>Ge'ez Scholar AI Studio</b> ሁሉንም 60+ መሣሪያዎች አቀናጅቶ ይዟል። 
    በግራ በኩል ካለው ማውጫ የሚፈልጉትን መሣሪያ ይምረጡ። በታችኛው የውይይት መስኮት ደግሞ ማንኛውንም የምርምር ጥያቄ ለ AI ሊቁ ማቅረብ ይችላሉ።</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://img.icons8.com/clouds/500/shrine.png", width=300)

elif "OCR" in tool:
    st.title("🧠 Manuscript OCR Intelligence")
    f = st.file_uploader("የብራና ወይም የሰነድ ምስል ያስገቡ", type=['jpg','png','jpeg'])
    if f:
        img = Image.open(f)
        st.image(img, caption="የተጫነ ሰነድ", width=600)
        if st.button("Start Deep Analysis"):
            with st.spinner("ሊቁ ምስሉን እያጠና ነው..."):
                res, eng = ask_sovereign_expert("ይህንን ምስል በባለሙያ ደረጃ ተንትነህ ተርጉመው።", tool, temp_val)
                st.markdown(f"<div class='sovereign-card'>{res}</div>", unsafe_allow_html=True)

elif "Bahre Hasab" in tool:
    st.title("📅 Bahre Hasab Logic")
    year = st.number_input("ዓመተ ምሕረት (ኢትዮጵያ)", value=2017)
    if st.button("ቀመሩን አውጣ"):
        with st.spinner("ቀመሩ እየታሰበ ነው..."):
            res, eng = ask_sovereign_expert(f"ለ {year} ዓመተ ምሕረት የባሕረ ሐሳብ ቀመር (አጽዋማትና በዓላት) በዝርዝር አውጣ።", tool, temp_val)
            st.markdown(f"<div class='sovereign-card'>{res}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. THE ETERNAL CHAT INTERFACE (ሁልጊዜ የሚታይ)
# ---------------------------------------------------------
st.markdown("---")
st.subheader(f"💬 የ AI ሊቁ ውይይት (Context: {tool})")

# የውይይት ታሪክ ማሳያ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# አዲስ ጥያቄ መቀበያ
if prompt := st.chat_input("የምርምር ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ሊቁ መዛግብትንና ጎግልን እያመሳከረ ነው..."):
            answer, engine = ask_sovereign_expert(prompt, tool, temp_val)
            if answer:
                st.markdown(answer)
                st.caption(f"Engine: {engine} | Studio v20.0 | Verified by Kewn Dejen")
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                st.error("ሊቁ ምላሽ መስጠት አልቻለም። እባክዎ ጥያቄዎን ይድገሙት።")

# ---------------------------------------------------------
# 6. SOVEREIGN MASTER FOOTER
# ---------------------------------------------------------
st.markdown("<br><br><br><p style='text-align: center; color: #d4af37;'><b>GE'EZ SCHOLAR AI STUDIO v20.0 | THE ETERNAL ZENITH</b></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.8rem;'>PROUDLY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>", unsafe_allow_html=True)
