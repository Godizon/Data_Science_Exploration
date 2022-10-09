import pandas as pd

#type you code here :)

df = pd.read_csv('data.csv')

print(df.to_string()) 

print(df.head(3)) #prints the first 3 rows of the dataset
print(df.tail(3)) #prints the last 3 rows of the dataset
print(df) #prints the entire dataset
