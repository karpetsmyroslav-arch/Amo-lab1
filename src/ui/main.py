import tkinter as tk
from ui.windows.linear_ui import LinearUI
from ui.windows.curved_ui import CurvedUI
from ui.windows.cycled_ui import CycledUI


def main():
    root = tk.Tk()
    linear_ui = LinearUI(root)
    tk.Button(root, text= "Open", command= lambda: linear_ui.mainloop()).grid()
    curved_ui = CurvedUI(root)
    tk.Button(root, text="Open", command=lambda: curved_ui.mainloop()).grid()
    root.mainloop()





if __name__ == '__main__':
    main()