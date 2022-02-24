liste = [1,2,3,4,5]

iterator = iter(liste)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))

def cube(start,stop):
    for i in range(start,stop):
        yield i ** 3
    
cubeGenerator = cube(2,10)
print(cubeGenerator)
print(next(cubeGenerator))
print(next(cubeGenerator))
print(next(cubeGenerator))
print(next(cubeGenerator))
print(next(cubeGenerator))
