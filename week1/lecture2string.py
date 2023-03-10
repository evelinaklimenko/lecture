#Python - является динамически типизированным языком ( Он определяет тип данных переменной исходя из значения которое ей присвоено)
# Alt + Z -> сместить код 

# Название переменных 
# 1. имя переменной не может начинаться с цифры  
# 2. нельзя использовать зарезервированные слова 
# 3. имя не может содержать спец.символы (@.%,...)Можно использовать "_"

# Snake Cade -> hello _world
# Camel Case -> helloworld

""" Строки (str())"""
# Строки - Неизменяемый тип данных,предназначен для хранения текста (любые символы),строки заключаются всегда в одинарные или двойные ковычки 

# Синтаксис :
#string1 = 'строка с одинарными кавычками' можем использовать в тексте ""
#string2 = "строка с двойнной кавычкой" можем использовать в тексте ''
# string3 = 'так делать нельзя'
# внутри двойных ковычек все одинарные ковычки ''являются просто символами или наоборот .
#string4 =""" Многострочный текст,тут можно использовать любые ковычки """

# Множественное присваивание 
# z,x,y = 1,4,5

# len() -> возвращает длину строки (кол-во символов в строке)

# str_ = 'hello '
# print(len(str_))

"""Экранированные последовательности"""
# это последовательности,которые начинаются с символа '/' за которыми следует один или более символов 

"""Экранизация строк """

# спец символы 
# 1. '\n' # перенос на новую строку 
#str_ = 'hello\n'
#num = 4
#print(str_*num)
#умножение строки на число -> дублирование строк 

#2. ''\t'' -> отвечает за табуляцию 
#  str = 'Hello\tworld'#print(str_)

#3.

#4. '\\' -> отображает одинарную(двойную) кавычку 
# print(" Чтобы экранировать нужен \\") 

# 5. '\*' -> the same as 4.

# 6. '\r' -> возвращает каретку в начало строки 
# print('Hello,my name is \rhhhh')

# 7.'\v' -> перенос на новую строку со смещением вправо на длину предыдущей строки 
# print('hello\vworld')

# 8. '\a' -> гудок встроенного в систему динамика (не работает на новых моделях ноотбука)


# 9.Конкатенация строк 
#str1 = 'hello'
#str2 = 'world'
#print(str1 + '' + str2) 

"""Форматирование строк"""
# 1. c использование %
# 2. с использованием метода . format()
# 3. Интерполяция строк (f-строки)
# %
#name = input('enter your name: ')
#result = 'Hello, %s' % name
#print(result)

# . format(переменную)
#name = input('enter your name: ')
#result = 'hello,{}'.format(name)
#print(result)

# f
#name = input('enter your name:')
#result = f'hello, {name}'
#print(result)


"""Методы строк"""
#print(dir('hello'))

# Методы типов данных - функция , к которой обращаемся через точку 

# Методы на is
# str.isalpha() -> проверяет состоит ли строка только из букв
# str.islower() -> состоит ли строка из символов нижнего регистра (с маленькой буквы)
# str.isalnum() -> состоит ли наша строка только из цифр и букв
# print('hello'.isalpha())

# .lower() -> переводит строку в нижний регистр 
#str1 = "Hello"
#str2 = str1.lower()
#print(str1.lower)

# . upper() -> Переводит строку в верхний регистр 
# str = 'hello'
# print(str.upper())

# . title() -> делает первую букву каждого слова заглавной

# .strip() -> убирает пробельные символы в начале и в конце строки 
# a= '    hello '
# print(a)
# print(a.strip())

#.lstrip() -> убирает пробелы в начале строки
#.rstrip() -> убирает пробелы в конце строки 

# .replase(old,new,{count}) -> меняет старое(old) в строке на новое(new)(count - кол-во раз)
# a = 'ha ha ha ha '
# print(a.replace('ha','new',5)) (кол-во изменений)

# split(разделитель) -> делит строку по разделителю
# a = 'hello world'
# print(a.split('o'))# по умолчанию делит по пробелу


"""Индексы"""
# индексы - порядковый номер символа в строке

#'h e l l o'
# 0 1 2 3 4

"""Срезы"""
#str{start:stop:step}
# a = 'hello world'
# print(a{::}) # все слово {:}
# print(a{0}) # первый элемент строки 
# print(a{-1}) # последний элемент строки {index}
# print(a{::-1}) # переворачивает строку
# print(a{:5}) # hello
# print(a{::2}) # выводит через один элемент 
# print(a{3:}) # начиная с третьего индекса 
# print(a{:6}) # до 6 индекса (не включая его)




#****************************
# срезы - нахождение подстроки,step по умолчанию 1

# a = 'hello world'
# print(a[1::2])

# print (abc[-3:])
# выведет последние три последних буквы

# print (a[-1]+a[1;-1]+a[0])

# endswith(substring) -> возращает True,
# eсли строка заканчивается на substring

# text = 'hello world'
# b = text.endswith('world')
# print(b)
 
# startswith(substring,[start],[end])-> возвращает True ,если строока начинается с подстроки 
#  text = 'hello world'
#  b = text.startswith('world',6)
#  print(b)

# count(substring) -> считает кол-во вхождений substring в строке 
# text = 'hello world!'
# b = text.count('!!')
# print(b)

# index(substring,start,end)  -> принимает подстроку и возвращает индекс в строке(если нет такой  substring нет то возвращает ошибку )
# text = 'hello world'
# b = text.index('l',5)
# print(b)


# text = 'hello world'
# b = text.index('l',5)
# text[b] ='d'# TypeError (так как не может заменить переменную)
# print(text)

#  text = 'hello world'
# b = text.index()
# text[b] ='d'# TypeError (индекс не может оставаться пустым )
# print(text)

# find(substring,start,end) ->анологично index(),Разница заключается в том что если substring нет в строке -возвращается -1
# text = 'hello world'
# b = text.find(' ') 
# print(b)

# zfill(width) ->  Делает длину строки не меньше width,по необходимости заполняет первые символы 0(нулями)
# text = 'hello'
# print(text.zfill(10))
# вывод : 00000hello


# isdigit() -> проверяет состоит ли наша строка из чисел (true/false)
# a = input('введите число:')
# b = a.isdigit()
# print(b)

# a = input('введите число:')
# if a.isdigit():
#     print(int(a))




# isnumeric()
# isdecimal()


#'Разделитель', join(iterable) -> соеденяет строку по разделителю,которая находится в iterable (в кавычках)
# text = 'milk,water,bread'
# print(text.split(','))

# text = 'milk,water,bread'
# list_ = text.split(',') #['milk', 'water','bread']
# join_ = '==>'.join(list_)
# print(join_)
#вывод :разделяет слова тем что указано в кавычках


'************************************************'
# id() -> возвращает номер ячейки в памяти 
# text ='hello'
# text2 = text.replace('h', 'o')
# print(text)
# print(text2)._
# print(id(text))
# print(id(text2))
# вывод : заменяет символы на другие 

# list_ = ['hello','world']
# print(id(list_))
# list_[0] = 'hi'
# print(id(list_))


# text = 'coder'
# print(text[1:4])
# text[0]
# text[-1]
# print(text[-1]+text[1:-1]+text[0])
# вывод: поменяет последний символ поменяет с первым 



# command = "G()()()()(al)"
# print(command.replace('()','o').replace('(al)','al'))
# вывод:заменит "G()()()()(al)" на Gooooal

lst = list(map(int, input('Введите свои баллы по математике, английскому языку и литературе через пробел: ').split()))
a = (f'Ваш средний балл составляет: {sum(lst) / len(lst)}')
if a > 69 or a == 69:
  print('Вы допущены к экзаменам ',a)
else:
  print('Вы не допущены к экзаменам',a)