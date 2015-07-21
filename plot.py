import csv 
import sys
import numpy as np
import matplotlib.pyplot as plt
import math

temps = []
X_av = []
Y_av = []
Z_av = []
X_st = []
Y_st = []
Z_st = []


with open(sys.argv[1]) as csvfile:
       reader = csv.reader(csvfile, delimiter=',', quotechar='|')
       for row in reader:
         temps.append(row[1])
         X_av.append(row[2])
         Y_av.append(row[3])
         Z_av.append(row[4])
         X_st.append(row[5])
         Y_st.append(row[6])
         Z_st.append(row[7])
         
         

plt.plot(temps,X_av,label="X_av")
plt.plot(temps,Y_av,label="Y_av")
plt.plot(temps,Z_av,label="Z_av")
plt.plot(temps,X_st,label="X_st")
plt.plot(temps,Y_st,label="Y_st")
plt.plot(temps,Z_st,label="Z_st")
plt.xlabel("time[ms]")
plt.ylabel("accelration[m/s^2]")
plt.legend(bbox_to_anchor=(1.00, 1), loc=1, borderaxespad=0.)
plt.show()
