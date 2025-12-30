import streamlit as st
import google.generativeai as genai
import time

# 1. የገጹ ገጽታ
st.set_page_config(page_title="Geez Intellect AI", page_icon="📜")
st.title("📜 Ge'ez Intellect AI")
st.markdown("##### የግዕዝ ሥነ-ጽሁፍ፣ ቅኔ እና ታሪክ ረዳት")

# 2. API Key (ከSecrets)
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key አልተገኘም!")
    st.stop()

# 3. ሞዴል መረጣ ( gemini-2.0-flash ለነፃ አገልግሎት ምርጥ ነው)
model = genai.GenerativeModel(
    model_name='gemini-2.0-flash',
    system_instruction="አንተ 'Ge'ez Sage' የተባልክ የግዕዝ ቋንቋ እና የቅኔ ሊቅ ነህ። መልስህ ጥልቅ እና አስተማሪ ይሁን።"
)

# 4. የንግግር ታሪክ
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. ጥያቄ እና መልስ
if prompt := st.chat_input("የግዕዝ ጥያቄዎን እዚህ ይጻፉ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # AI መልስ እንዲሰጥ መጠየቅ
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            if "429" in str(e):
                st.warning("⚠️ ይቅርታ፣ AIው ለጊዜው ተጨናንቋል። እባክህ 20 ሰከንድ ቆይተህ ገጹን Refresh አድርገህ ድገመው።")
            else:
                st.error(f"ስህተት ተፈጥሯል፦ {e}")
