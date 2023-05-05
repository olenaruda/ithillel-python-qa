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


# natural_number_to_check = int(input("Enter a natural number: "))
# check_power_of_two(natural_number_to_check)
