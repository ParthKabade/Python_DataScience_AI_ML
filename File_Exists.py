import os

def main():
    Ret=os.path.exists("Demo.txt")
        
    if(Ret==True):
        print("File is present in current directory")
    else:
        print("There is no such file")

if __name__=="__main__":
    main()

"""
Program Start
      │
      ▼
Import os Module
      │
      ▼
main()
      │
      ▼
os.path.exists("Demo.txt")
      │
      ▼
Operating System
      │
      ▼
File Exists?
      │
 ┌────┴─────┐
 │          │
Yes        No
 │          │
 ▼          ▼
True      False
 │          │
 ▼          ▼
Print     Print
Present   Not Present
      │
      ▼
Program End
"""