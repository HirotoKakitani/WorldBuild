#import Tkinter as tk
from Tkinter import *

INFO = "Info Page"
class InfoPage(Frame):
    def __init__(self, parent,controller, prevSelect):
        Frame.__init__(self, parent)
        label = Label(self,text="Info Entry")
        label.pack(pady=10,padx=10)
        self.controller = controller
        self.prevSelect = prevSelect    #points to the selection page this entry came from
        self.nameHistory = []
 
        self.title = Entry(self)
        self.title.pack(pady=10, padx=10)
        self.backButton = Button(self, text="Back", command=lambda:controller.showFrame(INFO))
        self.backButton.pack(pady=10,padx=10) 
        
        self.saveButton = Button(self,text="Save", command=self.save)
        self.saveButton.pack(pady=10, padx=10)
        
        #TODO text area testing
        
        #TODO-=-= image insertion test
        photo=PhotoImage(file='testimg.gif')
        self.textP = Text(root, height=20,width=20)
        self.textP.insert(END,'\n')
        self.textP.image_create(END,image=photo)
        self.textP.pack()
        
        self.scrollbar = Scrollbar(self)
        self.textArea = Text(self,height=2)
        self.scrollbar.pack(side=RIGHT,fill=Y, padx=(0,10), pady=10)
        self.textArea.pack(side=LEFT,fill="both", padx=(10,0), pady=10)
        self.scrollbar.config(command=self.textArea.yview)
        self.textArea.config(yscrollcommand=self.scrollbar.set)
        self.textArea.insert(END,"testing text widget\nhello thgis is a new line\nwaaaaaaah\nhello")
        
        
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
