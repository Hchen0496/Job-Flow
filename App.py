import tkinter as tk
from tkinter import ttk #Getting Tabs from this library

class TabsControl(tk.Frame):
   def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent)
        self.tabControl = ttk.Notebook(self)
        self.tabs1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tabs1, text ="Main Record")
        self.parent.labelA = ttk.Label(self, text = "This is on Frame One")
        self.parent.labelA.grid(column=1, row=1)

       
class MainApplication(tk.Frame):

    #Initializing the start of the Window
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self, self.parent)
        self.configure_Gui()
        self.TabControls = TabsControl(self)
        self.TabControls.pack(expand=1, fill = 'both')
        #self.Widgets()
        
    #Windows
    def configure_Gui(self):
        self.parent.title("JobSeeker Organizer") #Window Name
        self.parent.iconphoto(True, tk.PhotoImage(file='O:\Python\Job Seeker Organization\Images\Icon_Organizer.png')) #Window Icon set to True applies to all windows
        self.parent.minsize(500,400)
        #self.parent.bg("ADD8E6")

    #def Widgets(self):

        
#To return the result
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop() #Infinite Loop
