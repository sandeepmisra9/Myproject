import pandas as pd
data = {
  'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
  'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
  'Manchester', 'Cairo', 'Osaka'],
  'gender' : ['M', 'F', 'F', 'M', 'M', 'F', 'F'],
  'Jersey size' : ['L', 'P', 'L', 'XL', 'M', 'S', 'XL'],
  'meal' : ['veg', 'vegan', 'g free', 'non veg', 'salads', 'veg', 'non veg'],
  'age': [41, 28, 33, 34, 38, 31, 37],
  'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0] }

row_labels = [101, 102, 103, 104, 105, 106, 107]
# how to convert a data frame
df = pd.DataFrame(data=data, index=row_labels)
#print(df)
header = df.head(n=2)
print (header)
header = df.tail(n=2)
print (header)
cities = df['city']
print (cities)
header = df.city
# print (header)
#header = df.city[102]
# print (header)
header = cities[102]
print (header)
header = df.loc[103]
print (header)
import numpy as np
d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}
# print (pd.DataFrame(d))
l = [{'x': 1, 'y': 2, 'z': 100},
{'x': 2, 'y': 4, 'z': 100},
{'x': 3, 'y': 8, 'z': 100}]
print ('now printing l\n',pd.DataFrame(l))









