import Tkinter as tk

INFO = "Info Page"
class InfoPage(tk.Frame):
    def __init__(self, parent,controller, prevSelect):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Info Entry")
        label.pack(pady=10,padx=10)
        self.controller = controller
        self.prevSelect = prevSelect    #points to the selection page this entry came from
        self.nameHistory = []
 
        self.title = tk.Entry(self)
        self.title.pack(pady=10, padx=10)
        self.backButton = tk.Button(self, text="Back", command=lambda:controller.showFrame(INFO))
        self.backButton.pack(pady=10,padx=10) 
        
        self.saveButton = tk.Button(self,text="Save", command=self.save)
        self.saveButton.pack(pady=10, padx=10)
        
    def save(self):
        newTitle = self.title.get()
        if newTitle in self.nameHistory:
            print "Name has not changed"

        elif len(self.nameHistory) == 0:
            print "First time saving"
            self.nameHistory.append(newTitle)
            self.prevSelect.createButton(newTitle, self, INFO)
          
        else:
            print "updating existing button: ", self.nameHistory[-1]
            self.prevSelect.updateButton(self.nameHistory[-1], newTitle)
            self.nameHistory.append(newTitle)
