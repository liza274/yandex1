# A

def make_list(length, value=0):
    lst = []
    for _ in range(length):
        lst.append(value)
    return lst

# B

def make_matrix(size, value=0):
    if isinstance(size, int):
        size = [size, size]
    result = [[value] * size[0] for _ in range(size[1])]
    return result

# C

def gcd(*args):
    a = list(args)
    while len(a) > 1:
        while a[1]:
            a[0], a[1] = a[1], a[0] % a[1]
        a.pop(1)
    return a[0]

# D

def month(num, lang='ru'):
    MONTHS = {
        'ru': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
               'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December']
             }

    return MONTHS[lang][num - 1]

# E

def to_string(*data, sep=' ', end='\n'):
    string = ''
    data = list(data)
    while data:
        item = data.pop(0)
        string += str(item)
        if data:
            string += sep
    return string + end