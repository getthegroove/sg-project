import socket
import sys
from math import floor

def plotSensorsData (inputString,t,file):
	lFloat =Strings2Floats(inputString.split(','))
	numSensors = floor(len(lFloat)/3)
	for i in range(0,numSensors):
		p=lFloat[i*3:3*(i + 1)]
		print('Sensor',(i+1), ": ",p,sep='')
	        times.append(t)
                values.append([p[0],p[1],p[2]])
		file.write(str(t) + ", " + str(p[0]) + ", " + str(p[1]) + ", " + str(p[2]) +"\n")
	valueDict = dict(zip(times,values))	
	print('\n')
        

def Strings2Floats(listString):
	out=[]
	for j in range(0,len(listString)-1):
		out.append( float(listString[j]))
	return out

delta_t = int(sys.argv[1])
filename = sys.argv[2]
file = open(filename,"a")
go=True
bufferSize=1024
port=5555
UDPSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddress = ('', port)
print('Listening on port ', port)
UDPSocket.bind(serverAddress)
t=0
times = []
values = []
valueDict = {}

try:
	while t <= 10000:
		[data,attr] = UDPSocket.recvfrom(bufferSize)
		plotSensorsData(data.decode("utf-8"),t,file)
		t = t+delta_t
except KeyboardInterrupt:
	go=False

finally:
	UDPSocket.close()
file.close()
print("\nfertig =)")
