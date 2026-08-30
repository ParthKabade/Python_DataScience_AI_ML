#python3 ProcessSrvillence.py 2 MarvellousLog
#python3 ProcessSrvillence.py time_interval Folder_Name
#               0                   1               2

import psutil
import sys
import os

def main():
    Border="-"*85
    print(Border)
    print("-------------------Marvellous Platform Survellance System------------------")
    print(Border,"\n")

    #--h & --u handling
    if(len(sys.argv)==2):
        if(sys.argv[1]=='--h' or sys.argv[1]=='--H'):
            print("This Automation script is Use to perfome ")
            print("1:It fetch the information of running procces")
            print("2:It fetch the information about the RAM")
            print("3:It fetch the information about the Secondary Storage as HDD")
            print("4:It fetch the information about the MicroProcessor")
            print("5:It gets Auto Scheduled Perodically")
            print("6:it maintains all records into log file")
            print("7:its send the og files through mail periodically")



        elif(sys.argv[1]=='--u' or sys.argv[1]=='--U'):
            print("Use Automation script as :")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval :Time in minetues for periodic execution")
            print("Folder_Name :Name of folder for the log file creation")


        else:
            print("Unabel to procees as there is no matching arguments")
            print("Plese use --h or --u flag.for getting more details")

    #Actual project code
    elif(len(sys.argv)==3):
        pass

    else:
        print("Invalid Number of Arguments")
        print("Unabel to Proced as Arguments are not matching")
        print("Plese use --h or --u flag.for getting more details")

    print("\n",Border)
    print("---------ThankYou for Using Marvellous Platform Survellance System---------")
    print("-------------------Marvellous Platform Survellance System------------------")
    print(Border)

if __name__=="__main__":
    main()