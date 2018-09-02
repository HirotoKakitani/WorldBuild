import Tkinter as tk

INFO = "Info Page"
class InfoPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Info Entry")
        label.pack(pady=10,padx=10)
        self.infoFrame={}   #dict for all pages within info frames
        
        backButton = tk.Button(self, text="Back", command=lambda:controller.showFrame(INFO))
        backButton.pack(pady=10,padx=10)


