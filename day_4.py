age = 18
name = 'Сергей'
print(('Меня зовут {0} мне {1} и я люблю язык Python').format(name,age))
print(('Меня зовут {fio} мне {old} и я люблю язык Python').format(fio=name,old=age))
print(f'Меня зовут {name} мне {age} и я люблю язык Python')
print(f'Меня зовут {name.upper()} мне {age * 2} и я люблю язык Python')


#Списки - операторы и функции работы с ними

s1 = 'Москва,Тверь,Вологда'
s2 =[2,3,4,3,5,2]
s3 = [1,2,3.4,[-1,-2,-3],4]
s4 = list ['12sdf', 213, 3.4, True]
s5 = list ('python')
s6 = [21129,5521129,64,839943,943,455,1233,9943,1023,21129]
print((s2[0] + s2[1] + s2[2] + s2[3] + s2[4] + s2[5]) / 6)
s2[0] = 3
s2[1] = 'Удовлетворительно'
print(s2)
print(s4)
print(s5)
print(sorted(s6))
print(sorted(s6,reverse= True))
print(s2 + s6)
print(s1 * 3)
print('Удовлетворительно' in s2)

del s3[1]
print(s3)