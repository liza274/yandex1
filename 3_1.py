# A

num = int(input())
all_good = True
words = []
for _ in range(num):
    words.append(input())
for word in words:
    if word[0] not in 'абв':
        all_good = False
if all_good:
    print('YES')
else:
    print('NO')

# B

string = input()

for letter in string:
    print(letter)

# C

length = int(input())
count = int(input())

for _ in range(count):
    string = input()
    if len(string) <= length:
        print(string)
    else:
        print(f'{string[:length - 3]}...')

# D

while string := input():
    if string[-3:] != '@@@':
        if string[0:2] == '##':
            string = string[2:]
        print(string)

# E

string = input()

palindrome = True

for pos in range(len(string) // 2):
    if string[pos] != string[~pos]:
        palindrome = False
        break

if palindrome:
    print('YES')
else:
    print('NO')

# F

count = int(input())

bunnies = 0
for _ in range(count):
    string = input().split()
    for word in string:
        if word == 'зайка':
            bunnies += 1

print(bunnies)

# G

string = input()
lst = string.split()
print(int(lst[0]) + int(lst[1]))

# H

count = int(input())

for _ in range(count):
    string = input()
    if 'зайка' in string:
        print(string.index('зайка') + 1)
    else:
        print("Заек нет =(")

# I

while string := input():
    if not (pos := string.find('#')) + 1:
        print(string)
    elif string[:pos]:
        print(string[:pos])

# J

text = ''

while (string := input()) != 'ФИНИШ':
    text += string.lower()

text = text.replace(' ', '')

maximum = 0
most_frequent_char = ''

for char in text:
    count = text.count(char)
    if count > maximum:
        maximum = count
        most_frequent_char = char
    elif count == maximum:
        if char < most_frequent_char:
            most_frequent_char = char

print(most_frequent_char.lower())