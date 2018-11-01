import numpy as np
from numpy import mean
a=np.array([1,2,3])#创建数组
print(a)
print(type(a))
print(a.shape)
a=a.reshape((1,-1))#重新定义数组，-1代表3
print(a.shape)
b=np.array([1,2,3,4,5,6])
print(b.shape)
b=b.reshape((2,-1))
print(b.shape)
print(b)
b=b.reshape(-1,2)
print(b)
b[2,0]=55#给数组的某一元素赋值
print(b)
c=np.zeros([3,3])#创建全为0的数组
print(c)
c=np.ones((2,3))#创建全为1的数组
print(c)
c=np.full((3,3),2)#创建全为x的数组
print(c)
d=np.eye(3)#创建对角矩阵，对角为1
print(d)
e=np.random.random((3,4))#创建元素为0-1的随机数组
print(e)
f=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(f)
g=f[1:,1:3]
print(g)
f[range(2),1]+=10
print(f)
h=f>10
print(h)
print(f[h])
i=np.array([1,2])
print(i.dtype)
i=np.array([2.2,32.1])
print(i.dtype)
j=np.array(i,dtype=np.int64)
print(j)
print(np.random.uniform(3,4))#3-4的随机数
print(np.random.uniform(1,100))
a=np.array([[1,2],[3,4]])
print(np.tile(a, (1,2)))#横向为a的一倍，纵向为a的两倍
print(np.tile(a,(2,1)))
a=np.array([[5,3,2,5],[6,3,2,4]])
print(a.argsort())#按行排序
print(a.argsort(axis=0))#按列排序
print(a.T)#转置
print(np.transpose(a))#转置
a=np.array([1,2,3,4,5])
print(np.mean(a))#求平均值