import Tkinter as tk

START = "Start Page"
SELECT = "Select Page"
MAP = "Map Page"
INFO = "Info Page"
DIAG = "Diagram Page"

#inheriting from tkinter
class WorldBuild(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}   #dictionary of pages
    
        #initialize different page types
        for f,t in zip((StartPage, SelectPage, SelectPage, SelectPage),(START,MAP,INFO,DIAG)):
            frame = f(container, self) if f==StartPage else f(container, self, t)
            self.frames[t] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.showFrame(START)
    
    #gets appropriate frame from dictionary
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    #creates a new page
    def createEntry(self, cont, pageType, pageNum):
        if pageType == MAP:
            newFrame = MapPage(tk.Frame(self),self)
            cont.typeFrames[pageNum] = newFrame
            newFrame.grid(row=0,column=0,sticky="nsew") #TODO this might be causing not raising entries
            cont.num += 1
            print cont.typeFrames
            cont.updateButtons()
        elif pageType == INFO:
            #TODO copy above 
            pass
        else:
            #TODO copy above
            pass
        return 

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
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=pageType)
        label.pack(pady=10,padx=10)
        self.typeFrames = {}
        backButton = tk.Button(self, text="Back", command=lambda:controller.showFrame(START))
        backButton.pack(pady=10,padx=10)
        
        self.num = 0
        newButton = tk.Button(self,text="New Entry",command=lambda:controller.createEntry(self,pageType,self.num))
        newButton.pack(pady=10,padx=10)

    #create a new button/element for the new entry        
    def updateButtons(self):
        selButton = tk.Button(self, text=self.num-1, command=lambda:self.showEntry(self.num-1))
        selButton.pack(pady=10,padx=10)

    #TODO issue: not raising entries
    def showEntry(self, cont):
        frame = self.typeFrames[cont]
        frame.tkraise()
        
class MapPage(tk.Frame): 
    def __init__(self, parent,controller): 
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Map Entry")
        label.pack(pady=10,padx=10)
        self.mapFrame = {}   #dict for all pages within map frames
        
        backButton = tk.Button(self, text="Back", command=lambda:controller.showFrame(START))
        backButton.pack(pady=10,padx=10)

class InfoPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Info Entry")
        label.pack(pady=10,padx=10)
        self.infoFrame={}   #dict for all pages within info frames
        
        backButton = tk.Button(self, text="Back", command=lambda:controller.showFrame(START))
        backButton.pack(pady=10,padx=10)


class DiagramPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Diagram Entry")
        label.pack(pady=10,padx=10)
        self.diagramFrame={}    #dict for all pages within diagram frames
        
        backButton = tk.Button(self, text="Back", command=lambda:controller.showFrame(START))
        backButton.pack(pady=10,padx=10)

app = WorldBuild()
app.mainloop()
