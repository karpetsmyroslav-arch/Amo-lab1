import tkinter as tk
from ui.windows.linear_ui import LinearUI
from ui.windows.curved_ui import CurvedUI
from ui.windows.cycled_ui import CycledUI


def main():
    root = tk.Tk()
    tk.Button(root, text= "Open", command= lambda: LinearUI(root)).grid()
    tk.Button(root, text="Open", command=lambda: CurvedUI(root)).grid()
    tk.Button(root, text="Open", command=lambda: CycledUI(root)).grid()
    root.mainloop()





if __name__ == '__main__':
    main()