#import Tkinter as tk
from Tkinter import *
MAP = "Map Page"
class MapPage(Frame): 
    def __init__(self, parent,controller): 
        Frame.__init__(self, parent)
        label = Label(self,text="Map Entry")
        label.pack(pady=10,padx=10)
        
        backButton = Button(self, text="Back", command=lambda:controller.showFrame(MAP))
        backButton.pack(pady=10,padx=10)
        
        saveButton = Button(self,text="Save")
        saveButton.pack(pady=10, padx=10)


