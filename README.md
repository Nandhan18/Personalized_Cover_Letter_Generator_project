# 📄 AI Cover Letter Generator

An **AI-powered assistant** that transforms the job application process. By analyzing your **Resume** against a **Job Description**, this tool generates a personalized, ATS-optimized cover letter in seconds using the lightning-fast **Groq inference engine**.

---

## 🚀 Live Demo

Check out the live application here: **[project Link](https://personalizedcoverlettergeneratorproject.streamlit.app/)**

---

## ✨ Features

* **Smart Ingestion:** Upload Resumes and JDs in **PDF, DOCX, TXT**, or **Image** formats.
* **OCR Powered:** Integrated **Tesseract OCR** to extract text from scanned documents and images (`JPG`, `PNG`).
* **Llama 3.3 70B Intelligence:** Leverages the **Groq API** for high-speed, high-quality professional writing.
* **ATS Optimization:** Specifically engineered prompts to highlight keyword alignment and skills.
* **Modern UI:** A sleek, dark-themed interface built with **Streamlit**.
* **Secure:** Built-in support for Streamlit Secrets to keep your API keys safe.

---

## 🧠 Technologies Used

| Technology | Purpose |
| --- | --- |
| **Streamlit** | Web interface and UI components |
| **Groq API** | Ultra-fast AI inference engine |
| **Llama 3.3 70B** | Advanced LLM for professional content generation |
| **Tesseract OCR** | Optical Character Recognition for image-based files |
| **PyPDF2 / Docx** | Document parsing and text extraction |
| **Python** | Core application logic |

---

## 📂 Project Structure

```text
AI-Cover-Letter-Generator
│
├── .streamlit/
│   ├── config.toml         # UI Configuration
│   └── secrets.toml        # API Keys (Local only)
├── new.py                  # Main Application logic
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
├── .gitignore              # Files to exclude from Git
└── LICENSE                 # MIT License

```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-cover-letter-generator.git
cd ai-cover-letter-generator

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt

```

*Note: Ensure [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) is installed on your system.*

### 3. Configure API Keys

Create a `.streamlit/secrets.toml` file in the root directory:

```toml
GROQ_API_KEY = "your_groq_api_key_here"

```

### 4. Run the Application

```bash
streamlit run new.py


## 🖥️ How It Works

1. **Upload:** Provide your Resume and the Job Description.
2. **Extract:** The app parses text using `PyPDF2`, `python-docx`, or `pytesseract` based on file type.
3. **Analyze:** The extracted text is sent to **Llama 3.3 70B** via Groq.
4. **Generate:** A professional cover letter is synthesized, focusing on matching your experience to the job requirements.
5. **Export:** Review the result on-screen and download it for your application.

---



## 💡 Future Improvements

* [ ] **Match Scoring:** Visual compatibility percentage between Resume and JD.
* [ ] **Multi-Language:** Support for generating letters in different languages.
* [ ] **Feedback Loop:** AI-driven suggestions to improve your resume.

---

## 👨‍💻 Author

**Velugu Athrinandhan**
*B.Tech CSIT Student | Python  Developer | AI Enthusiast*

---

## 📜 License

This project is licensed under the **MIT License**.

⭐ Support

If you like this project, please star the repository on GitHub ⭐
