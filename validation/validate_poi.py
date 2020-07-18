#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

################ Part-1 ###########################
#clf = DecisionTreeClassifier()
#clf.fit(features, labels)
#pred = clf.predict(features)
#score = accuracy_score(pred,labels
#print "Full data training Acc: ",score
# This part is overfitted and gives acc of 0.989
#==================================================
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(features,labels,test_size = 0.3, random_state = 42)

clf = DecisionTreeClassifier()
clf.fit(X_train,y_train)
pred = clf.predict(X_test)

score = accuracy_score(pred,y_test)
print "(70/30) training/test Acc (for test): ",score


### it's all yours from here forward!
