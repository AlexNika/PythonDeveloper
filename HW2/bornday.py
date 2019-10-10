# МОДУЛЬ 3

birthyear = 1799
birthday = 26

asp_birthyear = input('Введите ГОД рождения А.С Пушкина: ')
if asp_birthyear.isdigit() and int(asp_birthyear) == birthyear:
    asp_birthday = input('Введите ДЕНЬ рождения А.С Пушкина: ')
    if asp_birthday.isdigit() and int(asp_birthday) == birthday:
        print('Верно')
    else:
        print('Неверный ДЕНЬ рождения')
else:
    print('Неверный ГОД рождения')
