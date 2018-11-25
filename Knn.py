# -*- coding=utf-8 -*-
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler#数据标准化模块
from sklearn.neighbors import KNeighborsClassifier#knn分类器
from numpy import *
import matplotlib.pyplot as plt
iris=load_iris()#导入鸢尾花数据集
print(iris.data)
# print(iris.target)
# print(shape(iris.data))
# print(len(iris.target))
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=33)
# ss=StandardScaler()
# X_train=ss.fit_transform(X_train)#将数据化标准化
# X_test=ss.transform(X_test)
# print(X_train)
# print(X_test)
knc=KNeighborsClassifier()
knc.fit(X_train,y_train)
y_predict=knc.predict(X_test)
print(y_predict)
print(y_test)
error=0.0
for i in range(len(y_predict)):
    if(y_predict[i]!=y_test[i]):
        error+=1
errorpercent=error/len(y_predict)
print("error",errorpercent)
x=[n[0] for n in X_train]
y=[n[1] for n in X_train]
x1=[n[0] for n in X_test]
y1=[n[1] for n in X_test]

plt.scatter(x,y,c=y_train,marker='*')
plt.scatter(x1,y1,c=y_predict,marker='x')
plt.show()
# print(knc.score(X_test,y_test))