# 4. Fourth task -------------------------------------------------------------------------------------------------------
# Напишіть функцію change_list, яка приймає список і змінює місця його перший і останній елемент.
# У вихідному списку щонайменше 2 елементи.


def change_list(catalogue: list) -> list:
    first_element = catalogue[0]
    last_element = catalogue[-1]
    catalogue[-1], catalogue[0] = first_element, last_element
    return catalogue


# print(change_list([True, 2, 3, 4, {'test': 'third task'}]))