import sys
from diary_case import storage


conn = storage.connect()
storage.initialize(conn)

def show_tasklist():
    tasks = storage.find_all(conn)

    for task in tasks:
        storage.print_task(task)


def add_task():
    print('\nСоздана задача с номером {}'.format(storage.add_task(conn)))


def edit_task():
    print('\nЗадача номер {} отредактирована'.format(storage.edit_task(conn)))


def delete_task():
    print('Уделана задача с номером {}'.format(delete_task))


def close_task():
    storage.close_task(conn)


def open_task():
     storage.open_task(conn)


def action_show_menu():
    print('''
Ежедневник

    1. Вывести список задач
    2. Добавить задачу
    3. Отредактировать задачу
    4. Удалить задачу
    5. Завершить задачу
    6. Начать задачу сначала
    m. Показать меню
    q. Выйти
    ''')


def  action_exit():
    sys.exit(0)


actions = {
    '1': show_tasklist,
    '2': add_task,
    '3': edit_task,
    '4': delete_task,
    '5': close_task,
    '6': open_task,
    'm': action_show_menu,
    'q': action_exit
    }

if __name__== '__main__':
    action_show_menu()

    while True:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команда')
