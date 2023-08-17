'''
2. Modulo

Напишите программу, которая вычисляет остаток от деления n-го числа Фибоначчи на число m.

Формат ввода
Целые числа n и m через пробел, где n от 1 до 10^15, m от 2 до 10^3.

Формат вывода
Последняя цифра числа F_n.
'''
def pisano(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if (previous == 0 and current == 1):
            return i + 1
def f(n):
    if n < 2: return n
    else:
        a = 0 
        b = 1
        for i in range(1, n):
            a, b = b, ((a + b))
        return b

n, m = input().split()
n = int(n)
m = int(m)
p = pisano(m)
print(f(n%p)%m)

