import tkinter as tk
    
class MainApplication(tk.Frame):

    #Initializing the start of the Main APP GUI
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.configure_Gui()
        #self.Widgets()

    #Windows Basic GUI
    def configure_Gui(self):
        self.master.title("JobSeeker Organizer") #Window Name
        self.master.iconphoto(True, tk.PhotoImage(file='O:\Python\Job Seeker Organization\Images\Icon_Organizer.png')) #Window Icon set to True applies to all windows
        self.master.minsize(500,400)
        self.master.config(bg="red")

    #def Widgets(self):

if __name__ == "__main__":
    root = tk.Tk()
    #App = MainApplication(root)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop() #Infinite Loop
