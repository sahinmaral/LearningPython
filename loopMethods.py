
for item in range(10,90,2):
    print(item)

listExample = list(range(10,90,2))
print(listExample)

greeting = 'Hello there'

for index,letter in enumerate(greeting):
    print(f'index : {index} , letter : {letter}')

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

print(list(zip(list1,list2)))

numbers = [x for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x % 2 == 0]
print(numbers)

years = [1983,1999,2008,1956,1986]

ages = [2019-year for year in years]

numbers = [(x,y) for x in range(3) for y in range(3)]