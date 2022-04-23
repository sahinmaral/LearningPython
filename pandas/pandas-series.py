import pandas as pd

numbers = [20,30,40,50]
letters = ['a','b','c','d']

# pandas_series = pd.Series(numbers)
pandas_series = pd.Series(letters)

# values - keys
pandas_series = pd.Series(numbers,letters)

print(pandas_series['a'],pandas_series[0])

print(pandas_series)

print(pandas_series.sum())