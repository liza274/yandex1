# A

s = input()
while s != 'Три!':
    print('Режим ожидания...')
    s = input()
print('Ёлочка, гори!')

# B

count = 0
while (s := input()) != 'Приехали!':
    if 'зайка' in s:
        count += 1
print(count)

# C

start, stop = int(input()), int(input())

for i in range(start, stop + 1):
    print(i, end=' ')

# D

start, stop = int(input()), int(input())

if stop >= start:
    for i in range(start, stop + 1):
        print(i, end=' ')
else:
    for i in range(start, stop - 1, -1):
        print(i, end=' ')

# E

summa = 0

while (price := float(input())) != 0:
    if price >= 500:
        price *= 0.9
    summa += price

print(summa)

# F

a, b = int(input()), int(input())

while a != 0 and b != 0:
    if a >= b:
        a -= b
    else:
        b -= a

print(a + b)

# G

a, b = a1, b1 = int(input()), int(input())

while a != 0:
    a, b = b % a, a

print(a1 * b1 // (a + b))

# H

info = input()
repeat = int(input())

for _ in range(repeat):
    print(info)

# I

num = int(input())

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(factorial)

# J

x, y = 0, 0

while (direction := input()) != 'СТОП':
    n = int(input())
    if direction == 'ВОСТОК':
        x += n
    elif direction == 'ЗАПАД':
        x -= n
    elif direction == 'СЕВЕР':
        y += n
    elif direction == 'ЮГ':
        y -= n
        
print(y)
print(x)

# K

num = int(input())

summa = 0

while num > 0:
    summa += num % 10  # s = s + num % 10
    num //= 10  # num = num // 10

print(summa)

# L

num = int(input())

maximum = -1

while num > 0:
    if num % 10 > maximum:
        maximum = num % 10
    num = num // 10

print(maximum)

# M

count = int(input())

first = 'яяяяяяяя'

for _ in range(count):
    name = input()
    if name < first:
        first = name

print(first)

# N

num = int(input())

divisor = 2
prime = True

if num <= 1:
    prime = False
else:
    for divider in range(2, int(num**0.5 + 1)):
        if num % divider == 0:
            prime = False
            break

if prime is True:
    print('YES')
else:
    print('NO')

# O

places = int(input())

bunnies = 0

for i in range(places):
    nature = input()
    if 'зайка' in nature:
        bunnies += 1
print(bunnies)

# P

num = int(input())

original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if original_num == reversed_num:
    print('YES')
else:
    print('NO')