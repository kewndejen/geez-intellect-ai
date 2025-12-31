import streamlit as st
import google.generativeai as genai
import datetime

# 🔱 1. IMPERIAL PAGE SETUP
st.set_page_config(page_title="Ge'ez Scholar AI Studio", page_icon="🔱", layout="wide")

# Professional Navy & Gold Theme
st.markdown("""
    <style>
    .stApp { background-color: #001f3f; color: #ffffff; font-family: 'Montserrat', sans-serif; }
    h1 { color: #FFD700 !important; text-align: center; font-family: 'Cinzel Decorative', serif; }
    [data-testid="stSidebar"] { background-color: #001226 !important; border-right: 3px solid #D4AF37; }
    .sovereign-card { background: rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 15px; border: 1px solid #D4AF37; }
    [data-testid="stChatInput"] { border: 2px solid #D4AF37 !important; background-color: #ffffff !important; border-radius: 10px; }
    [data-testid="stChatInput"] textarea { color: #000000 !important; }
    </style>
    """, unsafe_allow_html=True)

# 🔱 2. THE ENGINE (Gemini 1.5 Flash Only)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key አልተገኘም!")

def ask_geez_scholar(prompt, tool):
    # ሆን ብለን 1.5-flashን ብቻ እንጠቀማለን (429ን ለመከላከል)
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=f"You are Ge'ez Scholar AI created by Deacon Kewn Dejen. Expert in {tool}."
    )
    try:
        response = model.generate_content(prompt)
        return response.text, "gemini-1.5-flash"
    except Exception as e:
        # ስህተቱን በግልጽ እንዲያሳየን እናደርጋለን
        return f"❌ የቴክኒክ ስህተት፦ {str(e)}", "None"

# 🔱 3. SIDEBAR & UI
with st.sidebar:
    st.markdown("<h1>🔱 GE'EZ STUDIO</h1>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center; color:#FFD700;'>GRAND ARCHITECT: DEJ. KEWN DEJEN</div>", unsafe_allow_html=True)
    st.markdown("---")
    tool = st.selectbox("መሣሪያ ይምረጡ", ["Qene Analysis", "Manuscript OCR", "Bahre Hasab", "Fetha Nagast"])

st.markdown(f"<h1>GE'EZ SCHOLAR AI STUDIO</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state: st.session_state.messages = []
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

if prompt := st.chat_input("ጥያቄዎን እዚህ ያስገቡ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        answer, engine = ask_geez_scholar(prompt, tool)
        st.markdown(answer)
        st.caption(f"Engine: {engine} | v1900.0")
        st.session_state.messages.append({"role": "assistant", "content": answer})
