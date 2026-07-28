#using the shutil module to get disk usage statistics and pandas to create a DataFrame and save it as a CSV file
import shutil
import pandas as pd

drive_name = "C:\\"

stats = shutil.disk_usage(drive_name)

total_size = round(stats.total / (1024 ** 3), 2)  # Convert bytes to GB
free_space = round(stats.free / (1024 ** 3), 2)  # Convert bytes to GB
used_space = round(stats.used / (1024 ** 3), 2)  # Convert bytes to GB  

#creating a list of values and index for the DataFrame
values = [drive_name, total_size, free_space, used_space]
index = ['Drive Name', 'Total Size (GB)', 'Free Space (GB)', 'Used Space (GB)']

#Pairing the lists elements and convert the data into a 2D Tabular format
data_frame = pd.DataFrame(list(zip(index, values)), columns=['Information', 'Report'])  

data_frame.to_csv("disk_usage_report.csv")  #Save the DataFrame to a CSV file  

print("Disk usage statistics: ")
print("Total Size (GB):", total_size, "Free Space (GB):", free_space, 
      "Used Space (GB):", used_space)
