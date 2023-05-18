# NOTES

# Skip -------------------------------------------------------------------------------------
# def skip(condition=True, reason=''):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if condition:
#                 print(reason)
#             else:
#                 print(func(*args, **kwargs))
#         return wrapper
#     return decorator
#
#
# @skip(condition=True, reason='Skipped because of JIRA-123 bug')
# def two_plus_two():
#     return 2 + 2 == 4
#
#
# print(two_plus_two())

# Lesson 11 -------------------------------------------------------------------------------------
# Наслідування - Inheritance
#
# class Person:
#
#     brain = True
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def get_name(self):
#         return f'My name {self.first_name}'
#
#
# person = Person('Joe', 'Coen')
# print(person.first_name)
# print(person.get_name())
# print(person.brain)
#
#
# # class Student(Person):
# #
# #     def __init__(self, first_name, last_name, graduate):
# #         super().__init__(first_name, last_name)  # щоб не дублювати батьківський клас
# #         self.graduate = graduate
# #
# #     def get_graduate(self):
# #         return f'My graduate {self.graduate}'
# #
# #
# # student = Student('Marta', 'Lee', 'Master')
# #
# # print(student.get_graduate())
# # print(student.get_name())
#
#
#
# class Student(Person):
#
#     def __init__(self, first_name, last_name, graduate):
#         super().__init__(first_name, last_name)  # щоб не дублювати батьківський клас
#         self.graduate = graduate
#
#     def get_graduate(self):
#         return f'My graduate {self.graduate}'
#
#     def get_name(self):
#         return f'My name {self.first_name} in student class'
#
#
# student = Student('Marta', 'Lee', 'Master')
#
# print(student.get_graduate())
# print(student.get_name())  #спочатку те що в класі, а потім те, що в батьківському класі
#
# # множинне наслідування -------------------------------------------------------------------------------------
# # майже не використовується
#
# class Employee(Person, Student):
#
#     def __init__(self, first_name, last_name, graduate, salary):
#         # super(Person, self).__init__(first_name, last_name)
#         # super(Student, self).__init__(пкфвгфеу)
#         # super().__init__(first_name, last_name, graduate)
#         self.salary = salary
#
#     def get_salary(self):
#         return self.salary
#
#
# employee = Employee('Mike', 'Bein', 'Master', 3000)
# print(employee.get_name())
# print(employee.get_graduate())
# print(employee.get_salary())
#
# print(Employee.__mro__)  # магічний метод, який показує наші етапи наслідування


# Інкапсуляція -  Incapsulation  -------------------------------------------------------
#
# class Student:
#
#     def __init__(self, first_name, last_name, graduate):
#         self.first_name = first_name  # public
#         self._last_name = last_name  # protected
#         self.__graduate = graduate  # private
#
#     def get_graduate(self):
#         return self.graduate
#
#     def _get_first_name(self):
#         return self.first_name
#
#     def __get_last_name(self):
#         return self._last_name
#
#
# student = Student('Joe', 'Coin', 'Master')
# # print(student.first_name)
# # print(student._last_name)
# # # print(student.__graduate)
# # print(student._Student__graduate)
# # print(student.__dict__) # що є у класі  {'first_name': 'Joe', '_last_name': 'Coin', '_Student__graduate': 'Master'}
#
# print(student.get_graduate())
# print(student._get_first_name())
# print(student._Student__get_last_name())


# ПОЛІМОРФІЗМ - Polymorpism  -------------------------------------------------------

# один і той самий інтерфейс, який може виконувати різні завдання

print(len('My string'))
print(len([1, 2, 3, 4]))
print(len({'Name': 'Joe', 'Address': 'Kyiv'}))


# Абстракція - Abstraction
# базовий клас

from abc import ABC, abstractmethod


class People(ABC):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    @abstractmethod
    def get_last_name(self):
        pass
        # return self.last_name


class Student(People):

    def __init__(self, first_name, last_name, graduate):
        super().__init__(first_name, last_name)
        self.graduate = graduate

    def get_graduate(self):
        return self.graduate

    def get_last_name(self):
        return f'{self.last_name}'


student = Student('Olena', 'Ruda', 'Master')
print(student.first_name)



# Module ARG PARSE ----------------------------------------------------------------------------------

import argparse
# аргументи і опції до нашого продукту

parser = argparse.ArgumentParser(description="My first argparse")

parser.add_argument("--a", type=int, default=5, help="Left operand of summ")  # --url could be
parser.add_argument("--b", type=int, default=10, help="Right operand of summ")  #

args = parser.parse_args()

print(args.a + args.b)

# (venv) oruda@macbook-pro pythonProject % cd Lesson_11_170523
# (venv) oruda@macbook-pro Lesson_11_170523 % cd Lesson_11
# (venv) oruda@macbook-pro Lesson_11 % python lesson_11.py --a 5 --b 22

