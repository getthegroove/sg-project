from sklearn import tree
from sklearn.externals.six import StringIO
import sys
import csv
import numpy as np
import pydot 
import pickle

features = []
classes = []

treename = sys.argv[1]
for x in range(2,len(sys.argv)):
    with open(sys.argv[x],"r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        rows = list(reader)
        maxSecond = int(rows[len(rows)-1][0])
        print(maxSecond)
        tempFeature = []
        i=1
        for row in rows:
            tempFeature += row[1:7]
            if (i%2 == 0):
               features.append(tempFeature)
               tempFeature = []
               classes.append(int(row[0])*100/maxSecond)
            i += 1
            
            

           
           
          
print(features[0])
print(classes)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, classes)
pickle.dump(clf, open("save_"+treename+".p","wb"))

with open(treename+".dot", "w") as f:
    f = tree.export_graphviz(clf, out_file=f)

dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf(treename+".pdf")
