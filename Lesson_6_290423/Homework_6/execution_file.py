from homework_6 import check_power_of_two, square, is_prime, change_list, to_dict, sum_range

if __name__ == '__main__':
    natural_number_to_check = int(input("Enter a natural number: "))
    check_power_of_two(natural_number_to_check)

    side_of_a_square_to_check = int(input("Enter a natural number for the length of the side of a square: "))
    square_details = square(side_of_a_square_to_check)
    print(f'Square\'s area, perimeter and diagonal are: {square_details}')

    print(is_prime(999.9))

    print(change_list([True, 2, 3, 4, {'test': 'third task'}]))

    print(to_dict(["test", "Olena", "new_dict", True, 5, 6]))

    print(sum_range(1, 3))

