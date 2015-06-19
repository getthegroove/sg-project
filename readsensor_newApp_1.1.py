import socket, traceback
import sys
from time import *


#Name der Zieldatei
filename = sys.argv[1]

file = open(filename,"a")
host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
t = time()*1000


while (((time()*1000)-t)<5000):
 try:
  message, address = s.recvfrom(8192)
  data = str(message).split(',')
  file.write(str( int( (time()*1000)-t ) )+','+data[2]+','+data[3]+','+data[4].replace("'","") +'\n')
  print (message)
 except (KeyboardInterrupt, SystemExit):
  file.close()
  raise
 except:
  traceback.print_exc()
