import os
import PyPDF2 as py2

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
        

