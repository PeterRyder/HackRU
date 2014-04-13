from Tkinter import *
import sys
import ttk
from tkFileDialog import *
from tkFileDialog import *
from files import *
import os
import time
import os.path

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
        print "Removing " + str(filename) + "\n" "Ignoring " + str(self.ignore_list.get())
        
        
        
        self.createWindow()

    def choose_folder(self):
        Tk().withdraw()
        foldername = askdirectory()
        self.file_age = self.get_textbox_input() 
        
        print "Removing files in directory " + str(foldername) + " which are older than " + str(self.file_age) + " " + str(self.time_select.get()) + "\n" + "Ignoring " + str(self.ignore_list.get()) + " Size " + str(self.size_list.get())
    
        
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
    
        self.file_chooser = Button(self, 
                                   text="Choose File", 
                                   bg="blue",
                                   fg="white",
                                   command=self.choose_file,
                                   highlightbackground="white"
                                   )
        
        self.file_chooser.grid(row=1,column=0,sticky=W)
        
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
        self.size_label.grid(row=3,column=1)
        
        self.size_select = StringVar()
        self.size_ext1 = ttk.Combobox(self,
                                      textvariable = self.size_select,
                                      state="readonly"
                                      )
        self.size_ext1["values"] = ("Kbs", "Mbs", "Gbs", "Tbs")
        self.size_ext1.current(0)
        self.size_ext1.grid(row=3,column=2,stick=W)
        
        self.size_list = StringVar()
        self.size_ext = Entry(self, textvariable=self.size_list)
        self.size_ext.grid(row=4,column=2,sticky=W)
        
        menubar = Menu(Root)
        
        filemenu = Menu(menubar)
        filemenu.add_command(label="Open File", command=self.choose_file)
        filemenu.add_command(label="Open Folder", command=self.choose_folder)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        
        Root.config(menu=menubar)
        Root.config(bg="white")
        
    def select_all(self):
        print "This button in progress"
        
    def confirm(self):
        count = 0
        for i in self.checkboxes.keys():
            #print self.checkboxes[i].get()
            if self.checkboxes[i].get() == "0":
                #print self.inputData.deleteFiles[count]
                #print self.inputData.deleteFiles[count][3]
                var = []
                var = list(self.inputData.deleteFiles)
                
                var1 = list(var[count])
                var1[3] = False
                var1 = tuple(var1)
                var[count] = var1
                var=set(var)
                
                self.inputData.deleteFiles = var
                
            count += 1
                
        for i in self.inputData.deleteFiles:
            print i
        
        self.top.destroy()
        
        
    def createWindow(self, foldername):
        self.top = Toplevel()
        self.top.title("Output")
        self.top.geometry("800x600")
        
        #top.checkAll = Button(top,
                              #text="Check All",
                              #command=self.select_all,
                              #)
        #top.checkAll.grid(row=0,column=0)
        
        
        
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
            
        if (self.size_ext1.get() == "Kbs"):
            size_multiplier = 1
        elif (self.size_ext1.get() == "Mbs"):
            size_multiplier = 2
        elif (self.size_ext1.get() == "Gbs"):
            size_multiplier = 3
        elif (self.size_ext1.get() == "Tbs"):
            size_multiplier = 4
        
        
        temp_string = self.ignore_list.get().split(',')
        
        print "Folder name: " + foldername
        print "File age: " + self.file_age
        print "Day amount: " + str(day_amount)
        print "Size: " + self.size_list.get()
        print "Multiplier: " + str(size_multiplier)
        print "Ignore List: ", temp_string
        
        
        
        
        self.inputData = Files(foldername, int(self.file_age), int(day_amount), int(self.size_list.get()), int(size_multiplier), temp_string)
        
        self.inputData.traverse()
        #inputData.printIt()
        
        self.checkboxes = {}
        
        i = 1
        for item in self.inputData.deleteFiles:
            #print item
            var = StringVar()
            cb = Checkbutton(self.top, variable=var)
            cb.select()
            self.top.text.window_create("end", window=cb)
            self.checkboxes[cb] = var
            
            
            txt = Label(self.top,
                        text=item[1]
                        )
            self.top.text.window_create("end", window=txt)
            
            self.top.text.insert("end", "\n")
            
            i = i+1
            
        confirmSelection = Button(self.top, text="OK", command=self.confirm)
        self.top.text.window_create("end", window=confirmSelection)
               
if __name__ == '__main__':
    
    Root = Tk()
    Root.geometry("300x120")
    Root.title("HackRU - EZ Cleaner")
    #Root.resizable(width=FALSE, height=FALSE)
    Root.config(bg="white")
    
    app = Application(master=Root)
    app.mainloop()
    Root.destroy()