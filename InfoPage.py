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
        self.tree = None #TREE
        #menu frame
        self.menuFrame=Frame(self,highlightbackground="green", highlightthickness=1)
        self.menuFrame.grid(row=0,column=0, sticky="nw")
        self.backButton = Button(self.menuFrame, text="Back", command=self.returnPage)   
        self.backButton.pack(side=LEFT)
        
        self.editButton = Button(self.menuFrame, text="Edit", command=self.edit)   
        self.editButton.pack(side=LEFT)

        self.saveButton = Button(self.menuFrame, text="Save", command=self.save, state=DISABLED)   
        self.saveButton.pack(side=LEFT)
        
        self.linkButton = Button(self.menuFrame, text="Link", command=self.link, state=DISABLED)   
        self.linkButton.pack(side=LEFT)
        
        #content frame
        self.contentFrame=Frame(self,highlightbackground="green",highlightthickness=1)
        self.contentFrame.grid(row=1,column=1, sticky="nesw")
        
        self.title=Entry(self.contentFrame,disabledforeground="black",state=DISABLED)
        self.title.pack()
        self.textArea=Text(self.contentFrame)  
        self.scrollbar=Scrollbar(self.contentFrame)

        self.textArea.pack(side=LEFT, fill=Y)
        self.scrollbar.pack(side=LEFT, fill=Y)
        self.scrollbar.config(command=self.textArea.yview)
        self.textArea.config(yscrollcommand=self.scrollbar.set)
        self.textArea.insert(END,"testing text widget\nhello thgis is a new line\nwaaaaaaah\nhello")
        self.textArea.config(state=DISABLED)
        
        #TODO image frame
        self.imageFrame=Frame(self, highlightbackground="green",highlightthickness=1)
        self.imageFrame.grid(row=1,column=0,sticky="nesw")
        imageLabel = Label(self.imageFrame, text="image frame")
        imageLabel.pack()

        
        #TODO-=-= image insertion test
        #photo=PhotoImage(file='testimg.gif')
        #self.textP = Text(root, height=20,width=20)
        #self.textP.insert(END,'\n')
        #self.textP.image_create(END,image=photo)
        #self.textP.pack()
        
        #reference frame
        self.referenceFrame = Frame(self, width=200, height=500, highlightbackground="green", highlightthickness=1)
        self.referenceFrame.grid(row=1, column=3, sticky="nse")
        self.referenceFrame.pack_propagate(False)
        self.innerText = Text(self.referenceFrame,width=100, height=500)
        self.refScroll = Scrollbar(self.referenceFrame, command=self.innerText.yview)
        self.innerText.configure(yscrollcommand=self.refScroll.set)
        self.innerText.pack(side=LEFT)
        self.refScroll.pack(side=RIGHT, fill=Y)
        self.refScroll.config(command=self.innerText.yview)
        self.innerText.configure(state="disabled")       
        
        #self.grid_columnconfigure(4, weight=1)
        #self.refTestbutton = Button(self.referenceFrame, text="test")
        #self.refTestbutton.pack()
        
    #TODO show previous frame accessed. for now, just go back to select page of page type
    def returnPage(self):
        #disable edit functions
        self.saveButton['state']='disabled'
        self.linkButton['state']='disabled'
        self.textArea.config(state=DISABLED)
        self.title.config(state=DISABLED)
        self.controller.showFrame(INFO)
    
    def onTreeClick(self, event):
        item = self.tree.selection()[0]
        parentNode = self.tree.parent(item)
        if parentNode == "INFO":
            #creates link to another info page
            self.innerText.configure(state="normal")
            frameName = item + "_Info Page"
            newButton = Button(self.referenceFrame, text=item, command=lambda:self.controller.showFrame(frameName))
            self.innerText.window_create("end", window=newButton)
            self.innerText.configure(state="disabled")
        elif parentNode == "DIAG":
            #TODO link to diag page
            print "diag entry"
            
        elif parentNode == "MAP":
            #TODO link to map page
            print "map entry"
            
        else:
            print "not found"
        
    #when item is selected, create a new button in page that will redirect to that frame
    def link(self):
        #1. get all frames excepy select pages and start page
        #2. place under correct entry
        treeWindow = Toplevel(self)
        self.tree = ttk.Treeview(treeWindow)      
        self.tree.bind("<Double-1>", self.onTreeClick)

        
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
