def area_number(x, y):
    
    if x == 0 and y == 0:
        return '0'
    elif x == 0 or y == 0:
        return '01'
    elif x > 0 and y > 0:
        return '1'
    elif x < 0 and y > 0:
        return '2'
    elif x < 0 and y < 0:
        return '3'
    else:
        return '4'


x = int(input('Введите значение координаты х: '))
y = int(input('Введите значение координаты y: '))

area = area_number(x, y)

if area == '0':
    print('Это начало координат')
elif area == '01':
    print('Точка находится на оси координат')
else:
    print('Точка принадлежит {} четверти'.format(area))