# Empty cell gives the bad data
import pandas as pd

a = pd.read_csv("dirty.csv")
a[" Calories"].fillna(123,inplace = True)

print(a.to_string())
