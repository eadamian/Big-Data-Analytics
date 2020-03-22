"""Avocado Pricing"""

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
uploaded = files.upload()

# uploading file
df = pd.read_csv("avocado.csv")

"""## ***What are the first 15 inputs of the data set?***"""

df.head(15)

"""## ***What is the mean of the 'total volume' column (data set)?***"""

df.groupby('region')[['Total Volume']].mean()

"""## ***What is the mean of the 'total volume' column (bar plot)?***"""

df1 = df.groupby('region')['Total Volume'].mean()
df1.drop(["TotalUS"], axis = 0, inplace = True) 
df1.plot(kind = 'bar',figsize = (15, 15))

"""## ***What is the standard deviation of the 'XLarge Bags' column (data set)?***"""

df.groupby('region')[['XLarge Bags']].std().sort_values(by = 'XLarge Bags', ascending = False)

"""## ***What is the standard deviation of the 'XLarge Bags' column (line plot)?***"""

df.groupby('region')['XLarge Bags'].std().plot(x = 'region',y = "number of XLarge Bags", figsize = (15, 15))

"""## ***Which 5 regions currently sells the most amount of avocados?***"""

df1 = df.groupby('region')[['Total Volume']].sum().sort_values(by = 'Total Volume', ascending = False)
df1.head(5)

"""## ***Is average pricing higher with “conventional” or “organic” type?***"""

df.groupby('type')[['AveragePrice']].mean()

"""## ***Has consumerism for avocados increased, decreased, or stayed the same (2015 and 2018- data set)***"""

df.sort_values(by='Date', ascending = True)

"""## ***Has consumerism for avocados increased, decreased, or stayed the same (2015- bar plot)***"""

df2 = df[['Date', 'Total Volume']].head(10)
plt.figure(figsize=(5, 10))
sns.barplot(x = 'Total Volume', y = 'Date', data = df2)

"""## ***Has consumerism for avocados increased, decreased, or stayed the same (2018- bar plot)***"""

df2 = df[['Date', 'Total Volume']].tail(10)
plt.figure(figsize=(5, 10))
sns.barplot(x = 'Total Volume', y = 'Date', data = df2)

"""## ***What is the average price of avocados in each region?***"""

df.groupby('region')[['AveragePrice']].mean().sort_values(by = 'AveragePrice', ascending = True)

"""## ***Do consumers purchase more avocados in small bags or large bags?***"""

df.groupby('type')[['Small Bags', 'Large Bags']].sum()

"""## ***From all avocados produced, how many are small, medium, or large?***
## ***NOTE: 4046 = small, 4225 = medium, 4770 = large***
"""

df2 = df.groupby(['region'])['4046', '4225', '4770'].sum()
df2.drop(['TotalUS'], axis = 0, inplace = True)
df2.plot(kind = 'bar', stacked = True, figsize = (15, 20))

"""## ***How have the sizes of small avocados changed between 2015 and 2018 in the US?***"""

df.groupby('year')['4046'].mean().plot(kind = 'pie', subplots = True)

"""## ***How have the sizes of medium avocados changed between 2015 and 2018 in the US?***"""

df.groupby('year')['4225'].mean().plot(kind = 'pie', subplots = True)

"""## ***How have the sizes of large avocados changed between 2015 and 2018 in the US?***"""

df.groupby('year')['4770'].mean().plot(kind = 'pie', subplots = True)
