import os
import sys
import re

#function for moving of files
#s and d are source and destination locations
def moving(file,folder):
    s=start_dir+"\\"+file
    d=start_dir+"\\"+folder+"\\"+file
    os.rename(s,d)

#either take file path as input or set path according to your downloads here
if len(sys.argv)==1:
    start_dir="C:\\Users\\hp\\Downloads"
else:
    start_dir=sys.argv[1]
directory={"codes":["cpp","c","py","html","o"],
           "images":["png","jpeg","jpg","gif"],
           "videos":["mp4","wmv","mkv","mov","mpg"],
           "docs":["pdf","doc","docx","xml","ppt","txt","xml","zip","rar"],
           "audio":["mp3","mp2","wav"],
           "other":[]
           }

for dir in directory.keys():
    s=start_dir+"\\"+dir
    os.makedirs(s,exist_ok=True)

#initialising files list
files=[]
#now checking if the file exists in that directory or not
for file in os.listdir(start_dir):
    path=start_dir+"\\"+file
    if os.path.isfile(path):
        files.append(file)

for file in files:
    name=re.split('[.]',file)
    format=str(name[len(name)-1])
    format=format.lower()
    name=".".join(name)
    print(name)
    flag=0
    for dir in directory.keys():
        if format in directory[dir]:
            moving(name,dir)
            flag=1
            break

    if flag==0:
        moving(name,"other")