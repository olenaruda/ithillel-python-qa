# 5. Fifth task --------------------------------------------------------------------------------------------------------
# Напишіть функцію to_dict(lst), яка приймає аргумент у вигляді списку і повертає словник,
# в якому кожен елемент списку є ключем і значенням.
# Передбачається, що елементи списку відповідатимуть правилам завдання ключів у словниках.


def to_dict(lst: list) -> dict:
    # list_to_dict = dict(zip(lst, lst))
    list_to_dict = {str(first_agr): second_arg for first_agr, second_arg in zip(lst, lst)}  # dict comprehension
    return list_to_dict


# print(to_dict(["test", "Olena", "new_dict", True, 5, 6]))