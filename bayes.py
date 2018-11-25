#-*- coding=utf-8 -*-
'''
Created on 2018年11月20日

@author: songxuan
'''
from numpy import *
from pip._vendor.pyparsing import line
def loadDataSet():
    postingList=[['my','dog','has','flea','problems','help','please'],
                 ['maybe','not','take','him','to','dog','park','stupid'],
                 ['my','dalmation','is','so','cute','I','love','him'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['mr','licks','ate','my','steak','how','to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']]
    classVec=[0,1,0,1,0,1]
    return postingList,classVec
def createVicatList(dataSet):
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet|set(document)
    return list(vocabSet)
def setOfWord2Vec(vocabList,inputSet):
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:
            print("the word %s is not in my vocabulary!"%word)
    return returnVec
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    pAbusive=sum(trainCategory)/float(numTrainDocs)
    p0Num=ones(numWords);p1Num=ones(numWords)
    P0Denom=2.0;p1Denom=2.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
        else:
            p0Num+=trainMatrix[i]
            P0Denom+=sum(trainMatrix[i])
    p0Vect=log(p0Num/P0Denom);p1Vect=log(p1Num/p1Denom)
    return p0Vect,p1Vect,pAbusive
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1=sum(vec2Classify * p1Vec)+log(pClass1)
    p0=sum(vec2Classify * p0Vec)+log(1-pClass1)
    if p1>p0:
        return 1;
    else:
        return 0;
def testNB():
    listOPosts,listClasses=loadDataSet()
    myVocatList=createVicatList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWord2Vec(myVocatList, postinDoc))
    p0V,p1V,pAb=trainNB0(array(trainMat), array(listClasses))
    testEntry=['love','my','dalmation']
    thisDoc=array(setOfWord2Vec(myVocatList, testEntry))
    print(thisDoc)
    print(testEntry,'classified as:',classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry=['stupid','garbage']
    thisDoc=array(setOfWord2Vec(myVocatList, testEntry))
    print(testEntry,"classified as :",classifyNB(thisDoc, p0V, p1V, pAb))
def bagOfWords2VecMN(vocabList,inputSet):
    returnVec=[0]*len(vocabList)
    for words in inputSet:
        if words in vocabList:
            returnVec[vocabList.index(words)]+=1
    return returnVec
def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)#注意大写
    return [tok.lower() for tok in listOfTokens if len(tok)>2]
def spamTest():
    docList=[];classList=[];fullText=[]
    for i in range(1,26):
        wordList=textParse(open('D:\\data\MLiA_SourceCode\\machinelearninginaction\\Ch04\\email\\spam\\%d.txt'%i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList=textParse(open('D:\\data\\MLiA_SourceCode\\machinelearninginaction\\Ch04\\email\\ham\\%d.txt'%i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList=createVicatList(docList)
    trainingSet=range(50);
    testSet=[]
    for i in range(10):
        randIndex=int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[];trainClasses=[]
    for docIndex in trainingSet:
        trainMat.append(setOfWord2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam=trainNB0(array(trainMat), array(trainClasses))
    errorCount=0;
    for docIndex in testSet:
        wordVector=setOfWord2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam)!=classList[docIndex]:
            errorCount+=1
    countErrorRate(float(errorCount)/len(testSet))
def countErrorRate(error):
    rw=open("D:\\data\\MLiA_SourceCode\\machinelearninginaction\\Ch04\\email\error.txt",'a')
    rw.write(str(error))
    rw.write(" ")
def testEverErrorRate():
    for i in range(10000):
        spamTest()
    fr=open("D:\\data\\MLiA_SourceCode\\machinelearninginaction\\Ch04\\email\error.txt",'r')
    data=[]
    for line in fr.xreadlines():
        data.extend(line.split())
    sum=0.0
    for d in data:
        sum+=float(d)
    print(sum/len(data))
    print(len(data))
def localWords():
    import feedparser
    d=feedparser.parse('http://feed.cnblogs.com/blog/sitehome/rss')
    print(d.feed.title)
    print(d.feed.subtitle)
    print(d.feed.link)
    print(type(d.entries))
    print(len(d.entries))
    print([e.title for e in d.entries][:5])
    print(d.entries[1].title)
    print(d.entries[0].summary)
def testMaxError():
    fr=open("D:\\data\\MLiA_SourceCode\\machinelearninginaction\\Ch04\\email\error.txt",'r')
    max=0.0
    data=[]
    for word in fr.readlines():
        data.extend(word.split())
    for d in data:
        if(float(d)>max):
            max=float(d)
    print(len(data))
    print("max:",max)
# localWords()
testMaxError()
# testEverErrorRate()





