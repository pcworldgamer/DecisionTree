# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:27:37 2018

@author: indiedevpt
"""

from sklearn import tree

#data - height, weight and shoe size
X=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],
	[171,75,42],[181,85,43]]

#classification
Y=['male','female','female','female','male','male','male','female','male',
	'female','male']

#decision tree classifier
clf=tree.DecisionTreeClassifier()

#trending data
clf=clf.fit(X,Y)

#predict
prediction=clf.predict([[160,50,33]])

print(prediction)