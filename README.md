# Customizable Resume Generator (PDF)

A command-line Python script that helps you generate a customizable PDF resume. Choose your preferred font size, font color, and background color using simple command-line arguments!

---

##  How It Runs (Flow)

1. Run the script using Python.
2. You will be asked:  
   **"Do you want to fetch resume from API? (y/n)"**
   - Type `y` to auto-fetch your resume using your name.
   - Type `n` to enter resume data manually.
3. If you choose API, you'll be asked to enter your name.
4. Once data is fetched or manually entered, the PDF will be generated automatically with the provided styles.

---

##  Features

- Generate a clean and modern resume in PDF format
- Command-line **customization options**:
  - Font size (`--font-size`)
  - Font color (`--font-color` in hex, e.g., `#000000`)
  - Background color (`--background-color` in hex, e.g., `#FFFFFF`)
- Fetch resume data from an **online API** or enter manually


---

##  Project Setup

1. **Clone the repository**

```bash
git clone https://github.com/reshmibodepudi/resume-generator.git
cd resume-generator
```
2. **Install dependencies**

```bash
pip install fpdf2 requests
```
3. **Run the script**

```bash
python generate_resume.py --font-size 12 --font-color "#000000" --background-color "#FFFFFF"
```

---

##  Installation

```bash
pip install fpdf requests
