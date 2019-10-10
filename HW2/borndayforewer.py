# МОДУЛЬ 5

birthyear = 1799
birthday = 26
asp_birthyear = ''
asp_birthday = ''

while not asp_birthyear.isdigit() or int(asp_birthyear) != birthyear:
    asp_birthyear = input('Введите ГОД рождения А.С Пушкина: ')
while not asp_birthday.isdigit() or int(asp_birthday) != birthday:
    asp_birthday = input('Введите ДЕНЬ рождения А.С Пушкина: ')
print('Верно')
