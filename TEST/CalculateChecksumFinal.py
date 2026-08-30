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


def main():
    Ret=CalculateChecksum("Demo.txt")

    print("Checksum of file is :",Ret)

if __name__=="__main__":
    main()