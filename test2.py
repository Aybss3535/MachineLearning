#-*- coding=utf-8 -*-
'''
Created on 2018年11月17日

@author: songxuan
'''
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import lineStyles
from matplotlib.patches import ArrowStyle
plt.figure(1)
x=np.linspace(-np.pi, np.pi, 365, endpoint=True)
c,s=np.cos(x),np.sin(x)
plt.plot(x,c,color="blue",linewidth=1.0,linestyle="-",label="cos",alpha=0.5)#aplha透明度
plt.plot(x,s,"ro",label="sin",linewidth=1.0)
plt.title("cos&sin")
ax=plt.gca()#坐标轴操作
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi])
plt.yticks(np.linspace(-1,1,5))
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor="white",edgecolor="None",alpha=0.2))#坐标数字的背景
plt.legend(loc="upper left")
plt.grid()
# plt.axis([-1,1,-0.5,0.5])#设置显示范围
# plt.fill_between(x, np.abs(x)>0.5, c,c>0.5, color="green",alpha=0.5)#填充
t=1
plt.plot([t,t],[0,np.cos(t)],color="y",linestyle="--")
plt.annotate("cos(1)",xy=[t,np.cos(t)],xycoords="data",xytext=(+10,+30)
             ,textcoords="offset points",arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=0.2"))
plt.show()

