from tkinter import *


class Window(Frame):
    """docstring for Window"""

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master


root = Tk()
app = Window(root)
root.mainloop()
