
import sys
sys.path.append("C:/Users/KAY3SF/Desktop/Training/PythonT/OperatingSystemScan")


import  OSReader as OSR
from time import time
import decimal

def main():
    while(1):
        start = time()
        OSR.CPU_Reader.DisplayCPU_Usage()
        OSR.RAM_Reader.DisplayRAM_Usage()
        OSR.RAM_Reader.RamTest(10)
        OSR.DISK_Reader.DisplayDisk_Usage()
        end = time()
        print("Time Elapsed: "+str(round(end - start,2))+"s")
        print("NEXT BATCH")

if __name__ == "__main__":
    main()