class Files():

	def __init__(self,p="C:",n=1,m=1,d=1,s=1,o=1,ig=set([])):
		self.path = p
		self.num = n
		self.months = m
		self.days = d
		self.size = s
		self.option = o
		length = num*months*days*3600
		largest = size*(1024**option)
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
		        if time.time() - length > os.path.getmtime(root + "\\" + name):
		            self.deleteFiles.add((root+"\\"+name, name, time.ctime(os.path.getmtime(root + "\\" + name)), True))
		        if os.path.getsize(root+"\\"+name)/largest > 0:
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