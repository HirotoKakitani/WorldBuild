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
        self.tree = None

        #menu frame
        self.menuFrame=Frame(self,highlightbackground="green", highlightthickness=1)
        #self.menuFrame.configure(background='white')
        
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
        #self.contentFrame.configure(background='white')
        
        self.title=Entry(self.contentFrame,disabledforeground="black",state=DISABLED)
        self.title.pack()
        self.textArea=Text(self.contentFrame,width=50,height=50)  
        self.scrollbar=Scrollbar(self.contentFrame, command=self.textArea.yview)

        self.textArea.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=LEFT, fill=Y)
        #self.scrollbar.config(command=self.textArea.yview)
        self.textArea.config(yscrollcommand=self.scrollbar.set)
        self.textArea.insert(END,"testing text widget\nhello thgis is a new line\nwaaaaaaah\nhello")
        self.textArea.config(state=DISABLED)
        
        #TODO image frame
        self.imageFrame=Frame(self, highlightbackground="green",highlightthickness=1)
        #self.imageFrame.configure(background='white')
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
        self.referenceFrame = Frame(self,highlightbackground="green", highlightthickness=1)
        self.referenceFrame.grid(row=1, column=2, sticky="nesw")
        self.innerText = Text(self.referenceFrame, width=25)#!! width has to be small to fit
        
        self.refScroll = Scrollbar(self.referenceFrame, command=self.innerText.yview)
        self.innerText.configure(yscrollcommand=self.refScroll.set)
        self.innerText.pack(side=LEFT, fill=BOTH, expand=True)

        self.refScroll.pack(side=LEFT, fill=Y)
        self.refScroll.config(command=self.innerText.yview)
        self.innerText.configure(state="disabled")       


        self.grid_columnconfigure(0,weight=1, uniform="row1")
        self.grid_columnconfigure(1,weight=4, uniform="row1")
        self.grid_columnconfigure(2,weight=1, uniform="row1")
        self.grid_rowconfigure(1,weight=1)
        
    #TODO show previous frame accessed. for now, just go back to select page of page type
    def returnPage(self):
        #disable edit functions
        self.saveButton['state']='disabled'
        self.linkButton['state']='disabled'
        self.textArea.config(state=DISABLED)
        self.title.config(state=DISABLED)
        self.controller.showFrame(INFO)
    
    #creates a reference button when an entry is selected from tree
    #TODO need to create button only when entry is clicked
    #TODO need to prevent outside clicking when Toplevel is present
    #TODO need to link button to refer to clicked entry
    def onTreeClick(self, event):
        #--------------------
        # removes text in the selected area
        print "selection test"
        print SEL_FIRST
        print SEL_LAST
        i = self.textArea.index(SEL_FIRST)
        j = self.textArea.index(SEL_LAST)
        print i, j
        #print self.textArea.delete(i,j)
        #creates a button in place of text
        buttonText = self.textArea.get(i,j)
        self.textArea.delete(i,j)
        testref = Button(self.textArea, text=buttonText)
        self.textArea.window_create(i, window=testref)
        #--------------------
        
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
        
    #shows tree of entries to select from
    def link(self):
        selected_text=None
        
        #prints warning if no text is selected when link is pressed
        try: 
            selected_text = self.textArea.selection_get()
        except:
            print "Please select text"
            warningWindow = Toplevel(self)
            warningLabel = Label(warningWindow,text="\nNo text selected!\n")
            warningLabel.pack()  

        #get all frames except select pages and start page and place under correct entry
        else:
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
