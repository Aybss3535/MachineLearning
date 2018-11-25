#-*- coding=utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib
from pandas._libs.tslibs.offsets import key
from Tkconstants import FIRST
from matplotlib.dates import seconds
decisionNode=dict(boxstyle="sawtooth",fc="0.8")
leafNode=dict(boxStyle="round4",fc="0.8")#fc用于设定边框背景灰度
arrow_args=dict(arrowstyle="<-")#connectionstyle="arc3,rad=0.2"
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    zh_font = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\STKAITI.TTF')
    createPlot.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',
                           xytext=centerPt,textcoords='axes fraction',
                           va="center",ha="center",bbox=nodeType,arrowprops=arrow_args,FontProperties=zh_font)
def createPlot(inTree):
    fig=plt.figure(1,facecolor="white")
    fig.clf()#清除图像窗口
#     createPlot.ax1=plt.subplot(111,frameon=False)
#     plotNode(u"决策节点", (0.5,0.1), (0.1,0.5), decisionNode)
#     plotNode(u"叶节点", (0.8,0.1), (0.3,0.8), leafNode)
#     plt.show()
    axprops=dict(xticks=[],yticks=[])
    createPlot.ax1=plt.subplot(111,frameon=False,**axprops)
    plotTree.totalW=float(getNumLeafs(inTree))
    plotTree.totalD=float(getTreeDepth(inTree))
    plotTree.xoff=-0.5/plotTree.totalW;
    plotTree.yoff=1.0;
    plotTree(inTree, (0.5,1.0), '')
    plt.show()
def getNumLeafs(myTree):
    numLeafs=0
    firstStr=myTree.keys()[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__=='dict'):
            numLeafs+=getNumLeafs(secondDict[key])
        else:
            numLeafs+=1
    return numLeafs
def getTreeDepth(myTree):
    maxDepth=0
    firstStr=myTree.keys()[0]
    secondDict=myTree[firstStr]
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__=='dict'):
            thisDepth=1+getTreeDepth(secondDict[key])
        else:
            thisDepth=1
        if(thisDepth>maxDepth):
            maxDepth=thisDepth
    return maxDepth
def retrieveTree(i):
    listOfTrees=[{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
        {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head':{0:'no',1:'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]
def plotMidText(cntrPt,parentPt,txtString):
    xMid=(parentPt[0]-cntrPt[0])/2.0+cntrPt[0]
    yMid=(parentPt[1]-cntrPt[1])/2.0+cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)
def plotTree(myTree,parentPt,nodeTxt):
    numLeafs=getNumLeafs(myTree)
    depth=getNumLeafs(myTree)
    firstStr=myTree.keys()[0]
    cntrPt=(plotTree.xoff+(1.0+float(numLeafs))/2.0/plotTree.totalW,plotTree.yoff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict=myTree[firstStr]
    plotTree.yoff=plotTree.yoff-1.0/plotTree.totalD
    for key in secondDict.keys():
        if(type(secondDict[key]).__name__=='dict'):
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xoff=plotTree.xoff+1.0/plotTree.totalW
            plotNode(secondDict[key], (plotTree.xoff,plotTree.yoff), cntrPt, leafNode)
            plotMidText((plotTree.xoff,plotTree.yoff), cntrPt, str(key))
    plotTree.yoff=plotTree.yoff+1.0/plotTree.totalD
# myTree=retrieveTree(0)
# print(myTree)
# num=getNumLeafs(myTree)
# depth=getTreeDepth(myTree)
# print(num)
# print(depth)
# createPlot(myTree)
