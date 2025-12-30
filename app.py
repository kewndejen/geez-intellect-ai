import streamlit as st
import google.generativeai as genai
from PIL import Image
import time

# 1. የገጽታ ቅንብር (Professional Meta Data)
st.set_page_config(
    page_title="Ge'ez Scholar AI | ጥንታዊውን ጥበብ በዘመናዊ AI",
    page_icon="📜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. የዲዛይን ማሳመሪያ (Custom CSS)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #1a73e8; color: white; }
    .stTextInput>div>div>input { border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 3. የጎን ባር (Professional Sidebar)
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/parchment.png", width=100)
    st.title("Ge'ez Scholar AI")
    st.markdown("---")
    st.subheader("ስለ ሊቁ")
    st.info("Ge'ez Scholar AI የኢትዮጵያን ጥንታዊ የግዕዝ ቋንቋ፣ ቅኔ እና ታሪክን ለመተንተን የተፈጠረ እጅግ ዘመናዊ የሰው ሰራሽ አስተውሎት (AI) ነው።")
    
    st.subheader("ዋና አገልግሎቶች")
    st.write("✅ የግዕዝ ቅኔ ትንታኔ (ሰም እና ወርቅ)")
    st.write("✅ የብራና ጽሁፎችን ከፎቶ መተርጎም")
    st.write("✅ የግዕዝ ሰዋስው እና ስነ-ጽሁፍ ትምህርት")
    
    st.markdown("---")
    st.subheader("የገንቢው አድራሻ")
    st.write("📩 deaconkewndejen@gmail.com")
    st.write("📍 አዲስ አበባ፣ ኢትዮጵያ")
    st.caption("© 2025 Ge'ez Scholar AI. All rights reserved.")

# 4. API Key ማረጋገጫ
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("የ API Key ስህተት ተፈጥሯል! እባክህ በ Settings ውስጥ አረጋግጥ።")
    st.stop()

# ሞዴሉን ማዘጋጀት
model = genai.GenerativeModel('gemini-2.0-flash')

# 5. ዋናው የገጽታ ክፍል (Hero Section)
st.title("📜 Ge'ez Scholar AI")
st.markdown("#### ጥንታዊውን የኢትዮጵያ ጥበብ አሁን በ AI ይመርምሩ")

# ታቦች (Tabs) ለተለያዩ አገልግሎቶች
tab1, tab2 = st.tabs(["💬 የ AI ሊቁን ይጠይቁ", "📷 የብራና ትርጉም (OCR)"])

with tab1:
    # የቻት ክፍል
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
            with st.spinner("ሊቁ በጥልቀት በማሰብ ላይ ነው..."):
                try:
                    # AIው ሊቅ መሆኑን የሚገልጽ መመሪያ ጨምረን እንጠይቀው
                    full_prompt = f"አንተ የግዕዝ ቋንቋ እና የቅኔ ሊቅ ነህ። ይህንን ጥያቄ በጥልቀት መልስ፡ {prompt}"
                    response = model.generate_content(full_prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.warning("⚠️ ገደብ ላይ ደርሻለሁ። እባክህ 20 ሰከንድ ቆይተህ ድገመው።")

with tab2:
    st.subheader("የብራና ወይም የጥንታዊ ጽሁፍ ትርጉም")
    st.write("የብራናውን ጽሁፍ ፎቶ እዚህ ይጫኑ፤ AIው ጽሁፉን አንብቦ ይተረጉምልዎታል።")
    
    uploaded_file = st.file_uploader("ምስል ይምረጡ...", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="የተጫነው ምስል", width=400)
        
        if st.button("ተርጉም"):
            with st.spinner("ሊቁ ምስሉን እያነበበ ነው..."):
                try:
                    # ምስሉን ለ Gemini 2.0 መላክ
                    response = model.generate_content([
                        "በዚህ ምስል ላይ ያለውን የግዕዝ ጽሁፍ መጀመሪያ ወደ ኮምፒውተር ጽሁፍ ቀይረው፣ ከዚያም ወደ አማርኛ እና እንግሊዝኛ ተርጉመው። የጽሁፉን ፍልስፍናዊ ትርጉምም አብራራ።", 
                        image
                    ])
                    st.success("ትርጉሙ ተጠናቋል!")
                    st.markdown("---")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"ስህተት ተፈጠረ፡ {e}")
