plates = int(input('Количество тарелок: '))
fairy = float(input('Количество моющего средства: '))

sum_plates = 0

while plates > 0 or fairy > 0:
    if plates == 0:
        print('\nВымыто тарелок: {} шт \nОсталось моющего средства: {} мл'.format(sum_plates, fairy))
        break
    elif fairy == 0:
        print('\nМоющее средство закончилось. Осталось тарелок: {} шт'.format(plates))
        break

    plates -= 1
    fairy -= 0.5
    sum_plates +=1

    print('Осталось {} мл моющего средства'.format(fairy))