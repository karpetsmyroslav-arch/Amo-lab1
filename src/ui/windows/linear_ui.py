import tkinter as tk
from tkinter import Frame

from ui.elements.enter_variable import EnterVariable



class LinearUI(tk.Toplevel):
    def __init__(self, master: tk.Tk ):
        super().__init__(master)


        self.title("Linear")
        self.master = master
        self.geometry("300x300")


        frame = tk.Frame(self)
        frame.grid()



        self.a = EnterVariable(frame, "Введіть значення а")
        self.a.grid(row=0, column=0)
        self.c = EnterVariable(frame, "Введіть значення c")
        self.c.grid(row=1, column=0)
        self.x = EnterVariable(frame, "Введіть значення x")
        self.x.grid(row=2, column=0)

        self.answer = tk.Label(frame,text="Відповідь")
        self.answer.grid(row=3, column=0, columnspan=2)


