print(4 > 2 )
print(4 > 7 )
a = 5
b = 7.8
volume = a > b
volum = a < b
volu = a >= b
vol = a <= b
vo = a == b
v= a != b
print(volume)
print(volum)
print(volu)
print(vol)
print(vo)
print(v)
print(type(volume))
y = 1.85
print(y >= -2 and y <= 5)
print(y < -2 or y > 5  )
print(not(a % 2 == 0 or a % 3 == 0 ))



# Строки

s1 = 'Панда'
s2 = 'Panda'
text = '''Я Python выучил бы только за то,
что есть популярные курсы.
Много хороших курсов '''
s3 = 'Я люблю'
s4 = 'язык Python'
s5 = 'ха'
s6 = 'уууууулетаю на Гаити'
print(s1)
print(s2)
print(text)
print(s3 + ' ' + s4)
print(s5 * 10)
print(len(s6))
print('у' in s6)
print(s6 == 'уууууулетаю на Гаити' )
print(s6 != 'уууууулетаю на Гаити')
print(s3 > s4 )
print(ord('Л'))
print(ord('л'))


# Знакомство с индексами
e1 = 'Hello Python '
e2 = 'h'
print(e1[0])
print(e1[0:5])
print(e1[0:12:3])
print(e1[::-1])
print(e2 + e1[1:])
