import json

# Знайти ідентифікатор групи, де знаходиться найбільша кількість жінок, народжених після 1977 року.
# Як відповідь необхідно вказати через пробыл ідентифікатор знайденої групи і скільки в ній було жінок,
# народжених після 1977 року. Файл group_people.json

with open('group_people.json', 'r') as json_file:
    data_people = json.load(json_file)

max_women = 0
group_id = None

for group in data_people:
    women_count = 0
    for person in group['people']:
        if person['gender'] == 'Female' and person['year'] > 1977:
            women_count += 1
        if women_count > max_women:
            max_women = women_count
            group_id = group['id_group']

print(f'{group_id} {max_women}')