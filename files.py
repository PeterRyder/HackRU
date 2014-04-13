class Files(self):

	def __init__(self,p="C:",n=1,m=1,d=1,s=1,o=1,ig=set([])):
		self.path = p
		self.num = n
		self.months = m
		self.days = d
		self.size = s
		self.option = o
		self.ignore = ig
		self.deleteFiles = set([])
		

	def traverse(self):
		for root, dirs, files in os.walk(path):
		    for name in files:
		    #####################################################################
		    #                                                                   #
		    #    Checks for older and large files in a given directory tree     #
		    #                                                                   #
		    #####################################################################    
		        if time.time() - length > os.path.getmtime(root + "\\" + name):
		            deleteFiles.add((root+"\\"+name,name, time.ctime(os.path.getmtime(root + "\\" + name)), True))
		        if os.path.getsize(root+"\\"+name)/largest > 0:
		            deleteFiles.add((root+"\\"+name,name, os.path.getsize(root+"\\"+name),True))
		    #####################################################################
		    #                                                                   #
		    #    Checks for empty folders in the directory                      #
		    #                                                                   #
		    #####################################################################
		    for directory in dirs:
		        if os.listdir(root+"\\"+directory)==[]:
		            deleteFiles.add( ( root+"\\"+directory, directory , True) )