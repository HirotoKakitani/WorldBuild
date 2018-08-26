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
		
		self.frames={}	#dict. of all frames of application
		
		frame = StartPage(container, self)
		
		self.frames[StartPage] = frame
		
		frame.grid(row=0, column=0, sticky="nsew")
		
		self.show_frame(StartPage)
	
	#gets appropriate frame from dictionary
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
	
	
class StartPage(tk.Frame):
	def __init__(self, parent,controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="test page")
		label.pack(pady=10,padx=10)
		
app = WorldBuild()
app.mainloop()