from utility import extracttext, extractkeywords

res=extracttext("Project1/resumes")

with open("Project1/job_description.txt",'r') as f:
    jobdescription=f.read()

extractkeywords(res, jobdescription)   

