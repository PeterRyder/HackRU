import os
import os.path
import time

class logging():

	def __init__(self, files=[]):
		self.files = files

	def log(self):
		log = open(os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen\\Logs\\Reinigen Log " + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + ".txt"), "w")
		for i in self.files:
			log.write(self.files[1] + " deleted from directory " + self.files[0] + "\n")
		log.close()

	def ignore(self):
		ign = open(os.path.join(os.path.expanduser("~") , "\\AppData\\Roaming\\Reinigen\\ignore.txt"), "a")
		for i in self.files:
			ign.write(self.files + " , ")
		ign.close()