import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections = []
clients = []

IP = '0.0.0.0'
PORT = 4444
s.bind((IP, PORT))
s.listen(1)
print("Listening for clients on: " + IP + ":" + str(PORT))

def handler(c, a):
	while True:
		try:
			data = c.recv(1024)
			for connection in connections:
				connection.send(data)
		except:
			print(str(a[0]) + ':' + str(a[1]), 'disconnected')
			connections.remove(c)
			c.close()
			break

def run():
	while True:
		c, a = s.accept()
		connections.append(c)
		cThread = threading.Thread(target=handler, args=(c, a))
		cThread.deamon = True
		cThread.start()
		print(str(a[0]) + ':' + str(a[1]), 'connected')

run()
