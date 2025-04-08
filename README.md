# Customizable Resume Generator (PDF)

A command-line Python script that helps you generate a customizable PDF resume. Choose your preferred font size, font color, and background color using simple command-line arguments!

---

##  Features

-  **Generate a stylish resume in PDF**
-  **Customize**:
  - Font size (`--font-size`)
  - Font color (`--font-color` in hex, e.g., `#000000`)
  - Background color (`--background-color` in hex, e.g., `#FFFFFF`)
-  Fetch resume data from an online API or enter manually


---

##  Technologies Used

- Python 
- [`fpdf2`](https://pyfpdf.github.io/fpdf2/) - for creating PDF documents
- `requests` - for API integration

---

##  Installation

```bash
pip install fpdf2 requests


---

##  Usage

###  Basic Command

```bash
python generate_resume.py --font-size 12 --font-color "#000000" --background-color "#FFFFFF"


