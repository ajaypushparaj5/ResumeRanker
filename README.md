ResumeRanker 🧠📄

ResumeRanker is a Python-based automation tool that extracts text from PDF resumes, compares skills with a given job description using NLP (spaCy), and ranks candidates based on matching keywords.

🔧 Features
- 📥 Extracts text from multiple resumes (PDF format)
- 🧠 Uses spaCy NLP to identify key skills
- 📄 Compares resumes against a job description
- 📊 Ranks resumes by keyword matches

📁 Project Structure

```
ResumeRanker/                  <-- Root Git repository (your project folder)
│
├── .git/                      <-- Git metadata
├── .gitignore                 <-- Git ignore rules
├── venv/                      <-- Virtual environment (should be ignored)
│
├── ResumeRanker/              <-- Your actual project code (subfolder with same name)
│   ├── __pycache__/           <-- Python bytecode cache (should be ignored)
│   ├── main.py                <-- Main script
│   ├── utility.py             <-- Helper functions
│   ├── resumes/               <-- Folder with sample PDF resumes
│   └── job_description.txt    <-- Job description text
│
└── README.md                  <-- This file
```

⚙️ Requirements
- Python 3.x
- [spaCy](https://spacy.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)

🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ajaypushparaj5/ResumeRanker.git
   cd ResumeRanker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # OR
   source venv/bin/activate  # On Linux/Mac
   ```

3. Install dependencies:
   ```bash
   pip install PyPDF2 spacy
   python -m spacy download en_core_web_sm
   ```

🚀 Usage
Store the Resumes in resumes directory as PDFs.

Run the main script:
```bash
python ResumeRanker/main.py
   ```

📌 Output
* Prints matching skills per resume
* Ranks resumes based on matched keywords

🙌 Author
Ajay Shyam Sundar P