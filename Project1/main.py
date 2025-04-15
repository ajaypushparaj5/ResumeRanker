from utility import extracttext

res=extracttext("Project1/resumes")

for file in res:
    print(file)
    print(res[file])
    print("***************")
    
