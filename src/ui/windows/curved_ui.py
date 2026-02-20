import tkinter as tk
from tkinter import Frame
from ui.elements.enter_variable import EnterVariable


class CurvedUI(tk.Toplevel):
    def __init__(self, master: tk.Tk):
        super().__init__(master)


        self.title("Curved")
        self.master = master

        frame = tk.Frame(self)
        frame.grid()

        self.a = EnterVariable(frame, "Введіть значення а")
        self.a.grid(row=0, column=0)
        self.c = EnterVariable(frame, "Введіть значення c")
        self.c.grid(row=1, column=0)
        self.x = EnterVariable(frame, "Введіть значення k")
        self.x.grid(row=2, column=0)
        self.x = EnterVariable(frame, "Введіть значення p")
        self.x.grid(row=3, column=0)

