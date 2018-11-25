#-*- coding=utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
#散点图
ax=fig.add_subplot(3,3,1)
n=128
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
T=np.arctan2(x,y)
# plt.axes([0.1,0.1,0.80,0.80])#设置外边的那个框
ax.scatter(x, y, s=75, c=T, alpha=0.25)#s大小c颜色
plt.xlim(-1.5,1.5)#设置x轴刻度的取值范围
plt.xticks(np.linspace(-1.5, 1.5, 5, endpoint=True))#设置x轴刻度的表现方式
plt.ylim(-1.5,1.5)#设置y轴刻度的取值范围
plt.yticks(np.linspace(-1.5, 1.5, 5, endpoint=True))
plt.axis()
plt.xlabel("x")
plt.ylabel("y")
plt.title("scatter")
#柱状图
ax=fig.add_subplot(3,3,2)
n=10
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
ax.bar(X,+Y1,facecolor="#9999ff",edgecolor="white")
ax.bar(X,-Y2,facecolor="#ff9999",edgecolor="white")
for x,y in zip(X,Y1):
    plt.text(x, y+0.05, "%.2f"%y, ha="center", va="bottom")
for x,y in zip(X,Y2):
    plt.text(x,-y-0.05,"%.2f"%y,ha="center",va="top")
#饼图
ax=fig.add_subplot(3,3,3)
n=20
Z=np.ones(n)
Z[-1]*=2
ax.pie(Z, explode=Z*0.05, labels=["%.2f"%(i/float(n)) for i in Z], 
        colors=["%.2f"%(i/float(n)) for i in range(n)])
plt.gca().set_aspect("equal")#使饼图变圆
plt.xticks([]),plt.yticks([])
#极坐标图
ax=fig.add_subplot(334,polar=True)
n=20
theta=np.arange(0.0,2*np.pi,2*np.pi/n)
rad=10*np.random.rand(n)
plt.plot(theta,rad)
#热图
ax=fig.add_subplot(335)
from matplotlib import cm
data=np.random.rand(3,3)
cmap=cm.get_cmap("rainbow", 100)
map=plt.imshow(data, cmap=cmap, aspect="auto", interpolation="nearest", vmin=0, vmax=1)
#3D图
from mpl_toolkits.mplot3d import axes3d
ax=fig.add_subplot(336,projection="3d")
ax.scatter(1,1,3,s=100)
#热力图
ax=fig.add_subplot(3,1,3)
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
X,Y=np.meshgrid(x,y)
plt.contourf(X,Y,f(X,Y),8,alpha=.75,cmap=plt.cm.get_cmap("hot", 1000))
plt.savefig("./fig.png")
plt.show()




