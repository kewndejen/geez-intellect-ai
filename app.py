import streamlit as st
import google.generativeai as genai

# 1. የገጹ ገጽታ ቅንብር
st.set_page_config(page_title="Ge'ez Intellect AI", page_icon="📜")
st.title("📜 Ge'ez Intellect AI")
st.markdown("##### የግዕዝ ሥነ-ጽሁፍ፣ ቅኔ እና ታሪክ ረዳት")

# 2. API Keyን ከSecrets መውሰድ
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key አልተገኘም! እባክህ በ Settings ውስጥ 'GOOGLE_API_KEY' አክል")
    st.stop()

# 3. ሞዴሉን ማዘጋጀት (Flash ሞዴል ለነፃ አገልግሎት የተሻለ ነው)
model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction="አንተ 'Ge'ez Sage' የተባልክ የግዕዝ ቋንቋ እና የቅኔ ሊቅ ነህ። መልስህ ሁልጊዜ ጥልቅ እና አስተማሪ ይሁን።"
)

# 4. የንግግር ታሪክ (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. ጥያቄ መቀበያ እና መልስ መስጫ
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
            # ስህተት ሲፈጠር (ለምሳሌ ገደብ ሲያልቅ) የሚታይ መልእክት
            error_msg = str(e)
            if "429" in error_msg or "ResourceExhausted" in error_msg:
                st.warning("⚠️ ይቅርታ፣ በአሁኑ ሰዓት ብዙ ተጠቃሚዎች እያስተናገድኩ ስለሆነ የነፃ አገልግሎት ገደብ ላይ ደርሻለሁ። እባክህ ከ1 ደቂቃ በኋላ በድጋሚ ሞክር።")
            else:
                st.error("አዝናለሁ፣ ያልታወቀ ስህተት ተፈጥሯል። እባክህ ገጹን Refresh አድርገህ ሞክር።")import streamlit as st
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
