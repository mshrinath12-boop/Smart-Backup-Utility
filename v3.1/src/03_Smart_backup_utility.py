import os
import shutil
import logging
import time
from datetime import datetime
from datetime import date
logging.basicConfig(
    filename= "Automation.log",
    level= logging.INFO,
    format= "%(asctime)s | %(levelname)s | %(message)s"

)
run_date= date.today()
source_folder= "files"
backup_folder= "Backups"
start_time= time.time()
start_datetime= datetime.now()
success_count= 0
failed_count= 0
skipped_count= 0
total_files= 0
if os.path.isdir(source_folder):
    if not os.path.exists(backup_folder):
        os.mkdir(backup_folder)
else:
    print(f"Source folder not found: {source_folder}")        
for root,dirs,files in os.walk(source_folder):
    for file in files:
        total_files+=1
        source_path= os.path.join(root,file)
        relative_path= os.path.relpath(root,source_folder)
        destination_folder=os.path.join(backup_folder,relative_path)
        destination_path= os.path.join(destination_folder,file)
        os.makedirs(destination_folder,exist_ok=True)
        try:    
            shutil.copy2(source_path,destination_path)
            success_count+=1
            logging.info(f"File copied suucessfully: {file}")
            print(f"File copied successfully: {file}")
        except FileNotFoundError:
            logging.error(f"Requested file not found: {file}")
            print(f"File not found error: {file}")
            failed_count+=1
        except PermissionError:
            logging.error(f"Access denied to the requested file: {file}")
            print(f"Access denied to the requested file: {file}")
            failed_count+=1
        except IsADirectoryError:
            logging.error(f"Requested file is a directory: {file}")
            print(f"Requested file is a directory: {file}")
            failed_count+=1
        except OSError as e:
            logging.error(f"The following error is : {e}")
            print(f"The following error is: {e}")
            failed_count+=1
end_time= time.time()
end_datetime= datetime.now()
execution_time= end_time-start_time
with open ("Smart_backup_utility.txt","w") as report:
    report.write("===============================\n")
    report.write("Smart Backup report\n")
    report.write("===============================\n")
    report.write(f"Run Date: {run_date}\n")
    report.write(f"Start Time: {start_datetime.strftime('%d %m %Y %H:%M:%S')} \n")
    report.write(f"End time: {end_datetime.strftime('%d %m %Y %H:%M:%S')}\n")
    report.write(f"Execution Time: {execution_time:.3f} seconds\n")
    report.write(f"Source Folder: {source_folder}\n")
    report.write(f"Backup Folder: {backup_folder}\n")
    report.write(f"Total Files: {total_files}\n")
    report.write(f"Successfully copied: {success_count}\n")
    report.write(f"Failed copies: {failed_count}\n")
    report.write(f"Backup completed of: {source_folder}")
print(f"Backup completed of: {source_folder}")    








    

