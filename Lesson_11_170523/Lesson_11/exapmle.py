from random import choice

# NEW METHOD

class Person:

    def __new__(cls, *arg, **kwargs):
        instance = super().__new__(cls)
        return

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


person = Person('Joe', 'Coen')
print(person.first_name)


class A:

    this_is_attribute = ''

    def __new__(cls, *args, **kwargs):
        other = choice([Dog, Cat])
        instance = super().__new__(other)
        return instance

    def __init__(self, name):
        self.name = name


class Cat:

    def say(self):
        print('Meo')


class Dog:

    def say(self):
        print('Woof')


a = A('Joe')
a.say()