import psutil
import decimal

def DisplayRAM_Usage():
    getUsedVirtualMemory = psutil.virtual_memory()[3]/1000000000
    getAvailVirtualMemory = psutil.virtual_memory()[4]/1000000000

    print ("RAM memory used: ",str(psutil.virtual_memory()[2])+"%")
    print ("RAM Used (GB): ",str(round(getUsedVirtualMemory,2))+"GB")
    print ("RAM Available (GB): ",str(round(getAvailVirtualMemory,2))+"GB")

def RamTest(testRange):
    for i in range(testRange):
        RamTest(testRange-1)
