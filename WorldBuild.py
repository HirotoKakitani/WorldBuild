import Tkinter as tk
from MapPage import MapPage
from InfoPage import InfoPage
from DiagramPage import DiagramPage
START = "Start Page"
SELECT = "Select Page"
MAP = "Map Page"
INFO = "Info Page"
DIAG = "Diagram Page"

#inheriting from tkinter
class WorldBuild(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        tk.Tk.geometry(self,"500x500")  #TODO check resizing
        self.container.pack_propagate(0)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames={}   #dictionary of pages
 
        #initialize different page types
        for f,t in zip((StartPage, SelectPage, SelectPage, SelectPage),(START,MAP,INFO,DIAG)):
            frame = f(self.container, self) if f==StartPage else f(self.container, self, t)
            self.frames[t] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.showFrame(START)
   
    def showFrame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        print "showing:", cont

    #creates a new entry under correct page
    def createEntry(self, cont, pageType, pageNum):
        if pageType == MAP:
            print "Creating Map Entry"
            newFrame = MapPage(self.container,self)
            self.frames[pageNum] = newFrame
            newFrame.grid(row=0,column=0,sticky="nsew")
            cont.num += 1
            print self.frames
            cont.createButton()

        elif pageType == INFO:
            print "Creating Info Entry"
            newFrame = InfoPage(self.container,self,cont)
            #newFrame = InfoPage(cont,self)
            #self.frames[pageNum] = newFrame
            newFrame.grid(row=0,column=0,sticky="nsew")
            cont.num += 1
            #TODO experimental end
            print self.frames
            newFrame.tkraise()  #!! this prevents creating a frame until saved

        else:
            print "Creating Diagram Entry"
            newFrame = DiagramPage(self.container,self)
            self.frames[pageNum] = newFrame
            newFrame.grid(row=0,column=0,sticky="nsew")
            cont.num += 1
            print self.frames
            cont.createButton()


class StartPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start page")
        label.pack(pady=10,padx=10)
        
        #initialize buttons - lambda expressions used to differentiate button callbacks
        mapButton = tk.Button(self, text="Map",command=lambda:controller.showFrame(MAP))
        mapButton.pack(pady=10,padx=10)
        
        infoButton = tk.Button(self, text="Info",command=lambda:controller.showFrame(INFO))
        infoButton.pack(pady=10,padx=10)
        
        diagramButton = tk.Button(self, text="Diagram",command=lambda:controller.showFrame(DIAG))
        diagramButton.pack(pady=10,padx=10)
    

class SelectPage(tk.Frame):
    def __init__(self,parent,controller,pageType):
        self.pageType = pageType
        self.controller = controller
        self.elementList = [] 
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=pageType)
        label.pack(pady=10,padx=10) 
        #label.grid(row=0,column=1,sticky="nsew")
        backButton = tk.Button(self, text="Back", command=lambda:controller.showFrame(START))
        backButton.pack(pady=10,padx=10)
        #backButton.grid(row=1,column=0,sticky="nsew")
        
        self.num = 0
        newButton = tk.Button(self,text="New Entry",command=lambda:controller.createEntry(self,pageType,self.num))
        newButton.pack(pady=10,padx=10)
        
        #newButton.grid(row=1,column=1,sticky="nsew")
        
    #create a new button/element for the new entry        
    def createButton(self,pageTitle, newEntry, pageType):
        self.controller.frames[pageTitle] = newEntry 
        selButton = tk.Button(self, text=pageTitle, command=lambda:self.controller.showFrame(pageTitle))
        selButton.pack(pady=10,padx=10)
        self.elementList.append(selButton)
    
    def updateButton(self, oldName, newName):
        #TODO iterate through buttons to find the one with old name. then change the name
        for i in self.elementList:
            print i['text']
            if i['text'] == oldName:
                i['text']=newName
                
app = WorldBuild()
app.mainloop()
