import psutil


def DisplayCPU_Usage():
    print("The CPU Usage is: ",str(psutil.cpu_percent(1))+"%")
    print("The CPU Speed is: ",str(psutil.cpu_freq()[0])+"Mhz")
    print("The CPU Count is: ",psutil.cpu_count())
    

