import psutil


def DisplayCPU_Usage():                                         #LOG DATA
    print("The CPU Usage is: ",str(psutil.cpu_percent(1))+"%", file = open("PC_LOGS.txt",'a'))
    print("The CPU Speed is: ",str(psutil.cpu_freq()[0])+"Mhz",file = open("PC_LOGS.txt",'a'))
    print("The CPU Count is: ",psutil.cpu_count(),file = open("PC_LOGS.txt",'a'))
    

