import psutil

def DisplayDisk_Usage():
    DiskUsedSpace = (psutil.disk_usage('/')[1])/1000000000
    DiskFreeSpace = (psutil.disk_usage('/')[2])/1000000000
    DiskUsagePercent = psutil.disk_usage('/')[3]
    
    print(f"Disk Used Space: {DiskUsedSpace:.2f}GB")
    print(f"Disk Free Space: {DiskFreeSpace:.2f}GB")
    print("Disk Usage: ",str(DiskUsagePercent)+"%")