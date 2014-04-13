from Tkinter import *
import sys
import ttk
from tkFileDialog import *
from tkFileDialog import *
from files import *
import os
import time
import os.path
import subprocess

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets() 
        
    def get_textbox_input(self):
        return self.age.get()
        
    
    def choose_file(self):
        Tk().withdraw()
        filename = askopenfilenames()
        #print "Removing " + str(filename) + "\n" "Ignoring " + str(self.ignore_list.get())
        
        self.createWindow()

    def choose_folder(self):
        Tk().withdraw()
        foldername = askdirectory()
        self.file_age = self.get_textbox_input() 
        
        #print "Removing files in directory " + str(foldername) + " which are older than " + str(self.file_age) + " " + str(self.time_select.get()) + "\n" + "Ignoring " + str(self.ignore_list.get()) + " Size " + str(self.size_list.get())
    
        if (foldername != ""):
            self.createWindow(foldername)
        
    def createWidgets(self):
        self.QUIT = Button(self, 
                           text="QUIT", 
                           bg="red", 
                           fg="white",
                           command=self.quit, 
                           #highlightbackground="white"
                           )

        self.QUIT.grid(row=2,column=0,sticky=W)
    
        #self.file_chooser = Button(self, 
                                   #text="Choose File", 
                                   #bg="blue",
                                   #fg="white",
                                   #command=self.choose_file,
                                   #highlightbackground="white"
                                   #)
        
        #self.file_chooser.grid(row=1,column=0,sticky=W)
        
        self.folder_chooser = Button(self, 
                                     text="Choose Folder", 
                                     bg="blue",
                                     fg="white",
                                     command = self.choose_folder, 
                                     highlightbackground="white"
                                     )

        self.folder_chooser.grid(row=0,column=0,sticky=W)
        self.time_interval = None
        self.time_select = ttk.Combobox(self,
                               textvariable=self.time_interval,
                               state="readonly",
                               )
        self.time_select["values"] = ("Days", "Months", "Years")
        self.time_select.current(0)
        self.time_select.grid(row=0,column=2,sticky=W)
        
        self.entry_label = Label(self,
                                 text="Age of File:",
                                 )
        self.entry_label.grid(row=1,column=1)
        
        self.age = StringVar()
        self.time_box = Entry(self, textvariable=self.age)
        self.age.set("1")
        self.time_box.grid(row=1,column=2,sticky=W)
        self.time_box.focus_set()
        
        self.ignore_label = Label(self, 
                                  text="Ignore List"
                                  )
        self.ignore_label.grid(row=2,column=1)
        
        self.ignore_list = StringVar()
        self.ignore_ext = Entry(self, textvariable=self.ignore_list)
        self.ignore_ext.grid(row=2,column=2,sticky=W)
        
        self.size_label = Label(self,
                                text="File Size"
                                )
        self.size_label.grid(row=4,column=1)
        
        self.size_select = StringVar()
        self.size_ext1 = ttk.Combobox(self,
                                      textvariable = self.size_select,
                                      state="readonly"
                                      )
        self.size_ext1["values"] = ("Bytes", "Kbs", "Mbs", "Gbs", "Tbs")
        self.size_ext1.current(0)
        self.size_ext1.grid(row=3,column=2,stick=W)
        
        self.size_list = StringVar()
        self.size_ext = Entry(self, textvariable=self.size_list)
        self.size_list.set("1")
        self.size_ext.grid(row=4,column=2,sticky=W)
        
        self.log_option = IntVar()
        self.log_config = Checkbutton(self, variable = self.log_option, text="Log")
        self.log_config.grid(row=3,column=0,stick=W)
        self.log_config.select()
        
        self.show_log_folder = IntVar()
        self.log_folder = Checkbutton(self, variable = self.show_log_folder, text="Show Log")
        self.log_folder.grid(row=4,column=0,stick=W)
        self.log_folder.deselect()
    
        
        menubar = Menu(Root)
        
        filemenu = Menu(menubar)
        filemenu.add_command(label="Open File", command=self.choose_file)
        filemenu.add_command(label="Open Folder", command=self.choose_folder)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        
        Root.config(menu=menubar)
        Root.config(bg="white")
        
    def confirm(self):
        entireStructure = []
        entireStructure = list(self.inputData.deleteFiles)    
        
        
        outputIgnoreList = []
        count = 0
        for i in self.ignore_checkboxes:
            if i.get() == 1:
                item = list(entireStructure[count])
                path = item[0]
                #print path
                outputIgnoreList.append(path)
                
            count += 1
        
        log = logging(outputIgnoreList)
        log.ignore()        
        
        
        count = 0
        for i in self.checkboxes:
            #print self.checkboxes[i].get()
            if i.get() == "0":
                
                #print self.inputData.deleteFiles[count]
                #print self.inputData.deleteFiles[count][3]
                
                item = list(entireStructure[count])
                #print item
                item[3] = False
                #print i.get()
                #print item[1]
                #print item
                item = tuple(item)
                entireStructure[count] = item
            count += 1
        

        
        entireStructure=set(entireStructure)
        self.inputData.deleteFiles = entireStructure
        
        #print self.log_option.get()
        log = False
        if (self.log_option.get() == 1):
            log = True
        self.inputData.delete_checked(log)

            
        print(self.show_log_folder.get())
        if (self.show_log_folder.get() == 1):
            #print("test")
            path = os.path.expanduser("~")
            path = path + "\\AppData\\Roaming\\Reinigen\\Logs"
            #print path
            os.system('explorer ' + path) 
        
        self.top.destroy()
        
    
    def selectAll(self):
        for i in self.checkboxes:
            if i.get() == "0":
                i.set("1")
                
                
    def deselectAll(self):
        for i in self.checkboxes:
            #print self.checkboxes[i].get()
            if i.get() == "1":
                i.set("0")      
        
    def createWindow(self, foldername):
        self.top = Toplevel()
        self.top.title("Output")
        self.top.geometry("400x800")
    
        self.top.vsb = Scrollbar(self.top, orient="vertical")
        self.top.text = Text(self.top, width=40, height=20, 
                            yscrollcommand=self.top.vsb.set,bg="white")
        self.top.vsb.config(command=self.top.text.yview,bg="white")
        self.top.vsb.pack(side="right", fill="y")
        self.top.text.pack(side="left", fill="both", expand=True)
        
        
        #filepath, number, months, days, size, size option, ignore
        
        day_amount = 0
        if (self.time_select.get() == "Days"):
            day_amount = 1
        elif (self.time_select.get() == "Months"):
            day_amount = 31
        elif (self.time_select.get() == "Years"):
            day_amount = 365
        
        if (self.size_ext1.get() == "Bytes"):
            size_multiplier = 0
        if (self.size_ext1.get() == "Kbs"):
            size_multiplier = 1
        elif (self.size_ext1.get() == "Mbs"):
            size_multiplier = 2
        elif (self.size_ext1.get() == "Gbs"):
            size_multiplier = 3
        elif (self.size_ext1.get() == "Tbs"):
            size_multiplier = 4
        
        temp_string = []
        if self.ignore_list.get() != '':
            temp_string = self.ignore_list.get().split(',')
        
        
        #print "Folder name: " + foldername
        #print "File age: " + self.file_age
        #print "Day amount: " + str(day_amount)
        #print "Size: " + self.size_list.get()
        #print "Multiplier: " + str(size_multiplier)
        #print "Ignore List: ", temp_string
        
        self.inputData = Files(foldername, int(self.file_age), int(day_amount), int(self.size_list.get()), int(size_multiplier), temp_string)
        
        self.inputData.traverse()
        #inputData.printIt()
        
        selectAll = Button(self.top,
                           text="Select All",
                           command=self.selectAll
                           )
        self.top.text.window_create("1.0", window=selectAll)
        
        deselectAll = Button(self.top,
                           text="Deselect All",
                           command=self.deselectAll
                           )
        self.top.text.window_create("1.0", window=deselectAll)
        
        self.checkboxes = []
        self.ignore_checkboxes = []
        
        i = 1
        for item in self.inputData.deleteFiles:
            #print item

        
            txt = Label(self.top,
                        text=item[1]
                        )
            
            
            self.top.text.insert("end", "\n")
            
            self.top.text.window_create("end", window=txt)
            
            var = StringVar()
            cb = Checkbutton(self.top, variable=var,text="Remove",anchor=E,justify=RIGHT)
            cb.select()
            self.top.text.window_create("end", window=cb)
            self.checkboxes.append(var)            
            
            var1 = IntVar()
            cb = Checkbutton(self.top, variable=var1,text="Ignore",anchor=E,justify=RIGHT)
            cb.deselect()
            self.top.text.window_create("end", window=cb)
            self.ignore_checkboxes.append(var1)            
            
            i = i+1
            
        
            
        confirmSelection = Button(self.top, text="OK", command=self.confirm)
        self.top.text.window_create("1.0", window=confirmSelection)
               
if __name__ == '__main__':
    
    Root = Tk()
    Root.geometry("300x123")
    Root.title("HackRU - EZ Cleaner")
    #Root.resizable(width=FALSE, height=FALSE)
    Root.config(bg="white")
    
    app = Application(master=Root)
    app.mainloop()
    Root.destroy()