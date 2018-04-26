'''
Created on 24-Apr-2018

@author: Appu
'''
x = 3;
print(type(x))
print(x)
print(x**3)

t= True
f = False

print(type(t))
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = sb.load_dataset('iris')
sb.distplot(df['petal_length'],kde = False)
plt.show()