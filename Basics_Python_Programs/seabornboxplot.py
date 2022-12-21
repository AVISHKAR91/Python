# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 16:16:00 2021

@author: anilk
"""

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



import seaborn as sns
# Load the data

titanic = sns.load_dataset("titanic")

#sns.boxplot(x='day',y='total_bill',data=tips)
sns.boxplot(x='sex',y='tip',data=titanic)
plt.show()

titanic.info()

y=titanic[['sex']].value_counts()
print(y.index)
x=y.index.map(lambda x:x[0])
plt.bar(x,y)
plt.show()



sns.countplot(x="sex",data=titanic)
plt.show()


sns.countplot(x="day",hue="sex",data=titanic)
plt.show()

sns.distplot(x=titanic['titanic'],kde=True,color="darkred",bins=30)

sns.heatmap(titanic.isnull(),yticklabels=False,cmap="viridis")
  


