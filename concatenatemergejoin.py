import numpy as np 
import pandas as pd

data = {'A': ['A0', 'A1', 'A2', 'A3'],
		'B': ['B0', 'B1', 'B2', 'B3'],
		'C': ['C0', 'C1', 'C2', 'C3']}

df1 = pd.DataFrame(data=data, index = [0, 1, 2, 3])
df2 = pd.DataFrame(data=data, index = [4, 5, 6, 7])
df3 = pd.DataFrame(data=data, index = [8, 9, 10, 11])

#concatenate is used to join dataframes provided they have the same dimensions across the axis on which they are joined
print("concatenate is used to join dataframes provided they have the same dimensions across the axis on which they are joined")
#Joining via rows (ensure the number/name of columns are similar)
print("Joining via rows (ensure the number/name of columns are similar)")
print(pd.concat([df1, df2, df3]))
print("\n\n")
#Joining via columns (ensure the number of row indices are same Otherwise NaN will be logged.
print("Joining via columns (ensure the number of row indices are same Otherwise NaN will be logged.")
print(pd.concat([df1, df2, df3], axis=1))
print("\n\n")

#merge is used to join two tables based on one or more key columns
print("merge is used to join two more tables based on one or more key columns")

data1 = {'A': ['A0', 'A1', 'A2', 'A3'],
		'B': ['B0', 'B1', 'B2', 'B3'],
		'key': ['K0', 'K1', 'K2', 'K3']}
data2 = {'A': ['A4', 'A5', 'A6', 'A7'],
		'B': ['B4', 'B5', 'B6', 'B7'],
		'key': ['K0', 'K1', 'K2', 'K3']}

left = pd.DataFrame(data=data1)
right = pd.DataFrame(data=data2)

#simple left join on key
print("simple left merge on key")
print(pd.merge(left, right, on = 'key', how='left'))
print("\n\n")
#simple right join on key
print("simple right merge on key")
print(pd.merge(left, right, on = 'key', how='right'))
print("\n\n")
#simple inner join on key
print("simple inner merge on key")
print(pd.merge(left, right, on = 'key', how='inner'))
print("\n\n")
#simple outer join on key
print("simple outer merge on key")
print(pd.merge(left, right, on = 'key', how='outer'))
print("\n\n")
#merge using multiple keys
print("merge using multiple keys")

data1 = {'A': ['A0', 'A1', 'A2', 'A3'],
		'B': ['B0', 'B1', 'B2', 'B3'],
		'key1': ['K0', 'K1', 'K2', 'K3'],
		'key2': ['K0', 'K1', 'K2', 'K3']}
data2 = {'A': ['A4', 'A5', 'A6', 'A7'],
		'B': ['B4', 'B5', 'B6', 'B7'],
		'key1': ['K0', 'K0', 'K2', 'K3'],
		'key2': ['K0', 'K0', 'K2', 'K3']}

left = pd.DataFrame(data=data1)
right = pd.DataFrame(data=data2)

#simple left join on key
print("simple left merge on key")
print(pd.merge(left, right, on = ['key1', 'key2'], how='left'))
print("\n\n")
#simple right join on key
print("simple right merge on key")
print(pd.merge(left, right, on = ['key1', 'key2'], how='right'))
print("\n\n")
#simple inner join on key
print("simple inner merge on key")
print(pd.merge(left, right, on = ['key1', 'key2'], how='inner'))
print("\n\n")
#simple outer join on key
print("simple outer merge on key")
print(pd.merge(left, right, on = ['key1', 'key2'], how='outer'))
print("\n\n")

#join is used to join two tables based on the indices and column names have to be different
print("join is used to join two tables based on the indices and column names have to be different")
data1 = {'A': ['A0', 'A1', 'A2', 'A3'],
		'B': ['B0', 'B1', 'B2', 'B3']
		}
data2 = {'C': ['C4', 'C5', 'C6', 'C7'],
		'D': ['D4', 'D5', 'D6', 'D7']}

left = pd.DataFrame(data=data1, index = ['I0', 'I1', 'I2', 'I3'])
right = pd.DataFrame(data=data2, index = ['I0', 'I1', 'I2', 'I4'])
print(left.join(right))
print("\n\n")
print(left.join(right, how = 'outer'))
print("\n\n")
print(left.join(right, how = 'inner'))
print("\n\n")
print(left.join(right, how = 'left'))
print("\n\n")
print(left.join(right, how = 'right'))
print("\n\n")