import google.generativeai as genai

def initialize_gemini(api_key):
    """Initializes the High-Priest of Logic (Gemini 2.0)"""
    genai.configure(api_key=api_key)
    # Optimized for speed and multimodal reasoning
    return genai.GenerativeModel('gemini-2.0-flash')

def process_ancient_script(image_file):
    """
    Specifically tuned for OCR on images, 
    perfect for the Visual OCR Lab.
    """
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([
        "Act as a master paleographer. Transcribe and translate any text found in this image. "
        "Maintain the original formatting and highlight cultural nuances.", 
        image_file
    ])
    return response.text
