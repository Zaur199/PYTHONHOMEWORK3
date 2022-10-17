# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [2.4, 6.8, 1.9, 0.456, 4.25, 3.08]
max = 0
min = 1
result = 0
for i in range(len(lst)):
    x = lst[i] % 1  + 0.0001
    if x > max:
        max = x
    elif x == 0.001:
        print('Совпадение')
    elif x < min:
        min = x
result = max - min
print(f'{lst} => {result:.2f}')