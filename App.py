from tkinter import *
from tkinter import ttk #Getting Tabs from this library
import tkinter as tk

class Tabs(tk.Frame):
  def __init__(self, parent):
    self.parent = parent
    tk.Frame.__init__(self, self.parent)
    self.tabControl = ttk.Notebook(self.parent) #Initializing Tabs
    self.style = ttk.Style(self.parent) #initializing the Styling of the Tabs
    self.style.theme_use('default')
    self.style.configure('TNotebook.Tab', background="#add8e6")
    self.style.map("TNotebook", background= [("selected", "red")])
    self.add_Tabs() #Calling in the Function of adding Tabs
    self.Tabs1() #Calling in the function of the First Tab layer top
    self.Tabs2() #Calling in the function of the Second Tab
    
  def add_Tabs(self):
    #We initialize Tab 1 & 2
    self.tabs1 = ttk.Frame(self.tabControl)
    self.tabs2 = ttk.Frame(self.tabControl)
    #from the Parent of the Switching Tab, we add in Tab 1 & 2, and then we name each of them
    self.tabControl.add(self.tabs1, text ="Main Record")
    self.tabControl.add(self.tabs2, text ="Add New Record")
    #Made sure we pack the parent tab and add arguments of how we want it to appear on windows
    self.tabControl.pack(expand=True, fill = 'both',padx = 10, pady = 10)
  
  def Tabs1(self):
    #Top Frame
    self.topframe = Frame(self.tabs1)
    self.topframe.pack(anchor = N,side=TOP,fill=X,expand=FALSE, pady = (0,20))
    #DropDown Menu
    self.Dropdown = OptionMenu(self.topframe, "master", "Man")
    self.Dropdown.pack(expand = FALSE, fill=X)
    #Company's Name
    self.label1 = Label(self.topframe, height = 1, width = 13, text = " Company's Name:", font=("Latha", 10),padx=5)
    self.textbox1 = Text(self.topframe, height = 1, width = 25)
    self.label1.pack(side = LEFT,expand = FALSE, fill= NONE)
    self.textbox1.pack(side = LEFT, expand = TRUE, fill=X)
    #Position/Role Display Box
    self.label2 = Label(self.topframe, height = 1, width = 10, text = "Position/Role:", font=("Latha", 10))
    self.textbox2 = Text(self.topframe, height = 1, width = 20)
    self.label2.pack(side= LEFT, expand = FALSE, fill=NONE)
    self.textbox2.pack(side= LEFT, expand = TRUE, fill=X)
    #Date Applied Display Box
    self.label3 = Label(self.topframe, height = 1, width = 10, text = "Date Applied:", font=("Latha", 10))
    self.textbox3 = Text(self.topframe, height = 1, width = 20)
    self.label3.pack(side = LEFT, expand = FALSE, fill=NONE) 
    self.textbox3.pack(side = LEFT, expand = TRUE, fill=X)
    
    #Middle Frame
    self.middleframe = Frame(self.tabs1)
    self.middleframe.pack(anchor = N,side=TOP,fill=X,expand=FALSE, pady = (0,20))
    #Job Board
    self.label4 = Label(self.middleframe, height = 1, width = 10, text = "Job Board:", font=("Latha", 10))
    self.textbox4 = Text(self.middleframe, height = 1, width = 15)
    self.Buttons1 = Button(self.middleframe, text = "Switch to List")
    self.label4.pack(side = LEFT, expand = FALSE, fill= NONE)
    self.textbox4.pack(side = LEFT, expand = TRUE, fill= X)
    self.Buttons1.pack(side = RIGHT, fill= NONE)

    #Mid-bottom Frame
    self.mbtmFrame = Frame(self.tabs1)
    self.mbtmFrame.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE,pady=(0,20))
    #Labels & Textboxes Description Box 
    self.label5 = Label(self.mbtmFrame, height = 1, width = 12, text = "Description: ", font=("Latha", 10))
    self.textbox5 = Text(self.mbtmFrame, height = 5, width = 20)
    self.label5.pack(anchor = N, side= LEFT, expand = FALSE, fill= NONE)
    self.textbox5.pack(fill= BOTH, expand=TRUE)
    
    #Bottom Frame
    self.bottomframe = Frame(self.tabs1)
    self.bottomframe.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE)
    #Others Display Box
    self.label5 = Label(self.bottomframe, height = 1, width = 12, text = "Others: ", font=("Latha", 10))
    self.textbox5 = Text(self.bottomframe, height = 5, width = 20)
    self.label5.pack(anchor = N,side = LEFT,  expand = FALSE, fill= NONE)
    self.textbox5.pack(fill= BOTH, expand=TRUE)

  def Tabs2(self):
    #Top Frame for Tab 2
    self.topframe = Frame(self.tabs2)
    self.topframe.pack(anchor = N,side=TOP,fill=X,expand=FALSE, pady = (0,20))
    #Button for Top Frame
    self.Button1 = Button(self.topframe, text = "Add New Record")
    self.Button1.pack(side = TOP, fill= X)
    #Labels & Textboxes For Company's Name
    self.label1 = Label(self.topframe, height = 1, width = 13, text = " Company's Name:", font=("Latha", 10),padx=5)
    self.textbox1 = Text(self.topframe, height = 1, width = 25)
    self.label1.pack(side = LEFT,expand = FALSE, fill= NONE)
    self.textbox1.pack(side = LEFT, expand = TRUE, fill=X)
    #Labels & Textboxes For Positions
    self.label2 = Label(self.topframe, height = 1, width = 10, text = "Position/Role:", font=("Latha", 10))
    self.textbox2 = Text(self.topframe, height = 1, width = 20)
    self.label2.pack(side= LEFT, expand = FALSE, fill=NONE)
    self.textbox2.pack(side= LEFT, expand = TRUE, fill=X)
    #Labels & Textboxes For Date Applied
    self.label3 = Label(self.topframe, height = 1, width = 10, text = "Date Applied:", font=("Latha", 10))
    self.textbox3 = Text(self.topframe, height = 1, width = 20)
    self.label3.pack(side = LEFT, expand = FALSE, fill=NONE) 
    self.textbox3.pack(side = LEFT, expand = TRUE, fill=X)

    #Middle Frame for Tab 2
    self.middleframe = Frame(self.tabs2)
    self.middleframe.pack(anchor = N,side=TOP,fill=X,expand=FALSE, pady = (0,20))
    #Labels & Textboxes Job Board
    self.label4 = Label(self.middleframe, height = 1, width = 10, text = "Job Board: ", font=("Latha", 10))
    self.textbox4 = Text(self.middleframe, height = 1, width = 15)
    self.label4.pack(side = LEFT, expand = FALSE, fill= NONE)
    self.textbox4.pack(side = LEFT, expand = TRUE, fill= X)
    
    #Mid-bottom Frame for Tab 2
    self.mbtmFrame = Frame(self.tabs2)
    self.mbtmFrame.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE,pady=(0,20))
    #Labels & Textboxes Description Box 
    self.label5 = Label(self.mbtmFrame, height = 1, width = 12, text = "Description: ", font=("Latha", 10))
    self.textbox5 = Text(self.mbtmFrame, height = 5, width = 20)
    self.label5.pack(anchor = N, side= LEFT, expand = FALSE, fill= NONE)
    self.textbox5.pack(fill= BOTH, expand=TRUE)
    
    #Bottom Frame for Tab 2
    self.bottomframe = Frame(self.tabs2)
    self.bottomframe.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE)
    #Labels & Textboxes Others Display Box 
    self.label6 = Label(self.bottomframe, height = 1, width = 12, text = "Others: ", font=("Latha", 10))
    self.textbox6 = Text(self.bottomframe, height = 5, width = 20)
    self.label6.pack(anchor = N,side = LEFT,  expand = FALSE, fill= NONE)
    self.textbox6.pack(fill= BOTH, expand=TRUE)

class menuBar(tk.Frame):
  def __init__(self, parent):
    self.parent = parent
    tk.Frame.__init__(self, self.parent)
    #Initiazliing menubar
    self.menubar = tk.Menu(self.parent)
    self.parent.config(menu = self.menubar)
    self.File_Menu()
    self.Edit_Menu()

  def File_Menu(self):
    #add menu item to the menu
    file_menu = tk.Menu(self.menubar,tearoff=FALSE) #initializing file_menu to the Menu on menubar
    file_menu.add_command(label ="File", command=NONE) #adding commands in the file_menu
    file_menu.add_command(label ="New File", command=NONE)
    file_menu.add_command(label ="Save", command=NONE)
    file_menu.add_command(label ="Save As", command=NONE)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=self.destroy)
    self.menubar.add_cascade(label ="File", menu=file_menu) #adding cascade from file_menu into menubar

  def Edit_Menu(self):
    #add menu iten to the menu
    edit_menu = tk.Menu(self.menubar, tearoff=FALSE) #initializing file_menu to the Menu on menubar
    edit_menu.add_command(label ="Undo", command=NONE) #adding commands in the file_menu
    edit_menu.add_command(label ="Cut", command=NONE)
    edit_menu.add_command(label ="Copy", command=NONE)
    edit_menu.add_command(label ="Paste", command=NONE)
    edit_menu.add_command(label="Delete", command=NONE)
    edit_menu.add_command(label="Select All", command=NONE)
    edit_menu.add_separator()
    self.menubar.add_cascade(label ="Edit", menu=edit_menu) #adding cascade from file_menu into menubar

class MainApplication(tk.Frame):
    #Initializing the start of the Window
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent)
        self.configure_Gui()
        self.Widgets()
        
    #Windows
    def configure_Gui(self):
        self.parent.title("Job Flow") #Window Name
        self.parent.iconphoto(True, tk.PhotoImage(file='./Images/Icon_Organizer.png')) #Window Icon set to True applies to all windows
        #self.parent.maxsize(900,720)
        self.parent.minsize(900,720)
        #self.config(bg = "#add8e6")

    def Widgets(self):
      self.MenuBar = menuBar(self.parent)
      self.TabControls = Tabs(self.parent)

#To return the result
if __name__ == "__main__":
    root = tk.Tk()
    #App = MainApplication(root)
    MainApplication(root).pack()
    root.mainloop() #Infinite Loop

