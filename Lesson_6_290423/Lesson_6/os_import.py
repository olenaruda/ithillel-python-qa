import os
import shutil

# print(os.getcwd())  # /Users/oruda/ithillel/pythonProject/Lesson_6_290423/Lesson_6
#
# print(os.cpu_count())
#
# print(os.mkdir('test'))  # параметр має бути стрінгою
#
# for _ in range(1, 10):
#     print(os.mkdir(f'test_{_}'))
#
# print(os.scandir('.'))  # усі файли в поточній директорії

# for item in os.scandir('.'):
#     new_item: os.DirEntry = item
#     print(item.name)
#     # print(item.path)


# os.mkdir('hello')

# os.remove('test')  # потрібні пермішени

shutil.rmtree('test')  # видаляє усе і не повертає