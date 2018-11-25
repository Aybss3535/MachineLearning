# -*- coding=utf-8 -*-
from numpy import *
from os import listdir
from __builtin__ import str
from sklearn.neighbors import KNeighborsClassifier
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,i*32+j]=int(lineStr[j])
    return returnVect
def handWritingClassTest():
    hwLabel=[]
    dir=listdir("F:/trainingDigits")
    m=len(dir)
    trainingMat=zeros((m,1024))
    for i in range(m):
        filenameStr=dir[i]
        fileStr=filenameStr.split('.')[0]
        hwLabel.append(fileStr.split('_')[0])
        trainingMat[i,:]=img2vector('F:/trainingDigits/%s'%filenameStr)
    knn=KNeighborsClassifier()
    knn.fit(trainingMat, hwLabel)
    testListFile=listdir("F:/testDigits")
    n=len(testListFile)
    testLabel=[]
    error=0.0
    for i in range(n):
        filenameStr=testListFile[i]
        testLabel.append(filenameStr.split('_')[0])
        real=int(filenameStr.split('_')[0])
        pred=int(knn.predict(img2vector('F:/testDigits/%s'%filenameStr)))
        print('the true label is %s and the predict label is %s'%(real,pred))
        if(real!=pred):
            error+=1
    print('error=%s'%error)
    print('errorpercent=%s'%(error/float(n)))
handWritingClassTest();