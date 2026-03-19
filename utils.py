import spacy
from skills import skills_list

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    text = text.lower()
    found = []
    
    for skill in skills_list:
        if skill in text:
            found.append(skill)
    
    return found