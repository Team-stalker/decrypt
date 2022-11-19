# -*- coding: utf-8 -*-

s = 'ршф ыфэлш туфйф нужшв, шфтщ ужкф тжсф чхжшв' 

# Алфавит
alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

for n in range(len(alpha)):
    translated = ''
    for symbol in s:
        if symbol in alpha:
            num = alpha.find(symbol)
            num = num - n
            if num < 0:
                num = num + len(alpha)
            translated = translated + alpha[num]
        else:
            translated = translated + symbol
    print('Ключ взлома #%s: %s' % (n, translated))

