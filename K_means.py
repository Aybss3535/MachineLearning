# -*- coding=utf-8 -*-
from numpy import *
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
def loadData(fileName):
    fr=open(fileName)
    dataMat=[]
    for line in fr.readlines():
        x=line.strip().split()
        dataMat.append(list(map(float,x)))
    return dataMat
def getDis(vecA,vecB):
    return sqrt(sum(power(vecA-vecB,2)))
def createCent(dataMat,k):
    n=shape(dataMat)[1]#一个数据具有的坐标数目
    cent=mat(zeros((k,n)))
    for i in range(n):
        minJ=min(dataMat[:,i])
        maxJ=max(dataMat[:,i])
        gap=float(maxJ-minJ)
        cent[:,i]=minJ+gap*random.rand(k,1)
    return cent
def K_Means(dataMat,k,getDis=getDis,createCent=createCent):
    m=shape(dataMat)[0]#数据个数
    cent=createCent(dataMat,k)
    dataAlloca=mat(zeros([m,2]))#用于存储数据所属的类及距离类的距离
    change=True
    while change:
        change=False
        for i in range(m):#遍历每个数据
            mindis=inf;minindex=-1
            for j in range(k):#遍历每个类中心
                dis=getDis(dataMat[i,:],cent[j,:])
                if dis<mindis:
                    mindis=dis;minindex=j
            if dataAlloca[i,0]!=minindex:
                change=True
            dataAlloca[i,:]=minindex,mindis
#             print(dataAlloca)
        for i in range(k):
            newData=dataMat[nonzero(dataAlloca[:,0].A==i)[0]]
            cent[i,:]=mean(newData, axis=0)#计算该类的点的坐标平均值,axis=0纵向
    return dataAlloca,cent
dataMat=mat(loadData("D:/data/randomData.txt"))
# dataAllocat,cent=K_Means(dataMat, 2)
isir=load_iris().data
dataAllocat,cent=K_Means(dataMat, 4)
# print(isir)
# print(dataAllocat)
# print(cent)
# x=[dataMat[i,0] for i in range(shape(dataMat)[0])]
# print(x)
# y=[dataMat[i,1] for i in range(shape(dataMat)[0])]
# print(y)
# pred=[dataAllocat[i,0] for i in range(shape(dataAllocat)[0])]
# print(pred)
# plt.scatter(x,y,c=pred,marker="x")
x1=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]
print(dataAllocat)
for i in range(shape(dataMat)[0]):
    if(dataAllocat[i,0]==0.0):
        x1.append(dataMat[i,0])
        y1.append(dataMat[i,1])
    if(dataAllocat[i,0]==1.0):
        x2.append(dataMat[i,0])
        y2.append(dataMat[i,1])
    if(dataAllocat[i,0]==2.0):
        x3.append(dataMat[i,0])
        y3.append(dataMat[i,1])
    if(dataAllocat[i,0]==3.0):
        x4.append(dataMat[i,0])
        y4.append(dataMat[i,1])
plt.plot(x1,y1,'or',marker="x")
plt.plot(x2,y2,'og',marker="o")
plt.plot(x3,y3,'ob',marker="*")
plt.plot(x4,y4,'oy',marker="v")

plt.show()
# print(len(dataAllocat[nonzero(dataAllocat[:,0].A==0)[0]]))
# print(len(dataAllocat[nonzero(dataAllocat[:,0].A==1)[0]]))
# print(len(dataAllocat[nonzero(dataAllocat[:,0].A==2)[0]]))