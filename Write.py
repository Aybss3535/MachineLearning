# -*- coding=utf-8 -*-
import random
import os
file=open("D:/data/randomData.txt","w")
for i in range(80):
    x=random.random()*10
    y=random.random()*10
    file.write(str(x))
    file.write("\t")
    file.write(str(y))
    file.write("\n")
print("随机数生成完成")