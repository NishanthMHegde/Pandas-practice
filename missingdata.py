import numpy as np 
import pandas as pd

data = {'A': [1, 2, 3], 'B': [5, 6, np.nan], 'C': [7, np.nan, np.nan]}
df = pd.DataFrame(data)
print(df)
print("\n\n")

#dropna() drops all rows having one or more na
print("dropna() drops all rows having one or more na")
print(df.dropna())
print("\n\n")

#dropna(axis=1) drops all columns having one or more na
print("dropna(axis=1) drops all columns having one or more na")
print(df.dropna(axis=1))
print("\n\n")
#dropna(thresh=xyz) drops all rows not having at least threshold amount of non na values
print("dropna(thresh=xyz) drops all rows not having at least threshold amount of non na values")
print(df.dropna(thresh=1))
print("\n\n")
#dropna(thresh=xyz) drops all rows not having at least threshold amount of non na values
print("dropna(thresh=xyz) drops all rows not having at least threshold amount of non na values")
print(df.dropna(thresh=2))
print("\n\n")
#dropna(axis=1, thresh=xyz) drops all columns not having at least threshold amount of non na values
print("dropna(axis=1, thresh=xyz) drops all columns not having at least threshold amount of non na values")
print(df.dropna(axis=1, thresh=1))
print("\n\n")
print("dropna(axis=1, thresh=xyz) drops all columns not having at least threshold amount of non na values")
#dropna(axis=1, thresh=xyz) drops all columns not having at least threshold amount of non na values
print(df.dropna(axis=1, thresh=2))
print("\n\n")

#fillna() is used to fill all NAN with a given value
print("fillna() is used to fill all NAN with a given value")
print(df.fillna(value='CUSTOM VALUE'))
print("\n\n")
#df[column name].fillna() is used to fill all NAN belonging to a column with a given value
print("df[column name].fillna() is used to fill all NAN belonging to a column with a given value")
print(df['C'].fillna(value='CUSTOM VALUE'))
print("\n\n")

#filling the mean value of the column
print("filling the mean value of the column")
print(df['C'].fillna(value=df['C'].mean()))
print("\n\n")