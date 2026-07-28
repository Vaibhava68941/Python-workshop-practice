#!/usr/bin/env python3

import os
import datetime
import shutil

def backup_dir(source,destination):

      os.makedirs(destination, exist_ok=True)
      today=datetime.date.today()
      backup_name=os.path.join(destination,f"backup_{today}.tar.gz")

      try:
          shutil.make_archive(backup_name.replace('.tar.gz',''),'gztar',source)
          print("Backup created successfully {backup_name}")

      except Exception as e:
          print("Error creating backup:{e}")

source_dir="/home/ubuntu/Python-workshop-practice/"
destination_dir="/home/ubuntu/Python-workshop-practice/backups"

backup_dir(source_dir,destination_dir)









