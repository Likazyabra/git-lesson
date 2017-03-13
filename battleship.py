'''Классический морской бой, это поле 10х10 клеток
На этом поле можно разместить 1 четырехпалубник
2 трехпалубника
3 двухпалубника
4 однопалубных
корабли нельзя ставить диагонально или квадратиком
только по горизонтали или по вертикали
так же корабли не должны соприкасаться'''
import random

class Battlefield:
    size = 10 # размер поля 10 X 10
    ship_amount = 10 # Количество кораблей, может и не надо
    max_point = 5

    ship_list = [] # Список кораблей,  может быть список из объектов?



    def add_ships(self): # добавляем корабли

        '''
        Можно при расстановке бронировать не только координаты коробля, но и помечать соседние точки вокруг корабля как занятые
        '''

        all_points = [i for i in range(1, self.size ** 2 + 1, 1)]
        print(all_points)



        amount = self.max_point

        for deck in range(1, self.max_point, 1):
            print('Количество палуб {}'.format(deck))
            for ship in range(1, amount, 1):
                print(random.randint(1, 100)) # только числа должны быть из списка all_points
                # и удалять из этого списка забронированные и соседние
            amount -= 1



    def fire(self, coordinate): #стреляем
       # если попали, то записываем в dead_points и ставим flag если убили
       # и удалить из списка кораблей ship_list
        pass



class Ship:

    flag = False # True  - убит
    dead_points = [] # куда уже попадали

    def __init__(self, size, points):
        self.size = size # количество клеток
        self.points = points # зарезервированные клетки
    pass


battlefield = Battlefield()
battlefield.add_ships()

