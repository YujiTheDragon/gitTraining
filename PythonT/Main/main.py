
import sys
sys.path.append("C:/Users/KAY3SF/Desktop/Training/PythonT")


import  OSReader as OSR

def main():
    while(1):
        OSR.CPU_Reader.DisplayCPU_Usage()
        OSR.RAM_Reader.DisplayRAM_Usage()
        OSR.Disk_Reader.DisplayDisk_Usage()
        print("\nNEXT BATCH")

if __name__ == "__main__":
    main()