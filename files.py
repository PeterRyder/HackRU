import os
import os.path
import time
from send2trash import send2trash
from logging import *

class Files():

	#Initializations 
	def __init__(self,p="C:",n=1,d=1,s=1,o=1,ig=[]):
		self.path = p
		self.num = n
		self.days = d
		self.size = s
		self.option = o
		#youngest file to add to the delete list
		self.length = self.num*self.days*3600
		#smallest file size to add
		self.largest = self.size*(1024**self.option)
		#File types to be ignored
		self.ignore = tuple(ig)
		self.deleteFiles = set([])

	#Find all files and directories that can be deleted and add them to the set deleteFiles 
	def traverse(self):
		#Declare list of files and directories to ignore and removes ignore directories that no longer exist
		ignore_paths = ignore_path_check()
		#For each file and empty directory add it to a delete list
		for root, dirs, files in os.walk(self.path):
		    for name in files:
				#If the file directory is not in the ignore list, check other criteria
				if root + "\\" + name not in ignore_paths:
				#####################################################################
				#     Checks for older and large files in a given directory tree    #
				#####################################################################
					if len(self.ignore) > 0:
						if (not name.endswith(self.ignore)) and (self.length > 0) and (time.time() - self.length > os.path.getmtime(root + "\\" + name)):
							self.deleteFiles.add((root+"\\"+name, name, time.ctime(os.path.getmtime(root + "\\" + name)), True))
						if (not name.endswith(self.ignore)) and (self.largest > 0) and (os.path.getsize(root+"\\"+name)/self.largest > 0):
							self.deleteFiles.add((root+"\\"+name, name, os.path.getsize(root+"\\"+name),True))
					else:
						if (self.length > 0) and (time.time() - self.length > os.path.getmtime(root + "\\" + name)):
							self.deleteFiles.add((root+"\\"+name, name, time.ctime(os.path.getmtime(root + "\\" + name)), True))
						if (self.largest > 0) and (os.path.getsize(root+"\\"+name)/self.largest > 0):
							self.deleteFiles.add((root+"\\"+name, name, os.path.getsize(root+"\\"+name),True))
		    #####################################################################
		    #   		  Checks for empty folders in the directory             #
		    #####################################################################
		    for directory in dirs:
				#If the directory is not in the ignore file and it is empty, delete it
				if root + "\\" + directory not in ignore_paths and os.listdir(root+"\\"+directory)==[]:
					self.deleteFiles.add( ( root+"\\"+directory, directory, "THIS FOLDER IS EMPTY!" , True) )	

	#Goes through the files after they've been selected for deleting 
	def delete_checked(self,log=True):
		if len(self.deleteFiles): 
			logVals = []
			#Check if all values are being deleted from a directory, if so, delete that instead
			self.checkEmpty(logVals)
			#For each file to be deleted, write the file into the log and send the file to the recycling bin
			for file_name in self.deleteFiles:
				#If the file is listed for deletion (4th value of tuple is True)
				if file_name[3] == True:
					#Write the file to the log file and delete it
					logVals.add(file_name)
					send2trash(file_name[0])
			#Close the file 
			if log == True and len(logVals) > 0:
				myLog = logging(logVals)
				myLog.log()


	#Function to print 
	def printIt(self):
		for i in self.deleteFiles:
			print i

	#Check if any of the directories would be empty from all the values inside them being deleted; if so, delete the directory and not each file 
	def checkEmpty(self, log_file):
		for root, dirs, files in os.walk(self.path,False):
			#Count of the number of files set to be deleted in each directory
			count = 0
			#If a file is set to be deleted, increment count
			for name in files:
				if (root+"\\"+name, name, time.ctime(os.path.getmtime(root + "\\" + name)), True) in self.deleteFiles:
					count+=1;
				if (root+"\\"+name, name, os.path.getsize(root+"\\"+name),True) in self.deleteFiles:
					count += 1            
			#If all of the files of a directory are set to be deleted, delete the directory instead
			if count == len(os.listdir(root)) and (not (( root, root.split('\\')[-1], "THIS FOLDER IS EMPTY!" , False) in self.deleteFiles)):
				log_file.append(( root, root.split('\\')[-1], "THIS FOLDER IS EMPTY!" , False))
				send2trash(root)

	#Early stage function designed to recommend a directory that the file should be used should the user prompt not to delete it 
	def suggest_move(name):
		#Different common file types for default microsoft libraries
		documents_ext = [".doc", ".docx", ".log", ".msg", ".odt", ".pages", ".rtf", ".tex", ".txt", ".wpd", ".wps", ".ppt", ".pptx", ".pps", ".xlr", ".xls", ".xlsx", ".pdf"]		
		musics_ext = [".aif", ".iff", ".m3u", ".m4a", ".mid", ".mp3", ".mpa", ".ra", ".wav", ".wma", ".flac"]
		pictures_ext = [".bmp", ".dds", ".gif", ".jpg", ".png", ".psd", ".pspimage", ".tga", ".thm", ".tif", ".tiff", ".yuv"]
		videos_ext = [".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv", ".m4v", ".mov", ".mp4", ".mpg", ".rm", ".srt", ".swf", ".vob", ".wmv"]
		#If the file type of name matches one in documents, music...etc, recommended it 
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