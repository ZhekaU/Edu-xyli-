#Основные методы строк
s1 = 'python'
s2 = s1.upper()
s3 = 'abrakadabra'
s4 = '45'
s5 = 'Пупкин Залупкин Иван'
s6 = '1, 2,  3,    5,   4,    6, 7 '
s7 = (s6.replace(' ','').split(','))
s8 = '     Hello World    \n'
print(s1.upper())
print(s2)
print(s2.lower())
print(s3.count('ra'))
print(s3.count('ra',4, 10))
print(s3.find('br'))
print(s3.find('br',2))
print(s3.rfind('br'))
print(s3.replace('a','d'))
print(s3.replace('ab','D'))
print(s3.replace('a','d',3))
print(s3.isalpha())
print(s4.isdigit())
print(s4.rjust(5, '0'))
print(s5.split(" "))
print(s6.replace(' ','').split(','))
print('8===8'.join(s7))
print(','.join(s5))
print(','.join(s5.split()))
print(s8.strip())


# Спецсимволы, экранирование символов, raw-строки
s8 = 'Шла Саша по \\шоссе\\ \n и сосала сушку '
s9 ='\tШла Саша по \\шоссе\\ \n и сосала сушку '
s10 = r'\tШла Саша по \\шоссе\\ \n и сосала сушку '
print(s8)
print(s9)
print(s10)