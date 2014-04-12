import os
import os.path
import time

sixMonths = 15778463

files = []

for root, dirs, files in os.walk("C:\Users\loweyj\desktop"):
    for name in files:
        if time.time() - sixMonths > os.path.getmtime(root + "\\" + name):
            #print name + "\t" , time.ctime(os.path.getmtime(root + "\\" + name))
            hi.append((root+"\\"+name,name, time.ctime(os.path.getmtime(root + "\\" + name))))
        
for i in files:
    print i