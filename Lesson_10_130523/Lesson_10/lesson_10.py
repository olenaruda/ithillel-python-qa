import datetime
import time
from random import randint


# NOTES

# any() -> []
# all() -> [] приймають ітеруємий обьект


# a = [1, 2]
# b = 4
# c = 'My string'
# d = ''
#
# # if a == 2 or b == 2 or
# if any([a, b, c, d]):
#     print('True')
# else:
#     print('False')
#
# if all([a, b, c, d]):
#     print('True')
# else:
#     print('False')

# if a:
#     print('True')
# else:
#     print('False')

# print(any([True for i in range(10000) if i == 5000]))  # генератор

# pip list
# python -m venv venv
# .\venv\Scripts\activate   # source venv/bin/activate
# pip install pytest
# pip install selenium
# deactivate # вийти з віртуального енву
# pip freeze > requirements.txt # збирає усі залежності і інфу про пакети
# pip install -r requirements.txt


# Decorators

# def cat():
#     print('Meo')
#
# cat()
#
# def cat():
#     def say():
#         return 'Meo'
#     return say()
#
# print(cat())


# def say_something():
#     return 'Glory Ukraine'
#
#
# def say_after_function(func):
#     print(func)
#     print('Do something')
#
#
# say_after_function(say_something())
#
#
# def animal(type_animal='cat'):
#
#     def cat():
#         return "Meo"
#
#     def dog():
#         return "Woof"
#
#     if type_animal == "cat":
#         return cat
#     else:
#         return dog
#
# print(animal())
# print(animal()())


# def cat():
#     print('Meo')


# def my_decorator(func):
#     def my_wrapper():
#         print(f'Start')
#         func()
#         print(f'End')
#     return my_wrapper
#
#
# # my_decorator(cat())
#
# @my_decorator
# def dog():
#     print('Woof !')
#
# dog()


# def my_decorator(func):
#     def my_wrapper():
#         start = datetime.datetime.now()
#         func()
#         finish = datetime.datetime.now()
#         delta = finish - start
#         print(f'Time for {func} {delta}')
#     return my_wrapper
#
#
# @my_decorator
# def dog():
#     time.sleep(2)
#     print('Woof !')
#
#
# dog()


# Result: Time for <function dog at 0x103d465f0> 0:00:02.004548


# def my_decorator(func):
#     def my_wrapper(arg1, arg2):
#         print(f'I get {arg1} and {arg2}')
#         func(arg1, arg2)
#     return my_wrapper
#
#
# @my_decorator
# def full_name(first_name, last_name):
#     print(f'My full name {first_name} {last_name}')
#
# full_name('Joe', 'Koen')

# I get Joe and Koen
# My full name Joe Koen

#
# def my_decorator(func):
#     def my_wrapper(*args, **kwargs):
#         print(f'I get args - {args}')
#         print(f'I get kwargs - {kwargs}')
#         func(*args, **kwargs)
#     return my_wrapper
#
# # @my_decorator
# # def my_func():
# #     print('Python is cool')
#
# @my_decorator
# def my_func(*args, **kwargs):
#     for _ in args:
#         print(_)
#     print(f'Our kwargs {kwargs}')
#     print('Python is cool')
#
#
# kwargs_param = {'q': 2, 'p': 4}
# args_param = (1, 22, 3, 4)
# my_func(*args_param, **kwargs_param)


# my_func()


# def summ(*args, c = 12, d = 22):
#     print(args)
#     print(sum((args)))
#
#
# summ(1, 2, 3, 4, 55, 44, 2, 4, 5)


# OOP

# john = {
#     "name": "Joe",
#     "age": 23,
#     "salary": 20000
# }
#
# mark = {
#     "name": "Mark",
#     "age": 25,
#     "salary": 20000
# }
#
#
# def get_name(person: dict) -> str:
#     return person["name"]
#
#
# def update_salary(person: dict) -> int:
#     return person["salary"] * 0.1


# LOCAL_VAR = 'Python'
#
# class People:
#
#     country = 'Ukraine'  # змінна
#
#     def __init__(self, name: str, age: int):#   конструктор класу
#         self.name = name
#         self.age = age
#
#     def my_name_is(self) -> str:  # метод
#         return f"my name {self.name}"
#
#     def my_age(self) -> str:
#         return f"my age {self.age}"
#
#     def language(self) -> str:
#         return f"my language {LOCAL_VAR}"
#
#
# vadym: People = People('Vadym', 20)
#
# print(vadym.my_name_is())
# print(vadym.language())
#
#
# class DataGeneration:
#
#     @staticmethod
#     def generation_name(name):
#         new_name = f'{name} {randint(1, 50000)}'
#         return new_name
#
#
# data_generator = DataGeneration()
# print(data_generator.generation_name('Joe'))
