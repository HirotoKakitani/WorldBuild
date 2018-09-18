#import Tkinter as tk
from Tkinter import *
import ttk

INFO = "Info Page"
class InfoPage(Frame):
    def __init__(self, parent,controller, prevSelect):
        Frame.__init__(self, parent)
        self.controller = controller
        self.prevSelect = prevSelect    #points to the selection page this entry came from
        self.nameHistory = []
        self.referenceList = []
        
        #TODO menu frame
        self.menuFrame=Frame(parent,highlightbackground="green", highlightthickness=1)
        self.menuFrame.grid(row=0,column=1)
        
        #TODO content frame
        self.contentFrame=Frame(parent,highlightbackground="green",highlightthickness=1)
        self.contentFrame.grid(row=1,column=1)

        
        self.backButton = Button(self.menuFrame, text="Back", command=self.returnPage)   
        self.backButton.pack(side="top", fill="both", expand=True)
        #self.backButton = Button(self, text="Back", command=self.returnPage)
        #self.backButton.grid(row=0,column=0, sticky="nw")
        
        self.editButton = Button(self.menuFrame, text="Edit", command=self.edit)   
        self.editButton.pack()
        #self.editButton = Button(self, text="Edit", command=self.edit)
        #self.editButton.grid(row=0,column=1, sticky="nw")

        self.saveButton = Button(self.menuFrame, text="Save", command=self.save, state=DISABLED)   
        self.saveButton.pack()
        #self.saveButton = Button(self,text="Save", command=self.save, state=DISABLED)
        #self.saveButton.grid(row=0,column=2, sticky="nw")
        
        self.linkButton = Button(self.menuFrame, text="Link", command=self.link, state=DISABLED)   
        self.linkButton.pack()
        #self.linkButton = Button(self, text="Link", command=self.link, state=DISABLED)
        #self.linkButton.grid(row=0,column=3, sticky="nw")

        #TODO-=-= image insertion test
        #photo=PhotoImage(file='testimg.gif')
        #self.textP = Text(root, height=20,width=20)
        #self.textP.insert(END,'\n')
        #self.textP.image_create(END,image=photo)
        #self.textP.pack()
        
        self.title=Entry(self.contentFrame,disabledforeground="black",state=DISABLED)
        self.title.pack()
        #self.title = Entry(self, disabledforeground="black",state=DISABLED)
        #self.title.grid(row=1,column=4, columnspan=1)
        self.textArea=Text(self.contentFrame)  
        self.scrollbar=Scrollbar(self.contentFrame)

        self.textArea.pack()
        self.scrollbar.pack()
        #self.scrollbar = Scrollbar(self)
        #self.textArea = Text(self)
        #self.textArea.grid(row=3,rowspan=1, column=4,columnspan=1, sticky="ns") 
        #self.scrollbar.grid(row=3, column=4, sticky="nse")
        self.scrollbar.config(command=self.textArea.yview)
        self.textArea.config(yscrollcommand=self.scrollbar.set)
        self.textArea.insert(END,"testing text widget\nhello thgis is a new line\nwaaaaaaah\nhello")
        self.textArea.config(state=DISABLED)
        
        #self.grid_columnconfigure(4, weight=1)
        
        self.tree = ttk.Treeview(self)      
        self.tree.bind("<Double-1>", self.onTreeClick)
        
        #TODO testing embedded frame
        self.referenceFrame = Frame(parent, width=200, height=600, highlightbackground="green", highlightthickness=1)
        self.referenceFrame.grid(row=1, column=0)
        self.refTestbutton = Button(self.referenceFrame, text="test")
        #self.refTestbutton.grid(row=0,column=0)
    #TODO show previous frame accessed. for now, just go back to select page of page type
    def returnPage(self):
        #disable edit functions
        self.saveButton['state']='disabled'
        self.linkButton['state']='disabled'
        self.textArea.config(state=DISABLED)
        self.title.config(state=DISABLED)
        self.tree.grid_remove()
        self.controller.showFrame(INFO)
    
    def onTreeClick(self, event):
        item = self.tree.selection()[0]
        parent = self.tree.parent(item)
        
        print item, " with parent ", self.tree.parent(item)
        print "you clicked on", self.tree.item(item,"text")
        
    #TODO when item is selected, create a new button in page that will redirect to that frame
    def link(self):
        #1. get all frames excepy select pages and start page
        #2. place under correct entry
        self.tree.insert("","end", iid="DIAG", text="Diagrams")
        self.tree.insert("","end", iid="MAP", text= "Maps")
        self.tree.insert("","end", iid="INFO", text= "Info")
        
        for i in self.controller.frames:
            print i
            if "_Info Page" in i:
                treeText = i.replace("_Info Page", "")
                self.tree.insert("INFO","end", iid=treeText, text= treeText)
            elif "_Map Page" in i:
                treeText = i.replace("_Map Page", "")
                self.tree.insert("MAP","end", iid=treeText, text= treeText)
            elif "_Diagram Page" in i:
                treeText = i.replace("_Diagram Page", "")
                self.tree.insert("DIAG","end", iid=treeText, text= treeText)          
            else:
                print i + " not found!"
            
        self.tree.grid(row=2,rowspan=3,column=0,columnspan=4)
        
    #activates text entry areas
    def edit(self):
        self.saveButton['state']='normal'
        self.linkButton['state']='normal'
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
