#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel='linear')

### Full Data set ###
print "====================================="
print "Complete Data Set"
print "====================================="
t0 = time()
clf.fit(features_train, labels_train)
temp = time() - t0
t0 = temp
print "Training Time: ", round(t0, 3), "s"

t1 = time()
prediction = clf.predict(features_test)
temp = time() - t1
t1 = temp
print "Prediction Time: ", round(t1, 3), "s"

print "Total Time: ", round(t0 + t1, 3), "s"

score = accuracy_score(labels_test, prediction)
print "The accuracy is: ", round(score * 100, 3), "%"

### One percent of the Data set ###
print "====================================="
print "1% of the Data Set"
print "====================================="
features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
temp = time() - t0
t0 = temp
print "Training Time: ", round(t0, 3), "s"

t1 = time()
prediction = clf.predict(features_test)
temp = time() - t1
t1 = temp
print "Prediction Time: ", round(t1, 3), "s"

print "Total Time: ", round(t0 + t1, 3), "s"

score = accuracy_score(labels_test, prediction)
print "The accuracy is: ", round(score * 100, 3), "%"
#########################################################


 