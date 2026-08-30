import sys
import os
import hashlib

def CalculateChecksum(FileNam):
    fobj=open(FileNam,"rb")

    hobj=hashlib.md5()

    Buffer=fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def FindDuplicate(DirectoryName):
    Ret=False

    Ret=os.path.exists(DirectoryName)
    if Ret==False:
        print("Patch is invalid")
        return

    Ret=os.path.isdir(DirectoryName)
    if Ret==False:
            print("it is not a directory")
            return

    Duplicate={}

    Unique=0
    Same=0

    for FolderName,SubFolder,Fileman in os.walk(DirectoryName):
         for fname in Fileman:
              fname=os.path.join(FolderName,fname)

              CheckSum=CalculateChecksum(fname)

              print(f"{fname} :{CheckSum}")

              if CheckSum in Duplicate:
                   Same=Same+1
                   Duplicate[CheckSum].append(fname)
              else:
                   Unique=Unique+1
                   Duplicate[CheckSum]=[fname]
    print(f"Unique files Found :{Unique}")
    print(f"Duplicate files Found :{Unique}")
def main():
    FindDuplicate("Marvellous")

if __name__=="__main__":
    main()