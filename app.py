"""
🔱 GE'EZ STUDIO | Sovereign Masterpiece v-Infinity
Created by: Grand Architect Deacon Kewn Dejen
Description: High-level AI Studio for Ethiopic Studies, 60 Pillars of Wisdom.
"""

import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
from docx import Document
import time
import random
import datetime
import sqlite3
import re
import os
from PIL import Image
import io

# ==================== ክፍል ፩: የገጽ ማዋቀር & CSS ====================
def setup_imperial_theme():
    st.set_page_config(
        page_title="GE'EZ STUDIO | Sovereign Masterpiece",
        page_icon="🔱",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Majestic Emerald & Gold Imperial UI
    imperial_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Montserrat:wght@400;700&family=Abyssinica+SIL&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at center, #004d26 0%, #001a0d 100%); 
        color: #ffffff; 
        font-family: 'Montserrat', sans-serif; 
    }
    
    h1, h2, h3 { 
        font-family: 'Cinzel Decorative', serif; 
        color: #FFD700 !important; 
        text-align: center;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #001a0d 0%, #000a05 100%) !important;
        border-right: 4px solid #FFD700;
    }
    
    .sovereign-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 25px; border-radius: 15px;
        border: 1px solid rgba(255, 215, 0, 0.4);
        border-left: 10px solid #FFD700;
        margin-bottom: 20px;
    }

    .stButton>button {
        background: linear-gradient(45deg, #FFD700 0%, #B8860B 100%) !important;
        color: #000000 !important; font-weight: 900 !important;
        border-radius: 10px !important; height: 3.5em; width: 100%; transition: 0.5s ease;
    }
    
    [data-testid="stChatInput"] { 
        border: 3px solid #FFD700 !important; 
        background-color: #ffffff !important; 
        border-radius: 15px !important; 
    }
    [data-testid="stChatInput"] textarea { color: #000000 !important; font-weight: bold; }
    
    .citation { font-size: 0.85rem; color: #FFD700; border-top: 1px solid #ffffff33; margin-top: 15px; padding-top: 10px; font-family: monospace; }
    </style>
    """
    st.markdown(imperial_css, unsafe_allow_html=True)

# ==================== ክፍል ፪: የሰነድ አሰራር ====================
class GeezDocumentProcessor:
    def extract_text(self, uploaded_file):
        ext = uploaded_file.name.split('.')[-1].lower()
        text = ""
        try:
            if ext == 'pdf':
                reader = PdfReader(uploaded_file)
                for page in reader.pages: text += page.extract_text()
            elif ext in ['docx', 'doc']:
                doc = Document(uploaded_file)
                for para in doc.paragraphs: text += para.text + "\n"
            return text if text.strip() else "No text found."
        except Exception as e:
            return f"Error: {e}"

# ==================== ክፍል ፫: የ AI ሞተር ====================
class SovereignAIEngine:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.available_models = self._discover_models()

    def _discover_models(self):
        try:
            models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            priority = ["models/gemini-1.5-flash", "models/gemini-2.0-flash-exp", "models/gemini-1.5-pro", "models/gemini-pro"]
            return [p for p in priority if p in models] or [models[0]]
        except: return ["models/gemini-1.5-flash"]

    def generate_response(self, prompt, context, tool):
        model_name = self.available_models[0]
        sys_instr = f"""
        You are 'Ge'ez Scholar AI v-Infinity', created by Grand Architect Deacon Kewn Dejen.
        Current Tool: {tool}. Base: 60 Pillars of Wisdom.
        Knowledge Source (PDF/Word): {context[:25000]}
        
        Task: Provide scholarly, direct, and deep analysis. Support Ge'ez/Amharic.
        Tone: Sovereign, ancient, and wise. Avoid fluff.
        """
        
        for model_id in self.available_models:
            try:
                model = genai.GenerativeModel(model_name=model_id, system_instruction=sys_instr)
                # Retry Loop for Quota (429)
                for attempt in range(3):
                    try:
                        response = model.generate_content(prompt)
                        if response and response.text:
                            return {'success': True, 'response': response.text, 'model': model_id}
                    except Exception as e:
                        if "429" in str(e):
                            time.sleep(attempt * 7)
                            continue
                        break
            except: continue
            
        return {'success': False, 'response': "❌ ሊቁ በአሁኑ ሰዓት መዛግብቱን ለመክፈት አልቻሉም።"}

# ==================== ክፍል ፬: የውሂብ አስተዳደር ====================
class GeezDataManager:
    def __init__(self):
        self.db_path = "geez_studio.db"
        self._init_db()
        
    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS messages (role TEXT, content TEXT, timestamp TIMESTAMP)')
            
    def save_chat(self, role, content):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('INSERT INTO messages VALUES (?, ?, ?)', (role, content, datetime.datetime.now()))

# ==================== ክፍል ፭: ዋና አሰራር ====================
def main():
    setup_imperial_theme()
    
    # 🔱 identity
    st.markdown("<h1>🔱 GE'EZ STUDIO v-Infinity</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#FFD700;'>Grand Architect: Deacon Kewn Dejen</p>", unsafe_allow_html=True)

    # API Auth
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
    else:
        st.sidebar.error("API Key Missing in Secrets!")
        st.stop()

    processor = GeezDocumentProcessor()
    ai_engine = SovereignAIEngine(api_key)
    data_manager = GeezDataManager()

    # Sidebar: The Ark of 60 Pillars
    with st.sidebar:
        st.markdown(f"<div style='background:linear-gradient(45deg, #FFD700, #B8860B); padding:10px; border-radius:10px; text-align:center; color:#000; font-weight:bold;'>DEACON KEWN DEJEN</div>", unsafe_allow_html=True)
        st.markdown("---")
        
        # Document Vault
        uploaded_files = st.file_uploader("📂 ሰነድ ይጫኑ (PDF/Word)", type=['pdf', 'docx'], accept_multiple_files=True)
        combined_context = ""
        if uploaded_files:
            for f in uploaded_files:
                combined_context += f"\n[FILE: {f.name}]\n" + processor.extract_text(f)
            st.success(f"✅ {len(uploaded_files)} ሰነዶች ተነበዋል")

        # The 60 Pillars Organization
        pillar = st.selectbox("የጥበብ ምሰሶ", ["Advanced AI Labs", "Archives & Law", "Heritage & Science", "University Hub", "Mysticism & Qene"])
        tools = {
            "Advanced AI Labs": ["Manuscript OCR", "Linguistic Bridge", "Script Authentication", "Root Finder", "Voice of Wisdom"],
            "Archives & Law": ["Universal Library", "Fetha Nagast AI", "Synaxarium Analysis", "Royal Decrees"],
            "Heritage & Science": ["Ancient Medicine", "Archeology Hub", "Heritage Map", "Iconography Vision"],
            "University Hub": ["Bahre Hasab Pro", "Abu Shaker Astronomy", "Numerology Lab"],
            "Mysticism & Qene": ["Sem-na-Worq (Qene)", "St. Yared Zema Lab", "Theology Hub", "Scholar Roleplay"]
        }
        tool = st.radio("Labs", tools[pillar])
        
        if st.button("🔄 REBOOT SYSTEM"):
            st.cache_resource.clear()
            st.rerun()

    # Chat Interface
    if "messages" not in st.session_state: st.session_state.messages = []
    
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"], unsafe_allow_html=True)

    if prompt := st.chat_input(f"Consult the {tool} expert..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(f"<b>{prompt}</b>", unsafe_allow_html=True)

        with st.chat_message("assistant"):
            with st.spinner("ሊቁ መዛግብቱን በጥልቀት እያመሳከረ ነው..."):
                res = ai_engine.generate_response(prompt, combined_context, tool)
                if res['success']:
                    full_res = f"<div>{res['response']}</div><div class='citation'>Source: {res['model']} | Masterpiece v-Infinity</div>"
                    st.markdown(full_res, unsafe_allow_html=True)
                    st.session_state.messages.append({"role": "assistant", "content": full_res})
                    data_manager.save_chat("assistant", res['response'])
                else:
                    st.error(res['response'])

    st.markdown("<br><hr><p style='text-align:center; color:#FFD700;'><b>GE'EZ SCHOLAR AI STUDIO | Grand Architect Deacon Kewn Dejen</b></p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
