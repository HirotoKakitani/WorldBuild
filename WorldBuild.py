import Window as w
import Tkinter as tk

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
        startFrame = StartPage(container, self)
        mapFrame = MapPage(container, self)
        infoFrame = InfoPage(container,self)
        diagramFrame= DiagramPage(container, self)
        self.frames[StartPage] = startFrame
        self.frames[MapPage] = mapFrame
        self.frames[InfoPage] = infoFrame
        self.frames[DiagramPage] = diagramFrame
    
        startFrame.grid(row=0, column=0, sticky="nsew")
        
        self.showFrame(StartPage)
    
    #gets appropriate frame from dictionary
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent,controller):
        self.controller = controller    #TODO might not need this??
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start page")
        label.pack(pady=10,padx=10)
        
        #initialize buttons - lambda expressions used to differentiate button callbacks
        mapButton = tk.Button(self, text="Map",command=lambda:self.callback("map"))
        mapButton.pack(pady=10,padx=10)
        
        infoButton = tk.Button(self, text="Info",command=lambda:self.callback("info"))
        infoButton.pack(pady=10,padx=10)
        
        diagramButton = tk.Button(self, text="Diagram",command=lambda:self.callback("diagram"))
        diagramButton.pack(pady=10,padx=10)
       
    #goes to appropriate page based on which button is pressed 
    def callback(self, buttonType):
        if buttonType == "map":
            print self.controller.frames    #TODO look into  why showFrame is not working 
#            self.controller.showFrame(MapPage)
            print "Going to map page"
        elif buttonType == "info":
            print "Going to info page"
        else:
            print "Going to diagram page"

class MapPage(tk.Frame): 
    def __init__(self, parent,controller): 
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Map Page")
        label.pack(pady=10,padx=10)
        self.mapFrame = {}   #dict for all pages within map frames

class InfoPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Info Page")
        label.pack(pady=10,padx=10)
        self.infoFrame={}   #dict for all pages within info frames

class DiagramPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Diagram Page")
        label.pack(pady=10,padx=10)
        self.diagramFrame={}    #dict for all pages within diagram frames
        
app = WorldBuild()
app.mainloop()
