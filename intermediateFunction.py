number = 'test'

try:
    if not isinstance(number,int):
        raise TypeError('number must be integer')
except Exception as exception:
    print(exception)


def usAlma(number):
    def inner(power):
        return number ** power

    return inner

two = usAlma(2)
print(two(3))

# Ozellikle AOP mimarisinde kullanilir.
def myDecorator(func):
    def wrapper(name):
        print('before function')
        func(name)
        print('after function')
    return wrapper

# def sayHello():
#     print('hello')

# say_Hello = myDecorator(sayHello)
# say_Hello()

@myDecorator
def sayHello(name):
    print(f'hello {name}')

sayHello('ali')