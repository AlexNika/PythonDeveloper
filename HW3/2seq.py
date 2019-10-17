# Модуль 2

separators = [',', ';', '/']
my_list = input(f'Введите цифры. Разделитель может быть любым из списка {separators}: ')
sep = False
# Проверка на наличие правильного сепаратора
for s in separators:
    if s in my_list:
        sep = True
        my_list = list(map(int, my_list.split(sep=s)))
        break
if not sep:
    print('Вы ввели список цифр, разделенных неизвестным для программы разделителем')
    print('Разделители могут быть следующими:', *separators)
    print('Программа остановлена!')
    exit(1)
my_new_list = []
for i in my_list:
    if my_list.count(i) == 1:
        my_new_list.append(i)
print(f'Новый список с уникальными элементами исходного списка: {my_new_list}')
