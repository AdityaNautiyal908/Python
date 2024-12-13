# Python writing files (.txt,.json,.csv)

# with open("test.txt","a") as file:
#     file.write("Hello world" + "\n")
#     print("Write done")


file_path = "dest.txt"
source_txt = "source.txt"

with open(source_txt,"r") as file:
    content = file.read()

with open(file_path,"a") as dest:
    dest.write(content)

print("Text written from 1 file to another file")