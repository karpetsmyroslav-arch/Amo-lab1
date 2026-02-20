import tkinter as tk
from ui.windows.linear_ui import LinearUI


def main():
    root = tk.Tk()
    linear_ui = LinearUI(root)
    tk.Button(root, text= "Open", command= lambda: linear_ui.mainloop()).grid()
    root.mainloop()





if __name__ == '__main__':
    main()