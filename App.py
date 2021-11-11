import sys
sys.path.append("/Styles/Styling.py")
import tkinter as tk
from tkinter import ttk #Getting Tabs from this library
#from Styling import Tab1Style
#Tabstyler = Styling.Tab1Style()

class TabsControl(tk.Frame):
  def __init__(self, parent):
    self.parent = parent
    tk.Frame.__init__(self, self.parent)
    self.tabControl = ttk.Notebook(self.parent) #Initializing Tabs
    self.add_Tabs() #Calling in the Function of adding Tabs
    #self.Tabs1() #Calling in the function of the First Tab
    #self.Tabs2() #Calling in the function of the Second Tab
  
  def add_Tabs(self):
    #We initialize Tab 1 & 2
    self.tabs1 = ttk.Frame(self.tabControl)
    self.tabs2 = ttk.Frame(self.tabControl)
    #from the Parent of the Switching Tab, we add in Tab 1 & 2, and then we name each of them
    self.tabControl.add(self.tabs1, text ="Main Record")
    self.tabControl.add(self.tabs2, text ="Add New Record")
    #Made sure we pack the parent tab and add arguments of how we want it to appear on windows
    self.tabControl.pack(expand=True, fill = 'both', padx = 10, pady = 10)
    
  def Tabs1(self):
    self.TS = Tab1Style(self.parent)
    self.TS.pack()
    #self.parent.labelA = ttk.Label(self, text = "This is on Frame One")#self.parent.labelA.grid(column=1, row=1)
    #def Tabs2(self):
    #in-progress  
 
class MainApplication(tk.Frame):
    #Initializing the start of the Window
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent)
        self.configure_Gui()
        self.Widgets()
        
    #Windows
    def configure_Gui(self):
        self.parent.title("JobSeeker Organizer") #Window Name
        self.parent.iconphoto(True, tk.PhotoImage(file='./Images/Icon_Organizer.png')) #Window Icon set to True applies to all windows
        self.parent.minsize(500,400)
        #self.config(bg = "#add8e6")

    def Widgets(self):
      self.TabControls = TabsControl(self.parent)
      self.TabControls.pack()

#To return the result
if __name__ == "__main__":
    root = tk.Tk()
    #App = MainApplication(root)
    MainApplication(root).pack()
    root.mainloop() #Infinite Loop
