import psutil
import decimal

def DisplayDisk_Usage():
    DiskUsedSpace = (psutil.disk_usage('/')[1])/1000000000
    DiskFreeSpace = (psutil.disk_usage('/')[2])/1000000000
    DiskUsagePercent = psutil.disk_usage('/')[3]
    print("Disk Used Space: ",str(round(DiskUsedSpace,2))+"GB")
    print("Disk Free Space: ",str(round(DiskFreeSpace,2))+"GB")
    print("Disk Usage: ",str(DiskUsagePercent)+"%")