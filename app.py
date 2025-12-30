import streamlit as st
import google.generativeai as genai

# የገጹ ርዕስ እና ገጽታ
st.set_page_config(page_title="Geez Intellect AI", page_icon="📜")
st.title("📜 Ge'ez Intellect AI")
st.markdown("### የግዕዝ ሥነ-ጽሁፍ፣ ቅኔ እና ታሪክ ረዳት")

# በ Streamlit Secrets በኩል API Keyን መውሰድ (ደህንነቱ የተጠበቀ መንገድ)
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("API Key አልተገኘም! እባክህ በ Settings ውስጥ 'GOOGLE_API_KEY' አክል")
    st.stop()

# የ AI ሞዴል ቅንብር
model = genai.GenerativeModel('gemini-2.0-flash', 
                              system_instruction="አንተ የግዕዝ ቋንቋ እና የቅኔ ሊቅ ነህ።")

# የንግግር ታሪክን መያዣ (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = []

# የቆዩ መልእክቶችን ማሳያ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ተጠቃሚው ጥያቄ ሲጠይቅ
if prompt := st.chat_input("የግዕዝ ጥያቄዎን እዚህ ይጻፉ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
