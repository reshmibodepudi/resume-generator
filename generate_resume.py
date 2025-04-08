from fpdf import FPDF
import argparse
import requests

class ResumeGenerator(FPDF):
    def header(self):
        self.set_fill_color(*self.bg_color)
        self.rect(0, 0, 210, 297, 'F')
        self.set_font('Arial', 'B', 20)
        self.set_text_color(*self.font_color)
        self.cell(0, 10, self.name, ln=True, align='C')

        self.set_font('Arial', '', self.font_size_custom)
        self.set_text_color(50, 50, 50)

        line_1_parts = [self.email, self.phone]
        contact_line_1 = " | ".join(part for part in line_1_parts if part)
        self.cell(0, 6, contact_line_1, ln=True, align='C')

        line_2_parts = [self.address, self.twitter, self.linkedin, self.github]
        contact_line_2 = " | ".join(part for part in line_2_parts if part)
        self.multi_cell(0, 4, contact_line_2, align='C')
        self.ln(3)

    def section_title(self, title):
        self.set_draw_color(0, 102, 204)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)

        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 102, 204)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def section_body(self, items, bullet_points=True, section=""):
        self.set_font('Arial', '', self.font_size_custom)
        self.set_text_color(*self.font_color)

        for item in items:
            if isinstance(item, dict):
                title = item.get('title', '')
                start = item.get('startDate', '')
                end = item.get('endDate', '')
                duration = f"{start} to {end}" if start and end else ''

                if title:
                    self.set_font('Arial', 'B', self.font_size_custom)
                    if section == "PROJECTS" and duration:
                        x_before = self.get_x()
                        y_before = self.get_y()
                        self.cell(140, 8, title, ln=0)
                        self.set_font('Arial', '', self.font_size_custom - 1)
                        self.cell(0, 8, duration, ln=1, align='R')
                        self.set_y(y_before + 8)
                    else:
                        self.cell(0, 8, title, ln=True)

                for k, v in item.items():
                    if k.lower() not in ['title', 'startdate', 'enddate']:
                        self.set_font('Arial', '', self.font_size_custom)
                        self.multi_cell(0, 6, str(v))
                self.ln(3)
            else:
                safe_item = str(item).replace('•', '-').encode('latin-1', 'replace').decode('latin-1')
                if bullet_points:
                    self.cell(10, 6, chr(149), ln=0)
                else:
                    self.cell(10, 6, '', ln=0)
                self.multi_cell(0, 6, safe_item)
        self.ln(4)

    def section_list_inline(self, items):
        self.set_font('Arial', '', self.font_size_custom)
        self.set_text_color(*self.font_color)
        for item in items:
            safe_item = str(item).replace('•', '-').encode('latin-1', 'replace').decode('latin-1')
            self.cell(10, 6, chr(149), ln=0)
            self.multi_cell(0, 6, safe_item)
        self.ln(4)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def generate_resume_pdf(data, font_size, font_color, background_color):
    pdf = ResumeGenerator()
    pdf.set_margins(10, 10, 10)
    pdf.font_color = hex_to_rgb(font_color)
    pdf.bg_color = hex_to_rgb(background_color)
    pdf.font_size_custom = font_size  

    pdf.name = data.get('name', '')
    pdf.email = data.get('email', '')
    pdf.phone = data.get('phone', '')
    pdf.address = data.get('address', '')
    pdf.twitter = data.get('twitter', '')
    pdf.linkedin = data.get('linkedin', '')
    pdf.github = data.get('github', '')

    pdf.add_page()

    if data.get('summary'):
        pdf.section_title("SUMMARY")
        pdf.section_body([data['summary']], bullet_points=False)

    if data.get('education') and any(data['education']):
        pdf.section_title("EDUCATION")
        pdf.section_body(data['education'])

    if data.get('experience') and any(data['experience']):
        pdf.section_title("PROFESSIONAL EXPERIENCE")
        pdf.section_body(data['experience'])

    if data.get('skills') and any(data['skills']):
        pdf.section_title("TECHNICAL SKILLS")
        pdf.section_list_inline(data['skills'])

    if data.get('projects') and any(data['projects']):
        pdf.section_title("PROJECTS")
        pdf.section_body(data['projects'], section="PROJECTS")

    pdf.output("generated_resume_output.pdf")
    print("\n✨  Resume saved as 'generated_resume_output.pdf'")

def collect_resume_data():
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    phone = input("Enter your phone: ").strip()
    linkedin = input("Enter your LinkedIn URL: ").strip()
    github = input("Enter your GitHub URL: ").strip()
    address = input("Enter your address: ").strip()
    twitter = input("Enter your Twitter handle: ").strip()
    summary = input("Enter your summary: ").strip()
    education = input("Enter your education (comma-separated): ").split(',')
    experience = input("Enter your experience (comma-separated): ").split(',')
    projects = input("Enter your projects (comma-separated): ").split(',')
    skills = input("Enter your skills (comma-separated): ").split(',')

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "address": address,
        "twitter": twitter,
        "summary": summary,
        "education": [e.strip() for e in education],
        "experience": [e.strip() for e in experience],
        "projects": [p.strip() for p in projects],
        "skills": [s.strip() for s in skills]
    }

def fetch_resume_data_from_api(name):
    url = f"https://expressjs-api-resume-random.onrender.com/resume?name={name}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching from API: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Resume PDF Generator")
    parser.add_argument('--font-size', type=int, default=12)
    parser.add_argument('--font-color', type=str, default='#000000')
    parser.add_argument('--background-color', type=str, default='#FFFFFF')
    args = parser.parse_args()

    use_api = input("Do you want to fetch resume from API? (y/n): ").strip().lower()
    resume_data = {}

    if use_api == 'y':
        name = input("Enter your name (for API): ").strip()
        data = fetch_resume_data_from_api(name)
        if data:
            print("\n--- Resume data fetched from API ---")
            for key, value in data.items():
                print(f"{key.capitalize()}: {value}")
            resume_data = data
        else:
            print("Switching to manual entry...")
            resume_data = collect_resume_data()
    else:
        resume_data = collect_resume_data()

    generate_resume_pdf(resume_data, args.font_size, args.font_color, args.background_color)

if __name__ == '__main__':
    main()
