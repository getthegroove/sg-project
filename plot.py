import csv 
import sys
import numpy as np
import matplotlib.pyplot as plt
import math

temps = []
X = []
Y = []
Z = []
norm = []

with open(sys.argv[1]) as csvfile:
       reader = csv.reader(csvfile, delimiter=',', quotechar='|')
       for row in reader:
         temps.append(row[0])
         X.append(row[1])
         Y.append(row[2])
         Z.append(row[3])
         norm.append(math.sqrt(float(row[1])**2+float(row[1])**2+float(row[3])**2))
         

plt.plot(temps,X,label="X")
plt.plot(temps,Y,label="Y")
plt.plot(temps,Z,label="Z")
plt.plot(temps,norm,label="norm")
plt.xlabel("time[ms]")
plt.ylabel("accelration[m/s^2]")
plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
plt.show()
