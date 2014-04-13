import os
import os.path
import time

sixMonths = 15778463
largest = 1024**2

oldFiles = []
largeFiles = []
emptyFolders = []

for root, dirs, files in os.walk("C:\Users\loweyj\desktop"):
    for name in files:
    #####################################################################
    #
    #    Checks for older and large files in a given directory tree
    #
    #####################################################################    
        if time.time() - sixMonths > os.path.getatime(root + "\\" + name):
            #print name + "\t" , time.ctime(os.path.getmtime(root + "\\" + name))
            oldFiles.append((root+"\\"+name,name, time.ctime(os.path.getmtime(root + "\\" + name)), True))
        if os.path.getsize(root+"\\"+name)/largest > 0:
            largeFiles.append((root+"\\"+name,name, os.path.getsize(root+"\\"+name),True))
    #####################################################################
    #
    #    Checks for empty folders in the directory
    #
    #####################################################################
    for directory in dirs:
        if os.listdir(root+"\\"+directory)==[]:
            emptyFolders.append( ( root+"\\"+directory, directory , True) )


##Output the files that are too large or too old, and empty folders        
#for i in oldFiles:
    #print i
#for i in largeFiles:
    #print i
#for i in emptyFolders:
    #print i
