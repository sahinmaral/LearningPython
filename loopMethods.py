
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