# NOTES

# DICTIONARY --------------------------------------------------------------
# об'єднує певні об'єкти за взаємодією, послідовність
# ключ та значення, всі ключі унікальні (stg, int), значення - будь-який тип даних

# my_dict = {'name': 'John', 'age': 23, 'books': ['Python', 'Java'], 'id': True}
#
# print(len(my_dict))  # len - рахує тільки ключі
# print(my_dict['books'])  # рідше використовується частіше get
# print(my_dict['books'][0])
#
# print(my_dict.get('books'))
#
# # print(my_dict['bookss'])  # Exception
# # print(my_dict.get('bookss'))  # None
#
# print(my_dict.get('bookss', '!!!!'))
# # параметр відображається, чи є у словнику якийсь ключ, якщо немає - виводить '!!!!!'
# # саме цей метод рекомендується
#
#
# print(my_dict.values())  # всі значення - dict_values(['John', 23, ['Python', 'Java'], True])
# print(my_dict.keys())  # всі ключі - dict_keys(['name', 'age', 'books', 'id'])
#
# print(list(my_dict.values()))  # краще одразу форматувати в ліст
# print(list(my_dict.keys()))  # краще одразу форматувати в ліст
#
# print(tuple(my_dict.values()))
# print(tuple(my_dict.keys()))

# Об'єднання cловників

# my_dict = {'name': 'John', 'age': 23, 'books': ['Python', 'Java'], 'id': True}
# my_dict_2 = {'city': 'Kyiv', 'country': 'Ukraine'}
#
# # Option 1
# my_dict_new = my_dict | my_dict_2
# print(my_dict_new)
#
# # Option 2
# my_dict |= my_dict_2
# print(my_dict)

# my_dict = {'name': 'John', 'age': 23, 'books': ['Python', 'Java'], 'id': True}
# my_dict_2 = {'city': 'Kyiv', 'country': 'Ukraine'}
#
# my_dict.update(my_dict_2)
# print(my_dict)

# my_dict = {'name': 'John', 'age': 23, 'books': ['Python', 'Java'], 'id': True, 'city': 'Dnipro'}
# my_dict_2 = {'city': 'Kyiv', 'country': 'Ukraine'}
#
# my_dict.update(my_dict_2)  # останнє значення перезаписує перше
# print(my_dict)
#
# print(my_dict.items())
# print(list(my_dict.items()))
# # [('name', 'John'), ('age', 23), ('books', ['Python', 'Java']), ('id', True), ('city', 'Kyiv'), ('country', 'Ukraine')]
#
# print(my_dict.pop('city'))   # отримати якийсь ключ, забирає ключ значення зі словника і повертає значення
# print(my_dict.popitem())  # прибирає останнє значення

# my_dict = {'name': 'John', 'age': 23, 'books': ['Python', 'Java'], 'id': True, 'city': 'Dnipro'}
# my_dict_2 = {'city': 'Kyiv', 'country': 'Ukraine'}
#
# # last_value_in_dict = my_dict.popitem()
# # print(last_value_in_dict * 3)
# #
# # last_value_in_dict_ = my_dict.pop('name')
# # print(last_value_in_dict_ * 3)
# #
# # print(my_dict)
#
# # Додати щось до словника
#
# my_dict['zip_code'] = '02144'
# print(my_dict)
#
# # del my_dict['zip_code']
# # print(my_dict)
# #
# # print(my_dict.clear())
# # my_dict = {}
#
# # Входження у словник
# print('age' in my_dict)

### Set - множини - словник, який не має значень, або унікальний список (список з унікальними значеннями
# Set  {}

# empty_set = {}
# print(type(empty_set))  # <class 'dict'>
#
#
# empty_set = set()
# print(type(empty_set))  # <class 'set'>
#
# print(set('my_set_my_se'))
#
# my_list = [1, 23, 32, 32, 43, 1, 2, 3, 4, 2, 1, 32]
# print(set(my_list))
# print(list(set(my_list)))  # прибпати дублікати
#
# my_set = set(my_list)
# print(my_set)
# my_set_2 = my_set.add(222)
# print(my_set)
# print(list(my_set)[0])
#
# # frozenset()  # множина незмінна
#
# my_frozenset = frozenset()
# print(type(my_frozenset))  # <class 'frozenset'>

### Cycles for and while  --------------------------------------------------------------
# блок з кодом який дублюється певну кількість разів при якихось умовах

# count = 1
#
# while count <= 5:
#     print(count)
#     count += 1  # змінюємо значення на 1
#     continue
#     if count == 2:
#         name = input('Set name: ')
#         print(f'Count {count}')
#     else:
#         if name == 'Joe':
#             print(f'My name is {name}')
#             break  # перериває увесь цикл незалежно від умови
#         print('********')
#     if name == 'John':
#         print('Continue......')
#         continue  # зупиняємося у цій точці і починаємо з початку
#     print('***********')
#     print('***********')
#
# print('Finish')

# Debug - break points

# "For" cycle ------------------------------------
# ітеративно проходимося по ітерабельному об'єкту і виводимо значення елемент якоїсь послідовності (cловники, лісти, стрінги, тюпл)

# print(type(range(5)))  # <class 'range'>

# my_list = [1, 2, 3, 4, 5]

# print('My name is')
# for i in range(5): # range - клас, послідовність від нуля до 5
#     print('Olena Ruda ('  + str(i) + ')')

# print('My name is')
# for i in my_list:
#     print('Olena Ruda ('  + str(i) + ')')
#
# for i in 'my_list':
#     print(f'My value is {i}')
#
# for i in [1, 2, 3, 4, 5]:
#     print(f'My value is {i}')

# my_dict = {'name': 'John', 'age': 23, 'books': ['Python', 'Java'], 'id': True}
# for i in my_dict:
#     print(f'My value is {i}')
#
# # RANGE --------------------------------------------------------------------------------------------
#
# ages = [1, 2, 3, 4, 5]
#
# for age in ages:
#     print(f'My value is {age}')
#
# print(type(range(1))) # генерує рейндж від 0 до вказаного числа, не включаючи його
#
# a = 80
# for i in range(5, a+1, 2): # (початок, кінець, крок) - ітерації йдуть по i або j або _ якщо це щось неінформативне
#     print(f'My value is {i}')

# ENUMERATE
#
# ages = [1, 2, 3, 4, 5]
#
# for index, value in enumerate(ages, 2):
#     print(f'My value is {value} and index {index}')
#     if value == 3:
#         print(f"Finish. Index {index}")
#
# print(type(enumerate([], 1)))  # <class 'enumerate'>

# ages = [1, 2, 31, 4, 5]
# ages_2 = [14, 25, 31, 47, 54]
# ages_3 = [33, 245, 31, 437, 541]
#
# for i, j, z in zip(ages, ages_2, ages_3):
#     print(f'First list value {i}, second list value {j} and z: {z}')
#     if i == z:
#         print("Finish")
#         break
#
# print('Good')

# List comprehension and Dict comprehension
#
# my_list = []
#
# for i in range(8):
#     my_list.append(i**2)
#
# print(my_list)  # [0, 1, 4, 9, 16, 25, 36, 49]
#
# my_list_new = [x**2 for x in range(8)]  # генератор, працює швидше
# print(my_list_new)  # [0, 1, 4, 9, 16, 25, 36, 49]
#
# print(my_list == my_list_new)  # True
#
# my_list_new = [x**2 for x in range(8) if x %2 == 0]
# print(my_list_new)

# a = [x**2 if x % 2 == 0 else x**3 for x in range(10)]  # !!!!!!
# print(a)

names = ['Joe', 'Olena', 'Kate', 'Jane']
ages = [14, 25, 31, 47, 54]

my_dict = {name: age for name, age in zip(names, ages)}  # Dict comprehension

print(my_dict)

new_dict_2 = dict(zip(names, ages))
print(new_dict_2)


# 8. Additional task ----------------------------------------------------------------------------------

# Для тих хто бажає ще ДЗ можете написати програму "сортування бульбашкою". Опис алгоритму сортування бульбашкою:
# Алгоритм полягає в циклічних проходах по масиву, за кожен прохід елементи масиву попарно порівнюються і,
# якщо їх порядок неправильний, то здійснюється обмін. Обхід масиву повторюється до тих пір,
# поки масив не буде впорядкований.
