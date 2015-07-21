import csv 
import sys
import numpy as np
import matplotlib.pyplot as plt
import math


temps = []
X = []
Y = []
Z = []



with open(sys.argv[1]) as csvfile:
       reader = csv.reader(csvfile, delimiter=',', quotechar='|')
       for row in reader:
         temps.append(int(row[0]))
         X.append(float(row[1]))
         Y.append(float(row[2]))
         Z.append(float(row[3]))

         
         

plt.plot(temps,X,label="X")
plt.plot(temps,Y,label="Y")
plt.plot(temps,Z,label="Z")

plt.xlabel("time[ms]")
plt.ylabel("accelration[m/s^2]")
plt.legend(bbox_to_anchor=(1.00, 1), loc=1, borderaxespad=0.)
plt.show()
