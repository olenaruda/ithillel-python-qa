# NOTES

# a = 0
# b = 1
#
# a, b = b, a
# c, d = 6, True  # max - 3 variables
#
# print(a, b, c, d)

# розпаковка ліста, сету

# my_list = [1, 2, True]
# a, b, c = my_list
#
# print(a, b, c)

# my_list = 'pop'
# a, b, c = my_list
#
# print(a, b, c)


# GIT - розподілена система керування файлами та проектами
# будь-яка зміна зафіксована
# free, fast
# репзиторій - каталог файлової системи - локальний (наш комп'ютер)
# та віддалений (зафіксувати проект у певному стані та потім його розвивати)

# git init
# 1. git status - difference between local and remote repository
# 2. git add file_name.py or Folder_1/ - додати у віддалений репозиторій, віддати під коміт
# 2. git add. - усі одразу
# git commit - фіксація певних змін
# 3. git commit -m "що ми змінювати, комент" | # git commit -m "First commit"
# 4. git push - відправити зміни у віддалений
# git push origin main

# git branch -M (master/main branch)
# git push -u origin master
#

# README.MD - файл з описом нашого проекту
# .gitignore - дозволяє не відправляти у віддалений репозиторій певний набір файлів (.idea/)
# just create file gitignore: .idea/
# бранчування - окрема гілка - незалежний стан

# ammend - зміна файлу але не зміна назви коміта


# чи можна зробити те саме з гітлабом

# ВИНЯТКИ -----------------------------------------------------------------------------

# try:
#     True  # блок коду
# except:  # якщо отримуємо помилку - потрапляємо сюди
#     ...

# print(1/0)  # ZeroDivisionError: division by zero
# print(a)  # NameError: name 'a' is not defined

short_list = [1, 2, 3]
my_index = 5

# print(short_list[my_index]) # IndexError: list index out of range

# try:
#     print(short_list[my_index])
# except:
#     print(f"Need position in range {len(short_list)}")

# try:
#     print(1/0)
# except ZeroDivisionError as zero:
#     print(f'My error {zero}')



# try:
#     print(1/0)
# except IndexError:
#     print(f'Index error')
# except ZeroDivisionError as zero:
#     print(f'My error {zero}')

### -------> raise

class OrderCountError(Exception):
    pass

orders = [1, 2, 3, 4, 5]

# if len(orders) < 10:
#     raise OrderCountError


try:
    print(1/0)
except IndexError:
    print(f'Index error')
else:
    print('Else block')
finally:
    print("Finally")
