from pprint import pprint

import requests

# API тестування перевірити статус код і зробити маніпуляції з данними

# result = requests.get('https://www.google.com')
# print(result)
# print(result.text)

# URL = 'https://reqres.in/'

# get_result = requests.get(URL + '/api/users?page=2')
# print(get_result)  # <Response [404]>
# print(get_result.status_code)  # 404

# get_result = requests.get(URL + 'api/users?page=2')
# print(get_result)
# print(get_result.status_code)
# print(get_result.json())
#
# pprint(get_result.json())  # більш гарний json


# DATA = {
#     "name": "Morpheus",
#     "job": "leader"
# }
#
# post_result = requests.post(URL + 'api/users', data=DATA)
# print(post_result.status_code)
# pprint(post_result.json())
#
# user_id = post_result.json().get('id')
# print(f'User id - {user_id}')

# CHANGE_DATA = {
#     "name": "Olena",
#     "job": "QA"
# }
#
# put_result = requests.put(URL + 'api/users/2', data=CHANGE_DATA)
# print(put_result.status_code)
# pprint(put_result.json())
#
# get_result = requests.get(URL + 'api.users/2')
# get_result_2 = requests.get(URL + 'api.users/388')
# pprint(get_result_2.json())

#
# params_for_get = {'text': 'samsung'}
#
# get_result = requests.post('https://rozetka.com.ua/search/', params=params_for_get,
#                            headers=header,
#                            cookies=cookie,
#                            auth=)
#
# print(get_result.status_code)
# print(get_result)

STARWARS_API_URL = 'https://swapi.dev/api/'

result = requests.get(STARWARS_API_URL + 'people/1')
pprint(result.json())