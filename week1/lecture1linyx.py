"Лекция № 1 'Linyx'"
# pwd -> показывает абсолютный путь к директории (возвращает абсалютный путь до папке где мы находимся)
# ls -> показывает содержимое директории в которой находимся 
# ls -a -> показывает содежимое директории и ее скрытые папки без информации об этих папках и файлов
# ls -la -> показывает информацию о данной директории , а также скрытые файлы
# ls название папки/название папки

# cd название директории-> поменять директорию 
# cd -> выходит в корневую папку если не указать путь перемещения(переходит в домашнюю директорию)
# cd ~ -> переходит в домашнюю директорию 
# cd .. -> выйти на одну директорию выше(в предыдущую директорию)
# cd ../.. -> выйти на две директории выше 
# cd название директории/название папки/ название -> зайдет в определенную директорию по абсалютному пути если прописать путь
# cd. ->переходит в текущую директорию ( остаемся в ней же)
# cd test/test1-> переходит в папку test1,которая находится в папке test

# clear -> очистить терминал
# ctrl + l -> очистить терминал

# mkdir  -> создать директорию (папку)
# mkdir название папки/название папки -> создает папку в папке не переходя в данную папку
# mkdir test1 test2 -> создает папку test1 и test2 

# touch -> создает файл с любым расширением (txt;py и т,д)
# touch название папки/название файла -> создает файл в папке не переходя в данную папку
# touch название файла /название файла -> создает файлы которые мы указали 
# touch test{3,4}.txt-> создает файлы test3.txt и test.txt

# echo text > test.txt ->перезаписывает текст в файл test.txt
# echo text >>test.txt -> перезаписывает text в файл test.txt



# cp test.txt test1.txt -> копирует содержимое файла test.txt в файл test.txt
# cp test.txt test -> копирует файл test.txt в директорию test

# history -> выводит историю терминала 

# sudo <command> -> выполняет команду с правами администратора 
# sudo apt update -> скачивает последние версии ваших предложений 
# нажатие на клавишу Tab -> приводит к автозаполнению






# rm ->  удаление файла 
# rmdir -> удаление пустых директорий (папок)
# rm -rf -> удаление папок и файлов со всем содержимым
# rm- rf/ -> удаляет корневую папку НИКОГДА НЕ ПИСАТЬ 

# Как посмотреть содержимое папки не переходя в нее 

# tree -> показывает структуру папки 

# Скрытые файлы и папки обозначаются точкой(.)
# '*******************'

# nano -> открывает  файл или папку в текстовом редакторе( в терминале)
# Чтоб сохранить файл:
# ctrl + x -> запрос на сохранение
# shift y/n -> да или нет 

# vim -> редактор

# cat -> выводит записи данного файла в терминал
# cat test.txt -> показывает содержимое файла test.txt
# cat test.txt > test.txt -> скопирует содержимое  файла test.tx в файле test1.txt

# mv -> перенести файл/папку или изменять название
# mv название файл через пробел пишем путь куда перенести файл (название папки)
# mv название файла далее пробел new_название файла с его разришением
#  mv test.txt commands.txt -> переименует файл test.txt в commands.test
#  mv test.txt test -> перемещает файл  test.txt  в директорию test 




# Tap ->дополнит название папки или файла

# sudo -> дает авторства на дальнейшую (права автора)
# apt-get install -> скачать библеотеку ,пакеты
# apt-get uhdate -> находит обновление и обновляет 
# apt-get upgrade -> обновление полностью всех обнавлений 


# ctrl + / -> ставит в начале каждого предложения #
# ctrl + z -> отменяет последнее действие 
# ctrl+alt +T -> открывает терминал 
# && -> обьеденяет команды


"Лекция № 2 'Введение в GIT'"
# SSH key -> нужен для привязки компьютера к аккаунту 
# ssh-keygen -t rsa -b 4096 - C 'почта'
# cat id_rsa.pub -> выведет полный ssh ключ

# git init -> создается  скрытая папка .git 
# git remote add (name url)->добавляет удаленный репозиторий который находится на сервере 
# git pull ->стягивает изменения с ветки 
# git status -> показывает статус файла в проекте
# git add -> добавляет файлы в рабочей папке для дальнейшего коммита
# git commit -> добавляет все файлы в индексе  и  сохраняет их слепок 
# git branch -> список веток,выбор ветки -> показывает на какой ветке ты находишься 
# git checkout - производит переклюсение на ветку 
# git push -> отправляет в удаленный репозиторий 
# git reset  -> отвечает за файл с таким именем 
# git log -> просмотр истории коммитов
# git add . ->используется чтобы не прописывать все файлы
# git push --set-upstream origin -> пушить на определенную ветку в удаленный репозиторий
# Ветка мастер должна быть всегда в проекте 

# git merge -> слияние всех коммитов на одну ветку 
# git clone -> клонирование к себе в проект в созданный репозиторий к себе в локальную сть 
# readme -> инструкции для удаленного репозитория


# Данные и их типы
# В Python существует множество различных типов данных, которые подразделяются на категории: числа, последовательности, словари, наборы.

# boolean - логическое значение True или False
# int - представляет целое число, например, 1, 4, 8, 50.
# float - представляет число с плавающей точкой, например, 1.2 или 34.76
# complex - комплексные числа
# str - строки, например hello, Makers. В Python 3.x строки представляют набор символов в кодировке Unicode
# bytes - последовательность чисел в диапазоне 0-255
# byte array - массив байтов, аналогичен bytes с тем отличием, что может изменяться
# list - список
# tuple - кортеж
# set - неупорядоченная коллекция уникальных объектов
# frozen set - то же самое, что и set, только не может изменяться (immutable)
# dict - словарь, где каждый элемент имеет ключ и значение
# Изменяемые и неизменяемые типы данных
# В Python существуют изменяемые и неизменяемые типы. К неизменяемым (immutable) типам относятся:

# целые числа (int),
# числа с плавающей точкой (float), * комплексные числа (complex),
# логические переменные (bool),
# кортежи (tuple),
# строки (str),
# неизменяемые множества (frozen set).
# К изменяемым (mutable) типам относятся:

# списки (list),
# множества (set),
# словари (dict).
# Как уже было сказано ранее, при создании переменной, вначале создается объект, который имеет уникальный идентификатор, тип и значение, после этого переменная может ссылаться на созданный объект.

# Неизменяемость типа данных означает, что созданный объект больше не изменяется. Например, если мы объявим переменную k = 15, то будет создан объект со значением 15, типа int и идентификатором, который можно узнать с помощью функции id().


# Типы данных. Numbers
# Числовой тип данных в Python предназначен для хранения числовых значений. Это неизменяемый тип данных, что означает, что изменение значения числового типа данных приведет к созданию нового объекта в памяти (и удалению старого).

# Присвоив переменной num1 значение 33, мы создаем числовой объект, а с помощью записи del num1 можем удалить его.

# В Python есть четыре вида числового типа данных:

# int (целое число)
# long (длинное целое число [может быть представлено в восьмеричной или шестнадцатеричной системе исчисления])
# float (число с плавающей точкой: -0.2, 0.0, 3.14159265 и т.д.)
# complex (комплексное число)
# Целые числа int
# Числа в Python 3 ничем не отличаются от обычных чисел. Они поддерживают набор самых обычных математических операций:

# x + y - Сложение
# x - y - Вычитание
# x * y - Умножение
# x / y - Деление
# x // y - Получение целой части от деления
# x % y - Остаток от деления
# -x - Смена знака числа
# abs(x) - Модуль числа
# divmod(x, y) - Пара (x // y, x % y)
# x ** y - Возведение в степень
# pow(x, y[, z]) - xy по модулю (если модуль задан

# Однострочные комментарии начинаются со знака фунта «#», многострочные — начинаются и заканчиваются тремя двойными кавычками «"""».
# Чтобы присвоить значение пременной используется знак «=», а для сравнения —
# «==». Для увеличения значения переменной, или добавления к строке используется оператор «+=»,
#  а для уменьшения — «-=». Все эти операции могут взаимодействовать с большинством типов, в том числе со строками. Например
# mystring = "Hello"
# mystring += " world."
# print mystring
# Hello world.


# списки (lists) -> Списки — похожи на одномерные массивы (но вы можете использовать Список включающий списки — многомерный массив)
# кортежи (tuples) -> Кортежи — неизменяемые списки
# словари (dictionaries). словари — тоже списки, но индексы могут быть любого типа, а не только числовыми.

# Чтобы получить список цифр до числа <number> — используйте функцию range(<number>).

# rangelist = range(10) #Получаем список из десяти цифр (от 0 до 9)
# >>> print rangelist
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Операции над строками
# A + B — конкатенация;
# A * n — повторение n раз, значение n должно быть целого типа.

# логический тип данных (тип bool) Его также называют булевым
# У этого типа всего два возможных значения: True (правда) и False (ложь)
# a = True 
# print(type(a))
# # <class 'bool'>  
# b = False 
# print(type(b))
# # <class 'bool'> 

# В программировании False обычно приравнивают к нулю, а True – к единице.


# Логические операторы
# мы обозначаем сравнения словами "равно", "больше", "меньше". 
#  специальные знаки
# > (больше),
# < (меньше),
# >= (больше или равно),
# <= (меньше или равно),
# == (равно),
# != (не равно).
# Note: Не путайте операцию присваивания значения переменной, обозначаемую в языке Python одиночным знаком "равно", и операцию сравнения (два знака "равно").

# Присваивание и сравнение – разные операции.

# a = 10  
# b = 5  
# print(a + b > 14) # True  
# print(a < 14 - b) # False  
# print(a <= b + 5) # True  
# print(a != b) # True  
# print(a == b) # False  
# c = a == b 
# print(a, b, c) #(10, 5, False)  
# В данном примере выражение c = a == b состоит из двух подвыражений. Сначала происходит сравнение (==) переменных a и b. После этого результат логической операции присваивается переменной c. Выражение a, b, c просто выводит значения переменных на экран.


# Чтобы получить True при использовании оператора and, необходимо, чтобы результаты обоих простых выражений, которые связывает данный оператор, были истинными. Если хотя бы в одном случае результатом будет False, то и все сложное выражение будет ложным.
# Чтобы получить True при использовании оператора or, необходимо, чтобы результат хотя бы одного простого выражения, входящего в состав сложного, был истинным. В случае оператора or сложное выражение становится ложным лишь тогда, когда ложны оба составляющие его простые выражения.


# В языке Python есть еще унарный логический оператор not, т. е. отрицание. Он превращает правду в ложь, а ложь в правду.
# Унарный он потому, что применяется к одному выражению, стоящему после него, а не справа и слева от него как в случае бинарных and и or.

# print(not y < 15) # False  

# Инструкция if(...) вычисляет условие в скобках и, если результат true, то выполняет блок кода.
# b = 0 
# a = 50 
# n = 98 
# if n < 100:
#     b = n + a 
# print(b) 



"Лекция списки тип данных"

# num2 = [1, 2, 3, 4]
# num3 = list (['makers' 'bootcamp'])
# print(num3)

"Функция Range"

# 1. range(end) 
# num1 = list(range(10))
# print(num1)

# 2. range(start, end)
# numbers = list(range(1,11))
# print(numbers)

# 3. range(start, end, step)
# numbers = list(range(1, 10, 2))
# print(numbers)
# Вывод:[1, 3, 5, 7, 9]

# numbers = list(range(10,0, -1))
# print(numbers)

# Цикл for

# for i in range(1,11): # -> 1,2,3,4,56,7,8,9,10
#     print(i ** 2)
# numbers = list(range(1, 10, 2))
# Вывод :
# 1 
# .4
# .9
# .16
# .25
# .36
# .49
# .64
# .81
# .100

"Сравнение списков"

# numbers = [1, 2, 3, 4, 5]
# numbers = [1, 2, 3, 4, 5]
# print(numbers1 == numbers2)
# Вывод : True


# Списки могут содержать в списках строки и числа и обьекты других типов данных

"""индексация """

# numbers = [1, True, 'Makers', 8.9, (1, 2), ['hello']]
# print(numbers[4])
# Вывод :(1, 2)

# numbers = [1, True, 'Makers', 8.9, (1, 2), ['hello']]
# numbers[3] = 'Bootcamp'
# print(numbers)
# Вывод:[1, True, 'Makers', 'Bootcamp', (1, 2), ['hello']]

# numbers = [1, True, 'Makers', 8.9, (1, 2), ['hello']]
# numbers[3] = {1}
# print(numbers)


# users = ['Alise', 'Sam', 'Carly']

# for i in users:
#     print(i)


# users = ['Alise', 'Sam', 'Carly']

# for i in users:
#     print(f'Hello {users}')


"Методы списков"

# append(element)
# users = ['Alise', 'CAt']

# user = 'Tom'
# users.append(user)
# print(users)
# Вывод :['Alise', 'CAt', 'Tom']

# guests = []
# list_length = int(input('Enter number of guests: '))

# for i in range(list_length):
#     guest = input('Enter guest name: ')

#     guests.append(guest)

# print(guests)


# extend(list) -> сширяет список за счет другого списка
# users1 = ['Hello']
# users2 = ['world']
# users1.extend(users2)
# print(users1)
# Вывод :['Hello', 'world']



# users1 = ['Hello']
# users2 = ['world']
# print(users1 + users2)
# Вывод:['Hello', 'world']

# insert(index,element)
# users = ['Jon', 'Alic', 'Andi']

# users.insert(1, 'Raychel')
# print(users)
# Вывод :['Jon', 'Raychel', 'Alic', 'Andi']

# remove(element) -> удаляет первый элемент вхождения
# users = ['Jon', 'Cat', 'Alic', 'Cat', 'Andi']
# users.remove('Cat')
# print(users)
# Вывод:['Jon', 'Alic', 'Cat', 'Andi']

# pass -> работает как закрывающий элемент


# clear() ->  удаляет или очищает список 
# users = ['Jon', 'Cat', 'Alic', 'Cat', 'Andi']
# users.clear()
# print(users)
# Вывод:[]

# del -> удаляет обьект из памяти 
# users = ['Jon', 'Cat', 'Alic', 'Cat', 'Andi']
# del.users
# print(users)


# index(element)

# my_list = ['hello', 'makers', True, 6]
# print(my_list.index(4))

# pop(index)

# numbers = [1, 2, 3, 4, 5]
# number = numbers.pop(1)
# print(numbers)
# print(number)
# Вывод :[1, 3, 4, 5]
# 2

# count(element) ->

# numbers = [2, 4, 2, 2, 6, 8, 0, 2, 2, 2, ]
# print(numbers.count(2))
# Вывод: 6

# sort(key) -> сортирует 
# users = ['Jon', 'Cat', 'Alic', 'Cat', 'Andi']
# users.sort()
# print(users)
# # Вывод:['Alic', 'Andi', 'Cat', 'Cat', 'Jon']

# users = ['Jon', 'Cat', 'Alic', 'Cat', 'Andi']
# users.sort(key=len)
# print(users)
# # Вывод:['Jon', 'Cat', 'Cat', 'Alic', 'Andi']

# revers()

# users = ['Jon', 'Cat', 'Alic', 'Cat', 'Andi']
# users.reverse()
# print(users)

# copy()

# users1 = ['Tom', 'Bob', 'Ann']
# users2 = users1.copy()

# print(id(users1))
# print(id(users2))
# print(users1)
# print(users2)
# ВЫвод:139627865972224
# 139627866486016
# ['Tom', 'Bob', 'Ann']
# ['Tom', 'Bob', 'Ann']


"""Functions"""

# len() ->Возвращает длину списка

# numbers =[1, ,3 ,4]


# max(), min()

# numbers =[1, 4, 4]
# print(max(numbers))

# sum()

# numbers =[1, 4, 4, 6]
# print(sum(numbers))
# ВЫвод 

# sorted()
# numbers =[1, 4, 4, 6, 5]
# print(sorted(numbers))


# Ctrl + C -> закончить цикл while