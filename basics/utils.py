import os  #Importing the os module in the code 

print(os.system("chkdsk C:"))
print(os.system("systeminfo | find \"System Boot Time\""))
print(os.system("systeminfo"))
