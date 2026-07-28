//This Python script checks the system metrics disk space,RAM and server uptime for Linux and Windows servers. It uses the os module to execute system commands and display the results.
import os

print(os.system("df -h"))
print(os.system("free -h"))
print(os.system("uptime -p"))

//Windows server
print(os.system("chkdsk C:"))
print(os.system("systeminfo | find \"System Boot Time\""))
print(os.system("systeminfo"))
