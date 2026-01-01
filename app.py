import streamlit as st
import google.generativeai as genai
import time
import os
from PIL import Image
import PyPDF2
from docx import Document
from gtts import gTTS
import io

# ---------------------------------------------------------
# 1. IMPERIAL PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Ge'ez Scholar AI Studio | Deacon Kewn Dejen",
    page_icon="🔱",
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&display=swap');
    .stApp { background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); color: #ffffff; }
    h1, h2, h3 { font-family: 'Cinzel Decorative', serif; color: #FFD700 !important; text-align: center; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important; border-right: 4px solid #FFD700; }
    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000 !important; font-weight: 900 !important; border-radius: 12px !important;
    }
    .auth-card { background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; border: 1px solid #FFD700; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. SESSION STATE
# ---------------------------------------------------------
if 'users' not in st.session_state: st.session_state.users = {"admin": "kewn123"}
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'username' not in st.session_state: st.session_state.username = ""
if 'history' not in st.session_state: st.session_state.history = {}

# ---------------------------------------------------------
# 3. AI SOVEREIGN ENGINE (Resilient Logic)
# ---------------------------------------------------------
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key Missing!")
    st.stop()

def ask_ai_master(prompt, context="", file_data=None, mime=None):
    # የሚሰሩ ሞዴሎች ዝርዝር በቅደም ተከተል
    model_list = ["gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"]
    full_prompt = f"System: You are 'Ge'ez Scholar AI' created by Deacon Kewn Dejen. Context: {context}\n\nUser Question: {prompt}"
    
    last_error = ""
    for model_name in model_list:
        try:
            model = genai.GenerativeModel(model_name=model_name)
            # 429 ስህተት ከመጣ 3 ጊዜ ደጋግሞ ይሞክራል
            for attempt in range(3):
                try:
                    if file_data and mime:
                        response = model.generate_content([full_prompt, {'mime_type': mime, 'data': file_data}])
                    else:
                        response = model.generate_content(full_prompt)
                    return response.text, model_name
                except Exception as e:
                    if "429" in str(e):
                        time.sleep(5) # 5 ሰከንድ ይጠብቃል
                        continue
                    raise e
        except Exception as e:
            last_error = str(e)
            continue # ወደሚቀጥለው ሞዴል ይሸጋገራል
            
    return f"ሊቁ በአሁኑ ሰዓት ተጨናንቀዋል። ገደብዎ አልቋል፣ እባክዎ ጥቂት ደቂቃ ቆይተው ይሞክሩ። (ስህተት: {last_error})", "None"

# ---------------------------------------------------------
# 4. FILE & UI UTILS
# ---------------------------------------------------------
def extract_text(uploaded_file):
    name = uploaded_file.name.lower()
    try:
        if name.endswith('.pdf'):
            reader = PyPDF2.PdfReader(uploaded_file)
            return " ".join([page.extract_text() for page in reader.pages])
        elif name.endswith('.docx'):
            doc = Document(uploaded_file)
            return " ".join([p.text for p in doc.paragraphs])
    except: return ""
    return ""

# ---------------------------------------------------------
# 5. SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>")
    if not st.session_state.logged_in:
        st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
        mode = st.radio("Access", ["Login", "Register"])
        u = st.text_input("User")
        p = st.text_input("Pass", type="password")
        if st.button("Enter"):
            if mode == "Login":
                if u in st.session_state.users and st.session_state.users[u] == p:
                    st.session_state.logged_in, st.session_state.username = True, u
                    st.rerun()
                else: st.error("Wrong info")
            else:
                st.session_state.users[u] = p
                st.success("Registered!")
        st.markdown("</div>", unsafe_allow_html=True)
        st.stop()
    else:
        st.write(f"👑 Emperor: **{st.session_state.username}**")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
    
    st.markdown("---")
    tool = st.radio("System Tools", ["Document Analyzer", "Manuscript OCR", "Voice Assistant"])

# ---------------------------------------------------------
# 6. MAIN SYSTEM
# ---------------------------------------------------------
if st.session_state.logged_in:
    st.title(f"{tool} Center")

    with st.expander("📁 Upload File"):
        up_file = st.file_uploader("Upload PDF, DOCX, Image", type=['pdf', 'docx', 'png', 'jpg', 'jpeg'])
        doc_context, f_bytes, f_mime = "", None, None
        if up_file:
            if up_file.type in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
                doc_context = extract_text(up_file)
                st.success("Document Memorized.")
            else:
                f_bytes, f_mime = up_file.read(), up_file.type
                st.info("Image/Media Ready.")

    if st.session_state.username not in st.session_state.history:
        st.session_state.history[st.session_state.username] = []

    for chat in st.session_state.history[st.session_state.username]:
        with st.chat_message(chat["role"]): st.markdown(chat["content"])

    voice_on = st.checkbox("🎙️ Voice Response")
    
    if prompt := st.chat_input("Ask the AI..."):
        st.session_state.history[st.session_state.username].append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
                answer, engine = ask_ai_master(prompt, doc_context, f_bytes, f_mime)
                st.markdown(answer)
                if voice_on:
                    try:
                        tts = gTTS(text=answer[:300], lang='en')
                        audio_io = io.BytesIO()
                        tts.write_to_fp(audio_io)
                        st.audio(audio_io, format='audio/mp3')
                    except: pass
                st.session_state.history[st.session_state.username].append({"role": "assistant", "content": answer})

st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Deacon Kewn Dejen</b></p>", unsafe_allow_html=True)
