"""
parthkabade@Parths-MacBook-Air py_automation % python3 AutomationScript2.py --h
parthkabade@Parths-MacBook-Air py_automation % python3 AutomationScript2.py --u
"""
import sys

def main():
    
    
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("Help")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--u"):
            print("Usage")
        else:
            DirectoryName=sys.argv[1]
            print(f"Directory Name is {DirectoryName}")
    else:
        print("Invalid number of prameter")
        print("please use --u or--h for more info")

if __name__=="__main__":
    main()