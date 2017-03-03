import sqlite3


SQL_SELECT = '''
    SELECT
        id, title, body, runtime, status
    FROM
        task
    '''


def dict_factory(cursor, row):
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    return d



def connect(db_name=None):
    if db_name is None:
        db_name = ':diary:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn



def initialize(conn):

    with conn:

        cursor = conn.executescript('''
         CREATE TABLE IF NOT EXISTS task (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            title TEXT NOT NULL ,
            body TEXT NOT NULL DEFAULT '',
            runtime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            status TEXT NOT NULL DEFAULT 'Open'
        )
        ''')


def print_task(task):
    print('{task[id]} - {task[title]} - {task[body]} - {task[runtime]} - {task[status]}'.format(task=task))



def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT)
        return cursor.fetchall()


def input_date(id=0):

    if not id:
         task = (int(input('Введите номер задачи: ')),
                input('Введите название задачи: '),
                input('Введите текст задачи: '),
                input('Введите дату и время выполнения в формате "гггг-мм-дд чч:мм" : ')
        )
    else:
        task = (int(input('Введите номер задачи: ')),
                input('Введите название задачи: '),
                input('Введите текст задачи: '),
                input('Введите дату и время выполнения в формате "гггг-мм-дд чч:мм" : '),
                id
        )

    return task


def add_task(conn):

    cursor = conn.execute('''
    INSERT INTO task (id, title, body, runtime) VALUES (?,?,?,?)
    ''', input_date())

    return cursor.lastrowid


def edit_task(conn):
    current_task = find_task_by_id(conn)
    print_task(current_task)

    conn.execute('''
    UPDATE task SET id = ?, title = ?, body = ?, runtime = ? WHERE id = ?
    ''', input_date(current_task['id']))

    print('\nЗадача отредактирована')



def delete_task(conn):

    task = find_task_by_id(conn)

    cursor = conn.execute('''
    DELETE FROM task WHERE id = ?
    ''', (task['id'],))

    print('Уделана задача с номером {}'.format(task['id']))



def close_task(conn):

    current_task = find_task_by_id(conn)
    conn.execute('''
    UPDATE task SET status = 'Close' WHERE id = ?
    ''', (current_task['id'],))

    print('\nЗадача {} закрыта'.format(current_task['id']))



def open_task(conn):

    current_task = find_task_by_id(conn)
    conn.execute('''
    UPDATE task SET status = 'Open' WHERE id = ?
    ''', (current_task['id'],))

    print('\nЗадача {} открыта'.format(current_task['id']))



def find_task_by_id(conn):

    task_id = int(input('Введине номер задачи: '))

    with conn:
        cursor = conn.execute(SQL_SELECT + ' WHERE id = ?', (task_id,))

        #if not cursor:
        #    print('Задача с номером {} не найдена'.format(task_id))
        #else:
        return cursor.fetchone()





