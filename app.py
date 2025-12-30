import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. ገጽታ ቅንብር
st.set_page_config(page_title="Ge'ez Scholar AI", page_icon="📜", layout="wide")

# 2. Sidebar (የጎን ባር)
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/parchment.png")
    st.title("Ge'ez Scholar")
    st.info("ይህ በ AI የታገዘ የግዕዝ ሥነ-ጽሁፍ፣ ቅኔ እና የታሪክ ተመራማሪ ረዳት ነው።")
    st.write("---")
    st.subheader("አገልግሎቶች")
    st.write("- የግዕዝ ቅኔ ትንታኔ")
    st.write("- የብራና ትርጉም")
    st.write("- የግዕዝ ሰዋስው")
    st.write("---")
    st.write("📩 ለድጋፍ: deaconkewndejen@gmail.com")

# 3. ዋናው ገጽ
st.title("📜 Ge'ez Scholar AI")
st.subheader("ጥንታዊውን ጥበብ በዘመናዊ AI")

# API Key
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("API Key አልተገኘም!")
    st.stop()

model = genai.GenerativeModel('gemini-2.0-flash')

# 4. ፎቶ/ብራና መጫኛ (ለትርጉም)
uploaded_file = st.file_uploader("የብራና ወይም የጽሁፍ ፎቶ እዚህ ይጫኑ...", type=['png', 'jpg', 'jpeg'])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="የተጫነው ምስል", width=300)
    if st.button("ምስሉን ተርጉም"):
        with st.spinner("ሊቁ በማሰብ ላይ ነው..."):
            response = model.generate_content(["ይህንን ምስል በዝርዝር ተርጉምልኝ እና አብራራው", img])
            st.write("---")
            st.write(response.text)

# 5. የቻት ክፍል
st.write("---")
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
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.warning("⚠️ ገደብ ላይ ደርሻለሁ። እባክህ 20 ሰከንድ ቆይተህ ድገመው።")
