import sys
sys.path.append(r"C:/Users/KAY3SF/Desktop/Training/PythonT")

from OperatingSystemScan import OSReader as OSR



def WriteLogs():
    with open("PC_LOGS.txt",'a')as file:
        file.write(str(OSR.CPU_Reader.DisplayCPU_Usage()))
        file.write(str(OSR.DISK_Reader.DisplayDisk_Usage()))
        file.write(str(OSR.RAM_Reader.DisplayRAM_Usage()))