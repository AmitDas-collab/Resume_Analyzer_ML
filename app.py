import streamlit as st
from utils import extract_skills
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Smart Resume Analyzer")

# Input fields
resume = st.text_area("Paste your Resume")
job = st.text_area("Paste Job Description")

if st.button("Analyze"):

    # Extract skills
    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job)

    # TF-IDF similarity
    tfidf = TfidfVectorizer()
    matrix = tfidf.fit_transform([resume, job])
    score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0] * 100

    # Missing skills
    missing = list(set(job_skills) - set(resume_skills))

    # Output
    st.subheader("Results")
    st.write("Match Score:", round(score, 2), "%")
    st.write("Resume Skills:", resume_skills)
    st.write("Missing Skills:", missing)

    if missing:
        st.warning("You should learn: " + ", ".join(missing))
    else:
        st.success("Great match!")
        