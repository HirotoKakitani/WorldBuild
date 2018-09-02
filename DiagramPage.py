import Tkinter as tk

DIAG = "Diagram Page"
class DiagramPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Diagram Entry")
        label.pack(pady=10,padx=10)
        self.diagramFrame={}    #dict for all pages within diagram frames
        
        backButton = tk.Button(self, text="Back", command=lambda:controller.showFrame(DIAG))
        backButton.pack(pady=10,padx=10)


