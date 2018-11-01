# -*- coding=utf-8 -*-
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier#导入决策树
iris=load_iris()
print(iris.data)
print(iris.target)
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.25,random_state=33)
clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)
predict=clf.predict(x_test)
print(predict)
print(y_test)
x=[n[0] for n in x_train]
y=[n[1] for n in x_train]
test_x=[n[0] for n in x_test]
test_y=[n[1] for n in x_test]
print x
print y
plt.scatter(x, y,c=y_train,marker='x')
plt.scatter(test_x,test_y,c=predict,marker='*')
plt.scatter(test_x,test_y,c=y_test,marker='v')
plt.show()
