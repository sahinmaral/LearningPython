import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=['Column1','Column2','Column3','Column4','Column5'])

result = df
result = df.columns
result = df.head(5)
result = df.tail() # default => 5
result = df['Column1'].head()
result = df.Column1.head()

result = df[df > 50]

result = df.query('Column1 >= 50 & Column1 % 2 == 0')

print(result)