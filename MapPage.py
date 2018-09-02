import Tkinter as tk

MAP = "Map Page"
class MapPage(tk.Frame): 
    def __init__(self, parent,controller): 
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Map Entry")
        label.pack(pady=10,padx=10)
        
        backButton = tk.Button(self, text="Back", command=lambda:controller.showFrame(MAP))
        backButton.pack(pady=10,padx=10)
        
        saveButton = tk.Button(self,text="Save")
        saveButton.pack(pady=10, padx=10)


