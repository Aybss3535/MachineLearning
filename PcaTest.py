# -*- coding=utf-8 -*-
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
iris=load_iris()
data=iris.data
target=iris.target
pca=PCA(n_components=2)
newData=pca.fit_transform(data)
print(newData)
x_train,x_test,y_train,y_test=train_test_split(newData,target,random_state=33,test_size=0.25)
knn=KNeighborsClassifier()
knn.fit(x_train, y_train)
pred=knn.predict(x_test)
print(pred)
print(y_test)
x=[n for n in x_train[:,0]]
y=[n for n in x_train[:,1]]
x1=[n for n in x_test[:,0]]
y1=[n for n in x_test[:,1]]
plt.scatter(x, y,c=y_train, marker='x')
plt.scatter(x1,y1,c=pred,marker='o')
plt.show()
print(data)