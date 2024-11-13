# A

print("Привет, Яндекс!")

# B

name = input("Как Вас зовут?")
print(f"Привет, {name}")

# C

n = input()
print(n)
print(n)
print(n)

# D

cash = int(input())
price = int(38 * 2.5)
print(cash - price)

# E

price = int(input())
weight = int(input())
cash = int(input())
print(cash - price * weight)

# F

name = input()
price = int(input())
weight = int(input())
cash = int(input())
print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {price * weight}руб")
print(f"Внесено: {cash}руб")
print(f"Сдача: {cash - price * weight}руб")

# G

N = int(input())
arg = "Купи слона!\n"
print(f"{arg * N}")

# H

num = int(input())
punishment = input()
string = f'Я больше никогда не буду писать "{punishment}"! \n'
print(string * num)

# I

am = int(input())
chi = int(input())
re = int(am * chi / 2)
print(re)

# J

name = input()
locker = int(input())
group = locker // 100 
spisok = locker % 10
crib = locker // 10 % 10
print(f'Группа №{group}.')
print(f'{spisok}. {name}.')
print(f'Шкафчик: {locker}.')
print(f'Кроватка: {crib}.')

# K

a = int(input())
b = a // 1000 % 10
c = a // 100 % 10
d = a // 10 % 10
p = a % 10 
print(f'{c}{b}{p}{d}')

# L

a = int(input())
b = int(input())
c = a // 100 % 10 + b // 100 % 10
d = a // 10 % 10 + b // 10 % 10
e = a % 10 + b % 10
print(f'{c % 10}{d % 10}{e % 10}')

# M

a = int(input())
b = int(input())
print(b // a)
print(b % a)

# N

red = int(input())
green = int(input())
blue = int(input())
b = red + blue
print(b + 1)

# O

a = int(input())
b = int(input())
c = int(input())
print(f'{((a + c // 60 + (b + c % 60) // 60) % 24):0>2}:{((b + c % 60) % 60):0>2}')

# P

a = int(input())
b = int(input())
c = int(input())
print(f'{((b - a) / c):.2f}')

# Q

a = int(input())
b = int(input(), 2)
print(a + b)

# R

a = int(input(), 2)
b = int(input())
print(b - a)

# S

good = input()
price = int(input())
weight = int(input())
cash = int(input())

price_string = str(weight) + 'кг * ' + str(price) + 'руб/кг'
sum_string = str(price * weight) + 'руб'
cash_string = str(cash) + 'руб'
change_string = str(cash - price * weight) + 'руб'

print('================Чек================')
print(f'Товар: {good:>28}')
print(f'Цена: {price_string:>29}')
print(f'Итого: {sum_string:>28}')
print(f'Внесено: {cash_string:>26}')
print(f'Сдача: {change_string:>28}')
print('===================================')

# T

total_weight = int(input())
total_price = int(input())
price_1 = int(input())
price_2 = int(input())

weight_1 = int((total_price - price_2) * total_weight / (price_1 - price_2))
weight_2 = int(total_weight - weight_1)

print(weight_1, weight_2)

