import os
import PyPDF2 as py2
import spacy 

def extracttext(directory):
    resumetext = {}
    files = os.listdir(directory)
    for file in files:
        if file.endswith(".pdf"):
            reader = py2.PdfReader(os.path.join(directory, file))
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            resumetext[file] = text
        else:
            print("Not a pdf file")
            os.remove(os.path.join(directory, file))
            print(f"{file} removed")
    return resumetext

def extractkeywords(resumetext,jobdescription):
    nlp=spacy.load("en_core_web_sm")
    doc2=nlp(jobdescription)
    skills=[token.text.lower() for token in doc2 if token.pos_=="NOUN"]
    print("Skills in job description: ",skills)
    for i in resumetext:
        doc1=nlp(resumetext[i])
        
        found = {i:[token.text.lower() for token in doc1 if token.text in skills]}
        
        print(f"Skills found in {i}: {found[i]}")
        print("******************************************")

    