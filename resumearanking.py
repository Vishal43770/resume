import os
import pandas as pd
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)
            text = ""
            for page in pdf.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text
            return text
    except Exception as e:
        st.error(f"Error reading PDF {file_path}: {e}")
        return ""

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    # Calculate cosine similarity
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()

    return cosine_similarities

# Streamlit Interface
st.title("Resume Ranking Application")

# Job Description Input
job_description = st.text_area("Enter the Job Description:", height=200)

# Resume Upload
uploaded_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

if job_description and uploaded_files:
    resumes = []
    filenames = []
    temp_dir = "temp_resumes"  # Create a temporary directory
    os.makedirs(temp_dir, exist_ok=True)

    for uploaded_file in uploaded_files:
        try:
            file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            resumes.append(extract_text_from_pdf(file_path))
            filenames.append(uploaded_file.name)
        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {e}")
    
    # Clean up temporary files
    for file_path in [os.path.join(temp_dir, f) for f in os.listdir(temp_dir)]:
        os.remove(file_path)
    os.rmdir(temp_dir)

    # Rank resumes
    if resumes:
        scores = rank_resumes(job_description, resumes)
        st.write("Ranking resumes...")

        # Display results
        results = pd.DataFrame({"Resume": filenames, "Score": scores})
        results = results.sort_values(by="Score", ascending=False)
        st.dataframe(results)
    else:
        st.warning("No valid resumes were processed.")
elif not job_description and uploaded_files:
    st.warning("Please enter a job description.")
elif job_description and not uploaded_files:
    st.warning("Please upload at least one resume.")
else:
    st.info("Please enter a job description and upload resume PDFs to start ranking.")
