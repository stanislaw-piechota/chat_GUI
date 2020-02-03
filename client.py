import socket, _thread, sys
from tkinter import *
import config

data = config.Config()
messages = []

win = Tk()

canvas = Canvas(win, width=400, height=400)
canvas.pack()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((data.IP, data.PORT))

entry = Entry(win, width=50)
canvas.create_window(160, 15, window=entry)

label = Label(win, text='')
canvas.create_window(300, 380, window=label)

def sendMsg():
    msg = data.NICK + ": " + entry.get()
    s.send(bytes(msg, "utf-8"))
    entry.delete(0, END)

def slideMessages():
    canvas.delete(messages[0])
    messages.remove(messages[0])
    for mess in messages:
        xcoord, ycoord = canvas.coords(mess)[0], canvas.coords(mess)[1]
        canvas.coords(mess, (xcoord, ycoord-20))

def getMsg(s):
    pad = -20
    while True:
        if pad+40 > 360:
            slideMessages()
        else:
            pad+=20
        text = s.recv(1024).decode('utf-8')
        label = Label(win, text=text)
        messages.append(canvas.create_window(400-3.2*len(text), 40+pad, window=label))


_thread.start_new_thread(getMsg, (s, ))

button = Button(win, text="ENTER", bg="green", command=sendMsg)
canvas.create_window(360, 15, window=button)

win.mainloop()
