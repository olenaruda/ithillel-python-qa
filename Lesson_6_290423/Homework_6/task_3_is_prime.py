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


# print(is_prime(999.9))
