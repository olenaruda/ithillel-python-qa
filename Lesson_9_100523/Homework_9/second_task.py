import json

# Знайти найуспішнішого менеджера за підсумковою сумою продажів.
# Як відповідь потрібно через пробыл вказати спершу його ім'я, потім прізвище і після загальну суму його продажів.
# Файл manager_sales.json

with open('manager_sales.json', 'r') as json_file:
    sales = json.load(json_file)

max_sales = 0
best_manager_name = ''
best_manager_surname = ''

for manager in sales:
    manager_name = manager['manager']['first_name']
    manager_surname = manager['manager']['last_name']
    sum_of_sales = sum([car['price'] for car in manager['cars']])
    if sum_of_sales > max_sales:
        max_sales = sum_of_sales
        best_manager_name = manager_name
        best_manager_surname = manager_surname

print(f'{best_manager_name} {best_manager_surname} {max_sales}')