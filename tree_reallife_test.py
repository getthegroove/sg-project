import socket, traceback
import pickle
from sklearn import tree
import sys
import time
from time import *
import math

def m(values):
	x = 0
	y = 0
	z = 0
	for v in values:
		x = x + float(v[0])
		y = y + float(v[1])
		z = z + float(v[2])
	return [x/len(values), y / len(values), z / len(values)]

def std(values,average):
    x,y,z = 0,0,0
    for v in values:
        x += (float(v[0])-average[0])**2
        y += (float(v[1])-average[1])**2
        z += (float(v[2])-average[2])**2
    return[math.sqrt(x/len(values)),math.sqrt(y/len(values)),math.sqrt(z/len(values))]



filename = sys.argv[1]
window_size = int(sys.argv[2])
clf = pickle.load(open("save_"+filename+".p","rb"))


host = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
t = time()*1000

templist = []


while (1):
 try:
  message, address = s.recvfrom(8192)
  data = str(message).split(',')
  templist.append([str(data[2]),str(data[3]),str(data[4])])
  if((time()*1000)-t >= window_size):
     average = m(templist)
     res = clf.predict(average + std(templist,average))[0]
     #res = clf.predict_proba(average + std(templist,average))[0]
     #print("static="+str(res[0])+" "+"right-left="+str(res[1])+" "+"forward-backward="+str(res[2])+" "+"up-down="+str(res[3])+"\n")
     if (res==0):
       print("static "+"\n")
     elif (res==1):
       print("right-left"+"\n")
     elif (res==2):
       print("forward-backward"+"\n")
     elif(res==3):
       print("up-down"+"\n")
     templist = []
     t=time()*1000
 except (KeyboardInterrupt, SystemExit):
  file.close()
  raise
 except:
  traceback.print_exc()
