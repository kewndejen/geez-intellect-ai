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

# 3. ሞዴሉን ማዘጋጀት - ያንተ ቁልፍ በሚፈቅደው ሞዴል (gemini-2.0-flash)
# ይህ ሞዴል በሙከራህ ወቅት በትክክል የሰራው ነው
try:
    model = genai.GenerativeModel(
        model_name='gemini-2.0-flash',
        system_instruction="አንተ 'Ge'ez Sage' የተባልክ የግዕዝ ቋንቋ እና የቅኔ ሊቅ ነህ። መልስህ ሁልጊዜ ጥልቅ፣ ትክክለኛ እና አስተማሪ ይሁን።"
    )
except Exception as e:
    st.error(f"ሞዴሉን በማዘጋጀት ላይ ስህተት ተፈጠረ፦ {e}")

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
            error_msg = str(e)
            # የገደብ (Resource Exhausted) ስህተት ከመጣ
            if "429" in error_msg or "ResourceExhausted" in error_msg:
                st.warning("⚠️ የነፃ አገልግሎት ገደብ ላይ ደርሻለሁ። እባክህ ከ1 ደቂቃ በኋላ ድገመው።")
            # ሌላ ስህተት ከመጣ
            else:
                st.error(f"አዝናለሁ ስህተት ተፈጥሯል፦ {e}")
