#import Tkinter as tk
from Tkinter import *

DIAG = "Diagram Page"
class DiagramPage(Frame):
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        label = Label(self,text="Diagram Entry")
        label.pack(pady=10,padx=10)
        self.diagramFrame={}    #dict for all pages within diagram frames
        
        backButton = Button(self, text="Back", command=lambda:controller.showFrame(DIAG))
        backButton.pack(pady=10,padx=10)


