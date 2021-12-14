from tkinter import *
import tkinter as tk
from tkinter import ttk #Getting Tabs from this library
from tkinter import messagebox
from tkinter.filedialog import askopenfile
from typing import List
from PIL import Image, ImageTk, ImageSequence
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
    # initializing Tab 1 & 2 & it's layout
    self.tabs1 = ttk.Frame(self.tabControl)
    self.tabs2 = ttk.Frame(self.tabControl)
    self.tabControl.add(self.tabs1, text ="Main Record")
    self.tabControl.add(self.tabs2, text ="Add New Record")
    self.tabControl.pack(expand=True, fill = 'both',padx = 10, pady = 10)
    #Tab 1 will always be the default Tab
    self.Tabs1() #Calling in the function of the First Tab layer top
    #DropDown Menu & it's fetching Data from the database
    #value_inside = tk.StringVar(self) #default values starting point
    #value_inside.set("Select Job")
    #self.Dropdown = OptionMenu(self.topframe, value_inside, *CompanyNameList) # the *variable means to align them in vertical, without it, it would be in vertical
    #self.Dropdown.pack(side = LEFT,anchor = N,expand = FALSE, fill=X)
  def Tabs1(self):
    self.destroy_all_windows()
    #MYSQL function for ComboBox
    Select_CompanyName_Sql = "select id, CompanyName from flowing"
    mycursor.execute(Select_CompanyName_Sql)
    CompanyNameList = []
    for i in mycursor.fetchall():
      CompanyNameList.append(str(i[0]) + ". " + str(i[1]))  
    #Function to pull records from MYSQL Database onto widget Entry
    def lookupJobs(event):
      option = CompanyName_cb.get()
      cid = option.split("-")[0]
      query = "select * from flowing where id = %s"
      mycursor.execute(query,(cid,))
      rows = mycursor.fetchall()
      for i in rows:
        idlist.set(i[0])
        companynamelist.set(i[1])
        rolelist.set(i[2])
        datelist.set(i[3])
        jobboardlist.set(i[4])
        Descriptionlist.set(i[5])
        otherlist.set(i[6]) 
    #Initalizing all textvariable as StringVar for MYSQL to read Data
    idlist = StringVar(); 
    companynamelist = StringVar();
    rolelist = StringVar();
    datelist = StringVar();
    jobboardlist = StringVar();
    Descriptionlist = StringVar();
    otherlist = StringVar();  
    #Top, Middle, Mid-Bottom, & Bottom Frame for Tab 1
    self.topframe = Frame(self.tabs1, bg = "#CBC3E3")
    self.middleframe = Frame(self.tabs1, bg = "#CBC3E3")
    self.mbtmFrame = Frame(self.tabs1, bg = "#CBC3E3")
    self.bottomframe = Frame(self.tabs1, bg = "#CBC3E3")
    self.topframe.pack(anchor = N,side=TOP,fill=X,expand=FALSE, pady = (0,20))  
    self.middleframe.pack(anchor = N,side=TOP,fill=X,expand=FALSE, pady = (0,20)) 
    self.mbtmFrame.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE,pady=(0,20))
    self.bottomframe.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE)  
    #Combo box DropDown to select Company's Name Only
    selected_Company_Name = tk.StringVar()
    CompanyName_cb = ttk.Combobox(self.topframe, textvariable = selected_Company_Name, state = 'readonly')
    CompanyName_cb['values'] = CompanyNameList
    CompanyName_cb.pack(side = LEFT,anchor = N,expand = FALSE, fill=X) 
    CompanyName_cb.bind("<<ComboboxSelected>>", lookupJobs)
    #All Labels 
    Idlabel = Label(self.topframe, height = 1, width = 5, text = " ID:", font=("Latha", 10), bg = "#CBC3E3")
    CompanyName_Label = Label(self.topframe, height = 1, width = 13, text = " Company's Name:", font=("Latha", 10),padx=5,bg = "#CBC3E3")
    Roles_Label = Label(self.topframe, height = 1, width = 10, text = "Position/Role:", font=("Latha", 10),bg = "#CBC3E3")
    Date_Applied_Label = Label(self.topframe, height = 1, width = 10, text = "Date Applied:", font=("Latha", 10),bg = "#CBC3E3")
    Job_Board_Label = Label(self.middleframe, height = 1, width = 10, text = "Job Board:", font=("Latha", 10),bg = "#CBC3E3")
    Description_Label = Label(self.mbtmFrame, height = 1, width = 12, text = "Description: ", font=("Latha", 10),bg = "#CBC3E3")
    Others_Label = Label(self.bottomframe, height = 1, width = 12, text = "Others: ", font=("Latha", 10),bg = "#CBC3E3")
    #All Entry box for each content
    id_Text = Entry(self.topframe, width = 5, textvariable=idlist)
    CompanyName_Text_Box = Entry(self.topframe, width = 25, textvariable=companynamelist)
    Roles_textbox = Entry(self.topframe, width = 20, textvariable=rolelist)
    Date_Applied_Text_Box = Entry(self.topframe, width = 20, textvariable=datelist)
    Job_Board_Text_Box = Entry(self.middleframe, width = 15, textvariable=jobboardlist)
    Description_Text_Box = Entry(self.mbtmFrame, width = 20, justify= LEFT, textvariable = Descriptionlist)
    Others_Text_Box = Entry(self.bottomframe, width = 20, textvariable = otherlist)
    #All Buttons
    Button2_Image = tk.PhotoImage(file ='./Images/Download.png')
    Buttons1 = Button(self.middleframe, text = "Switch to List", command = self.Switch_View)
    Buttons2 = Button(self.middleframe, text = "Download Resume", image = Button2_Image, command = None)
    #All Widgets Layout Management
    Idlabel.pack(side = LEFT, fill =X)
    id_Text.pack(side = LEFT, fill =X)
    CompanyName_Label.pack(side = LEFT,expand = FALSE, fill= NONE)
    CompanyName_Text_Box.pack(side = LEFT, expand = TRUE, fill=X)
    Roles_Label.pack(side= LEFT, expand = FALSE, fill=NONE)
    Roles_textbox.pack(side= LEFT, expand = TRUE, fill=X)
    Date_Applied_Label.pack(side = LEFT, expand = FALSE, fill=NONE) 
    Date_Applied_Text_Box.pack(side = LEFT, expand = TRUE, fill=X)
    Job_Board_Label.pack(side = LEFT, expand = FALSE, fill= NONE)
    Job_Board_Text_Box.pack(side = LEFT, expand = TRUE, fill= X)
    Buttons1.pack(side = RIGHT, fill= NONE)
    Buttons2.pack(side = RIGHT, fill= NONE)
    Description_Label.pack(anchor = N, side= LEFT, expand = FALSE, fill= NONE)
    Description_Text_Box.pack(fill= BOTH, expand=TRUE)
    Others_Label.pack(anchor = N,side = LEFT,  expand = FALSE, fill= NONE)
    Others_Text_Box.pack(fill= BOTH, expand=TRUE)
  def Tabs2(self):
    self.topframe = Frame(self.tabs2, bg = "#CBC3E3")
    self.middleframe = Frame(self.tabs2, bg = "#CBC3E3")
    self.mbtmFrame = Frame(self.tabs2, bg = "#CBC3E3")
    self.bottomframe = Frame(self.tabs2, bg = "#CBC3E3")
    self.topframe.pack(anchor = N,side=TOP,fill=X,expand=FALSE, pady = (0,20)) 
    self.middleframe.pack(anchor = N,side=TOP,fill=X,expand=FALSE, pady = (0,20)) 
    self.mbtmFrame.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE,pady=(0,20))
    self.bottomframe.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE)
    #All Labels for each content
    self.Company_Name_Label = Label(self.topframe, bd = 5, underline = 0, height = 1, width = 13, text = "*Company's Name:", font=("Latha", 10),padx=5, bg = "#CBC3E3")
    self.Roles_Label = Label(self.topframe, underline = 0, height = 1, width = 10, text = "*Position/Role:", font=("Latha", 10), bg = "#CBC3E3")
    self.Date_Applied_Label = Label(self.topframe, underline = 0, height = 1, width = 10, text = "*Date Applied:", font=("Latha", 10), bg = "#CBC3E3")
    self.Job_Board_Label = Label(self.middleframe, height = 1, width = 10, text = "Job Board: ", font=("Latha", 10), bg = "#CBC3E3")
    self.Description_Label = Label(self.mbtmFrame, height = 1, width = 12, text = "Description: ", font=("Latha", 10), bg = "#CBC3E3")
    self.Others_Label = Label(self.bottomframe, height = 1, width = 12, text = "Others: ", font=("Latha", 10), bg = "#CBC3E3")
    #All Text/Entry Widgets for each content
    self.Company_Name_Text_Box = Entry(self.topframe, width = 20, bd = 3)
    self.Roles_Text_Box = Entry(self.topframe, width = 20, bd = 3)
    self.Date_Applied_Text_Box = Entry(self.topframe, width = 20, bd = 3)
    self.Job_Board_Text = Entry(self.middleframe, width = 15, bd = 3)
    self.Description_Text_Box = Entry(self.mbtmFrame, width = 20, bd = 3)
    self.Others_Text_Box = Entry(self.bottomframe, width = 20, bd = 3)
    #All Buttons
    self.Upload_Resume_Button = Button(self.middleframe, text="Upload Resume", command = self.Upload) #Upload Resume Button
    self.Button1 = Button(self.bottomframe, text = "Add New Record", command=self.Submit) #Add/Submit New Record
    #All widgets Layout Management
    self.Company_Name_Label.pack(side = LEFT,expand = FALSE, fill= NONE)
    self.Company_Name_Text_Box.pack(side = LEFT, expand = TRUE, fill=X)
    self.Roles_Label.pack(side= LEFT, expand = FALSE, fill=NONE)
    self.Roles_Text_Box.pack(side= LEFT, expand = TRUE, fill=X)
    self.Date_Applied_Label.pack(side = LEFT, expand = FALSE, fill=NONE) 
    self.Date_Applied_Text_Box.pack(side = LEFT, expand = TRUE, fill=X)
    self.Job_Board_Label.pack(side = LEFT, expand = FALSE, fill= NONE)
    self.Job_Board_Text.pack(side = LEFT, expand = TRUE, fill= X)
    self.Upload_Resume_Button.pack(side = RIGHT, fill= NONE)
    self.Description_Label.pack(anchor = N, side= LEFT, expand = FALSE, fill= NONE)
    self.Description_Text_Box.pack(fill= BOTH, expand=TRUE)
    self.Others_Label.pack(anchor = N,side = LEFT,  expand = FALSE, fill= NONE)
    self.Others_Text_Box.pack(fill= BOTH, expand=TRUE)
    self.Button1.pack(fill= X)
  def Submit(self):
    #Initiated all variables to recieve all text inputs
    CompanyName = self.Company_Name_Text_Box.get();
    Roles = self.Roles_Text_Box.get();
    DateApplied = self.Date_Applied_Text_Box.get();
    JobBoard = self.Job_Board_Text.get();
    Descriptions = self.Description_Text_Box.get();
    Others = self.Others_Text_Box.get();
    #If one or more box are missing before submitting
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
      self.Company_Name_Text_Box.delete(0, END)
      self.Roles_Text_Box.delete(0, END)
      self.Date_Applied_Text_Box.delete(0, END)
      self.Job_Board_Text.delete(0, END)
      self.Description_Text_Box.delete(0, END)
      self.Others_Text_Box.delete(0, END) 
      #Refresh Tab1 for updated values 
      self.after(1000, self.Tabs1)
  def Switch_View(self):
    self.destroy_all_windows()
    #Top Frame
    self.topframe = Frame(self.tabs1)
    self.topframe.pack(anchor = N,side=TOP,fill=BOTH,expand=TRUE, pady = (0,20))
    #Viewing in list box 
    self.list = Listbox(self.topframe, width = 40, height = 10, selectmode=MULTIPLE)
    self.list.pack(side = LEFT,anchor = N,expand = True, fill=BOTH)
    #button to switch back to default viewing
    Buttons1 = Button(self.topframe, text = "Switch to Default View", command = self.Tabs1)
    Buttons1.pack(anchor = N,side = RIGHT, fill= NONE)
    #Scroll bar vertical on Listbox
    sb = Scrollbar(self.topframe, orient=VERTICAL)
    sb.pack(side = RIGHT, fill = Y)
    self.list.configure(yscrollcommand=sb.set)
    sb.config(command = self.list.yview)
    #Database 
    Select_CompanyName_Sql = "select * from flowing"
    mycursor.execute(Select_CompanyName_Sql)
    Lists = mycursor.fetchall()
    All_values = []
    for i in Lists:
      self.list.insert(0, i)
  def destroy_all_windows(self):
    #Destroying previous View of Tabs
    self.tabs1.destroy()
    self.tabs2.destroy()
    #Recreating Tab 1 to List View
    self.tabs1 = ttk.Frame(self.tabControl)
    self.tabControl.add(self.tabs1, text ="Main Record")
    #Recreate Tab 2 to keep the pattern of Tab 1 and 2 in sequential order
    self.tabs2 = ttk.Frame(self.tabControl)
    self.tabControl.add(self.tabs2, text ="Add New Record")
    self.tabControl.pack(expand=True, fill = 'both', padx = 10, pady = 10)  
    self.Tabs2()
  def Upload(self):
    #Upload button command
    file = askopenfile(mode ='r', filetypes =[('All Files', '*.*')])
    data=(file)
    if file is not None:
      mycursor.execute("insert into flowing(Resume) values(%s,%s,%s)",data)
      content = file.read()
      print(content)
      mycursor.execute("commit")
      mydb.close()
    else:
      print("Cancelled")
  #def add_document(self):

  #def downloaded(self):
    #download button command
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