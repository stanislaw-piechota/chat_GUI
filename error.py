from tkinter import *

class Error():
    def __init__(self, text):
        win = Tk()

        canvas = Canvas(win, width=200, height=40)
        canvas.pack()

        err_label = Label(win, text=text, fg="red")
        canvas.create_window(100, 10, window=err_label)

        win.mainloop()
