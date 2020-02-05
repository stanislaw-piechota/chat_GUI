from tkinter import *
import socket

class Config():
    def __init__(self):
        self.IP, self.PORT, self.NICK = '127.0.0.1', 4444, 'guest'
        win = Tk()

        canvas = Canvas(win, width=400, height=400)
        canvas.pack()

        label1 = Label(win, text="Podaj IP serwera:")
        canvas.create_window(200, 20, window=label1)
        entry1 = Entry(win)
        canvas.create_window(200, 40, window=entry1)

        label2 = Label(win, text="Podaj port:")
        canvas.create_window(200, 60, window=label2)
        entry2 = Entry(win)
        canvas.create_window(200, 80, window=entry2)

        label3 = Label(win, text="Podaj nick:")
        canvas.create_window(200, 100, window=label3)
        entry3 = Entry(win)
        canvas.create_window(200, 120, window=entry3)

        button = Button(win, text="ENTER", bg="green", command=lambda:self.send_data \
        (entry1, entry2, entry3, win, canvas))
        canvas.create_window(200, 160, window=button)

        win.mainloop()

    def send_data(self, entry1, entry2, entry3, win, canvas):
        ip = entry1.get()
        try:
            port = int(entry2.get())
            nick = entry3.get()
            win.destroy()
            self.IP = ip
            self.PORT = port
            self.NICK = nick
        except ValueError:
            err_label = Label(win, text="Wprowadz poprawny port", fg="red")
            canvas.create_window(200, 180, window=err_label)
