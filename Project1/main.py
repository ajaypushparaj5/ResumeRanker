from utility import extract_text_from_directory

res=extract_text_from_directory("Project1/resumes")

for file in res:
    print(file)
    print(res[file])
    print("***************")
    
