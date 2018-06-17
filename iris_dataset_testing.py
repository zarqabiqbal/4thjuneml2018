#!/usr/bin/python3
from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

#load iris data in iris variable
iris = load_iris()

x=[0,50,100]

#training the data
train_data = np.delete (iris.data,x,axis=0)
train_target = np.delete (iris.target,x)

#testing the data
test_data = iris.data[x]
test_target = iris.target[x]

#calling the decision tree classifier which take the decision
clf = tree.DecisionTreeClassifier()

#trained the target according to input data
trained = clf.fit(train_data,train_target)

#give input and take predictive output
predicted = trained.predict([[7. , 3.2 , 4.2 , 1.7]])

#print predictive output where 0(setosa) ,1(versicolor) & 2( virginia)
print(predicted)
