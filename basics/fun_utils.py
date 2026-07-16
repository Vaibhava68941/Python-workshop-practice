import os         
import datetime

def run_command(command):
    print(os.system(command))

def show_date():
    return datetime.datetime.today()

today = show_date()
print(today)

#run_command("date")  #calling a funtion    
#run_command("systeminfo")  #calling a funtion