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


# print(sum_range(20, 3))