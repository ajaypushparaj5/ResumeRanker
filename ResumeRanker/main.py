from utility import extracttext, extractkeywords, rankresume

res=extracttext("ResumeRanker/resumes")

with open("ResumeRanker/job_description.txt",'r') as f:
    jobdescription=f.read()

found=extractkeywords(res, jobdescription)   
print("****************************")
rank=rankresume(found)
