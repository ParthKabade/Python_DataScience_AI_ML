##########################################################################################################################
#
#   Importing required Libraries
#
##########################################################################################################################
import os
import sys
import schedule
import time

##########################################################################################################################
#
#   Function Name: DirectoryScanner
#   Input:         Name of Directory
#   Description:   Delete all empty Files periodically
#   Date:          19/07/2026
#   Author:        Parth Nilesh Kabade
#
##########################################################################################################################
def DirectoryScanner(DirectoryPath):
    Border="_"*40

    timestamp=time.ctime()

    logfilename="Marvellous%s.log"%(timestamp)
    logfilename=logfilename.replace(" ","_")
    logfilename=logfilename.replace(":","_")

    Ret=False
    Ret=os.path.exists(DirectoryPath)

    if(Ret==False):
        print("Marvellous Automation Error : There is no such Directory with name ",DirectoryPath)
        return
    
    Ret=os.path.isdir(DirectoryPath)

    if(Ret==False):
        print("Marvellous Automation Error : It is not a directory with name :",DirectoryPath)
        return


    print("log File gets created with name :",logfilename)

    fobj=open(logfilename,"w")

    fobj.write(Border+"\n")

    fobj.write("Marvellous Automation script\n")

    fobj.write(Border+"\n\n")
    
    fobj.write("Files from the directory are\n\n")

    fobj.write(Border+"\n")

    Totalfiles=0
    Emptyfiles=0

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for FName in FileName:
            Totalfiles=Totalfiles+1
            FName=os.path.join(FolderName,FName)
            fobj.write(f"{FName} : {os.path.getsize(FName)} Bytes\n")

            if(os.path.getsize(FName)==0):
                Emptyfiles=Emptyfiles+1
                os.remove(FName)
    fobj.write(Border+"\n")
    fobj.write(f"Total filesh scanned :{Totalfiles}\n")
    fobj.write(f"Total empty files found and deleted :{Emptyfiles}\n")

    fobj.write(Border+"\n")
    fobj.write("Log file gets created at :"+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()
##########################################################################################################################
#
#   Function Name: main
#   Input:         Command Line Arguments
#   Description:   It controls the script
#   Date:          19/07/2026
#   Author:        Parth Nilesh Kabade
#
##########################################################################################################################
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
        
            schedule.every(5).minutes.do(DirectoryScanner, sys.argv[1])
            
            while True:
               schedule.run_pending()
               time.sleep(1)
    else:
        print("Invalid number of prameter")
        print("please use --u or--h for more info")

    print(Border)
    print("Thank you for using Marvellous Script")
    print(Border)


##########################################################################################################################
#
#   Starter of the automation script
#
##########################################################################################################################
if __name__=="__main__":
    main()

"""
हा प्रोग्राम Automation Script आहे. याचे काम म्हणजे:

1. User कडून Directory चे नाव घेणे.
2. त्या Directory मधील सर्व Files Scan करणे.
3. 0 Bytes (Empty Files) असलेल्या Files Delete करणे.
4. Log File तयार करणे.
5. प्रत्येक 5 मिनिटांनी हेच काम पुन्हा करणे.

आता हा प्रोग्राम Python Internally कसा Execute होतो ते एकदम Step-by-Step मराठीत समजून घेऊया.

⸻

Program Execution Flow

          Program Start
                │
                ▼
     Python Interpreter सुरू होतो
                │
                ▼
       सर्व Libraries Import होतात
                │
                ▼
    सर्व Functions Memory मध्ये Load होतात
                │
                ▼
if __name__ == "__main__"
                │
                ▼
           main() Call
                │
                ▼
      Command Line Argument Check
                │
       ┌────────┴────────┐
       │                 │
      Invalid         Valid
       │                 │
       ▼                 ▼
 Error Message    DirectoryScanner()
                         │
                         ▼
              Directory Scan होते
                         │
                         ▼
               Empty Files Delete
                         │
                         ▼
               Log File तयार होते
                         │
                         ▼
 schedule.every(5).minutes.do(...)
                         │
                         ▼
         while True Loop सुरू
                         │
                         ▼
          schedule.run_pending()
                         │
                         ▼
      5 Minutes पूर्ण झाले का?
              │
       ┌──────┴──────┐
       │             │
      No            Yes
       │             │
       ▼             ▼
 sleep(1)    DirectoryScanner()
       │             │
       └──────┬──────┘
              ▼
         पुन्हा Loop

⸻

Step 1 : Program सुरू होतो

जेव्हा तुम्ही Terminal मध्ये लिहिता

python EmptyFileRemover.py Test

Python Interpreter हा Program वाचायला सुरुवात करतो.

⸻

Step 2 : Libraries Import होतात

import os
import sys
import schedule
import time

Internally Python प्रत्येक Module शोधतो.

Python Installation
        │
        ▼
     os Module
     sys Module
     time Module
     schedule Module

हे Modules RAM मध्ये Load होतात.

⸻

Step 3 : Functions Compile होतात

Python लगेच Function Execute करत नाही.

तो फक्त

def DirectoryScanner():

आणि

def main():

यांच्या Definitions Memory मध्ये ठेवतो.

Memory
DirectoryScanner()
main()

अजून कोणतीही Function चाललेली नसते.

⸻

Step 4 : खाली येतो

Python शेवटी येतो

if __name__=="__main__":

जेव्हा हा Program Direct चालवतो

__name__
↓
__main__

Condition True होते.

⸻

Step 5 : main() Call

Python आता

main()

Execute करतो.

Call Stack

main()

⸻

Step 6 : Border तयार होतो

Border="*"*40

Memory मध्ये

************************************

Store होते.

⸻

Step 7 : Argument Check

समजा

python Demo.py Test

आहे.

Internally

sys.argv
↓
[
"Demo.py",
"Test"
]
sys.argv[0]
↓
Program Name
Demo.py
sys.argv[1]
↓
Directory
Test

म्हणून

len(sys.argv)
↓
2

Condition True.

⸻

Step 8 : Help Check

Python तपासतो

Test=="--h"

False

⸻

नंतर

Test=="--u"

False

⸻

म्हणून

else

मध्ये जातो.

⸻

Step 9 : DirectoryScanner() Call

DirectoryScanner("Test")

Call Stack

main()
↓
DirectoryScanner()

⸻

Step 10 : Path Check

os.path.exists("Test")

Internally

Operating System
↓
Filesystem
↓
Test Folder आहे का?

जर

होय

↓

True

⸻

Step 11 : Directory आहे का?

os.path.isdir()

Operating System सांगतो

Folder
↓
True

⸻

Step 12 : Log File तयार करणे

open(logfilename,"w")

Internally

Python
↓
Operating System
↓
Create File
↓
Return File Descriptor
↓
Python File Object
fobj

⸻

Step 13 : os.walk()

हा सर्वात महत्त्वाचा भाग आहे.

Test
│
├── A.txt
├── B.txt
└── Demo
      │
      ├── C.txt
      └── D.txt

जेव्हा

os.walk(Test)

चालते

Internally

Folder
↓
Read Entries
↓
Directory सापडली?
↓
हो
↓
Recursive Call
↓
पुढची Directory

म्हणजे Python प्रत्येक Folder मध्ये स्वतःच जातो.

⸻

पहिला Iteration

FolderName
↓
Test
SubFolder
↓
Demo
Files
↓
A.txt
B.txt

⸻

दुसरा

FolderName
↓
Demo
Files
↓
C.txt
D.txt

⸻

Step 14 : प्रत्येक File ची Size

os.path.getsize()

Internally

Python
↓
Operating System
↓
File Metadata
↓
Size Return

उदा.

520 Bytes

⸻

Step 15 : Empty आहे का?

Size==0

जर

हो

↓

os.remove()

Internally

Python
↓
Operating System
↓
Delete File Entry
↓
Storage मुक्त

⸻

Step 16 : Function संपते

सर्व Files Scan झाल्यावर

fobj.close()

Internally

RAM Buffer
↓
Disk मध्ये Save
↓
File Close

⸻

Call Stack

main()

⸻

Step 17 : Schedule तयार करणे

schedule.every(5).minutes.do(...)

ही Line Function Execute करत नाही.

ती फक्त एक Job Register करते.

Memory मध्ये

Scheduler
↓
Job
↓
Run After 5 Minutes
↓
Function
↓
DirectoryScanner

अजून Scan झालेला नसतो.

⸻

Step 18 : Infinite Loop

while True

Internally

True ?
↓
हो
↓
Loop
↓
पुन्हा True
↓
Loop

कधीच संपत नाही.

⸻

Step 19 : run_pending()

schedule.run_pending()

Internally

Current Time
↓
Job Time
↓
Compare

उदा.

Current Time
↓
10:05
Job Time
↓
10:10
Current < Job
↓
Nothing

⸻

1 सेकंदानंतर

10:05:01

पुन्हा Check.

⸻

हे प्रत्येक सेकंदाला चालते.

⸻

Step 20 : 5 Minutes पूर्ण

समजा

10:10

झाले.

Current Time
↓
10:10
Job Time
↓
10:10

दोन्ही सारखे.

मग

DirectoryScanner()

Automatically Call होते.

Call Stack

main()
↓
while
↓
run_pending()
↓
DirectoryScanner()

⸻

ही Function पुन्हा

* Folder Scan करते.
* Empty Files Delete करते.
* नवीन Log File तयार करते.

⸻

Step 21 : पुन्हा Waiting

Function संपल्यावर

while

मध्ये परत येते.

run_pending()
↓
sleep(1)
↓
run_pending()
↓
sleep(1)

असेच सतत चालू राहते.

⸻

संपूर्ण Flow एका Diagram मध्ये

User
 │
 │ python EmptyFileRemover.py Test
 ▼
Python Interpreter
 │
 ▼
Import Modules
 │
 ▼
Load Functions
 │
 ▼
main()
 │
 ▼
Check Arguments
 │
 ▼
DirectoryScanner()
 │
 ├── Check Path
 ├── Create Log File
 ├── Traverse Directory
 ├── Get File Size
 ├── Delete Empty Files
 └── Close Log File
 │
 ▼
Register Scheduler
 │
 ▼
while True
 │
 ▼
run_pending()
 │
 ▼
5 Minutes पूर्ण?
 │
 ├── नाही → sleep(1) → पुन्हा Check
 │
 └── हो → DirectoryScanner() पुन्हा Execute
 │
 ▼
हे चक्र Program बंद होईपर्यंत सतत चालू राहते.

यामुळे हा प्रोग्राम एक Periodic Automation Script बनतो—तो सुरुवातीला एकदा Directory स्कॅन करतो आणि त्यानंतर प्रत्येक 5 मिनिटांनी आपोआप पुन्हा तेच काम करतो.
"""