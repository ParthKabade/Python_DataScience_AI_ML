import sys

def main():
    DirectoryName=sys.argv[1]

    print(len(sys.argv))
    print(f"Directory Name is {DirectoryName}")

if __name__=="__main__":
    main()

"""
User
 │
 ▼
python3 Demo.py Marvellous
 │
 ▼
Python Interpreter
 │
 ▼
sys.argv तयार होते

sys.argv
──────────────
[0] Demo.py
[1] Marvellous
 │
 ▼
DirectoryName = sys.argv[1]
 │
 ▼
Marvellous
 │
 ▼
Print
"""