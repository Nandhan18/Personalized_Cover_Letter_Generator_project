# 📄 AI Cover Letter Generator

An **AI-powered Cover Letter Generator** built using **Streamlit, PaddleOCR, and Ollama (Phi Model)**.
This application allows users to upload a **Resume and Job Description** in multiple formats and automatically generate a **personalized, ATS-optimized cover letter**.

---

# 🚀 Features

* 📂 Upload **Resume and Job Description**
* 🧾 Supports multiple file formats:

  * PDF
  * DOCX
  * TXT
  * Images (JPG, JPEG, PNG)
* 🔍 Extracts text from images using **PaddleOCR**
* 🤖 Generates personalized cover letters using **Ollama AI (Phi Model)**
* 🎨 Modern **dark-themed Streamlit interface**
* 💬 Chat history support
* ⬇️ Download generated cover letter

---

# 🧠 Technologies Used

* Python
* Streamlit
* PaddleOCR
* Ollama (Phi Model)
* PyPDF2
* python-docx
* Requests

---

# 📂 Project Structure

AI-Cover-Letter-Generator
│
├── new.py
├── requirements.txt
├── .gitignore
├── README.md

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

git clone https://github.com/yourusername/ai-cover-letter-generator.git

cd ai-cover-letter-generator

---

## 2️⃣ Install Python Dependencies

pip install -r requirements.txt

---

## 3️⃣ Install Ollama

Download Ollama from:

https://ollama.com

After installing Ollama, pull the **Phi model**:

ollama pull phi

Start the Ollama server:

ollama serve

---

## 4️⃣ Run the Application

streamlit run new.py

Then open your browser:

http://localhost:8501

---

# 🖥️ How the Application Works

1️⃣ Upload **Resume and Job Description files**

2️⃣ The system extracts text using:

* PyPDF2 → for PDF files
* python-docx → for DOCX files
* PaddleOCR → for images

3️⃣ Extracted content is combined and sent to the **Ollama AI model**

4️⃣ The AI model generates a **professional cover letter**

5️⃣ The user can **view and download the generated letter**

---

# 📌 Requirements

Your `requirements.txt` file should contain:

streamlit
requests
PyPDF2
python-docx
paddleocr
paddlepaddle

Install using:

pip install -r requirements.txt

---

# ⚠️ Important Notes

* **Ollama must be running locally** for AI generation.
* Large image files may take longer because of OCR processing.
* This project runs **locally using Streamlit**.

---

# 💡 Future Improvements

* Export cover letter as **PDF**
* Add **multiple AI model support**
* Resume keyword analysis
* Job compatibility scoring
* Deploy to **Streamlit Cloud or Docker**

---

# 👨‍💻 Author

Developed as part of an **AI-powered automation project using Python and modern AI tools**.

---

# 📜 License

This project is open-source and available under the **MIT License**.
