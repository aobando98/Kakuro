import Tkinter as tk
from Tkinter import StringVar, Tk, Spinbox, Button, Frame,Label
from functools import partial



class BattleScreen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        for row in range(10):
           for col in range(10):
                butt1 = Button(self, bg='blue', width=1)
                butt1.grid(row=row, column=col)

'''
class Controls(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        
        self.quit = Button(self, text="Quit", width=6, 
                           command=root.destroy)
        self.quit.pack()
    
'''

root = Tk()
screen = BattleScreen(root)
#controls = Controls(root)
#controls.pack(side="bottom", fill="x")
screen.pack(side="top", fill="both", expand=True)
root.mainloop()