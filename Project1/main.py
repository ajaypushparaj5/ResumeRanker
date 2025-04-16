from utility import extracttext, extractkeywords, rankresume

res=extracttext("Project1/resumes")

with open("Project1/job_description.txt",'r') as f:
    jobdescription=f.read()

found=extractkeywords(res, jobdescription)   
print("****************************")
rank=rankresume(found)
