import json
import os

# NOTES

# Create files
# file = open('hellow_world.txt', 'w')   # файл створюється якщо його немає чи перезаписується повністю якщо вже є, "w" - це перезатирання
# file.write('Hello world!')
# file.write('Another Hello world!')
# file.close()  # обов'язково потрібно закривати файл
#
# # Write in
#
# file.read(5)  # буде читати з 6 символу
# file.seek(0, 2)  # курсор читання


# Exceptions ----------------------------------------------------------------------------------

# FileNotFoundError
# UnicodeDecodeError
# OSError, IOError

# filename = 'hellow_world.txt'
# try:
#     file = open(filename, 'r')
#     first_5_symbols = file.read(5)
#     print(f'First 5 symbols from file: {first_5_symbols}')
#     file.close()
#
# except (OSError, IOError) as e:
#     print(f'Unexpected error found during work with: {filename}\nError: {e}')

# context manager
# with open("") as file

# magic methods:
# __enter__()
# __exit__()

# serialization - збереження у тимчасовий файл, читання звідти - десеріалізація

# file system
# os.getcwd()  - путь относительно текущей директории
# os.chdir('..')
# os.scandir(new_current_dir)
# os.path.abspath
print(os.path.abspath('...'))

# генератор та ітератор, рекурсия функция