# -*- coding= utf-8 -*-
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import matplotlib
from numpy.core.fromnumeric import size
from matplotlib.font_manager import FontProperties
data=pd.read_csv("D:/data/electric.csv")
print(data)
# print(data.head(5))
sum=data.sum()
print(sum)
ind=np.arange(3)
x=[u'用户1',u'用户2',u'用户3']
width=0.35
print(ind)
zh_font = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\STKAITI.TTF')
plt.bar(ind, sum, width,label='sum num')
plt.rc('font',family="SimHei",size=13)
plt.xlabel(u"用户名",fontproperties=zh_font)
plt.ylabel(u"总耗电量",fontproperties=zh_font)
plt.title(u"电力窃漏电用户自动识别--总耗电量",FontProperties=zh_font)
plt.legend()
plt.xticks(ind,x,fontproperties=zh_font,rotation=40)
plt.show()
# print(data.sum())
# print(data.mean())
# print(data.describe())

# a=Series([3,5,2,5])
# print(a)
# b=Series([3,5,2,5],index=['d','b','a','c'])
# print(b)
# c={'Ohio':35000,'Tetas':42456,'Oregon':24422,'Utah':24363}
# d=Series(c)
# print(d)
# states=['Califoria','Oregon','Utah','Ohio','Tetas']
# e=Series(d,states)
# print(e)
# print(pd.isnull(data))
