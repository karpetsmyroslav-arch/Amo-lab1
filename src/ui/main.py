import tkinter as tk
from ui.windows.linear_ui import LinearUI
from ui.windows.curved_ui import CurvedUI
from ui.windows.cycled_ui import CycledUI


def main():
    root = tk.Tk()

    root.title("Основний модуль")
    root.geometry("300x300")

    tk.Button(root, text="Лінійний", command=lambda: LinearUI(root)).grid()
    tk.Button(root, text="Розгалужений", command=lambda: CurvedUI(root)).grid()
    tk.Button(root, text="Циклічний", command=lambda: CycledUI(root)).grid()

    root.mainloop()





if __name__ == '__main__':
    main()