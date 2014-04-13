import os
import os.path
import time

class logging():

	def __init__(self, files=[]):
		self.files = files

	def log(self):
		if not os.path.exists(os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen\\Logs")):
		        os.makedirs(os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen\\Logs"))
		log = open(os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen\\Logs\\ReinigenLog " + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + ".txt"), "w")
		for i in self.files:
			log.write(self.files[1] + " deleted from directory " + self.files[0] + "\n")
		log.close()

	def ignore(self):
		if not os.path.exists(os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen")):
			os.makedirs(os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen"))
		if os.path.isfile(os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen\\ignore.txt")):
			ign = open(os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen\\ignore.txt"), "a")
		else:
			ign = open(os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen\\ignore.txt"), "w")
		for i in self.files:
			ign.write(i + "\n")
		ign.close()