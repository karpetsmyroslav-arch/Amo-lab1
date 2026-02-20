import tkinter as tk
from tkinter import Frame
from ui.elements.enter_variable import EnterVariable
from lab_one.formulas.multiple import calculate_curved_function

class CurvedUI(tk.Toplevel):
    def __init__(self, master: tk.Tk):
        super().__init__(master)


        self.title("Curved")
        self.master = master
        self.geometry("300x300")


        frame = tk.Frame(self)
        frame.grid()

        self.a = EnterVariable(frame, "Введіть значення а")
        self.a.grid(row=0, column=0)
        self.c = EnterVariable(frame, "Введіть значення c")
        self.c.grid(row=1, column=0)
        self.k = EnterVariable(frame, "Введіть значення k")
        self.k.grid(row=2, column=0)
        self.p = EnterVariable(frame, "Введіть значення p")
        self.p.grid(row=3, column=0)

        self.answer = tk.Label(frame, text="Відповідь")
        self.answer.grid(row=4, column=0, columnspan=2)

        tk.Button(frame, text="Розрахувати", command=lambda: self.calculation_process()).grid(row=5, column=0)


    def calculation_process(self):
        a = float(self.a.value)
        k = float(self.k.value)
        c = float(self.c.value)
        p = float(self.p.value)

        self.answer["text"] = f"Y1: {calculate_curved_function(a=a, c=c, p=p, k=k)}"