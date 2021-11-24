from tkinter import *
from tkinter import ttk #Getting Tabs from this library
import tkinter as tk
from tkinter import messagebox
from typing import List
import mysql.connector

#Connected to an existing database
mydb = mysql.connector.connect(host="127.0.0.1", user="root", password="Redisforme24!", database="flow");
mycursor = mydb.cursor()

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
    #DropDown Menu & it's fetching Data from the database
    Select_CompanyName_Sql = "select CompanyName from flowing"
    mycursor.execute(Select_CompanyName_Sql)
    CompanyNameList = []
    Lists = mycursor.fetchall()
    for i in Lists:
        CompanyNameList.append(i)
      #default values starting point    
    value_inside = tk.StringVar(self) 
    value_inside.set("Select Job")
    self.Dropdown = OptionMenu(self.topframe, value_inside, *CompanyNameList) # the *variable means to align them in vertical, without it, it would be in vertical
    self.Dropdown.pack(side = LEFT,anchor = N,expand = FALSE, fill=X)
    #ID For each Record
    Select_ID_Sql = "select id from flowing"
    selected = self.Dropdown.get()
    Id = mycursor.fetchall()
    for i in Lists:
      if (selected == i):
        mycursor.execute(Select_ID_Sql)
        Id


    self.Idlabel = Label(self.topframe, height = 1, width = 5, text = " ID:", font=("Latha", 10),padx=5)
    self.idText = Text(self.topframe, self.Id, height = 1, width = 5)
    self.Idlabel.pack(side = LEFT, fill =X)
    self.idText.pack(side = LEFT, fill =X)
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
    self.Buttons2 = Button(self.middleframe, text = "Download Uploaded Resume")
    self.label4.pack(side = LEFT, expand = FALSE, fill= NONE)
    self.textbox4.pack(side = LEFT, expand = TRUE, fill= X)
    self.Buttons1.pack(side = RIGHT, fill= NONE)
    self.Buttons2.pack(side = RIGHT, fill= NONE)

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
    #Labels & Textboxes For Company's Name
    self.label1 = Label(self.topframe, height = 1, width = 13, text = " Company's Name:", font=("Latha", 10),padx=5)
    self.textbox1 = Entry(self.topframe, width = 25)
    self.label1.pack(side = LEFT,expand = FALSE, fill= NONE)
    self.textbox1.pack(side = LEFT, expand = TRUE, fill=X)
    #Labels & Textboxes For Positions
    self.label2 = Label(self.topframe, height = 1, width = 10, text = "Position/Role:", font=("Latha", 10))
    self.textbox2 = Entry(self.topframe, width = 20)
    self.label2.pack(side= LEFT, expand = FALSE, fill=NONE)
    self.textbox2.pack(side= LEFT, expand = TRUE, fill=X)
    #Labels & Textboxes For Date Applied
    self.label3 = Label(self.topframe, height = 1, width = 10, text = "Date Applied:", font=("Latha", 10))
    self.textbox3 = Entry(self.topframe, width = 20)
    self.label3.pack(side = LEFT, expand = FALSE, fill=NONE) 
    self.textbox3.pack(side = LEFT, expand = TRUE, fill=X)

    #Middle Frame for Tab 2
    self.middleframe = Frame(self.tabs2)
    self.middleframe.pack(anchor = N,side=TOP,fill=X,expand=FALSE, pady = (0,20))
    #Labels & Textboxes Job Board
    self.label4 = Label(self.middleframe, height = 1, width = 10, text = "Job Board: ", font=("Latha", 10))
    self.textbox4 = Entry(self.middleframe, width = 15)
    self.Button1 = Button(self.middleframe, text="Upload Resume") #Submit Resume Button
    self.label4.pack(side = LEFT, expand = FALSE, fill= NONE)
    self.textbox4.pack(side = LEFT, expand = TRUE, fill= X)
    self.Button1.pack(side = RIGHT, fill= NONE)
    
    #Mid-bottom Frame for Tab 2
    self.mbtmFrame = Frame(self.tabs2)
    self.mbtmFrame.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE,pady=(0,20))
    #Labels & Textboxes Description Box 
    self.label5 = Label(self.mbtmFrame, height = 1, width = 12, text = "Description: ", font=("Latha", 10))
    self.textbox5 = Entry(self.mbtmFrame, width = 20)
    self.label5.pack(anchor = N, side= LEFT, expand = FALSE, fill= NONE)
    self.textbox5.pack(fill= BOTH, expand=TRUE)
    
    #Bottom Frame for Tab 2
    self.bottomframe = Frame(self.tabs2)
    self.bottomframe.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE)
    #Labels & Textboxes Others Display Box 
    self.label6 = Label(self.bottomframe, height = 1, width = 12, text = "Others: ", font=("Latha", 10))
    self.textbox6 = Entry(self.bottomframe, width = 20,)
    self.label6.pack(anchor = N,side = LEFT,  expand = FALSE, fill= NONE)
    self.textbox6.pack(fill= BOTH, expand=TRUE)
    #Submit Button
    self.Button1 = Button(self.bottomframe, text = "Add New Record", command=self.Submit)
    self.Button1.pack(fill= X)
  
  def Submit(self):
    #Initiated all variables to recieve all text inputs
    CompanyName = self.textbox1.get();
    Roles = self.textbox2.get();
    DateApplied = self.textbox3.get();
    JobBoard = self.textbox4.get();
    Descriptions = self.textbox5.get();
    Others = self.textbox6.get();
    if (CompanyName =="" or Roles =="" or DateApplied == "" ):
      messagebox.showinfo("status","Field Required are missing")
    else:
      #insert all of our text values onto the database
      mycursor.execute("insert into flowing(CompanyName,Roles,DateApplied,JobBoard,Descriptions,Others) values('"+CompanyName+"','"+Roles+"','"+DateApplied+"','"+JobBoard+"','"+Descriptions+"','"+Others+"')")
      messagebox.showinfo("Status","Added Job Info")
      #commit & close the database
      mycursor.execute("commit")
      mydb.close()
      #clear textboxes after submission
      self.textbox1.delete(0, END)
      self.textbox2.delete(0, END)
      self.textbox3.delete(0, END)
      self.textbox4.delete(0, END)
      self.textbox5.delete(0, END)
      self.textbox6.delete(0, END)
    

  def Update(self):
    #Database purposes
    CompanyName = self.textbox1.get();
    Roles = self.textbox2.get();
    DateApplied = self.textbox3.get();
    JobBoard = self.textbox4.get();
    Descriptions = self.textbox5.get();
    Others = self.textbox6.get();

    mycursor.execute("update flowing set CompanyName='" + CompanyName +"', Roles='"+Roles+"', DateApplied = '"+DateApplied+"',JobBoard = '"+JobBoard+"', Descriptions = '"+Descriptions+"', Others = '"+Others+"'")
    mycursor.execute("commit")
    mydb.close()
  def DisplayRecord(self):
    ids = "select id from flowing"
    sql_select_query = "select CompanyName from flowing "
    if (id == ids):
      print ()
  def SelectOptions(choice):
    query = "select CompanyName from flowing"
    choice = query.get()
      
class menuBar(tk.Frame):
  def __init__(self, parent):
    self.parent = parent
    tk.Frame.__init__(self, self.parent)
    #Initiazliing menubar
    self.menubar = tk.Menu(self.parent)
    self.parent.config(menu = self.menubar)
    self.File_Menu()
    self.Edit_Menu()
    self.Help_Menu()

  def File_Menu(self):
    #add menu item to the menu
    file_menu = tk.Menu(self.menubar,tearoff=FALSE) #initializing file_menu to the Menu on menubar, tearoff is to get rid of the dashed line on top of the File & etc.. Menu Option
    file_menu.add_command(label ="File", command=NONE) #adding commands in the file_menu
    file_menu.add_command(label ="New File", command=NONE)
    file_menu.add_command(label ="Save", command=NONE)
    file_menu.add_command(label ="Save As", command=NONE)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=self.destroy)
    self.menubar.add_cascade(label ="File", menu=file_menu) #adding cascade from file_menu into menubar

  def Edit_Menu(self):
    #add Edit
    edit_menu = tk.Menu(self.menubar, tearoff=FALSE) 
    edit_menu.add_command(label ="Undo", command=NONE) 
    edit_menu.add_command(label ="Cut", command=NONE)
    edit_menu.add_command(label ="Copy", command=NONE)
    edit_menu.add_command(label ="Paste", command=NONE)
    edit_menu.add_command(label="Delete", command=NONE)
    edit_menu.add_command(label="Select All", command=NONE)
    edit_menu.add_separator()
    self.menubar.add_cascade(label ="Edit", menu=edit_menu) 

  def Help_Menu(self):
    #add Help menu
    help_menu = tk.Menu(self.menubar, tearoff=FALSE) 
    help_menu.add_command(label ="About", command=NONE) 
    help_menu.add_command(label ="Help")
    self.menubar.add_cascade(label ="Help", menu=help_menu) 
class Switch_View_List(tk.Frame):
  def __init__(self, parent):
    self.parent = parent
    tk.Frame.__init__(self, self.parent)


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

