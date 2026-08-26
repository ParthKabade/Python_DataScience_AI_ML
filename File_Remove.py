import os

def main():
    try:
        #fobj.remove()->not applicabel
        os.remove("Demo.txt")
        
    except FileNotFoundError as fobj:
        print("Files is not present in current directory")

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
os.remove("Demo.txt")
      │
      ▼
Operating System
      │
      ▼
File Exists ?
      │
 ┌────┴─────┐
 │          │
Yes        No
 │          │
 ▼          ▼
Delete   FileNotFoundError
 │          │
 ▼          ▼
End      except Block
"""