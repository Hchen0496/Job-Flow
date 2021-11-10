import tkinter as tk

#Initializing the start of the Main APP GUI
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent 
         

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title("JobSeeker Organizer") #Window Name
    root.iconphoto(False, tk.PhotoImage(file='O:\Python\Job Seeker Organization\Images\Icon_Organizer.png')) #Window Icon
    root.minsize(500,400) #Window Minimum Size
    root.mainloop() #Infinite Loop
