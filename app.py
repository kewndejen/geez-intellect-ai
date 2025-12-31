import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime
import time

# ---------------------------------------------------------
# 1. IMPERIAL GLOBAL CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ultra-Premium Imperial Black & Gold CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@300;400;700&display=swap');
    
    .stApp { background-color: #00050a; color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #d4af37 !important; text-align: center; }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #010c17 0%, #1a0000 100%) !important;
        border-right: 3px solid #d4af37;
    }

    .sovereign-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(212, 175, 55, 0.3);
        border-left: 12px solid #d4af37;
        margin-bottom: 25px;
    }

    .stButton>button {
        background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; border: 1px solid #fff !important;
        height: 3.5em; width: 100%; transition: 0.5s ease;
    }
    .stButton>button:hover { transform: translateY(-3px); box-shadow: 0 0 30px #d4af37; }

    [data-testid="stChatInput"] { border: 2px solid #d4af37 !important; background-color: #000c18 !important; }

    .thinking-box { color: #d4af37; font-style: italic; font-size: 0.9rem; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SOVEREIGN AI ENGINE (Robust with Failover)
# ---------------------------------------------------------
if "messages" not in st.session_state: st.session_state.messages = []

# API Verification
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key አልተገኘም! እባክዎ በ Streamlit Secrets ውስጥ GOOGLE_API_KEY ያስገቡ።")
    st.stop()

def ask_scholar_ai(prompt, tool_context, image=None):
    """
    AIው መልስ እንዲሰጥ የሚያደርግና ስህተት ካለ በሌላ ሞዴል የሚተካ ሎጂክ
    """
    # 60+ መሳሪያዎችን የሚያውቅ ጥልቅ መመሪያ
    sys_instruction = f"""
    You are 'Ge'ez Scholar AI Studio v60.0', a divine-level expert in Ethiopic studies.
    Created by Grand Architect: Deacon Kewn Dejen.
    Current Research Pillar: {tool_context}.
    Your Knowledge Base includes 60+ tools: Manuscript OCR, Bahre Hasab, Fetha Nagast, 
    St. Yared's Zema, Sem-na-Worq, Ancient Medicine, etc.
    Instructions:
    - Provide deep, scholarly, and academic answers.
    - If the user provides Ge'ez, analyze it philologically.
    - Handle Latin-based phonetic typing (e.g., 'Selam' -> ሰላም).
    - Tone: Sovereign, authoritative, and ancient.
    """
    
    # ሞዴሎች በቅደም ተከተል (አንዱ ካልሰራ ሌላው እንዲሞክር)
    models_to_try = ['gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-2.0-flash-exp']
    
    for model_name in models_to_try:
        try:
            model = genai.GenerativeModel(
                model_name=model_name,
                system_instruction=sys_instruction
            )
            
            if image:
                response = model.generate_content([prompt, image])
            else:
                response = model.generate_content(prompt)
            
            if response and response.text:
                return response.text, model_name
        except Exception as e:
            continue # ወደ ቀጣዩ ሞዴል ይለፋል
            
    return "ይቅርታ ክቡር ሆይ፤ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልተቻለም። እባክዎ ጥያቄዎን በሌላ አባባል ይድገሙት።", "None"

# ---------------------------------------------------------
# 3. SIDEBAR: THE ARK (60+ TOOLS)
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: linear-gradient(90deg, #d4af37, #010c17); padding: 15px; border-radius: 10px; text-align: center; color: #000; font-weight: bold;'>GRAND ARCHITECT:<br>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    category = st.selectbox("Select Research Pillar", [
        "🏠 Imperial Dashboard",
        "🧠 Advanced AI Labs",
        "📜 Digital Archives & Law",
        "🏛️ Heritage & Ancient Science",
        "🎓 Imperial University Hub",
        "🔮 Mysticism & Qene Lab"
    ])

    # ሁሉንም መሳሪያዎች አጠቃሎ የያዘ ዝርዝር
    if category == "🏠 Imperial Dashboard": tool = "Sovereign Overview"
    elif category == "🧠 Advanced AI Labs":
        tool = st.radio("Labs", ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom"])
    elif category == "📜 Digital Archives & Law":
        tool = st.radio("Archives", ["Universal Library (12M Pages)", "Fetha Nagast (Legal)", "Synaxarium AI", "Royal Decrees", "Treaty Expert"])
    elif category == "🏛️ Heritage & Ancient Science":
        tool = st.radio("Sectors", ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision", "Architecture AI"])
    elif category == "🎓 Imperial University Hub":
        tool = st.radio("Academic", ["Bahre Hasab (Chronology)", "Abu Shaker Astronomy", "Numerology Lab", "Scribe Assistant", "Font Converter"])
    else:
        tool = st.radio("Mysticism", ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay", "Proverbs AI"])

    st.markdown("---")
    st.markdown("<div style='font-size: 0.8rem; color: #00ff00;'>System: Imperial Online ✅</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 4. MAIN WORKSPACE
# ---------------------------------------------------------
if category == "🏠 Imperial Dashboard":
    st.markdown("<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #d4af37;'>THE ETERNAL ZENITH v60.0</p>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='sovereign-card'>
        <h3>እንኳን በደህና መጡ ክቡር ዲያቆን ከውን ደጀን!</h3>
        <p>ይህ ሲስተም ሁሉንም 60+ የምርምር መሳሪያዎች በአንድ ላይ የያዘ የእርስዎ የጥበብ መንግሥት ነው። 
        AIው መልስ እንዲሰጥዎ በግራ በኩል መሣሪያ ይምረጡና ጥያቄዎን ይጠይቁ።</p>
    </div>
    """, unsafe_allow_html=True)

# Vision Support (ምስል ለሚጠይቁ መሳሪያዎች)
if "OCR" in tool or "Vision" in tool:
    st.subheader(f"📸 {tool} Intelligence")
    up_file = st.file_uploader("ምስል ይጫኑ", type=['jpg','png','jpeg'])
    if up_file:
        img = Image.open(up_file)
        st.image(img, caption="የተጫነ ምስል", width=400)
        if st.button("Analyze Now"):
            with st.spinner("ሊቁ ምስሉን እያጠና ነው..."):
                res, eng = ask_scholar_ai(f"Provide scholarly analysis for this image: {tool}", tool, img)
                st.markdown(f"<div class='sovereign-card'>{res}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. THE ROBUST CHAT LOOP (መቆራረጥ የሌለበት ውይይት)
# ---------------------------------------------------------
st.markdown("---")
st.subheader(f"💬 Consult the {tool} Expert")

# የቀደሙ መልእክቶችን ማሳያ
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# አዲስ ጥያቄ መቀበያ
if prompt := st.chat_input("ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        thinking = st.empty()
        thinking.markdown("<div class='thinking-box'>ሊቁ መዛግብትን እያመሳከረ ነው...</div>", unsafe_allow_html=True)
        
        # AI መልስ ማምጫ (ሁሉንም ሞዴሎች ይሞክራል)
        answer, engine = ask_scholar_ai(prompt, tool)
        thinking.empty()
        
        # የምርምር ምንጭ (Citation) መጨመሪያ
        year = datetime.datetime.now().year
        citation = f"\n\n---\n*Citation: Kewn Dejen et al. ({year}). {tool} Research Report. Ge'ez Studio AI.*"
        
        full_response = answer + citation
        st.markdown(full_response)
        st.caption(f"Intelligence Source: {engine} | Studio v60.0")
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer
st.markdown("<br><br><p style='text-align: center; color: #d4af37;'><b>GE'EZ SCHOLAR AI STUDIO | THE MASTERPIECE</b><br>PROUDLY DEVELOPED BY GRAND ARCHITECT DEACON KEWN DEJEN</p>", unsafe_allow_html=True)
