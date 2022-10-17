# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input('Введите целое число:'))
neg_fibo = []
fibo = []
together_fibo = []
neg_fibo.append(1)
fibo.append(0)
fibo.append(1)
n = 1
for i in range(k - 1):
    n = - n
    fib = fibo[i] + fibo[i + 1]
    fibo.append(fib)
    neg_fibo.append(fib * n)
neg_fibo.reverse()
together_fibo = neg_fibo + fibo
print(f'Для k = {k} => {together_fibo}')