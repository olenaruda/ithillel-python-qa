# # 1. First task -----------------------------------------------------------------------------------
# # Існує список з іменами ["john", "marta", "james", "amanda", "marianna"],
# # перетворити рядок, щоб кожне ім'я явно починалися з великої літери.

# list_with_names = ["john", "marta", "james", "amanda", "marianna"]
# new_list = [name.title() for name in list_with_names]
#
# print(new_list)


# # 2. Second task -----------------------------------------------------------------------------------
# # Є список друзів ["John", "Marta", "James", "Amanda", "Marianna"].
# # Виведіть імена в консолі, кожен з нового рядка, вирівнюючи праву сторону,
# # використовуючи метод рядка та форматування через F String.
# # Також над іменами першим рядком виведіть NAME,
# # де NAME має бути посередині(string.center()), а решта простору заповнена символом "*"

# TITLE = "NAME"  # константи
# COUNT_OF_SYMBOLS = 30
# friends_names = ["John", "Marta", "James", "Amanda", "Marianna"]
#
# print(TITLE.center(COUNT_OF_SYMBOLS, '*'))
#
# for name in friends_names:
#     print(f"{name.rjust(COUNT_OF_SYMBOLS)}")

# friends_names = ["John", "Marta", "James", "Amanda", "Marianna"]
# title = "NAME"
#
# print(title.center(30, '*'))
#
# for name in friends_names:
#     print(f"{name.rjust(30)}")


# # 3. Third task ------------------------------------------------------------------------------------
# # У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] ,
# # перетворити його у список змінних для Пайтона snake_case, "friends_list", "my_tuple"]

# original_list = ["FirstItem", "FriendsList", "MyTuple"]
# changed_list = []
#
# for item in original_list:
#     if "FriendsList" in item:
#         new_item = "friends_list"
#         changed_list.append(new_item)
#     elif "MyTuple" in item:
#         new_item = "my_tuple"
#         changed_list.append(new_item)
#
# print(changed_list)


# # 4. Fourth task -----------------------------------------------------------------------------------
# # Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
# # Виведіть по черзі для усіх елементів словника повідомлення типу
# # My favorite programming language is Python. It was created by Guido van Rossum..
# # Видаліть, на ваш вибір, одну пару «мова: розробник» зі словника. Виведіть словник на екран.

# programming_languages = {'Javascript': 'Brendan Eich',
#                          'Python': 'Guido van Rossum',
#                          'Go': 'Robert Griesemer, Rob Pike, and Ken Thompson',
#                          'Java': 'James Gosling'}
#
# for lang, inventor in programming_languages.items():
#     print(f'My favorite programming language is {lang}. It was created by {inventor}')
#
# programming_languages.pop('Go')
# programming_languages.popitem()
# print(programming_languages)


# # 5. Fifth task ------------------------------------------------------------------------------------
# # Створіть англо-німецький словник, який називається e2g, і виведіть його на екран.
# # Слова для словника: stork / storch, hawk / falke, woodpecker / specht і owl / eule.
# # Виведіть німецький варіант слова owl. Додайте у словник, на ваш вибір, ще два слова та їхній переклад.
# # Виведіть окремо: словник; ключі і значення словника у вигляді списків.

# e2g = {'stork': 'storch', 'hawk': 'falke', 'woodpecker': 'specht', 'owl': 'eule'}
# print(f'In German the word owl is translated as: {e2g["owl"]}')
#
# e2g_extend = {'cat': 'katze', 'dog': 'hund'}
# e2g.update(e2g_extend)
# # e2g['cat'] = 'katze'
# # e2g['dog'] = 'hund'
#
# print(e2g)
# print(f'Keys of our English-German dictionary: {list(e2g.keys())}')
# print(f'Values of our English-German dictionary: {list(e2g.values())}')


# # 6. Sixth task ------------------------------------------------------------------------------------
# # Створіть багаторівневий словник subjects навчальних предметів.
# # Використайте наступні рядки для ключів верхнього рівня: 'science', 'humanities' і 'public'.
# # Зробіть так, щоб ключ 'science' був ім’ям іншого словника, який має ключі 'physics', 'computer science' і 'biology'.
# # Зробіть так, щоб ключ 'physics' посилався на список рядків зі значеннями
# # 'nuclear physics', 'optics' і 'thermodynamics'. Решта ключів повинні посилатися на порожні словники.
# # Виведіть на екран ключі subjects['science'] і значення subjects['science']['physics'].

# subjects = {'science':
#             {'physics': ['nuclear physics', 'optics', 'thermodynamics'],
#              'computer science': [],
#              'biology': []
#              },
#             'humanities': [],
#             'public': []
#             }
#
# print(f'Keys inside the dictionary \'science\' are: ')
# for key in subjects['science']:
#     print(f'{key}')
#
# print(f'\nValues inside the dictionary \'physics\' are: ')
# for value in subjects['science']['physics']:
#     print(f'{value}')


# # 7. Seventh task ----------------------------------------------------------------------------------
# # Напишіть програму, яка виводить словник, в якому ключі є числами від 1 до 15 (обидва включені),
# # а значення є квадратами ключів. Генерація ключів та значень має бути виконана через цикл.

# new_dict_for_the_task = {}
#
# for i in range(1, 16):
#     new_dict_for_the_task[i] = i ** 2
#
# print(new_dict_for_the_task)
