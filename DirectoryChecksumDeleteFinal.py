import sys
import os
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is invalid")
        return

    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not a directory")
        return

    Duplicate = {}

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)

            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]

    return Duplicate

def DeleteDuplicate(DirectoryName):
    MyDict = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    TotalDeleted = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                os.remove(subvalue)
                TotalDeleted = TotalDeleted + 1
        Count = 0

    print("Total deleted files : ",TotalDeleted)
    
def main():
    DeleteDuplicate("Test")

if __name__ == "__main__":
    main()


"""
हा प्रोग्राम आधीच्या प्रोग्रामपेक्षा एक पाऊल पुढे आहे. आधी आपण फक्त Checksum काढत होतो, पण आता समान Checksum असलेल्या Files शोधून Duplicate Files Delete करतो.

मी हा प्रोग्राम Internally RAM, Dictionary, Stack, Loop, OS Calls यांच्या दृष्टीने समजावून सांगतो.

⸻

Step 1 : Program सुरू होतो

import sys
import os
import hashlib

Python Interpreter हे तीन Modules Memory मध्ये Load करतो.

RAM
Python Program
     │
     ├── sys
     ├── os
     └── hashlib

⸻

Step 2 : Functions Memory मध्ये तयार होतात

CalculateChecksum()
FindDuplicate()
DeleteDuplicate()
main()

यांचे Address Memory मध्ये Store होतात.

Memory
1000 ---> CalculateChecksum()
2000 ---> FindDuplicate()
3000 ---> DeleteDuplicate()
4000 ---> main()

टीप: अजून कोणतेही Function Execute झालेले नसते.

⸻

Step 3 : main()

if __name__ == "__main__":
    main()

Python पाहतो

__name__ == "__main__"

म्हणून

main()

Call होतो.

⸻

Step 4 : main()

DeleteDuplicate("Test")

Call Stack

main()
↓
DeleteDuplicate()

⸻

Step 5 : DeleteDuplicate()

MyDict = FindDuplicate(DirectoryName)

आता

Call Stack
main()
↓
DeleteDuplicate()
↓
FindDuplicate()

⸻

Step 6 : Path Check

Ret = os.path.exists(DirectoryName)

OS ला विचारलं जातं

Test Folder आहे का?

समजा

Test/

असल्यामुळे

Ret = True

⸻

पुढे

Ret = os.path.isdir(DirectoryName)

OS तपासतो

Folder आहे का?

उत्तर

True

⸻

Step 7 : Empty Dictionary तयार होते

Duplicate = {}

RAM मध्ये

Duplicate
{}

यामध्ये

Key = Checksum
Value = File List

Store होणार आहे.

⸻

Step 8 : os.walk()

समजा Folder असा आहे

Test
    A.txt
    B.txt
    C.txt
    Demo
        D.txt

समजा

A.txt
आणि
C.txt
यांचा Data समान आहे.

⸻

पहिल्या Iteration मध्ये

FolderName
↓
Test
SubFolder
↓
Demo
FileName
↓
['A.txt','B.txt','C.txt']

⸻

Step 9 : First File

fname
↓
A.txt
fname = os.path.join(FolderName,fname)

बनते

Test/A.txt

⸻

Step 10 : Checksum

Checksum = CalculateChecksum(fname)

Call Stack

main()
↓
DeleteDuplicate()
↓
FindDuplicate()
↓
CalculateChecksum()

⸻

CalculateChecksum()

File Open

Disk
↓
A.txt
↓
OS
↓
File Object

⸻

MD5 तयार

MD5 Object

⸻

1024 Bytes वाचले

Buffer
↓
1024 Bytes

⸻

Update

MD5
↓
Updated

⸻

पुन्हा Read

1024
↓
1024
↓
500
↓
0

⸻

Final

Checksum
↓
AAAAA11111

Return

AAAAA11111

⸻

Step 11 : Dictionary मध्ये Store

if Checksum in Duplicate:

सध्या Dictionary

{}

म्हणून

False

Else

Duplicate[Checksum]=[fname]

Dictionary

{
AAAAA11111
:
[
Test/A.txt
]
}

⸻

Step 12 : दुसरी File

B.txt

Checksum

BBBBB22222

Dictionary

{
AAAAA11111 :
[
A.txt
],
BBBBB22222 :
[
B.txt
]
}

⸻

Step 13 : तिसरी File

C.txt

Checksum

AAAAA11111

आता

if Checksum in Duplicate

True

म्हणून

Duplicate[Checksum].append(fname)

Dictionary

{
AAAAA11111 :
[
A.txt,
C.txt
],
BBBBB22222 :
[
B.txt
]
}

याचा अर्थ

A.txt
आणि
C.txt
Duplicate आहेत.

⸻

Step 14 : चौथी File

D.txt

Checksum

CCCC33333

Dictionary

{
AAAAA11111 :
[
A.txt,
C.txt
],
BBBBB22222 :
[
B.txt
],
CCCC33333 :
[
D.txt
]
}

⸻

Step 15 : Return Dictionary

FindDuplicate()
↓
Return
↓
DeleteDuplicate()

आता

MyDict
↓
{
AAAAA11111 :
[
A.txt,
C.txt
],
BBBBB22222 :
[
B.txt
],
CCCC33333 :
[
D.txt
]
}

⸻

Step 16 : Filter

Result = list(filter(lambda x : len(x)>1,MyDict.values()))

पहिले

MyDict.values()

देईल

[
[A.txt,C.txt],
[B.txt],
[D.txt]
]

⸻

Filter

len()>1

म्हणून

Result
↓
[
[A.txt,C.txt]
]

कारण

Duplicate List
मध्ये
2 Files आहेत.

⸻

Step 17 : Delete Loop

Result
↓
[
[A.txt,C.txt]
]

Outer Loop

value
↓
[A.txt,C.txt]

⸻

Inner Loop

पहिले

subvalue
↓
A.txt
Count=1

Condition

Count>1

False

Delete नाही.

⸻

दुसरे

subvalue
↓
C.txt
Count=2

Condition

2>1

True

os.remove(C.txt)

Internally

OS ला Command

Delete
↓
C.txt

Disk मधून File Delete.

TotalDeleted
↓
1

⸻

Step 18 : जर तीन Duplicate असतील

समजा

[
A.txt,
C.txt,
D.txt
]

Loop

Count=1
↓
Keep A
Count=2
↓
Delete C
Count=3
↓
Delete D

नेहमी पहिली File ठेवतो.

बाकी Delete.

⸻

Step 19 : Print

Total deleted files : 1

⸻

Dictionary Internally

समजा

A.txt
Hello
↓
Checksum
12345
B.txt
Hi
↓
Checksum
99999
C.txt
Hello
↓
Checksum
12345

Dictionary

Duplicate
{
12345 :
[
A.txt,
C.txt
],
99999 :
[
B.txt
]
}

⸻

Call Stack Flow

main()
↓
DeleteDuplicate()
↓
FindDuplicate()
↓
CalculateChecksum()
↓
Return
↓
FindDuplicate()
↓
Return
↓
DeleteDuplicate()
↓
Delete Files
↓
main()
↓
Program End

⸻

संपूर्ण Flow Diagram

Program Start
      │
      ▼
Import Modules
      │
      ▼
main()
      │
      ▼
DeleteDuplicate()
      │
      ▼
FindDuplicate()
      │
      ▼
Check Folder Exists
      │
      ▼
os.walk()
      │
      ▼
Open Each File
      │
      ▼
Read 1024 Bytes
      │
      ▼
Generate MD5 Checksum
      │
      ▼
Store in Dictionary
      │
      ▼
All Files Completed
      │
      ▼
Filter Duplicate Lists
      │
      ▼
Keep First File
      │
      ▼
Delete Remaining Duplicate Files
      │
      ▼
Display Total Deleted
      │
      ▼
Program Ends

या प्रोग्राममधील महत्त्वाची कल्पना

* MD5 Checksum ही File च्या Content ची एक ओळख (fingerprint) असते. Content सारखा असेल तर Checksumही सारखाच येतो.
* Duplicate Dictionary मध्ये Key = Checksum आणि Value = त्या Checksum असलेल्या सर्व Files ची List ठेवली जाते.
* filter(lambda x: len(x) > 1, MyDict.values()) फक्त ज्या Lists मध्ये एकापेक्षा जास्त Files आहेत (म्हणजे Duplicate) त्या निवडतो.
* os.remove() ही System Call वापरून OS त्या File ला Disk वरून Delete करतो.
* प्रत्येक Duplicate Group मधील पहिली File ठेवली जाते, आणि उरलेल्या सर्व Files Delete केल्या जातात.
"""