from threading import Thread, Semaphore
from socket import socket
addres = ('127.0.0.1', 8000)
connections = {}

def handle(con, addr):
	connections[addr[1]] = {'ip':addr[1], 'connection':con}
	with con:
		while True:
			data = con.recv(1024)
			print(data)
			if not data:
				break
			con.sendall(data)
			for port, info in connections.items():
				if addr[1] == port:
					continue
				info['connection'].sendall(data)
				
	del connections[addr[1]]
	print('Done!')


with socket() as s:
	s.bind(addres)
	s.listen()
	
	while True:
		print ('waiting for connection...')
		info = s.accept()
		con = info[0]
		addr = info[1]
		print('connected ip', addr[0], addr[1]) 
		
		Thread(target = handle, args = info).start()
		
