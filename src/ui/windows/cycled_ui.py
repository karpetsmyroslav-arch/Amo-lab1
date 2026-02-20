import tkinter as tk
from ui.elements.enter_variable import EnterVariable
from lab_one.formulas.cycle import calculate_cyclic



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

        self.answer = tk.Label(frame, text="Відповідь")
        self.answer.grid(row=3, column=0, columnspan=2)

        tk.Button(frame, text="Розрахувати", command=lambda: self.calculation_process()).grid(row=4, column=0)

    def calculation_process(self):
        a = list(map(float, self.a.value.split(", ")))
        c = list(map(float, self.c.value.split(", ")))

        self.answer["text"] = f"Y1: {calculate_cyclic(a=a, b=c)}"

