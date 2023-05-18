import time
import datetime


# Створити декоратор який вимірює час виконання функції


def execution_time_decorator(func):
    def my_wrapper(*args):
        start_time = datetime.datetime.now()
        func(*args)
        end_time = datetime.datetime.now()
        execution_time = end_time - start_time
        print(f"The function {func.__name__} took {execution_time} seconds to execute.")
    return my_wrapper


@execution_time_decorator
def check_power_of_two(natural_number):
    time.sleep(3)
    try:
        if natural_number <= 0:
            raise ValueError("A number less or equal to zero cannot be a step of two")
        if natural_number & (natural_number - 1) == 0:
            print("YES")
        else:
            print("NO")
    except ValueError as e:
        print(f'An error occurred - {e}')


check_power_of_two(365787908343)
