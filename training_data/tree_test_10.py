import pickle
from sklearn import tree
import sys
import csv

tempFeature = []
result = []
features = []
#Name des verwendeten Baumes
filename = sys.argv[1]
#Decision-Tree laden
clf = pickle.load(open("save_"+filename+".p","rb"))

#zu testende CSV-Bewegungsdatei(gefenstert und "preprocessed")
with open(sys.argv[2],"r") as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     i = 1
     for row in reader:
         tempFeature = tempFeature + row[1:8]
         #jeweils wieder zwei ueberlappende Features dem Baum zum ueberpruefen geben
         if (i%2 == 0):
               features.append(tempFeature)
               #print(clf.predict(tempFeature))
               tempFeature = []
         i +=1
#print(features)
result = clf.predict(features)

print(result)
