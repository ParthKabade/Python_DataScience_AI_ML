import psutil
import sys
import os
import time
import schedule

def ProcessScan():
    for proc in psutil.process_iter():
        info=proc.as_dict(attrs=["pid","name","username","status"])
        info["cpu_percent"]=proc.cpu_percent(None)
        info["memory_percent"]=proc.memory_percent()

        print("-"*85)
        print(info)
        print("-"*85)

def PlatformSurvillance(FolderName):
    Border="-"*85

    Ret=False
    Ret=os.path.exists(FolderName)

    if Ret==True:
        Ret=os.path.isdir(FolderName)
        if(Ret==False):
            print("Unabel to proced as Folder Name is Existing But it is Not a Directory")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log file get created succesfully")

    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName=os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj=open(FileName,'w')

    print(f"Log file gets Succesfully created with name {FileName}")

    fobj.write(Border+"\n")
    fobj.write("-------------------Marvellous Platform Survellance System------------------\n")
    fobj.write(f"Log file Gets Created at {timestamp}\n")
    fobj.write(Border+"\n\n")
    
    #CPU INFORMATION
    fobj.write(f"------------------------------ CPU REPORT ------------------------------\n")
    fobj.write(f"Number of active CPU cores :{psutil.cpu_count()}\n")
    fobj.write(f"CPU usage :{psutil.cpu_percent()}\n")

    #RAM INFORMATION
    fobj.write(f"------------------------------ RAM REPORT ------------------------------\n")
    memory=psutil.virtual_memory()
    fobj.write(f"RAM usage :{memory.percent}\n")
    fobj.write(f"Total RAM availabel :{memory.total}\n")

    #NETWORK USAGE
    fobj.write(f"------------------------------ NETWORK REPORT ------------------------------\n")
    netobj=psutil.net_io_counters()
    fobj.write("Sent :%2.f MB\n"%(netobj.bytes_sent/(1024*1024)))
    fobj.write("Recived :%2.f MB\n"%(netobj.bytes_recv/(1024*1024)))
    fobj.write(f"\n"*10)

    fobj.write(f"{Border}\n")
    fobj.write(f"----------------------------- End of Log file -----------------------------\n")
    fobj.write(f"{Border}\n")

    fobj.close()

    
def main():
    ProcessScan()
    Border="-"*85
    print(Border)
    print("------------------------Marvellous Platform Survellance System-----------------------")
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
        #print(f"CPU usage :{psutil.cpu_percent()}")
        print("SCHEDULAR STARTED SUCCESFULLY")
        print("Press CMD+C/Ctrl+C to abort the process")
        schedule.every(int(sys.argv[1])).seconds.do(PlatformSurvillance,sys.argv[2])
        while 1:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of Arguments")
        print("Unabel to Proced as Arguments are not matching")
        print("Plese use --h or --u flag.for getting more details\n")

    print(Border)
    print("---------ThankYou for Using Marvellous Platform Survellance System---------")
    print("-------------------Marvellous Platform Survellance System------------------")
    print(Border)

if __name__=="__main__":
    main()