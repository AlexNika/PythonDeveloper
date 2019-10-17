# Модуль 3

separators = [',', ';', '/']
s1 = input(f'Введите список №1. Разделитель может быть любым из списка {separators}: ')
s2 = input(f'Введите список №2. Разделитель может быть любым из списка {separators}: ')
my_list1 = []
my_list2 = []
sep1 = False
sep2 = False

# Проверка ввода списка, как пустая строка (просто нажали Enter, т.е. ничего не ввели)
if s1 == '':
    sep1 = True
if s2 == '':
    sep2 = True

# Проверка на наличие правильного сепаратора
for s in separators:
    if s in s1:
        sep1 = True
        my_list1 = list(s1.split(sep=s))
    if s in s2:
        sep2 = True
        my_list2 = list(s2.split(sep=s))

# Проверка ввода списка, если ввели один элемент без сепаратора в конце, то создаем список из оодного элемента
# не рабоате логика. Как совместить непавильных сепаратор и единичный элемент пока не понял.
# if len(s1) != 0 and not sep1:
#     sep1 = True
#     my_list1.append(s1)
# if len(s2) != 0 and not sep2:
#     sep2 = True
#     my_list2.append(s2)

# Если правильный сепаратор не найден, то завершение программы
if not sep1 or (not sep2):
    print('Один из списков разделен неизвестным для программы разделителем')
    print('Разделители могут быть следующими:', *separators)
    print('Программа остановлена!')
    exit(1)

my_list1 = [i for i in my_list1 if i not in my_list2]
print(f'Список №1 с удаленными элементами, присутствующими в списке №2: {my_list1}')
