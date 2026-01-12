This is an impressive and beautifully designed Ge'ez/AI scholarly application! I can see it's a comprehensive platform for Ethiopian historical, linguistic, and cultural research with a stunning visual theme. Let me provide some observations and suggestions for enhancement:
Strengths:

    Beautiful Design - The emerald green and gold theme with Ethiopian aesthetics is excellent

    Comprehensive Features - 60+ tools organized into logical pillars

    Robust Architecture - Retry logic, model fallback, and document processing

    Multilingual Support - Ge'ez/Amharic integration

Suggestions for Enhancement:
1. Security & Configuration
python

# Add API key input for users without secrets configured
if "GOOGLE_API_KEY" not in st.secrets:
    api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")
    if api_key:
        genai.configure(api_key=api_key)
    else:
        st.warning("Please enter your Gemini API key")
        st.stop()

2. Enhanced Document Processing
python

def extract_enhanced_text(uploaded_file):
    """Better text extraction with error handling"""
    ext = uploaded_file.name.split('.')[-1].lower()
    text = ""
    
    try:
        if ext == 'pdf':
            reader = PdfReader(uploaded_file)
            for i, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text.strip():
                    text += f"\n[PAGE {i+1}]\n{page_text}\n"
                else:
                    # Try OCR fallback suggestion
                    text += f"\n[PAGE {i+1} - Image/Scanned content detected]\n"
                    
        elif ext in ['docx', 'doc']:
            doc = Document(uploaded_file)
            for i, para in enumerate(doc.paragraphs):
                if para.text.strip():
                    text += para.text + "\n"
                    
        return text if text.strip() else "No extractable text found"
        
    except Exception as e:
        st.error(f"Error processing {uploaded_file.name}: {str(e)}")
        return ""

3. Add Session State Management
python

# Initialize session state more comprehensively
if "messages" not in st.session_state:
    st.session_state.messages = []
if "global_memory" not in st.session_state:
    st.session_state.global_memory = ""
if "file_names" not in st.session_state:
    st.session_state.file_names = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_model" not in st.session_state:
    st.session_state.current_model = ACTIVE_MODELS[0] if ACTIVE_MODELS else None

4. Add Export Capabilities
python

# In sidebar, add export options
with st.sidebar:
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Export Chat"):
            chat_text = "\n".join([f"{m['role']}: {m['content']}" 
                                 for m in st.session_state.messages])
            st.download_button("Download Chat", chat_text, "geez_chat.txt")
    with col2:
        if st.button("📊 Clear Chat"):
            st.session_state.messages = []
            st.rerun()

5. Add Progress Tracking
python

# Track usage and provide feedback
if "usage_count" not in st.session_state:
    st.session_state.usage_count = 0

def increment_usage():
    st.session_state.usage_count += 1
    if st.session_state.usage_count % 10 == 0:
        st.balloons()  # Celebrate milestones

6. Improve Model Selection Logic
python

def get_optimal_model(question_length, tool_context):
    """Select model based on task complexity"""
    if question_length > 1000 or "translation" in tool_context.lower():
        return "models/gemini-1.5-pro"
    elif "analysis" in tool_context.lower() or "research" in tool_context.lower():
        return "models/gemini-1.5-flash"
    else:
        return ACTIVE_MODELS[0] if ACTIVE_MODELS else "models/gemini-pro"

7. Add Ge'ez Character Support
python

# Ensure proper Unicode handling for Ge'ez characters
def validate_geez_text(text):
    """Check for Ge'ez script characters"""
    geez_range = '\u1200-\u137F'  # Ethiopic Unicode range
    import re
    geez_chars = re.findall(f'[{geez_range}]', text)
    return len(geez_chars) > 0

8. Add Loading States with Ethiopian Symbols
python

# Replace generic spinner with themed one
def show_geez_spinner(message):
    symbols = ["፩", "፪", "፫", "፬", "፭", "፮", "፯", "፰", "፱", "፲"]
    placeholder = st.empty()
    for i in range(10):
        placeholder.markdown(
            f"<div style='text-align:center; color:#FFD700; font-size:24px;'>"
            f"{symbols[i]} {message}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.2)
    placeholder.empty()

9. Add File Preview Feature
python

# In the document vault section
if uploaded_files and st.session_state.global_memory:
    with st.expander("🔍 Preview Document Content", expanded=False):
        preview_text = st.session_state.global_memory[:2000] + "..." \
            if len(st.session_state.global_memory) > 2000 \
            else st.session_state.global_memory
        st.text_area("Extracted Text", preview_text, height=200)

10. Error Recovery Enhancement
python

def resilient_ask_scholar(prompt, tool_context, document_archive=""):
    """Enhanced error recovery with multiple strategies"""
    max_retries = 3
    base_delay = 2
    
    for retry in range(max_retries):
        try:
            answer, engine = ask_sovereign_scholar(prompt, tool_context, document_archive)
            if "❌" not in answer:  # Success
                return answer, engine
        except Exception as e:
            if retry == max_retries - 1:
                return f"System unavailable after {max_retries} attempts. Please try later.", "Error"
            time.sleep(base_delay * (2 ** retry))  # Exponential backoff
    
    return "Service temporarily unavailable. Please refresh and try again.", "None"

Quick Fix for Immediate Issues:

    Add requirements.txt:

txt

streamlit>=1.28.0
google-generativeai>=0.3.0
PyPDF2>=3.0.0
python-docx>=1.1.0

    Add model configuration:

python

# Configure generation parameters
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
]

This is already a very sophisticated application. The suggestions above would make it even more robust, user-friendly, and feature-complete while maintaining its beautiful Ethiopian aesthetic. The combination of cultural heritage preservation with modern AI technology is particularly impressive!
