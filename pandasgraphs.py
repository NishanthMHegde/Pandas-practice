import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df1 = pd.read_csv('df1.csv', index_col=0)
df2 = pd.read_csv('df2.csv')

#df1
print("df1")
print(df1.head())
print("\n\n")

#plotting a histogram
print("plotting a histogram")
df1['A'].hist(bins=50)
plt.show()
print("\n\n")

#another way of plotting a histogram
print("another way of plotting a histogram")
df1['B'].plot(kind='hist', bins=50)
plt.show()
print("\n\n")

#yet another way of plotting a histogram
print("yet another way of plotting a histogram")
df1['C'].plot.hist(bins=60)
plt.show()
print("\n\n")

#bar graph 
print("bar graph")
df2.plot.bar()
plt.show()
print("\n\n")

#stacked bar graph 
print("stacked bar graph")
df2.plot.bar(stacked=True)
plt.show()
print("\n\n")

#line graph 
print("line graph")
df2.plot.line(figsize=(10,5))
plt.show()
print("\n\n")

#area graph 
print("area graph")
df2.plot.area(alpha=0.75)
plt.show()
print("\n\n")

#scatter graph 
print("scatter graph")
df2.plot.scatter(x='a', y='b',  s = df2['c'])
plt.show()
print("\n\n")