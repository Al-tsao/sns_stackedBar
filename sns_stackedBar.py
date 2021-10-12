#Standard

import numpy as np

import pandas as pd

from numpy.random import randn

from pandas import Series, DataFrame

#Stats

from scipy import stats

#Matplotlib

import matplotlib as mpl

import matplotlib.pyplot as plt

#Seaborn

import seaborn as sns

#Draw

sns.set() #設定繪圖改為seaborn繪製

df = pd.DataFrame({ "ProductA": [5,5,5,5,5],
                    "ProductB": [6,6,6,6,6],
                    "ProductC": [7,7,7,7,7]}
                    , index=['day1','day2','day3','day4','day5'])

df.plot(kind='bar', stacked=True)

plt.xlabel('this is x')

plt.ylabel('this is y')

plt.title('this is a demo')

plt.legend(loc='upper right')

plt.show() #繪圖