import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
import time
from pypdf import PdfReader
from docx import Document
from bs4 import BeautifulSoup
from gtts import gTTS
import base64

# ---------------------------------------------------------
# 1. IMPERIAL CONFIGURATION & THEME
# ---------------------------------------------------------
st.set_page_config(page_title="Ge'ez Scholar AI | Deacon Kewn Dejen", page_icon="🔱", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Montserrat', sans-serif; }
    .stSidebar { background: linear-gradient(180deg, #000c18 0%, #300000 100%) !important; border-right: 5px solid #b8860b; color: white; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #b8860b; }
    .stButton>button { background: linear-gradient(45deg, #d4af37 0%, #8b6b00 100%); color: white; border-radius: 10px; font-weight: 800; width: 100%; }
    .auth-box { background: #fdfdfd; padding: 30px; border-radius: 20px; border: 2px solid #d4af37; box-shadow: 0 10px 40px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. DATA STORAGE & SESSION MANAGEMENT
# ---------------------------------------------------------
if "users" not in st.session_state: st.session_state.users = {"admin": "admin123"} # Mock DB
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "username" not in st.session_state: st.session_state.username = ""
if "chat_history" not in st.session_state: st.session_state.chat_history = []

# ---------------------------------------------------------
# 3. FILE PROCESSING FUNCTIONS (PDF, DOCX, HTML)
# ---------------------------------------------------------
def extract_text(file):
    fname = file.name
    if fname.endswith(".pdf"):
        reader = PdfReader(file)
        return " ".join([page.extract_text() for page in reader.pages])
    elif fname.endswith(".docx"):
        doc = Document(file)
        return " ".join([p.text for p in doc.paragraphs])
    elif fname.endswith(".html"):
        soup = BeautifulSoup(file, "html.parser")
        return soup.get_text()
    return ""

def text_to_speech(text):
    tts = gTTS(text=text[:250], lang='en') # Limits to first 250 chars for speed
    tts.save("response.mp3")
    with open("response.mp3", "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f'<audio controls src="data:audio/mp3;base64,{b64}">'

# ---------------------------------------------------------
# 4. AUTHENTICATION UI
# ---------------------------------------------------------
def auth_page():
    st.markdown("<h1 style='text-align: center;'>🔱 Ge'ez Scholar Login</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        tab1, tab2 = st.tabs(["Login", "Register"])
        with tab1:
            u = st.text_input("Username")
            p = st.text_input("Password", type="password")
            if st.button("Sign In"):
                if u in st.session_state.users and st.session_state.users[u] == p:
                    st.session_state.logged_in = True
                    st.session_state.username = u
                    st.rerun()
                else: st.error("Invalid Credentials")
        with tab2:
            new_u = st.text_input("New Username")
            new_p = st.text_input("New Password", type="password")
            if st.button("Register"):
                st.session_state.users[new_u] = new_p
                st.success("Account Created! Please Login.")

# ---------------------------------------------------------
# 5. MAIN SYSTEM (GE'EZ SCHOLAR CORE)
# ---------------------------------------------------------
if not st.session_state.logged_in:
    auth_page()
else:
    # API Setup
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Sidebar
    with st.sidebar:
        st.markdown(f"### 👑 Welcome, {st.session_state.username}")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
        st.markdown("---")
        portal = st.selectbox("Portals", ["Dashboard", "Neural Research Lab (Upload Files)", "History", "Business Hub"])
        st.image("https://img.icons8.com/clouds/500/crown.png", width=100)

    # PORTAL: DASHBOARD
    if portal == "Dashboard":
        st.title(f"Imperial Dashboard")
        st.markdown(f"<div style='background: #fff; padding: 20px; border-radius: 15px; border-left: 10px solid gold;'><h4>Master Architect: Deacon Kewn Dejen</h4>ይህ ሲስተም ማንኛውንም ፋይል (PDF, Image, Video) የማንበብ እና በድምፅ የመመለስ አቅም አለው።</div>", unsafe_allow_html=True)
        st.image("https://img.icons8.com/clouds/500/shrine.png", width=300)

    # PORTAL: RESEARCH LAB (FILE INTELLIGENCE)
    elif portal == "Neural Research Lab (Upload Files)":
        st.title("🧠 Neural Knowledge Integration")
        uploaded_files = st.file_uploader("Upload PDF, Docx, Images, or Video", accept_multiple_files=True)
        
        context_text = ""
        media_files = []

        if uploaded_files:
            for f in uploaded_files:
                if f.type in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "text/html"]:
                    context_text += f"\n[Document: {f.name}]\n" + extract_text(f)
                    st.success(f"Loaded: {f.name}")
                elif f.type.startswith("image/"):
                    img = Image.open(f)
                    media_files.append(img)
                    st.image(img, caption=f.name, width=200)
                elif f.type.startswith("video/"):
                    st.video(f)
                    st.info("Video loaded for analysis.")

        query = st.text_input("Ask anything about your files...")
        if query:
            with st.spinner("Analyzing across all sources..."):
                prompt = f"Context from uploaded files: {context_text}\n\nUser Question: {query}\n\n(Answer based ONLY on the provided files if relevant. If not, use your Ge'ez knowledge.)"
                inputs = [prompt] + media_files
                response = model.generate_content(inputs)
                
                st.markdown("### AI Response")
                st.write(response.text)
                
                # Voice Output
                st.markdown(text_to_speech(response.text), unsafe_allow_html=True)
                
                # Save History
                st.session_state.chat_history.append({"q": query, "a": response.text, "time": str(datetime.datetime.now())})

    # PORTAL: HISTORY
    elif portal == "History":
        st.title("📜 Chat History")
        for h in st.session_state.chat_history[::-1]:
            with st.expander(f"Query: {h['q']} ({h['time']})"):
                st.write(h['a'])

    # PORTAL: BUSINESS
    elif portal == "Business Hub":
        st.title("💰 Business & Licensing")
        st.markdown(f"""
        <div style='background: #fffdf5; padding: 30px; border-radius: 20px; border: 3px solid #d4af37; text-align: center;'>
            <h3>የዲያቆን ከውን ደጀን የጥበብ ማዕከል</h3>
            <p>የቴሌብር ቁጥር: 09XX XXX XXX</p>
            <p>CBE: 1000XXXXXXXXX</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'><b>PROUDLY DEVELOPED BY DEACON KEWN DEJEN</b></p>", unsafe_allow_html=True)
