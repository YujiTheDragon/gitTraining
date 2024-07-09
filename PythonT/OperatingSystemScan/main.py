import OSReader as OSR
from time import time
from datetime import datetime
import Visualization as VIS


def GetData():
    OSR.CPU_Reader.DisplayCPU_Usage()
    OSR.RAM_Reader.DisplayRAM_Usage()
    OSR.DISK_Reader.DisplayDisk_Usage()


def main():
    
    VIS.draw.DisplayData()
    open("PC_LOGS.txt", "w").close()
    with open("PC_LOGS.txt", "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
    start = time()
    GetData()
    end = time()
    print(f"Time Elapsed: {end-start:.2f}s")


if __name__ == "__main__":
    main()
