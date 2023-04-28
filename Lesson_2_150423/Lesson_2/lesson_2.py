# NOTES

# chmod +x main.py - усі права
# ls -la - права доступу
# b = None # змінна без данних,
# b = 10
# print(b)

# a = 1  # int()
hillel_lesson = 1
HILLEL_LESSON2 = 2
hillel123 = 3

# не рекомендовано, змінна не може починатися з цифри:
_hillel = 4
__HILLEL = 5
Hillel = 6
# 123hillel = 7

# PEP 8 - Style Guide for Python Code
Hillel2 = 'khkjfhjkhskjhfdjgsjdfjshdfjgjbnjcjhgfdhjkljnmkhkjfhjkhskjhfdjgsjdfjshdfjgjbnjcjhgfdhjkljnmkhkjfhjkhskjhfdjgsjdfjshdfjgjbnjcjhgfdhjkljnm'
Hillel3 = 'khkjfhjkhskjhfdjgsjdfjshdfjgjbnjcjhgfdhjkljnmkhkjfhjkhskjhfdjgsjdfjshdfjgjbnjcjhgfdhjkljnmkhkjfhjkhskjhfdj /' \
          'jdfjshdfjgjbnjcjhgfdhjkljnm'

# snake_case - змінні
first_variable = 1

def first_method():
    pass

# PascalCase/CamelCase - for classes
class MeClass:
    pass

# SCREAMING_SNAKE_CASE - константа, яка незмінна, e.g. ip of server
SCREAMING_SNAKE_CASE = '192.68.0.2'

# Types in Python ------------------------------------

# Boolean Type ------------------------------------
# True
# False

print(1 == 1) # True
print(1 == 2) # False

# Integer - ціле число ------------------------------------

print(123123123)

# Float - число з точкою ------------------------------------

print(23.1)

print(type(123123123))  # вбудована функція для визначення типу данних
print(type(23.1))

# List + Tuple + Set - послідовності ------------------------------------

print(type([1, '2', 3]))  # список list - int та string
print(type((1, 2, 3, 4)))  # tuple
print(type({(1, 2, 3, 4)}))  # set

# String  ------------------------------------
print(type('Hello'))

# Dictionary - ключ/значення ------------------------------------

print(type({'name': 'Olena', 'age': 30}))
print({'name': 'Olena', 'age': 30})


# Command + / - закоментувати

# ОПЕРАТОРИ  ------------------------------------

print(1+1)
print(1-1)
print(4*1)
print(36/10)

print(36%10)  # залишок від ділення = 6
print(36//10)  # ціла частина від ділення = 3

# ОПЕРАТОРИ ПОРІВНЯННЯ ------------------------------------

print(3>2)
print(3<2)
print(3==2)
print(3!=2)

print(2>=2)
print(3<=2)

# МОРЖОВИЙ ОПЕРАТОР  ------------------------------------

print(n:='!!!!!')

# print(n=1)

# ОПЕРАТОР ПОРІВНЯННЯ ------------------------------------

# is
# is not

# a = int(1)
# b = int(1)
# print(a is b)

# a = 1
# b = b
# print(a is b)

# a = 1
# b = 1
# print(a is b)

a = [1]  # list()
b = [1]  # list()
print(a == b)
print(id(a))
print(id(b))
print(type(a))
print(type(b))
print(a is b)  # False
print(a is not b)  # True
print(None is None)  # True

# змінни та незмінні типи данних

# ОПЕРАТОР ІДЕНТИФІКАЦІЇ ------------------------------------
# in and not

my_list = [1, 2, 3, 4]
print(2 in my_list)  # перевірка входження чи є якесь значення у нашому списку
print(2 not in my_list)
print(22 not in my_list)

# BUILT-IN FUNCTIONS ------------------------------------
# не можна використовувати як змінніб її не треба імпортувати
# int()
# print()
# type()
# id()
# input()

# print(*objects, sep=' ', end='\n', file=None, flush=False)
# *args - аргументи, стрінга, інтеджер, ліст, дикт
# sep - розділення
# end - перехід на новий рядочок
# print('Hello Ukraine', 'Glory', '2023', 22, [1, 2], {1: '0'}, sep='****', end='\n')
# print('Hello Ukraine', 'Glory', '2023', 22, [1, 2], {1: '0'}, sep='\n', end='!!!!')

int_variable = 12
my_string = str(int_variable)
print(my_string)
print(type(my_string))
print(id(int_variable))
print(id(my_string))

# input - функція вводу
# input('Set value: ')

# age = int(input('Set age: '))
# print(age)
# print(type(age))

# print(int(age))
# print(type(age))

# IF ELIF ELSE - УМОВИ ------------------------------------
# if
# elif
# else

# my_variable_1 = 2
# my_variable_2 = 5
my_variable_1 = 5
my_variable_2 = 5

# if my_variable_2 > my_variable_1:
#     my_variable_1 = my_variable_1 + 10
#     print(my_variable_1)
# else:
#     print(my_variable_2)

# if my_variable_2 < my_variable_1:
#     my_variable_1 = my_variable_1 + 10
#     print(my_variable_1)
# else:
#     print(my_variable_2)

if my_variable_2 < my_variable_1:
    my_variable_1 = my_variable_1 + 10
    print(my_variable_1)
elif my_variable_2 == my_variable_1:  # else if
    print('All good')
else:                                 # else
    print(my_variable_2)

# if True:
#     print('It\'s true')

# match case in python





