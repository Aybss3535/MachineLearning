#-*- coding=utf-8 -*-
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from numpy import *
import matplotlib.pyplot as plt
iris=load_iris()
data=iris.data
target=iris.target
x_train,x_test,y_train,y_test=train_test_split(data,target,test_size=0.25)
clf=DecisionTreeClassifier()
clf.fit(x_train, y_train)
pred=clf.predict(x_test)
print(pred)
print(y_test)
# error=0.0
# for i in range(shape(pred)[0]):
#     if(pred[i]!=y_test[i]):
#         error+=1
# print("error",error)
fig=plt.figure()
ax=plt.subplot(111)
x=[i[0] for i in x_train]
y=[i[1] for i in x_train]
x1=[i[0] for i in x_test]
y1=[i[1] for i in x_test]
plt.scatter(x, y,c=y_train, marker='x')
plt.scatter(x1,y1,c=pred,marker='o')
plt.show()


