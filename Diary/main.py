import sys
from diary_case import storage


conn = storage.connect()
storage.initialize(conn)

def show_tasklist():
    tasks = storage.find_all(conn)

    for task in tasks:
        storage.print_task(task)

# декоратор
def print_message(func):
    def wrapper(*args, **kwargs):
        result = func()
        print('{} задача с номером {}'.format(result[0], result[1]))
    return wrapper

@print_message
def add_task():
    return 'Добавлена', storage.add_task(conn)

@print_message
def edit_task():
    return 'Отредактирована', storage.edit_task(conn)


@print_message
def delete_task():
    return 'Удалена', storage.delete_task(conn)

@print_message
def close_task():
    return 'Закрыта', storage.close_task(conn)

@print_message
def open_task():
    return 'Открыта', storage.open_task(conn)


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
    conn.close()
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
