import streamlit as st
import google.generativeai as genai
import time

# የገጹ ርዕስ
st.set_page_config(page_title="Geez Intellect AI", page_icon="📜")
st.title("📜 Ge'ez Intellect AI")

# API Key ማረጋገጫ
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key አልተገኘም!")
    st.stop()

# ሞዴሉን ማዘጋጀት (Flash ሞዴል ለነፃ ተጠቃሚ ይሻላል)
model = genai.GenerativeModel('gemini-1.5-flash', 
                              system_instruction="አንተ የግዕዝ ቋንቋ እና የቅኔ ሊቅ ነህ።")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("የግዕዝ ጥያቄዎን እዚህ ይጻፉ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            # ጥያቄውን ለ AIው መላክ
            response = model.generate_content(prompt)
            message_placeholder.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            # ስህተት ሲፈጠር ለተጠቃሚው የሚታይ መልእክት
            if "429" in str(e) or "ResourceExhausted" in str(e):
                st.error("⚠️ የነፃ ጥያቄዎች መጠን ለጊዜው አልቋል። እባክህ 60 ሰከንድ ታግሰህ ድገመው።")
            else:
                st.error(f"አዝናለሁ፣ ስህተት ተፈጥሯል፦ {e}")
