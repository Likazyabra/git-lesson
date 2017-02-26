# Первое задание
from datetime import date

def new_year():
    today = date.today()
    next_year = date(today.year + 1, 1, 1)

    return (next_year - today).days

print('До нового года осталось {} дней'.format(new_year()))
