# -*- coding=utf-8 -*-
from numpy import *
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy import stats
import matplotlib.pyplot as plt
def autoNorm(dataSet):#归一化数据
    minValue=dataSet.min(0)
    maxValue=dataSet.max(0)
    ranges=maxValue-minValue
    dataSet=dataSet-tile(minValue,(dataSet.shape[0],1))
    normData=dataSet/tile(ranges, (dataSet.shape[0],1))
    return normData
iris=load_iris()
data=autoNorm(iris.data)
target=iris.target
x_train,x_test,y_train,y_test=train_test_split(data,target,test_size=0.25,random_state=33)
#获取欧式距离
def getDis(vecA,vecB):
    return sqrt(sum(power(vecA-vecB,2)))
def classify(input,x_train,y_train,k):
    #先计算预测数据与训练数据的欧氏距离
    m=shape(input)[0]
    n=shape(x_train)[0]
    predict=[]
    for i in range(m):
        dis=zeros([n,2])
        for j in range(n):
            dis[j,0]=getDis(input[i,:], x_train[j,:])
            dis[j,1]=y_train[j]
        sort=dis[:,0].argsort()
        dis=mat(dis[sort].tolist()) 
        pred=[]
        for j in range(k):
            pred.append(dis[j,1])
        predict.append(stats.mode(pred)[0][0])
    return predict
predict=classify(x_test, x_train, y_train, 3)
predict=np.array(map(int,predict))
error=0.0
for i in range(len(predict)):
    if(y_test[i]!=predict[i]):
        error=error+1.0
errorpercent=error/len(predict)
print("errorpercent",errorpercent)
x=[n for n in x_train[:,0]]
y=[n for n in x_train[:,1]]
x1=[n for n in x_test[:,0]]
y1=[n for n in x_test[:,1]]
plt.scatter(x, y,c=y_train, marker='x')
plt.scatter(x1,y1,c=predict,marker='o')
# plt.scatter(x1,y1,c=y_test,marker='v')
plt.show()