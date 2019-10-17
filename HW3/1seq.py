# Модуль 1

n = ''
while not n.isdigit():
    n = input('Вводите количество элементов списка: ')
n = int(n)
my_list = []
for i in range(n):
    my_list.append(int(input(f'Введите {i+1}-й элемент списка: ')))
my_list.sort()
print(f'Сортированный по возрастанию список: {my_list}')
