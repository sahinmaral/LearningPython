import pandas as pd

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples=s1,oranges=s2)

# df = pd.DataFrame(data)

list = [['Ahmet',50],['Ali',60],['Yagmur',70],['Sahin',100]]
dict = {'Name':['Ahmet','Ali','Yagmur','Sahin'],'Grade':[50,60,70,80]}

# df = pd.DataFrame(list,columns=['Name','Grade'])
df = pd.DataFrame(dict)

print(df)