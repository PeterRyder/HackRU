import os
import os.path
import time
from send2trash import send2trash
import shutil

num = 6
months = 1
days = 31
length = num*months*days*3600

option = 2
size = 1
largest = size*(1024**option)

path = "C:\Users\gallia\downloads\Test"

delete_files = set()

for root, dirs, files in os.walk(path):
    for name in files:
	if name == "lol1.txt":
	    delete_files.add((root+"\\"+name,name, time.ctime(os.path.getmtime(root + "\\" + name)), True))
    #####################################################################                                                               
    #    Checks for older and large files in a given directory tree     #
    #####################################################################    
        if time.time() - length > os.path.getatime(root + "\\" + name):
            #print name + "\t" , time.ctime(os.path.getmtime(root + "\\" + name))
            delete_files.add((root+"\\"+name,name, time.ctime(os.path.getmtime(root + "\\" + name)), True))
        if os.path.getsize(root+"\\"+name)/largest > 0:
            delete_files.add((root+"\\"+name,name, os.path.getsize(root+"\\"+name),True))
    #####################################################################                                                              
    #    		Checks for empty folders in the directory               #
    #####################################################################
    for directory in dirs:
        if os.listdir(root+"\\"+directory)==[]:
            delete_files.add( ( root+"\\"+directory, directory , True) )


##Output the files that are too large or too old, and empty folders        

#if you delete all files in a sub directory, delete subdirectory 

#for i in oldFiles:
    #print i
#for i in largeFiles:
    #print i
for i in emptyFolders:
    print i	

if len(delete_files): 
    #print del_folder  #debug
    #Creates a log file to write the deleted files and directories to
    log = open(os.path.join(path, "Reinigen Log.txt"), "w")
    for file_name in delete_files:
	#log.write(raw_input(file_name[1]))
        send2trash(file_name[0])
    log.close()

