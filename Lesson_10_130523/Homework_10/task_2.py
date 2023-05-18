import datetime

# Створити декоратор який кожен раз буде записувати у файл результат роботи якоїсь функції після її виклику
# (наприклад функція яка прораховує суму всіх переданих аргументів *args).
# Запис в файл формату ""Function launched at {час запуску} with result {результат роботи функції}


def write_to_file_decorator(func):
    def wrapper(*args):
        result = func(*args)
        launch_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open("function_results.txt", "a") as file:
            file.write(f"Function launched at {launch_time} with result {result}\n")
        print(f'File \"function_results.txt\" with function results has been created')
    return wrapper


@write_to_file_decorator
def sum_args(*args):
    return sum(args)


sum_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
