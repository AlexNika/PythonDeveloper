# МОДУЛЬ 4

birthyear = 1799
asp_birthyear = ''

while not asp_birthyear.isdigit() or int(asp_birthyear) != birthyear:
    asp_birthyear = input('Введите год рождения А.С Пушкина: ')

print('Верно')
