import os
import os.path
import time
import shutil

sixMonths = 15778463
check_path = "C:\Users\walkeb7\Downloads\Test"

delete_files = []

for root, dirs, files in os.walk(check_path):
    for name in files:
        if time.time() - sixMonths > os.path.getmtime(root + "\\" + name):
            delete_files.append(root+"\\"+name)
        
for i in delete_files:
    print i
    
if len(delete_files): 
    del_folder = check_path + "\Reinigen_files_3"
    os.makedirs(del_folder)
    for file_name in delete_files:
        shutil.move(file_name, del_folder) 
    
    if os.path.exists("C:\$recycle.bin"):
        print "successful pidgeon"
    #shutil.move(del_folder, "C:\$Recycle.Bin")ugygvy