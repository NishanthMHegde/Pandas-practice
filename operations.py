import numpy as np 
import pandas as pd

data = {'col1': [23, 25 ,99 , 23],
		'col2': [45, 47, 47, 38],
		'col3':['A', 'B', 'C', 'B']}

df = pd.DataFrame(data)

print(df.head())
print("\n\n")
#unique values in column1
print("unique values in column1")
print(df['col1'].unique())
print("\n\n")
#number of unique values in column2
print("number of unique values in column2")
print(len(df['col2'].unique()))
print("\n\n")
print("\n\n")
#number of unique values in column3 using nunique
print("number of unique values in column3 using nunique")
print(df['col3'].nunique())
print("\n\n")

#sort the dataframe by column1. Here all rows are shuffled and arranged in ascending order of column1
print("sort the dataframe by column1. Here all rows are shuffled and arranged in ascending order of column1")
print(df.sort_values(by='col1'))
print("\n\n")

#count the number of times each value occurs in col3
print("count the number of times each value occurs in col3")
print(df['col3'].value_counts())
print("\n\n")

#applying functions using apply() method
print("applying functions using apply() method")
def times2(x):
	return x*2

print(df['col1'].apply(times2))
print("\n\n")
print(df['col2'].apply(lambda x: x*2))
print("\n\n")
print(df['col3'].apply(len))
print("\n\n")