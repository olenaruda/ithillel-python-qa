# XML JSON YAML

# YAML - можна залишати коментарі

import json
import yaml
from pprint import pprint

users = [{'name': 'Joe'},
         {'name': 'Jack'}]

# yaml_obj = yaml.dump(users)
# print(yaml_obj)
# print(type(yaml_obj))  # <class 'str'>


# .yaml, .yml

with open('my_yaml.yaml', 'w') as f:
    data = yaml.dump(users, f)
