import streamlit as st
from streamlit_extras import add_vertical_space as avs
import google.generativeai as genai 
import os 
import PyPDF2
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel('gemini-pro')
def get_gemini_response(input,jd,text):
    print(input.format(text,jd))
    response=model.generate_content(input.format(text,jd))
    return response.text
def input_pdf_text(uploaded_file):
    reader=PyPDF2.PdfReader(uploaded_file)
    text=''
    for page_num in range(len(reader.pages)):
        page=reader.pages[page_num]
        text+=str(page.extract_text())
    return text

input_prompt=""" As an experienced ATS (Applicant Tracking System), proficient in the technical doma Software Engineering, Data Science, Data Analysis, 
Big Data Engineering, Web Develop Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Database Administrator, Network Engineer,
 AI Engineer, Systems Analyst, Full Stack Designer, IT Project Manager, and additional specialized areas, your objective is to resumes against provided job descriptions.
In a fiercely competitive job market, you in offering top-notch guidance for resume enhancement.
Assign precise matching perce (Job Description) and meticulously identify any missing keywords with utmost accuracy.
Resume(Extracted): {} 
Description:{}
I want the response in the following structure: 
The first line indicates the percentage match with the job description (JD). 
The second line presents a list of missing keywords. 
The third section provides a profile summary. Mention the title for all the three sections.
While generating the response put some space to separate all the three sections."""
st.set_page_config(page_title="Resume ATS Tracker",layout='wide')


avs.add_vertical_space(4)
col1,col2=st.columns([3,2])
with col1:
    st.title("CareerCraft")
    st.header("Navigate the Job market with Confidence!")
    st.markdown("""<p style='text-align: justify;'> Introducing CareerCraft, an ATS-Optimized Resume Analyzer your ultimate solution for optimizing job applications and accelerating career growth. Our innovative platform leverages advanced ATS technology to provide job seekers with valuable insights into their resumes' compatibility with job descriptions. From resume optimization and skill enhancement to career progression guidance, CareerCraft empowers users to stand out in today's competitive job market. Streamline your job application process, enhance your skills, and navigate your career path with confidence. Join CareerCraft today and unlock new opportunities for professional success! </p>""", unsafe_allow_html=True)
with col2:
    st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_column_width=True)
avs.add_vertical_space(10)
col1, col2 =st.columns([3,2])
with col2:
    st.header("Wide Range of offerings") 
    st.write("ATS-Optimized Resume Analysis")
    st.write('Resume Optimization')
    st.write('Skill Enhancement') 
    st.write('Career Progression Guidance')
    st.write('Tailored Profile Summaries')
    st.write('Streamlined Application Process')
    st.write('Personalized Recommendations')
    st.write("efficient career Navigation") 
with col1:
    st.image('https://static.vecteezy.com/system/resources/previews/029/216/477/non_2x/looking-for-the-perfect-candidate-young-woman-using-binoculars-vector.jpg', use_column_width=True) 
avs.add_vertical_space(10)
col1, col2 =st.columns([3,2]) 
with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd=st.text_area("Paste the Job Description") 
    uploaded_file=st.file_uploader("Upload Your Resume", type="pdf", help="Please uplaod the pdf") 
    submit = st.button("Submit") 
    if submit: 
        if uploaded_file is not None:
            text=input_pdf_text(uploaded_file)
            response=get_gemini_response (input_prompt,jd,text)
            st.subheader(response) 
with col2: 
        
        st.image('https://png.pngtree.com/png-vector/20220916/ourmid/pngtree-work-from-home-woman-png-image_6180588.png', use_column_width=True) 
avs.add_vertical_space(10)
col1, col2= st.columns([2, 3])
with col1: 
    st.image("https://apnsolar.com/wp-content/uploads/2023/01/pngwing.com-24-1024x715.png", use_column_width=True)
with col2:
    st.markdown("<h1 style='text-align: center;'>FAQ</h1>", unsafe_allow_html=True)
    st.write("Question: How does CareerCraft analyze resumes and job descriptions?")
    st.write("""Answer: CareerCraft uses advanced algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.""")
    avs.add_vertical_space(3) 
    st.write("Question: Can CareerCraft suggest improvements for my resume?")
    st.write("""Answer: Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles.""")
    avs.add_vertical_space(3) 
    st. write("Question: Is Career Craft suitable for both entry-level and experienced professionals?") 
    st.write("""Answer: Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.""") 
avs.add_vertical_space(10)
