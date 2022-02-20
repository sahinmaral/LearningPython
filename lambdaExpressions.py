def square(num): return num ** 2

numbers = [1,3,5,7,2,4]

# map sonucu map object dondurur

result = list(map(square,numbers))
result2 = list(map(lambda num:num ** 2,numbers))

squareLambda = lambda num: num ** 2

print(result)
print(result2)

for number in result:
    print(number)

def checkEven(number): return number % 2 == 0

checkEvenLambda = lambda num: num % 2 == 0

result3 = list(filter(checkEven,numbers))
result4 = list(filter(checkEvenLambda,numbers))

print(result3)
print(result4)

testNumber = 50

def globalValueChange():
    global testNumber

    print(f'testNumber : {testNumber}')

    testNumber = 100

    print(f'Changed testNumber to 100 : {testNumber}')

globalValueChange()
print(testNumber)