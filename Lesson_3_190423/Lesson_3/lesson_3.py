# NOTES

# Option for calculator with match case
# first_data = int(input('Enter first data '))
# second_data = int(input('Enter second data '))
# operation = input('Enter operation ')
#
#
# match operation:  # перевіряє данні які потрапляють у цю змінну
#     case '+':
#         result = first_data + second_data
#         print('Result ', result)
#     case '-':
#         result = first_data - second_data
#         print('Result ', result)
#     case '*':
#         result = first_data * second_data
#         print('Result ', result)
#     case '/':
#         result = first_data / second_data
#         print('Result ', result)
#     case _:
#         print('Operator is not valid!')

# Тернарний оператор
# Вміщує в собі умову, яку можна записати в один рядок

# celsius_temperature = int(input('Enter temperature: '))
# # kelvin_temperature = ((celsius_temperature * 9/5) + 32) if celsius_temperature > 0 else "Something wrong"
# # print(kelvin_temperature)
#
# if celsius_temperature > 0:
#     kelvin_temperature = ((celsius_temperature * 9 / 5) + 32)
# else:
#     kelvin_temperature = "Something wrong"
#
# print(kelvin_temperature)

# ТИПИ ДАНИХ ---------------------------------------------------------------------------------

# STRING -------------------------------------------------------------------------------------

# a = ''
# b = ""
# c = """"""  # not recommended - could be used as comment
# d = ''''''  # not recommended - could be used as comment

"""
This is a comment
"""

# a = 'Hello'
# b = 'Ukraine'
#
# print(a+b)
# print(a*3)
# # print(a*b)

# print('Hello', 'Ukraine')
#
# a = 'Hello {}'
# print(a.format('Ukraine'))
#
# a = 'Hello {} {} {}'
# print(a.format('Ukraine', 'Glory', '!!!'))

# f string -------------------------------------------------------------------------------------
# специфікатор форматів {1.0} ??

# name = 'John'
# age = 18
#
# print(f'My name is {name} and my age is {age}')

# конвертація -------------------------------------------------------------------------------------

# a = 98  # int
# b = 2.2  # float
# c = True  # Bool
#
# print(type(str(a)))
# print(type(str(b)))
# print(type(str(c)))
#
# age = 23
# print('My name is John' + str(age) + "age old")  # конкатинація

# пошук за індексом -------------------------------------------------------------------------------------

# letters = 'HelloWorld'
# print(letters[2])
# print(letters[6])
# print(letters[-1])
# print(letters[-2])

# slice[start: end: step] --------------------------------------------------------------------------------

# letters = 'HelloWorld'

# a = letters[3:]  # від третього до останнього
# print(a)
# b = letters[3:6]  # від третього до шосторо
# print(b)
# с = letters[::2]  # старт з нуля, кожен другий елемент нашого рядка
# print(с)

# print(len(letters))  # кількість елементів у нашому рядку

# split --------------------------------------------------------------------------------------------------

# letters = 'Hello, and, world, Ukraine, glory'
#
# print(letters.split(','))  # list
#
# print(letters.title())
# print(letters.lower())
# print(letters.lower())

# replace --------------------------------------------------------------------------------------------------
#
# letters = 'Hello, and, world, Ukraine, glory'
#
# print(letters.replace('and', 'or'))

# print("It's a string")
# print("It's \na string\t with \"pattern\"")  # екранування \n - новий рядок \t -табуляція

# Type of string --------------------------------------------------------------------------------------------------
# f"string"
# b"byte string"
# r"raw string"  # regex
#
# print('string'.encode('UTF-8'))  # b"string"
#
# path = "/Lesson_3/Git.pdf"
# path = "\\Homework_3\\homework_3.py"

# path = r"It\s \\\a string \n yes"  # raw - сирий рядочок
#
# print(path)

# List --------------------------------------------------------------------------------------------------
# набір об'ектів довільного типу

# my_list = []
# print(type(my_list))

# my_list = [1, 3, 4, 'string', 5.5, True]
# print(my_list)
#
# print(my_list[0])

# змінювати елементи списку

# my_list[0] = 'New'
#
# print(my_list)
#
# print(len(my_list))

# my_string = 'hello'
# my_list = list(my_string)
# print(my_list)  # ['h', 'e', 'l', 'l', 'o']
#
# auto = ['Audi', 'BMW', 'Subaru', 'Audi']
#
# # print('****'.join(auto))  # list to string
#
# # пошук який індекс у ауді
#
# # print(auto.index('Audi'))  # віддає лише перший елемент
#
# # index_value = auto.index('audi')
# # auto[index_value] = 'Audi auto'  # replace
#
# print(auto)
#
# print(auto.pop()) # забирає останній елемент зі списку
#
# print(auto)
#
# auto = ['Audi', 'BMW', 'Subaru', 'Audi', [1, 3, 55]]
#
# print(auto[4][2])
#
# auto.append(['Skoda', 'Alfa Romeo'])  # додає в кінець списку
#
# print(auto)
#
# print(auto[5][1])

# об'єднані списки

# auto = ['Skoda', 'Alfa Romeo']
# auto_2 = ['BMW', 'Subaru', 'Audi']
# auto.extend(auto_2)
# print(auto)
# print(auto + auto_2)

# cycles
# a = 1
# a = a + 1
# a += 1
#
# auto = ['Skoda', 'Alfa Romeo']
# index_for_del = auto.index('Skoda')
# # del auto[index_for_del]
# auto.remove('Skoda')
# print(auto)

# auto = ['Skoda', 'Alfa Romeo']
#
# if 'Skoda' in auto:
#     print('Skoda is present')
#     auto.remove('Skoda')
# else:
#     # pass
#     ...  # заглушка - ... та pass - ігнорує цей шматок коду
#
# print(auto)

# tuple (кортежі) --------------------------------------------------------------------------------------------------
# незмінні списки, не можна додати щось, видалити щось
# *args and return

# auto = ['Skoda', 'Alfa Romeo']
# a = tuple(auto)  # конвертувати ліст у тюпл
# print(a)
#
# my_tuple = (1, )
# print(type(my_tuple))  # <class 'tuple'>  кома обов'язкова
#
# # my_tuple = (1)
# # print(type(my_tuple))  # <class 'int'>
#
my_tuple_2 = 1, 2, 3, 4, 5
print(type(my_tuple_2))  # <class 'tuple'>
print(my_tuple_2)


mew_list = list(my_tuple_2)  # конвертувати тюпл у ліст
print(mew_list)
mew_list.append('Audi')
print(mew_list)

