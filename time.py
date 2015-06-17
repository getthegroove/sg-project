import socket
from time import *

bufferSize=1024
port=5555
UDPSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddress = ('', port)
print('Listening on port ', port)
UDPSocket.bind(serverAddress)
i = 0
t1 = time()
liste = []
try:
	while i < 100:
		i = i + 1
		[data,attr] = UDPSocket.recvfrom(bufferSize)
		liste.append(data)
finally:
	UDPSocket.close()
t2 = time()

t = t2-t1
freq = len(liste)/t
print([t1,t2,t])
print("frequenzy = " + str(freq))
