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
    for mess in messages:
        text = mess['text']
        messages.remove(mess)
        mess.destroy()

def getMsg(s):
    pad = 0
    while True:
        text = s.recv(1024).decode('utf-8')
        label = Label(win, text=text)
        canvas.create_window(400-3.2*len(text), 380-pad, window=label)
        #slideMessages()
        messages.append(label)
        pad+=20

_thread.start_new_thread(getMsg, (s, ))

button = Button(win, text="ENTER", bg="green", command=sendMsg)
canvas.create_window(360, 15, window=button)

win.mainloop()
