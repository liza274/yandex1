# A

print("Как Вас зовут?")
name = input()
print(f"Здравствуйте, {name}!")
print("Как дела?")
wibe = input()
if wibe == "хорошо":
    print("Я за вас рада!")
else:
    print("Всё наладится!")

# B

a = int(input())
b = int(input())
if a > b:
    print("Петя")
else:
    print("Вася")

# C

a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print("Петя")
elif b > a and b > c:
    print("Вася")
else:
    print("Толя")

# D

petya = int(input())
vasya = int(input())
tolya = int(input())

if vasya > petya > tolya:
    print('1. Вася')
    print('2. Петя')
    print('3. Толя')
elif vasya > tolya > petya:
    print('1. Вася')
    print('2. Толя')
    print('3. Петя')
elif petya > vasya > tolya:
    print('1. Петя')
    print('2. Вася')
    print('3. Толя')
elif petya > tolya > vasya:
    print('1. Петя')
    print('2. Толя')
    print('3. Вася')
elif tolya > petya > vasya:
    print('1. Толя')
    print('2. Петя')
    print('3. Вася')
elif tolya > vasya > petya:
    print('1. Толя')
    print('2. Вася')
    print('3. Петя')

# E

a = 7
b = 6
c = a - 3
d = b + 3
e = int(input())
m = int(input())
d = a + e
f = b + m
if d > f: 
    print("Петя")
else:
    print("Вася")

# F

year = int(input())
yes = False
if year % 400 == 0:
    yes = True
elif year % 100 == 0:
    yes = False
elif year % 4 == 0:
    yes = True
else:
    yes = False
if yes:
    print('YES')
else:
    print('NO')

# G

a = int(input())
b = a % 10
c = a // 10 % 10
d = a // 100 % 10
e = a // 1000 % 10
if b == e and c == d:
    print("YES")
else:
    print("NO")

# H

text = input()
if "зайка" in text:
    print("YES")
else:
    print("NO")

# I

a = input()
b = input()
c = input()
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)

# J

a = int(input())
b = a // 10 % 10 + a % 10
c = a // 100 % 10 + a // 10 % 10
if b > c:
    print(f'{b}{c}')
else:
    print(f'{c}{b}')

# K

num = int(input())
first = num // 100
second = num // 10 % 10
third = num % 10
middle = first + second + third - max(first, second, third) - min(first, second, third)
if max(first, second, third) + min(first, second, third) == middle * 2:
    print("YES")
else:
    print("NO")

# L

a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

# M

a = int(input())
b = int(input())
c = int(input())
if a % 10 == b % 10 == c % 10:
    print(a % 10)
elif a // 10 % 10 == b // 10 % 10 == c // 10 % 10:
    print(a // 10 % 10)
else:
    print("NO")

# N

a = int(input())
b = a % 10
c = a // 10 % 10
d = a // 100 % 10
e = min(b, c, d)
f = max(b, c, d)
g = b + c + d - e - f
if e == 0:
    print(f'{g}{e} {f}{g}')
else:
    print(f'{e}{g} {f}{g}')

# O

a = int(input())
b = int(input())
c = a % 10
d = a // 10 % 10
e = b % 10
f = b // 10 % 10
g = max(c, d, e, f)
t = min(c, d, e, f)
s = (c + d + e + f - g - t) % 10
print(f'{g}{s}{t}')

# P

petya = int(input())
vasya = int(input())
tolya = int(input())


first = max(petya, vasya, tolya)
third = min(petya, vasya, tolya)
second = petya + vasya + tolya - first - third

if first == petya:
    first_name = 'Петя'
elif first == vasya:
    first_name = 'Вася'
else:
    first_name = 'Толя'

if second == petya:
    second_name = 'Петя'
elif second == vasya:
    second_name = 'Вася'
else:
    second_name = 'Толя'

if third == petya:
    third_name = 'Петя'
elif third == vasya:
    third_name = 'Вася'
else:
    third_name = 'Толя'


print(f'{first_name: ^24}')
print(f'{second_name: ^8}{" ": ^16}')
print(f'{" ": ^16}{third_name: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')

# R

a = int(input())
b = int(input())
c = int(input())

maximum = max(a, b, c) ** 2 * 2
other = a ** 2 + b ** 2 + c ** 2

if maximum == other:
    print('100%')
elif maximum > other:
    print('велика')
else:
    print('крайне мала')

# T

nature1 = input() 
nature2 = input() 
nature3 = input() 
if nature1 > nature2: 
    nature1, nature2 = nature2, nature1 
if nature1 > nature3: 
    nature1, nature3 = nature3, nature1 
if nature2 > nature3: 
    nature2, nature3 = nature3, nature2 
if 'зайка' in nature1: 
    print(nature1, len(nature1)) 
elif 'зайка' in nature2: 
    print(nature2, len(nature2)) 
elif 'зайка' in nature3: 
    print(nature3, len(nature3))