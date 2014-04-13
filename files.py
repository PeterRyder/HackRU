import os
import os.path
import time
from send2trash import send2trash

class Files():

	def __init__(self,p="C:",n=1,m=1,d=1,s=1,o=1,ig=set([])):
		self.path = p
		self.num = n
		self.months = m
		self.days = d
		self.size = s
		self.option = o
		self.length = self.num*self.months*self.days*3600
		self.largest = self.size*(1024**self.option)
		self.ignore = ig
		self.deleteFiles = set([])
		

	def traverse(self):
		for root, dirs, files in os.walk(self.path):
		    for name in files:
		    #####################################################################
		    #                                                                   #
		    #    Checks for older and large files in a given directory tree     #
		    #                                                                   #
		    #####################################################################    
		        if time.time() - self.length > os.path.getmtime(root + "\\" + name):
		            self.deleteFiles.add((root+"\\"+name, name, time.ctime(os.path.getmtime(root + "\\" + name)), True))
		        if os.path.getsize(root+"\\"+name)/self.largest > 0:
		            self.deleteFiles.add((root+"\\"+name, name, os.path.getsize(root+"\\"+name),True))
		    #####################################################################
		    #                                                                   #
		    #    Checks for empty folders in the directory                      #
		    #                                                                   #
		    #####################################################################
		    for directory in dirs:
		        if os.listdir(root+"\\"+directory)==[]:
		            self.deleteFiles.add( ( root+"\\"+directory, directory, "THIS FOLDER IS EMPTY!" , True) )
	
	def delete_checked(self):
		if len(deletefiles): 
			#print del_folder  #debug
			#Creates a log file to write the deleted files and directories to
			log = open(os.path.join(path, "Reinigen Log.txt"), "w")
			for file_name in deletefiles:
				#log.write(raw_input(file_name[1]))
				send2trash(file_name[0])
			log.close()
		#possibly call traverse again to check for now empty directories and then call delete_checked again

	def printIt(self):
		for i in self.deleteFiles:
			print i
<<<<<<< 23f3fed6c4e3f4ddda24cbb4442317fe2d0aad71

	def checkEmpty(self):
		for root, dirs, files in os.walk(self.path):
			int count = 0;
			for directory in dirs:
		        if (root+"\\"+name, name, time.ctime(os.path.getmtime(root + "\\" + name)), True) in self.deletefiles:
		        	count+=1;
		        if (root+"\\"+name, name, os.path.getsize(root+"\\"+name),True) in self.deletefiles:
			        count += 1            
			if count == len(os.listdir(root+"\\"+directory)):
				send2trash(root+"\\"+directory)
=======
			
	
	def suggest_move(name):
		documents_ext = [".doc", ".docx", ".log", ".msg", ".odt", ".pages", ".rtf", ".tex", ".txt", ".wpd", ".wps", ".ppt", ".pptx", ".pps", ".xlr", ".xls", ".xlsx", ".pdf"]		
		musics_ext = [".aif", ".iff", ".m3u", ".m4a", ".mid", ".mp3", ".mpa", ".ra", ".wav", ".wma"]
		pictures_ext = [".bmp", ".dds", ".gif", ".jpg", ".png", ".psd", ".pspimage", ".tga", ".thm", ".tif", ".tiff", ".yuv"]
		videos_ext = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".mpg", ".rm", ".srt", ".swf", ".vob", ".wmv"]
		for ext in documents_ext:
			if name.endswith(ext):
				return "document"
		for ext in musics_ext: 
			if name.endswith(ext):
				return "music"
		for ext in pictures_ext:
			if name.endswith(ext):
				return "picture"
		for ext in videos_ext:
			if name.endswith(ext):
				return "video"	
		return "unknown"
	
	#def move_file(file_name, destination)
>>>>>>> 432e7c7609aaa86f075d622ee93073742ff6006a
