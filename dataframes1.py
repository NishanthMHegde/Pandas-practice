import numpy as np 
import pandas as pd

#A dataframe is a colletion of Series. Each series is a column  and multiple columns put together form a dataframe which is indexed.
print("A dataframe is a colletion of Series. Each series is a column  and multiple columns put together form a dataframe which is indexed.")
#pd.DataFrame(array/matrix of rows and columns, row_index, column names)
#let us seed a random
np.random.seed(0)
df = pd.DataFrame(np.random.randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['P', 'Q', 'R', 'S'])
print(df)
print("\n\n")

#another way
df = pd.DataFrame(data=np.random.randn(5, 4), index=['A', 'B', 'C', 'D', 'E'], columns=['P', 'Q', 'R', 'S'])
print(df)
print("\n\n")



#selecting a column. 
print("selecting a column")

print(df['P'])
print(df['Q'])
print(df['R'])
print("\n\n")

#Selecting multiple columns
print("Selecting multiple columns")
print(df[['P', 'Q']])
print(df[['R', 'S']])
print("\n\n")
#selecting a row using row name
print("selecting a row using row name")
print(df.loc['A'])
print(df.loc['B'])
print(df.loc['E'])
print("\n\n")

#selecting a row using row index
print("selecting a row using row index")
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])
print("\n\n")

#selecting a subset of a dataframe (single value subset)
print("selecting a subset of a dataframe (single value subset)")
print(df.loc['B', 'Q'])
print(df.loc['D', 'P'])
print("\n\n")
#selecting a subset of a dataframe 
print("selecting a subset of a dataframe")
print(df.loc[['B', 'A'], ['Q', 'P']])
print(df.loc[['C', 'D'], ['S', 'R']])
print("\n\n")

#creating a new column
print("creating a new column")

df['new'] = df['P'] + df['Q']
print(df)
print("\n\n")
#dropping a column.Mention axis=1, as df.shape gives (row, column) and column belongs to second value in tuple
print("dropping a column.Mention axis=1, as df.shape gives (row, column) and column belongs to second value in tuple")
df.drop('new', axis=1)
print(df)
print("\n\n")
#we can see the new column is not dropped as the drop was not inplace.
print("we can see the new column is not dropped as the drop was not inplace.")
#inplace drop
print("inplace drop")
df.drop('new', axis=1, inplace=True)
print(df)
print("\n\n")