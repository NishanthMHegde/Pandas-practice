import numpy as np 
import pandas as pd

outside_index = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside_index = [1, 2, 3, 1 ,2 ,3]
h_index = list(zip(outside_index, inside_index))
#convert to Pandas multi level index
multi_index = pd.MultiIndex.from_tuples(h_index)

#multi level indexed dataframe
print("multi level indexed dataframe")
df = pd.DataFrame(np.random.randn(6, 2), index=multi_index, columns = ['A', 'B'])
print(df)
print("\n\n")
#selecting data row wise (outside index)
print("selecting data row wise (outside index)")
print(df.loc['G1'])
print("\n")
print(df.loc['G2'])

#selecting data row wise (inside index)
print("selecting data row wise (inside index)")
print(df.loc['G1'].loc[1])
print("\n")
print(df.loc['G2'].loc[2])
print("\n")
print(df.loc['G2'].loc[[2, 1]])
print("\n\n")
#selecting data row wise (outside index) with columns
print("selecting data row wise (outside index) with columns")
print(df.loc['G1']['A'])
print("\n")
print(df.loc['G2']['B'])
print("\n\n")
#selecting data row wise (inside index) with columns
print("selecting data row wise (inside index) with columns")
print(df.loc['G1'].loc[1]['A'])
print("\n")
print(df.loc['G2'].loc[2]['B'])
print("\n")
print(df.loc['G2'].loc[[2, 1]][['A', 'B']])
print("\n\n")

#name of the outside and inside indices
print("name of the outside and inside indices")
print(df.index.names)
print("\n\n")
#new name for indices
df.index.names = ['Group', 'Num']
print("new name for indices")
print(df.index.names)
print("\n\n")

#dataframe with new indices
print("dataframe with new indices")
print(df)
print("\n\n")
#using cross section xs to get indices
print("using cross section xs to get indices")
print(df.xs('G1'))
print("\n\n")

#getting data by using inside index match instead of outside index
print("getting data by using inside index name match instead of outside index")
print(df.xs(1, level='Num'))