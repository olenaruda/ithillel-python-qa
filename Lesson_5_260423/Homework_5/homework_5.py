# First task
# Створити реалізацію квадратного рівняння a•x²+b•x+c=0(користувач вводить a, b, c),
# якщо дискримінант від'ємний викликати виняток DiscriminantError і вивести відповідне повідомлення.

class DiscriminantError(Exception):
    pass


a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
print(f"Now we are solving {a}•x²+{b}•x+{c}=0")

discriminant = b**2 - 4*a*c

try:
    if discriminant < 0:
        raise DiscriminantError("Discriminant is negative")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"The equation has one root: x = {x}")
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f"The equation has two roots: x1 = {x1}, x2 = {x2}")
except DiscriminantError as e:
    print(f"Error occurred - {e}")


# Second task
# Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа,
# оператора (як мінімум + і -) та іншого числа, розділених пробілом (наприклад, 1 + 1). Використовуйте str.split()
# a. Якщо вхідні дані не складаються з трьох елементів, генеруйте ексепшн FormulaError.
# b. Спробуйте перетворити перший і третій елемент на float ( float_value = float(str_value)).
# Спіймайте будь-яку ValueError і згенеруйте замість нього FormulaError
# c. Якщо другий елемент не є «+» або «-», киньте ексепшн FormulaError
