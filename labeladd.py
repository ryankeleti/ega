import fileinput,re
e=r"\}\{\d.\d.\d"

filename=input("file ")

with open(filename,'r') as file:
  filedata=file.read()

def  modify_file(file_name,pattern,value=""):  
    fh=fileinput.input(file_name,inplace=True)  
    for line in fh:
        replacement=value + line 
        line=re.sub(pattern,replacement,line)  
        sys.stdout.write(line)  
    fh.close()  

modify_file(filename,

