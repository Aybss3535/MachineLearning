# -*- coding=utf-8 -*-
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from numpy import *
import operator
from audioop import reverse
iris=load_iris()
data=iris.data
target=iris.target
pca=PCA(n_components=2)
newData=pca.fit_transform(data)
x_train,x_test,y_train,y_test=train_test_split(newData,target,test_size=0.25,random_state=33)
def classify0(inX,dataSet,label,k):
    datasetSize=dataSet.shape[0]
    dissMat=tile(inX,(datasetSize,1))-dataSet
    sqDissMat=dissMat**2
    sqDistance=sum(sqDissMat,axis=1)
    distance=sqDistance**0.5
    sortIndex=distance.argsort()
    classCount={}
    for i in range(k):
        votelabel=label[sortIndex[i]]
        if votelabel not in classCount.keys():classCount[votelabel]=0
        classCount[votelabel]+=1
    sortedDistance=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedDistance[0][0]
classify0(x_test[0], x_train, y_train, 3)
        
    
