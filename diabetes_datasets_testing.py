#!/usr/bin/python3
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn import tree
diabetes=load_diabetes()

x=[0,50,100]

#delete the test data and store remaining data into variable
trained_data = np.delete (diabetes.data,x,axis=0)

#delete the target data and store remaining data into variable
trained_target = np.delete (diabetes.target,x)

#extract the testing data
test_data = diabetes.data[x]

#call the decision tree classifier
dtc=tree.DecisionTreeClassifier()

#trained the machine for predictive output according to input data
trained=dtc.fit(trained_data,trained_target)

#collect predictive output
predictive_output=trained.predict(test_data)

#print predictive output
print(predictive_output)


