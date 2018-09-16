#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

len_ftrain = len(features_train[0])
print "No of features/columns in the data:", len_ftrain


######################################################

from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)
t0 = time()
print("training time with decision tree", time() - t0)

pred = clf.predict(features_test)
t1 = time()
print("testing time with decision tree", time() - t1)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print "Accuracy obtained using decision tree:", acc

#########################################################


