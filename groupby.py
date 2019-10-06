import numpy as np 
import pandas as pd

data = {'Company': ['AKAM', 'AKAM', 'MS', 'MS', 'VMW', 'VMW', 'GL', 'GL'], 
		'Sales Person': ['Nishanth', 'Jadeja', 'Kohli', 'Rohit', 'Ashwin', 'Pujara', 'Patel', 'Lee'],
		'Amount': [98, 110, 130, 87, 96, 78, 111, 94]}


df = pd.DataFrame(data)

#min, max, mean, std all automatically take in the column with the numerical values
print("min, max, mean, std all automatically take in the column with the numerical values")
print("mean")
print(df.groupby('Company').mean())
print("\n\n")
print("count")
print(df.groupby('Company').count())
print("\n\n")
print("min")
print(df.groupby('Company').min())
print("\n\n")
print("max")
print(df.groupby('Company').max())
print("\n\n")
print("std")
print(df.groupby('Company').std())
print("\n\n")
print("count() with loc")
print(df.groupby('Company').count().loc['AKAM'])
print("\n\n")
print("count() with loc")
print(df.groupby('Company').count().loc[['AKAM', 'MS']])
print("\n\n")
print("describe()")
print(df.groupby('Company').describe())
print("\n\n")
print("describe().transpose()")
print(df.groupby('Company').describe().transpose())
print("\n\n")
print(df.groupby('Company').describe().transpose()['VMW'])
print("\n\n")