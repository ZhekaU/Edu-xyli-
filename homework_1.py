# Отформатировать данную строку и убрать из нее все лишние символы
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
s1 = list(punctuations)
print(len(punctuations))
print(s1)
del s1[0:29]
print(s1)

my_str = "Привет!!!, Меня зовут --Евгений."
s3 = my_str.replace(',',' ').replace('--',' ')
print(s3)


#Проверить является ли a палиндромом
a = "мадам"
a1 = a[::-1]
print(a)
print(a1)
print(a1 == a)

a2 = 'Он в аду давно'
a3 = a2[::-1]
print(a3)
print(a2 == a3)