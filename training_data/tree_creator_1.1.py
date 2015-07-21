from sklearn import tree
from sklearn.externals.six import StringIO
import sys
import csv
import numpy as np
import pydot 
import pickle
#Feature-Liste fuer den Baum
features = []
#Klassen-Liste fuer den Baum
classes = []
#Prozessierte "Aufwaertsbewegungen"
up = ["Dennis_up1_processed.csv", "Matze_up1_processed.csv", "Jacob_up1_processed.csv", "Dennis_up2_processed.csv", "Matze_up2_processed.csv", "Jacob_up2_processed.csv"]
#Prozessierte "Abwaertsbewegung"
down = ["Dennis_down1_processed.csv", "Matze_down1_processed.csv", "Jacob_down1_processed.csv", "Matze_down2_processed.csv", "Jacob_down2_processed.csv"]
#Das erste Input-Argument bestimmt den Baumname 
treename = sys.argv[1]
#Die Files fuer die Aufwaertsbewegung nacheinander einlesen
for x in up:
    with open(x,"r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        rows = list(reader)
        #Beschreibt die Gesamtlaenge der aufgezeichneten Bewegung (letzte aufgezeichnete Zeit des Files)
        maxSecond = int(rows[len(rows)-1][0])
        print(maxSecond)
        #Aktuelles Feature
        tempFeature = []
        i=1
        for row in rows:
            tempFeature += row[1:7]
            #jeweils zwei ueberlappende Fenster werden als Feature benutzt
            if (i%2 == 0):
               features.append(tempFeature)
               tempFeature = []
               #berechne Klasse(Prozent von Gesamtzeit) des aktuellen Features
               classes.append(int(row[0])*100/maxSecond)
            i += 1
#Verarbeite "Abwaertsbewegungen", Klasse fuer Abwaertsbewegungen ist 200
for x in down:
    with open(x,"r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        rows = list(reader)
        tempFeature = []
        i=1
        for row in rows:
            tempFeature += row[1:7]
            if (i%2 == 0):
               features.append(tempFeature)
               tempFeature = []
               classes.append(200)
            i += 1
            
            

           
           
          
print(features[0])
print(classes)
#Decision-Tree erstellen und zwischenspeichern mit "pickle"
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, classes)
pickle.dump(clf, open("save_"+treename+".p","wb"))
#Decision-Tree pdf-Datei erstellen
with open(treename+".dot", "w") as f:
    f = tree.export_graphviz(clf, out_file=f)

dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf(treename+".pdf")
