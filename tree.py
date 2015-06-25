from sklearn import tree
from sklearn.externals.six import StringIO
import sys
import csv
import numpy as np
import pydot 
import pickle

files = []
Y = []
treename = sys.argv[1]
for i in range(2,len(sys.argv)):
    with open(sys.argv[i],"r") as csvfile:
        tmp_list = []
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
           files = files + [row[2:8]]
           Y.append(i-2)
          
print(files)
print(Y)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(files, Y)
pickle.dump(clf, open("save_"+treename+".p","wb"))

with open(treename+".dot", "w") as f:
    f = tree.export_graphviz(clf, out_file=f)

dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf(treename+".pdf")
