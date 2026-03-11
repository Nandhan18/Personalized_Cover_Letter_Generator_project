import os

# 🔥 Fix Paddle 3.x issues
os.environ["FLAGS_use_mkldnn"] = "0"
os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"

import streamlit as st
from datetime import datetime
import requests
import PyPDF2
import docx
from paddleocr import PaddleOCR
import tempfile

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Cover Letter Generator",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- DARK UI CSS (UNCHANGED FROM YOUR DESIGN) ----------------
st.markdown("""
<style>
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}

html, body, [data-testid="stAppViewContainer"], .stApp {
    background: linear-gradient(135deg, #0f172a, #111827) !important;
    min-height: 100vh;
    color: #e2e8f0;
}

section[data-testid="stSidebar"] {
    background-color: #0b1120 !important;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

h1 { color: #3b82f6 !important; }
h2, h3 { color: #60a5fa !important; }

.assistant-box {
    background-color: #1e293b;
    color: #e2e8f0;
    padding: 20px;
    border-radius: 12px;
    border-left: 4px solid #3b82f6;
    line-height: 1.8;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

# ---------------- INIT PADDLE OCR (3.x SAFE) ----------------
@st.cache_resource
def load_ocr():
    return PaddleOCR(
        lang="en",
        use_textline_orientation=True
    )

ocr = load_ocr()

# ---------------- FILE TEXT EXTRACTION ----------------
def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.name.split('.')[-1].lower()

    try:
        # Reset pointer (important for Streamlit)
        uploaded_file.seek(0)

        # TXT
        if file_type == "txt":
            return uploaded_file.read().decode("utf-8", errors="ignore")

        # PDF
        elif file_type == "pdf":
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text

        # DOCX
        elif file_type == "docx":
            doc = docx.Document(uploaded_file)
            return "\n".join([para.text for para in doc.paragraphs])

        # IMAGE → OCR
        elif file_type in ["jpg", "jpeg", "png"]:

            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            result = ocr.ocr(tmp_path)

            text = ""
            if result:
                for page in result:
                    if page:
                        for line in page:
                            if isinstance(line, list) and len(line) > 1:
                                text += line[1][0] + "\n"

            try:
                os.remove(tmp_path)
            except:
                pass

            return text

        else:
            return ""

    except Exception as e:
        return f"\n[Error reading {uploaded_file.name}: {str(e)}]\n"

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("💬 Chat History")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.current_chat = None
        st.rerun()

    st.divider()

    if len(st.session_state.history) == 0:
        st.info("No chats yet")
    else:
        for idx, chat in enumerate(st.session_state.history):
            if st.button(chat["title"], key=idx, use_container_width=True):
                st.session_state.current_chat = idx

# ---------------- MAIN ----------------
st.title("📄 Personalized Cover Letter Generator")
st.caption("Upload Resume + Job Description (Any Format)")

st.divider()

uploaded_files = st.file_uploader(
    "📂 Upload Resume & Job Description Files",
    type=["pdf", "txt", "docx", "jpg", "jpeg", "png"],
    accept_multiple_files=True
)

generate_btn = st.button("🚀 Generate Cover Letter", use_container_width=True)

# ---------------- GENERATE COVER LETTER ----------------
if generate_btn:

    if uploaded_files and len(uploaded_files) >= 2:

        with st.spinner("Reading documents and generating cover letter..."):

            combined_text = ""

            for file in uploaded_files:
                extracted_text = extract_text_from_file(file)
                combined_text += f"\n\n--- File: {file.name} ---\n"
                combined_text += extracted_text

            prompt = f"""
Write a professional, formal, ATS-optimized cover letter.

Use the information extracted from the following documents:

{combined_text}

Make it personalized, concise, and impactful.
"""

            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "phi",
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=120
                )

                if response.status_code == 200:
                    cover_letter = response.json().get("response", "")
                else:
                    cover_letter = "⚠️ Ollama Error: " + response.text

            except Exception as e:
                cover_letter = f"⚠️ Ollama server not running.\n{str(e)}"

        title = f"Generated - {datetime.now().strftime('%H:%M')}"

        st.session_state.history.append({
            "title": title,
            "cover_letter": cover_letter
        })

        st.session_state.current_chat = len(st.session_state.history) - 1

    else:
        st.error("❌ Please upload at least TWO files (Resume + Job Description).")

# ---------------- DISPLAY RESULT ----------------
if st.session_state.current_chat is not None:

    st.divider()

    chat = st.session_state.history[st.session_state.current_chat]

    st.markdown(f"### 📋 {chat['title']}")

    st.markdown(
        f"""
        <div class="assistant-box">
        {chat['cover_letter'].replace(chr(10), '<br>')}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.download_button(
        "⬇️ Download Cover Letter",
        data=chat["cover_letter"],
        file_name="cover_letter.txt",
        mime="text/plain",
        use_container_width=True
    )