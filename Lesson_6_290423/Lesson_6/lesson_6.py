# NOTES

# POSSIBLE CONTROL WORK after 5-6 lessons -------------------------------------------------------------------------

# python main.py --url www.rozetka.com
# під капотом їдемо на сайт розетки і беремо інфу яка є на головній сторінці (чи у каталозі товарів)
# перетворюємо у обьект, маніпулюємо, дістаємо лінки, перевіряємо чи вони валідні -
# якщо так, то записуємо в файл, якщо ні, то ексепшн

# python main.py --path /user/bin/file.pdf
# парсити якийсь пдф файл, де є лінки на наших партнерів
# перевіряти лінки і акумулювати у список і віддавати кастомеру

# YAML файл

# git status
# git add
# git commit -m "some comment"
# git push
# git push origin main


# FUNCTIONS ----------------------------------------------------------------------------------------------------

# функція - повертає значення, return - припинення функції та повернення певного значення
# процедура - не повертає значення
# метод - викликає функцію чи процедуру

# def get_max_number():
#     print('My first function')

# def get_max_number(a, b):  # параметри функції
#     if a > b:
#         return a
#     else:
#         return b
#     print('My first function')
#
#
# print(get_max_number(11, 12))
#
# max_value = get_max_number(100, 12)  # аргументи функції
# print(max_value)


# def get_max_number(a, b=10):  # параметри функції
#     if a > b:
#         return a
#     else:
#         return b
#
# value = get_max_number(7, 6)
# print(value)


# def get_max_number(a, b=10):  # параметри функції
#     if a > b:
#         return a, True
#     else:
#         return b, False
#
# # print(get_max_number(b=11, a=5))
# values = get_max_number(2, 4)
# print(values)
# print(type(values))
#
# value, is_true = values
# print(value, is_true)
# print(type(is_true))  # <class 'bool'>
# print(type(value))  # <class 'int'>


# ПОЗИЦІЙНІ АРГУМЕНТИ
# звичайний параметр
# параметр дефолтний
# *args - будь-які параметри позиційні - tuple()
# **kwargs - ключові параметри - dict()

# def get_max_number(age, type, *numbers, **addition_params):
#     max_number = numbers[0]
#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     if addition_params.get('lesson') == 5:
#         print(addition_params['my_name'])
#     print(age)
#     print(type)
#     return max_number
#
#
# print(get_max_number(1, int, 2, 4, 5, 22, 23, my_name='Olena', lesson=5, book='Python'))


# ЛОКАЛЬНІ ТА ГЛОБАЛЬНІ ЗМІНИ
#
# x = 50  # глобальна зміна. те що поза функції, не змінюється
#
#
# def func(x):
#     print(f'x = {x}')
#     x = 2
#     print(f'We change x to {x}')
#     return x
#
# # x = func(x)
# func(x)
#
# print(x)


# x = 90
#
#
# def func():
#     global x
#     print(f'x = {x}')
#     x = 2
#     print(f'We change x to {x}')
#
#
# func()
#
# print(f'Finish x = {x}')


# АННОТАЦІЇ В ПАЙТОНІ

# def get_max_number(a: int, b: int, my_list: list[int]) -> int:
#     if a > b:
#         return a
#     else:
#         return b
#
#
# print(get_max_number(1, 2))
# print(get_max_number(2.5, 2))


# ЛЯМБДА ------------------

# def func(x):
#     return x * x
#
#
# print(func(5))


# f = lambda x: x * x  # lambda - ключове слово, після двокрапки - return
# print(f(5))
#
# sum_func = lambda x, y: x + y
# print(sum_func(3, 8))
#
# def func(x):
#     def func_1(x):
#         print(f'Our x is {x}')
#     func_1(x)
#     return x * x
#
# # func_1(4)  # NameError: name 'func_1' is not defined. Did you mean: 'func'?
#
# print(func(5))


# MAP and FILTER functions ----------------------------------------------------

# map(func, *iterables) - проходитися функцією по усім ітерабельним
# my_list_1 = [22, 54, 88]
# my_list_2 = [25, 33]
# my_list_3 = [1, 4]

#
# def sum_two_number(x, y):
#     return x + y
#
#
# result = list(map(sum_two_number, my_list_1, my_list_2))   # <map object at 0x10f2ce320>
# result = list(map(lambda x, y: x * y, my_list_1, my_list_2, my_list_3))  # TypeError: <lambda>() takes 2 positional arguments but 3 were given
#
#
# print(result)


# result = (list(filter(lambda x: x > 50, my_list_1)))
#
# print(result)


# IMPORT ---------------------------------------------------------------------------------
import random
# #
# # print(random.randint(12, 123))
# #
# # my_list = [1, 2, True, {'a': 'test'}]
# # print(random.choice(my_list))
# #
# # # brew install - пакетний менеджер
# # pip install
#
# print(type(random))  # <class 'module'>

# def print_hi():
#     print(f'Hi')
#
#
# if __name__ == '__main__':
#     print(random.randint(12, 123))


# a = 1
# print(type(a) is int)
#
# print(isinstance(a, float))

# print(f'__name__: {__name__}');