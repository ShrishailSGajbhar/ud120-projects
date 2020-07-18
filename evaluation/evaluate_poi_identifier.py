#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(features,labels,test_size = 0.3, random_state = 42)

clf = DecisionTreeClassifier()
clf.fit(X_train,y_train)
pred = clf.predict(X_test)

score = accuracy_score(pred,y_test)
print "(70/30) training/test Acc (for test): ",score
print len(y_test)

print "Actual"," ","Predicted"
for i in range(len(pred)):
    print y_test[i]," ",pred[i]

from sklearn.metrics import precision_score, recall_score
print "precision: ",precision_score(pred, y_test)
print "recall: ",recall_score(pred, y_test)
