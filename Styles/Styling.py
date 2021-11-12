import tkinter as tk
from tkinter import ttk #Getting Tabs from this library

class TabStyle(tk.Frame):
  def __init__(self, parent):
    self.parent = parent
    tk.Frame.__init__(self, self.parent)
    self.style = ttk.Style(self) #initializing the Styling of the Tabs
  
  def Tab1Style(self):
    self.style.theme_create( "Tab1", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } }, 
            "TNotebook.Tab": { "configure": {"padding": [5, 1], "background": Mysky },
            "map": {"background": [("selected", Myyellow)], "expand": [("selected", [1, 1, 1, 0])] } } } )

    self.style.theme_use("dummy")
    self.style.configure('TNotebook.Tab', background="green3",width=15)
    self.style.map("TNotebook", background= [("selected", "green3")])