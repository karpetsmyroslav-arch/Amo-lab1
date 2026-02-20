import tkinter as tk
from tkinter import Frame

from ui.elements.enter_variable import EnterVariable



class CycledUI(tk.Toplevel):
    def __init__(self, master: tk.Tk ):
        super().__init__(master)


        self.title("Cycled")
        self.master = master



        frame = tk.Frame(self)
        frame.grid()



        self.a = EnterVariable(frame, "Введіть список значень а")
        self.a.grid(row=0, column=0)
        self.c = EnterVariable(frame, "Введіть список значень b")
        self.c.grid(row=1, column=0)

