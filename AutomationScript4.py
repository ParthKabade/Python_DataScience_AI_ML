
import sys

def main():
    
    
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is used to travel the direectory")
            print("for better usage please cheack --u flag")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--u"):
            print("Please exicute the script as")
            print(f"PYthon Filename.py {sys.argv[1]}")
            print("Directory name should be asolute path")
        else:
            DirectoryName=sys.argv[1]
            print(f"Directory Name is {DirectoryName}")
    else:
        print("Invalid number of prameter")
        print("please use --u or--h for more info")

if __name__=="__main__":
    main()