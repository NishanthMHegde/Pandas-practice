import numpy as np 
import pandas as pd
np.random.seed(0)
df = pd.DataFrame(np.random.randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['P', 'Q', 'R', 'S'])
print(df)
print("\n\n")

#conditional selection of rows
print("conditional selection of rows")
boolres = df['Q'] > 0
print(boolres)

print(df[boolres])
print("\n\n")

#another method
print(df[df['Q'] > 0])
print("\n\n")
#using AND operation using & symbol for comparing series
print("using AND operation using & symbol for comparing series")
print(df[(df['Q'] > 0) & (df['P'] <0)])
print("\n\n")
#using AND operation using & symbol for comparing series
print("using OR operation using | symbol for comparing series")
print((df[(df['Q'] > 0) | (df['P'] > 1)]))
print("\n\n")

#selecting columns after conditional selection
print("selecting columns after conditional selection")
resultdf = df[(df['Q'] > 0) & (df['P'] <0)]
resultdf = resultdf[['P', 'Q', 'R']]
print(resultdf)
print("\n\n")
#resetting index outofplace
print("resetting index outofplace. Will create a new column which is the index")
print(df.reset_index())
print("\n\n")
#setting new indice
print("setting new indice. This will convert a column to an index")
states = "KA AP TN KL MH".split()
#create a column to set it as index
df['states'] = states
print(df.set_index('states'))