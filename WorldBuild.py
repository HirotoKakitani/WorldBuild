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
        for f in (StartPage, MapPage, InfoPage, DiagramPage):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.showFrame(StartPage)
    
    #gets appropriate frame from dictionary
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start page")
        label.pack(pady=10,padx=10)
        
        #initialize buttons - lambda expressions used to differentiate button callbacks
        mapButton = tk.Button(self, text="Map",command=lambda:controller.showFrame(MapPage))
        mapButton.pack(pady=10,padx=10)
        
        infoButton = tk.Button(self, text="Info",command=lambda:controller.showFrame(InfoPage))
        infoButton.pack(pady=10,padx=10)
        
        diagramButton = tk.Button(self, text="Diagram",command=lambda:controller.showFrame(DiagramPage))
        diagramButton.pack(pady=10,padx=10)
       
class MapPage(tk.Frame): 
    def __init__(self, parent,controller): 
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Map Page")
        label.pack(pady=10,padx=10)
        self.mapFrame = {}   #dict for all pages within map frames

        testButton = tk.Button(self, text="testt")
        testButton.pack(pady=10,padx=10)

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
