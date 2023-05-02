import math


# 1. First task --------------------------------------------------------------------------------------------------------
# Дано натуральне число N. Виведіть слово YES, якщо число N є точним ступенем двійки, або слово NO інакше.
# 8 - YES, 3 - NO

def check_power_of_two(natural_number):
    try:
        if natural_number <= 0:
            raise ValueError("A number less or equal to zero cannot be a step of two")
        if natural_number & (natural_number - 1) == 0:
            print("YES")
        else:
            print("NO")
    except ValueError as e:
        print(f'An error occurred - {e}')


natural_number_to_check = int(input("Enter a natural number: "))
check_power_of_two(natural_number_to_check)


# 2. Second task -------------------------------------------------------------------------------------------------------
# Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення (за допомогою кортежу):
# периметр квадрата, площа квадрата та діагональ квадрата.

def square(side_of_a_square: int) -> tuple:
    square_area = side_of_a_square ** 2
    perimeter = side_of_a_square * 4
    diagonal = round((side_of_a_square * math.sqrt(2)), 2)
    return square_area, perimeter, diagonal


side_of_a_square_to_check = int(input("Enter a natural number for the length of the side of a square: "))
square_details = square(side_of_a_square_to_check)
print(f'Square\'s area, perimeter and diagonal are: {square_details}')


# 3. Third task --------------------------------------------------------------------------------------------------------
# Напишіть функцію is_prime, яка приймає 1 аргумент - число від 2 до 1000,
# і повертає True, якщо це просте число, і False в іншому випадку.


def is_prime(number) -> bool:
    try:
        assert isinstance(number, (int, float))
        assert 2 <= number <= 1000
        if isinstance(number, int):
            return True
        elif isinstance(number, float):
            return False
    except AssertionError:
        print(f"Number is out of range that is supported")


print(is_prime(999.9))


# 4. Fourth task -------------------------------------------------------------------------------------------------------
# Напишіть функцію change_list, яка приймає список і змінює місця його перший і останній елемент.
# У вихідному списку щонайменше 2 елементи.

def change_list(catalogue: list) -> list:
    first_element = catalogue[0]
    last_element = catalogue[-1]
    catalogue[-1], catalogue[0] = first_element, last_element
    return catalogue


print(change_list([True, 2, 3, 4, {'test': 'third task'}]))


# 5. Fifth task --------------------------------------------------------------------------------------------------------
# Напишіть функцію to_dict(lst), яка приймає аргумент у вигляді списку і повертає словник,
# в якому кожен елемент списку є ключем і значенням.
# Передбачається, що елементи списку відповідатимуть правилам завдання ключів у словниках.


def to_dict(lst: list) -> dict:
    # list_to_dict = dict(zip(lst, lst))
    list_to_dict = {str(first_agr): second_arg for first_agr, second_arg in zip(lst, lst)}  # dict comprehension
    return list_to_dict


print(to_dict(["test", "Olena", "new_dict", True, 5, 6]))


# 6. Sixth task --------------------------------------------------------------------------------------------------------
# Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
# Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями.

def sum_range(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    my_sum: int = 0
    for i in range(start, end + 1):
        my_sum += i
    return my_sum


print(sum_range(20, 3))

# Всі завдання в окремому файлі, виклик всіх задач реалізувати у файлі main.py у конструкції if __name__ == '__main__':
