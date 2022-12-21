# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:37:38 2022

@author: dhpcap
"""

from sklearn import datasets
dataset =datasets.load_wine() # load dataset
print ("Inputs: ", dataset.feature_names) # print the names of the 13 features
print ("Outputs: ", dataset.target_names) # print the label type of wine
print(dataset.data[0:3]) # print the wine data features

from sklearn.model_selection import train_test_split # import train_test_split function
inputs = dataset.data # input and outputs
outputs = dataset.target
X_train, X_test, y_train, y_test = train_test_split(inputs, outputs, test_size=0.3, random_state=1) # split dataset into training set and test set

from sklearn.naive_bayes import GaussianNB    # import Gaussian Naive Bayes model

classifer = GaussianNB() # create a Gaussian Classifier
classifer.fit(X_train, y_train) # train the model using the training sets
y_pred = classifer.predict(X_test) # predict the response for test dataset

from sklearn import metrics # import scikit-learn metrics module for accuracy calculation
print("Accuracy:", metrics.accuracy_score(y_test, y_pred)) # printing accuracy

import seaborn as sns
from sklearn.metrics import confusion_matrix # importing the required modules
cm = confusion_matrix(y_test, y_pred) # passing actual and predicted values
sns.heatmap(cm, annot=True)