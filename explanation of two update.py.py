# Import the necessary libraries
import os
import PyPDF2

# Define the job roles as a list of strings
job_roles = ["Software Developer/Engineer", "Systems Administrator", "Network Engineer", 
             "Database Administrator (DBA)", "Cybersecurity Analyst", "IT Support Specialist", 
             "Web Developer", "Cloud Architect/Engineer", "Data Scientist", "UI/UX Designer", 
             "Business Analyst", "Project Manager (IT)"]

# Define a function to analyze a resume
def analyze_resume(resume_text):
    # This function is supposed to analyze a resume and extract relevant information.
    # For simplicity, we'll just return the resume text.
    return resume_text

# Define a function to match a resume analysis with a job role
def match_job_role(resume_analysis, job_role):
    # This function is supposed to match a resume analysis with a job role.
    # For simplicity, we'll just return a random match score.
    return len(resume_analysis) % len(job_role)

# Specify the directory where the resumes are stored
resume_dir = r"C:\Users\mahar\Downloads\work"

# Get a list of all PDF files in the directory
resume_files = [f for f in os.listdir(resume_dir) if f.endswith(".pdf")]

# Analyze all resumes and store the analyses in a dictionary
resume_analyses = {}
for filename in resume_files:
    # Open each PDF file
    with open(os.path.join(resume_dir, filename), 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        # Initialize an empty string to store the resume text
        resume_text = ""
        # Loop over all pages in the PDF file
        for page_num in range(len(pdf_reader.pages)):
            # Get the current page
            page = pdf_reader.pages[page_num]
            # Extract the text from the current page and add it to the resume text
            resume_text += page.extract_text()
        # Analyze the resume and store the analysis in the dictionary
        resume_analyses[filename] = analyze_resume(resume_text)

# Match each resume with each job role and keep track of the best matches
best_matches = {}
for job_role in job_roles:
    # Initialize variables to store the best match and score for the current job role
    best_match = None
    best_score = None
    # Loop over all resume analyses
    for filename, resume_analysis in resume_analyses.items():
        # Calculate the match score for the current resume and job role
        match_score = match_job_role(resume_analysis, job_role)
        # If this is the first match or the score is better than the best score so far,
        # update the best match and score
        if best_match is None or match_score > best_score:
            best_match = filename
            best_score = match_score
    # Store the best match for the current job role in the dictionary
    best_matches[job_role] = best_match

# Print the best match for each job role
for job_role, best_match in best_matches.items():
    print(f"Best match for {job_role}: {best_match}")