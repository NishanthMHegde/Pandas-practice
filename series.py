import numpy as np 
import pandas as pd 

#Pandas series consists of an array of values, each one having an index. If an index is not specified, then integers ranging
#from 0 to n are used as indices.

#simple list to pandas series
print("simple list to pandas series")
my_list = [1, 2 ,3]
ser = pd.Series(my_list)
print(ser)
print("\n\n")
#numpy array to pandas series
print("numpy array to pandas series")
my_list = [1, 2 ,3]
ser = pd.Series(np.array(my_list))
print(ser)
print("\n\n")
#series with data and index
print("series with data and index")
my_list = [1, 2 ,3]
index = ['a', 'b', 'c']
ser = pd.Series(np.array(my_list), index)
print(ser)
print("\n\n")
#we can specify the data and index too
print("we can specify the data and index too")
my_list = [1, 2 ,3]
index = ['a', 'b', 'c']
ser = pd.Series(data=np.array(my_list), index=index)
print(ser)
print("\n\n")
#converting a dictionary having key and value pairs to a Series.
#here the key values are labels and values are the data
print("converting a dictionary having key and value pairs to a Series. here the key values are labels and values are the data")
d = {'a' : 100, 'b':200, 'c':300}
ser = pd.Series(d)
print(ser)
print("\n\n")

#indexing a pandas series
print("indexing a pandas series")
ser1 = pd.Series(data = [4, 5, 3, 10], index = ['USA', 'USSR', 'Russia', 'Germany'])
print(ser1)

print(ser1['USA'])
print(ser1['Germany'])
print("\n\n")
ser2 = pd.Series(data = [4, 5, 3, 10], index = ['USA', 'USSR', 'India', 'Italy'])
print(ser2)

#Adding or performing mathematical operations on Series
print("Adding or performing mathematical operations on Series")
print(ser1 + ser2)
#only index present in both the Series are added, rest are marked as NaN
print("only index present in both the Series are added, rest are marked as NaN")
print("\n\n")