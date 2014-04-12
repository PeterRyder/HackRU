import os
import os.path
import time

sixMonths = 15778463
largest = 1024**2

oldFiles = []
largeFiles = []

for root, dirs, files in os.walk("C:\Users\loweyj\desktop"):
    for name in files:
        if time.time() - sixMonths > os.path.getmtime(root + "\\" + name):
            #print name + "\t" , time.ctime(os.path.getmtime(root + "\\" + name))
            oldFiles.append((root+"\\"+name,name, time.ctime(os.path.getmtime(root + "\\" + name))))
        if os.path.getsize(root+"\\"+name)/largest > 0:
            largeFiles.append((root+"\\"+name,name, os.path.getsize(root+"\\"+name)))
        
for i in oldFiles:
    print i
for i in largeFiles:
    print i