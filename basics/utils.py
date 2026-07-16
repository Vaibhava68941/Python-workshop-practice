import os
import shutil  

#checking the disk usage of the root directory
total, used, free = shutil.disk_usage("/") 

# Convert the bytes to Gigabytes (1 GB = 1024^3 bytes)
total_disk_gb = total / (1024 ** 3)
used_disk_gb = used / (1024 ** 3)
free_disk_gb = free / (1024 ** 3)

# Print the formatted result
print(f"Total Disk Space: {total_disk_gb:.2f} GB")
print(f"Used Disk Space: {used_disk_gb:.2f} GB")
print(f"Free Disk Space: {free_disk_gb:.2f} GB")

//Windows server
print(os.system("chkdsk C:"))
print(os.system("systeminfo | find \"System Boot Time\""))
print(os.system("systeminfo"))
