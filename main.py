import os
import os.path
import time

for root, dirs, files in os.walk("C:\Users\loweyj\desktop"):
    for name in files:
        print  name + "\t " + time.ctime(os.path.getmtime(root + "\\" + name))