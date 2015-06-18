import socket, traceback
file = open("lol.txt","a")
host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
while 1:
 try:
  message, address = s.recvfrom(8192)
  data = str(message).split(',')
  file.write(data[2]+','+data[3]+','+data[4].replace("'","")+'\n')
  print (message)
 except (KeyboardInterrupt, SystemExit):
  file.close()
  raise
 except:
  traceback.print_exc()
