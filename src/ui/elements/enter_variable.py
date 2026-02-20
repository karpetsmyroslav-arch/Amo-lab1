import tkinter as tk
from tkinter import messagebox



class EnterVariable(tk.Frame):
    def __init__(self, master: tk.Frame, text: str):
        super().__init__(master)

        tk.Label(self, text=text).grid(row=0, column=0)
        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=1)

    @property
    def value(self):
        return self.entry.get()