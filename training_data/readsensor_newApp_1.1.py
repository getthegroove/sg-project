import socket, traceback
import sys
from time import *


#Name der Zieldatei
filename = sys.argv[1]
#Zieldatei oeffnen
file = open(filename,"a")
#socket fuer stream anlegen
host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
#startzeit in ms
t = time()*1000

#stream auslesen und die gelesenen Daten zusammen mit der aktuellen Zeit in ms in eine csv-Datei schreiben. Aufnahme dauert 20 Sekunden.
while (((time()*1000)-t)<20000):
 try:
  message, address = s.recvfrom(8192)
  data = str(message).split(',')
  file.write(str( int( (time()*1000)-t ) )+','+data[2]+','+data[3]+','+data[4].replace("'","") +'\n')
#testausgabe
  print (message)
 except (KeyboardInterrupt, SystemExit):
  file.close()
  raise
 except:
  traceback.print_exc()
