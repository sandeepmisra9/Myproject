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
print(df)
df.head(n=2)
