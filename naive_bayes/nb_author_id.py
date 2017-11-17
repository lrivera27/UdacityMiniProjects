#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
clf = GaussianNB()

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


