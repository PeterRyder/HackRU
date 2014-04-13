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
		ign = open(os.path.join(os.path.expanduser("~") , "\\AppData\\Roaming\\Reinigen\\ignore.txt"), "a")
		for i in self.files:
			ign.write(self.files + " , ")
		ign.close()

	#Check for if the directories of files in the ignore list still exist
	def ignore_path_check(self):
		ignore_list = []
		ignore_path = os.path.join(os.path.expanduser("~") , "AppData\\Roaming\\Reinigen\\ignore.txt")
		if os.path.exists(ignore_path):
			file = open(ignore_path)
			lines = file.readlines()
			file.close()
			file = open(ignore_path, "w")
			for line in lines:
				if os.path.exists(line):
					file.write(line)
					ignore_list.append(line)
			file.close()
		return ignore_list
