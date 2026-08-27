import sys
import os
import hashlib

def CalculateChecksum(FileNam):
    fobj=open(FileNam,"rb")

#MD5 (Message Digest Algorithm 5) हा एक Hashing Algorithm आहे. याचा उपयोग कोणत्याही Data किंवा File साठी एक Unique Fingerprint (Hash Value / Checksum) तयार करण्यासाठी केला जातो.

    hobj=hashlib.md5()

    Buffer=fobj.read(1000)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()


def main():
    Ret=CalculateChecksum("Demo.txt")

    print("Checksum of file is :",Ret)

if __name__=="__main__":
    main()