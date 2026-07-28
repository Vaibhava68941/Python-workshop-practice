import os
import datetime
import shutil

def backup_files(source, destination):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination, exist_ok=True)
    
    # Get today's date for the filename
    today = datetime.date.today()
    
    # shutil.make_archive appends '.zip' automatically, 
    # so we define the base path without the extension
    backup_base_path = os.path.join(destination, f'backup_{today}') 
    
    print(f"Creating backup at: {backup_base_path}.zip")
    
    # Create the zip archive
    shutil.make_archive(backup_base_path, 'zip', source)
    print("Backup completed successfully!")

# --- Define paths and call the function OUTSIDE the function block ---
source_dir = r"C:\Users\USER\Documents\Python-workshop-practice"  
destination_dir = r"C:\Users\USER\Documents\Python-workshop-practice\backups" 

backup_files(source_dir, destination_dir)

