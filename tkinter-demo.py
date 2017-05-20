from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Tic Tac Toe")
        self.pack(fill=BOTH, expand=1)
        quit_button = Button(self, text="Quit", command=self.client_exit)
        quit_button.place(x=0, y=0)

    @staticmethod
    def client_exit():
        exit()


root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()
