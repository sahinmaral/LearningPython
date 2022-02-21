try:
    x = int(input('x : '))
    y = int(input('y : '))
    print(x/y)
except(ZeroDivisionError):
    print('Sayi , sifira bolunemez')
except(ValueError) as valueError:
    print(f'Tip donusturmede hata , {str(valueError)}')
else:
    print('Exception kismina dusmezse calisacak kisim')
finally:
    print('finally')


