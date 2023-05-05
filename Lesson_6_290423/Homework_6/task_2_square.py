import math

# 2. Second task -------------------------------------------------------------------------------------------------------
# Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення (за допомогою кортежу):
# периметр квадрата, площа квадрата та діагональ квадрата.


def square(side_of_a_square: int) -> tuple:
    square_area = side_of_a_square ** 2
    perimeter = side_of_a_square * 4
    diagonal = round((side_of_a_square * math.sqrt(2)), 2)
    return square_area, perimeter, diagonal


# side_of_a_square_to_check = int(input("Enter a natural number for the length of the side of a square: "))
# square_details = square(side_of_a_square_to_check)
# print(f'Square\'s area, perimeter and diagonal are: {square_details}')
