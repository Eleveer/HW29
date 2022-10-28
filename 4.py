print('Введите два числа: ')
x = float(input())
y = float(input())
while y != 0:
    print(x+y, x-y, x*y, x/y, sep='\n')
    print('','Введите два числа: ', sep='\n')
    x = float(input())
    y = float(input())
if y == 0:
    print('На ноль делить нельзя!')
    
    
    
