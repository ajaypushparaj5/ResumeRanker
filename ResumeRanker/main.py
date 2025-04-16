from utility import extracttext, extractkeywords, rankresume

res=extracttext("resumes")

with open("job_description.txt",'r') as f:
    jobdescription=f.read()

found=extractkeywords(res, jobdescription)   
print("****************************")
rank=rankresume(found)
