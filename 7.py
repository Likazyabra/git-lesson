# не делала проверки, так что вводить числа нужно сознательно )

def func_perevod(num, sist):

    if sist == 10:
        print('Число {} в десятичной системе = {} '.format(num, func_decimal(str(num))))
    elif sist == 2:
        print('Число {} в двоичной системе = {} '.format(num, func_binary(num)))
    else:
        print('Вы ввели неверную систему')


def func_decimal(num):

    num_dec = 0
    rate = len(num) - 1
    for i in num:
        num_dec += int(i) * 2**rate
        rate -=1
    return num_dec


def func_binary(num):
    num_bin = ''
    i = num

    while i > 0:
        num_bin += str(int(i) % 2)
        i = int(i / 2)
    return num_bin[::-1]



num = int(input('Введите число: '))
sist = int(input('Введите систему измерения (2 - двоичная, 10 - десятеричная): '))

func_perevod(num, sist)