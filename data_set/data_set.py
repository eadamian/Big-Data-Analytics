# python program by Eric Adamian
# pandas/numpy data application to handle a data set

from pandas import Series, DataFrame

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# reading in data set as a dataframe
df = pd.read_csv("/Users/ericadamian/Desktop/data_set/approval_polllist.csv")

# print first 50 data entries
print("")
print("")
print("First 50 data entries:")
print("___________________________________________________________")
print(df.head(50))

# print last 50 data entries
print("Last 50 data entries:")
print("___________________________________________________________")
print(df.tail(50))

# entering statistical data on approval column
approval_mean = df['approve'].mean()
approval_max = df['approve'].max()
approval_min = df['approve'].min()
approval_sum = df['approve'].sum()
approval_std = df['approve'].std()

# displaying statistical data on approval column
print("Statistical data on Trump 'approval' column:")
print("___________________________________________________________")
print('Mean approval: ' + str(approval_mean))
print('Maximum approval: ' + str(approval_max))
print('Minimum approval: ' + str(approval_min))
print('Sum approval: ' + str(approval_sum))
print('Standard deviation approval: ' + str(approval_std))
print("")

# filtering first 10 entries for a subset of rows
print("Filter for 'pollster' column on entries called 'Gallup': ")
print("(Displays first 10 entries)")
print("___________________________________________________________")
print(df[df['pollster'].str.contains("Gallup")].head(10))
print("")

# selecting a subset of columns, displaying first 10 entries for each column
print("Displaying first 10 entries for 'pollster', 'grade', and 'population' columns: ")
print("___________________________________________________________")
print(df.loc[0:9,['pollster','grade','population']])
print("")

# displaying first 50 entries with approval rates greater than 45
print("Filter approval ratings greater than 45: ")
print("(Displays first 50 entries)")
print("___________________________________________________________")
print(df[df['approve'] > 45].head(50))
print("")

# filtering missing values, displaying first 10 entries
print("Filter any missing entries: ")
print("(Displays first 10 entries)")
print("___________________________________________________________")
print(df[df.isnull().any(axis=1)].head(10))
print("")

# displaying 10 entries for changing numeric values of 'approve' column 
# before and after update
print("Display approval column multiplied by 0.10: ")
print("(Displays first 10 entries)")
print("___________________________________________________________")
print("")
print("Before update: ")
print(df.loc[0:9, ['approve']])
print("")
print("After update: ")
df_update = df.loc[0:9, ['approve']].mul(.10)
print(df_update)
print("")

# sort previous data in a certain manner
print("Sort data from previous step in ascending order: ")
print("(Displays first 10 entries)")
print("___________________________________________________________")
df_update = df_update.sort_values(by = ['approve'], ascending = [True])
print(df_update.head(10))
print("")

# group data of a column in a certain manner
print("Grouping the 'approve' column by mean: ")
print("(Displays first 10 entries)")
print("___________________________________________________________")
print(df.groupby(['approve']).mean().head(10))
