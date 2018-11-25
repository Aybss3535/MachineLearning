#-*-coding=utf-8 -*-
from math import log
import treePlotter
from pip._vendor.webencodings import labels
from numpy.core.fromnumeric import choose
#计算香农熵（信息熵）,香农熵越小，则纯度越高
def calcShannonEnt(dataSet):
    numEntries=len(dataSet)
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1
    shannonEnt=0.0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries
        shannonEnt-=prob*log(prob,2)
        return shannonEnt
#创建数据
def createDataSet():
    dataSet=[[1,1,'yes'],
             [1,1,'yes'],
             [1,0,'no'],
             [0,1,'no'],
             [0,1,'no']]
    labels=['no surfacing','flippers']
    return dataSet,labels
#按照给定特征划分数据集
def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec=featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
#选择最好的数据划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures=len(dataSet[0])-1
    baseEntropy=calcShannonEnt(dataSet)
    bestInfoGrain=0.0;bestFeature=-1
    for i in range(numFeatures):
        featList=[example[i] for example in dataSet]
        uniqueVals=set(featList)
        newEntropy=0.0
        for value in uniqueVals:
            subDataSet=splitDataSet(dataSet, i, value)
            prob=len(subDataSet)/float(len(dataSet))
            newEntropy+=prob*calcShannonEnt(subDataSet)
        infoGain=baseEntropy-newEntropy
        if(infoGain>bestInfoGrain):
            bestInfoGrain=infoGain
            bestFeature=i
    return bestFeature
import operator
#选择所有特征中出现次数最多的类别
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount=sorted(classCount.iteritems(),
                            key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
#创建决策树
def createTree(dataSet,labels):
    classList=[example[-1] for example in dataSet]
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet)
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree
def classify(inputTree,featLables,testVec):
    firstStr=inputTree.keys()[0]
    secondDict=inputTree[firstStr]
    featIndex=featLables.index(firstStr)
    for key in secondDict.keys():
        if(testVec[featIndex]==key):
            if(type(secondDict[key]).__name__=='dict'):
                classLabel=classify(secondDict[key], featLables, testVec)
            else:
                classLabel=secondDict[key]
    return classLabel
# myDat,labels=createDataSet()
myTree=treePlotter.retrieveTree(0)
def storeTree(inputTree,filename):
    import pickle
    fw=open(filename,'w')
    pickle.dump(inputTree, fw)
    fw.close()
def grabTree(filename):
    import pickle
    fr=open(filename)
    return pickle.load(fr)
# storeTree(myTree, "D:/data/classifyStoryage.txt")
# tree=grabTree("D:/data/classifyStoryage.txt")
# print(tree)
# pred=classify(myTree, labels, [1,1])
# print(pred)
# shannonEnt=calcShannonEnt(myDat)
# print(shannonEnt)
# newData=splitDataSet(myDat, 0, 1)
# print(newData)
# bestFeature=chooseBestFeatureToSplit(myDat)
# print(bestFeature)
# tree=createTree(myDat, labels)
# print(tree)
fr=open('D:/data/MLiA_SourceCode/machinelearninginaction/Ch03/lenses.txt')
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lensesLabel=['age','prescript','astigmatic','tearRate']
tree=createTree(lenses, lensesLabel)
print(tree)
treePlotter.createPlot(tree)