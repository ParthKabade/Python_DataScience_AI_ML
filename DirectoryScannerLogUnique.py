import os
import sys
import time

def DirectoryScanner(DirectoryPath):
    timestamp=time.ctime()
#%s म्हणजे
#“येथे String Insert करा.”

    logfilename="Marvellous%s.log"%(timestamp)#*
    logfilename=logfilename.replace(" ","_")
    logfilename=logfilename.replace(":","_")

    print("log File gets created with name :",logfilename)

    fobj=open(logfilename,"w")

    fobj.write("Marvellous Automation script\n")
    
    fobj.write("Files from the directory are\n")


    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for FName in FileName:
            fobj.write(FName+"\n")

    fobj.close()

def main():
    Border="*"*40

    print(Border)
    print("Marvellous Automation script")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is used to travel the direectory")
            print("for better usage please cheack --u flag")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--u"):
            print("Please exicute the scrip as")
            print("PYthon Filename.py DirectoryName")
            print("Directory name should be asolute path")
        else:
            DirectoryScanner(sys.argv[1])
    else:
        print("Invalid number of prameter")
        print("please use --u or--h for more info")

    print(Border)
    print("Thank you for using Marvellous Script")
    print(Border)

if __name__=="__main__":
    main()

"""
logfilename="Marvellous%s.log"%(timestamp)

Python

↓

Placeholder शोधा

↓

%s मिळाला

↓

timestamp ची Value घ्या

↓

त्या जागी Insert करा
"""