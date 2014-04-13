from Tkinter import *
import sys
import ttk
from tkFileDialog import *
from tkFileDialog import *

from PIL import ImageTk,Image

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
        print "Removing " + str(filename)
    
    def choose_folder(self):
        Tk().withdraw()
        foldername = askdirectory()
        file_age = self.get_textbox_input() 
        
        print "Removing files in directory " + str(foldername) + " which are older than " + str(file_age) + " " + str(self.time_select.get())
        
    def createWidgets(self):
        self.QUIT = Button(self, 
                           text="QUIT", 
                           bg="red", 
                           fg="white",
                           command=self.quit, 
                           #highlightbackground="white"
                           )

        self.QUIT.grid(row=2,column=0)
    
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
        
        menubar = Menu(Root)
        
        filemenu = Menu(menubar)
        filemenu.add_command(label="Open File", command=self.choose_file)
        filemenu.add_command(label="Open Folder", command=self.choose_folder)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        
        Root.config(menu=menubar)
        Root.config(bg="white")

if __name__ == '__main__':
    
    Root = Tk()
    Root.geometry("350x100")
    Root.title("HackRU - EZ Cleaner")
    #Root.resizable(width=FALSE, height=FALSE)
    Root.config(bg="white")
    
    app = Application(master=Root)
    outputList = 
    app.mainloop()
    Root.destroy()