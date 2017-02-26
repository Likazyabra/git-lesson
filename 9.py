def this_is_palindrome(a):
    kol = int(len(a) / 2)
    if a[:kol] == a[::-1][:kol:]:
        return True
    else:
        return False


if this_is_palindrome(input('Введите строку для проверки: ')):
    print('Это палиндром')
else:
    print('Это не палиндром')