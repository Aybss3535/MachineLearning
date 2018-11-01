# -*- coding=utf-8 -*-
import pandas as pd
df=pd.read_csv("D:/data/train.csv")
label=df['TARGET']
df=df.drop(['ID','TARGET'],axis=1)
print(df)