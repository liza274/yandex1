# A

dim = int(input())

for i in range(dim):
    for j in range(dim):
        print((i + 1) * (j + 1), end=' ')
    print()

# B

dim = int(input())

for i in range(1, dim + 1):
    for j in range(1, dim + 1):
        print(f'{j} * {i} = {i * j}')

# C

dim = int(input())

count = 1
num = 1

while num <= dim:
    for i in range(count):
        if num > dim:
            break
        print(num, end=' ')
        num += 1
    print()
    count += 1

# D

count = int(input())

summa = 0

for _ in range(count):
    number = int(input())
    while number > 0:
        summa += number % 10
        number //= 10

print(summa)

# E

natures = int(input())

bunnies = 0

for _ in range(natures):
    counted = False
    while (s := input()) != 'ВСЁ':
        if s == 'зайка' and counted is False:
            bunnies = bunnies + 1
            counted = True

print(bunnies)

# F

count = int(input())

gcd = int(input())

for _ in range(count - 1):
    number = int(input())
    while number != 0 and gcd != 0:
        if number >= gcd:
            number %= gcd
        else:
            gcd %= number
    gcd = gcd + number

print(gcd)

# G

count = int(input())

base_delay = 3

for number in range(1, count + 1):
    for delay in range(base_delay):
        print('До старта', base_delay - delay, 'секунд(ы)')
    print(f'Старт {number}!!!')
    base_delay += 1

# H

count = int(input())

best_name = ''
best_sum = 0
for i in range(count):
    name = input()
    number = int(input())
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    if summa >= best_sum:
        best_sum = summa
        best_name = name

print(best_name)

# I

count = int(input())

result = 0

for _ in range(count):
    number = int(input())
    maximum = -1
    while number > 0:
        if number % 10 > maximum:
            maximum = number % 10
        number //= 10
    result = result * 10 + maximum

print(result)

# J

slices = int(input())

print('А Б В')
for a in range(1, slices - 1):
    for b in range(1, slices - a):
        c = slices - a - b
        print(a, b, c)

# K

count = int(input())

simple_counter = 0

for i in range(count):
    if (number := int(input())) > 1:
        simple = True
        divider = 2
        while divider <= int(number ** 0.5) and simple:
            if number % divider == 0:
                simple = False
            else:
                divider = divider + 1
        if simple is True:
            simple_counter = simple_counter + 1

print(simple_counter)

# L

height = int(input())
width = int(input())

cell_width = len(str(width * height))

number = 1
for _ in range(height):
    for _ in range(width):
        print(f'{number:>{cell_width}}', end=' ')
        number += 1
    print()

# M

height = int(input())
width = int(input())

cell_width = len(str(height * width))

for i in range(1, height + 1):
    for j in range(i, i + height * (width - 1) + 1, height):
        print(f'{j:>{cell_width}}', end=' ')
        if j == i + height * (width - 1):
            print()

# N

height = int(input())
width = int(input())

ceil_width = len(str(width * height))

if height > 0 and width > 0:
    for row in range(height):
        for column in range(width):
            if (row % 2) == 0:
                num = row * width + column + 1
            else:
                num = (row + 1) * width - column
            print(f'{num:>{ceil_width}}', end=' ')
        print()

# O

height = int(input())
width = int(input())

ceil_width = len(str(width * height))

for row in range(height):
    for column in range(width):
        if column % 2 == 0:
            num = column * height + row + 1
        else:
            num = (column + 1) * height - row
        print(f'{num:>{ceil_width}}', end=' ')
    print()

# P

size = int(input())
ceil_width = int(input())

string_length = size * ceil_width + (size - 1)

for row in range(size):
    for column in range(size):
        print(f'{((row + 1) * (column + 1)): ^{ceil_width}}', end='')
        if column == size - 1:
            print()
        else:
            print('|', end='')
    if row + 1 != size:
        print('-' * string_length)