#import Tkinter as tk
from Tkinter import *

INFO = "Info Page"
class InfoPage(Frame):
    def __init__(self, parent,controller, prevSelect):
        Frame.__init__(self, parent)
        self.controller = controller
        self.prevSelect = prevSelect    #points to the selection page this entry came from
        self.nameHistory = []
 
        self.title = Entry(self, disabledforeground="black")
        self.title.grid(row=1,column=1, columnspan=1,sticky="nesw")
        self.title.config(state=DISABLED)
        self.backButton = Button(self, text="Back", command=lambda:controller.showFrame(INFO))
        self.backButton.grid(row=0,column=0, sticky="nesw")
        
        self.editButton = Button(self, text="Edit", command=self.edit)
        self.editButton.grid(row=0,column=1, sticky="nesw")

        self.saveButton = Button(self,text="Save", command=self.save)
        
        self.linkButton = Button(self, text="Link", command=self.link)
        #TODO text area testing
        
        #TODO-=-= image insertion test
        #photo=PhotoImage(file='testimg.gif')
        #self.textP = Text(root, height=20,width=20)
        #self.textP.insert(END,'\n')
        #self.textP.image_create(END,image=photo)
        #self.textP.pack()
        
        self.scrollbar = Scrollbar(self)
        self.textArea = Text(self,width=5)
        #self.textArea = Text(self)
        
        self.textArea.grid(row=3,rowspan=1, column=1,columnspan=2, sticky="nesw") 
        self.scrollbar.grid(row=3, column=2, sticky="nesw")
        self.scrollbar.config(command=self.textArea.yview)
        self.textArea.config(yscrollcommand=self.scrollbar.set)
        self.textArea.insert(END,"testing text widget\nhello thgis is a new line\nwaaaaaaah\nhello")
        self.textArea.config(state=DISABLED)
       
    def link(self):
        contents = self.textArea.selection_get()
        print contents
        #TODO show new window with all entries 
        
    #activates text entry areas
    def edit(self):
        
        self.saveButton.grid(row=0,column=2, sticky="nesw")
        self.linkButton.grid(row=0,column=3, sticky="nesw")
        #self.saveButton.pack(pady=10, padx=10)
        #self.linkButton.pack(pady=10, padx=10)
        self.textArea.config(state=NORMAL)
        self.title.config(state=NORMAL)

    def save(self):
        self.textArea.config(state=DISABLED)
        self.title.config(state=DISABLED)
        newTitle = self.title.get()

        if newTitle in self.nameHistory or not newTitle:
            print "Name has not changed"

        elif len(self.nameHistory) == 0:
            print "First time saving"
            self.nameHistory.append(newTitle)
            self.prevSelect.createButton(newTitle, self, INFO)
          
        else:
            print "updating existing button: ", self.nameHistory[-1]
            self.prevSelect.updateButton(self.nameHistory[-1], newTitle)
            self.nameHistory.append(newTitle)
