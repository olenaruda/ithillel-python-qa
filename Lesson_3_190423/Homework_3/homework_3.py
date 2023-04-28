# 1. First task -----------------------------------------------------------------------------------
# Користувач вводить слово, якщо це слово є паліндромом, вивести '+', інакше '-'

# Option 1

word_for_check = input("Please enter your word: ")
word_palindrome = word_for_check[::-1]

if word_for_check == word_palindrome:
    print("+")
else:
    print("-")

# Option 2 (improved with check if this is a real word)

# word_for_check = input("Please enter your word: ")
#
# if word_for_check.isalpha():
#     if word_for_check == word_for_check[::-1]:
#         print("+")
#     else:
#         print("-")
# else:
#     print("This is not a word")


# 2. Second task -----------------------------------------------------------------------------------
# Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті, вивести 'YES', інакше 'NO'

# entered_text = input("Please enter your text: ")
# word_in_entered_text = input('Please enter a word that you would like to find in this text: ')
#
# if word_in_entered_text in entered_text:
#     print("YES")
# else:
#     print("NO")


# 3. Third task -----------------------------------------------------------------------------------
# Користувач водить рядок. Якщо він починається на 'abc', замінити їх на 'www', інакше додати в кінець рядка 'zzz'.

# new_line = input("Please enter your text: ")
#
# if new_line.startswith("abc"):
#     print(new_line.replace("abc", "www"))
# else:
#     print(new_line + "zzz")


# 4. Fourth task -----------------------------------------------------------------------------------
# Написати валідатор для пошти. Користувач вводить пошту, а програма повинна перевірити, що в пошті є символ '@' і '.',
# і якщо це так, вивести "YES", інакше "NO"

# email_address = input("Please enter your email address: ")
# symbol_in_email_1 = "@"
# symbol_in_email_2 = "."
#
# if symbol_in_email_1 in email_address and symbol_in_email_2 in email_address:
#     print("YES")
# else:
#     print("NO")


# 5. Fifth task -----------------------------------------------------------------------------------
# Користувач водить текст через пробіл. Конвертувати текст у список. Вивести останні 3 елементи зі списку,
# якщо список містить менше 3-х елементів, вивести повідомлення про те що кількість елементів менша за 3
# і вказати кількість елементів поточного списку

# users_text = input("Please enter your text here: ")
# users_text_list = users_text.split()
#
# if len(users_text_list) > 3:
#     print("The last 3 elements in the list are: {}".format(users_text_list[-3:]))
# else:
#     print("There are less than 3 elements in the list - only {}".format(len(users_text_list)))
