import tkinter as tk
from tkinter import ttk #Getting Tabs from this library

class TabStyle(tk.Frame):
  def __init__(self, parent):
    self.parent = parent
    tk.Frame.__init__(self, self.parent)
    self.style = ttk.Style(self) #initializing the Styling of the Tabs
  
  def Tab1Style(self):
    self.theme_use('default')
    self.configure('TNotebook.Tab', background="green3",width=15)
    self.map("TNotebook", background= [("selected", "green3")])