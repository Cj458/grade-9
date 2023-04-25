"""
Object Oriented Programming

1. class -> a class is like an object constructor, or a factory, 
or a blueprint for creating objects
a class has:
1. attribute or properties
2. methods(function)

# dunder methods: __init__(), __str__()


2. inheritance
"""
class Human:
    # constructor
    def __init__(self, iq, name, gender, race):
        self.iq = iq
        self.name = name
        self.gender = gender
        self.race = race

    def __str__(self):
        return f'{self.name} {self.race} {self.gender} {self.iq}'
   

   #method
    def talk(self, language):
        print('I speak', language)

    def walk(self):
        print('I can walk on my 2 legs')

    def eat(self):
        print('I can eat all the food in the world')



human1 = Human(289, 'Kamil', 'male', 'white')
human1.talk('Chinese')

print(human1)

human2 = Human(49, 'feng cheng', 'male', 'asian')

# class Car:
#     speed = 335



# ferrari = Car()

# mercedes = Car()

# print(ferrari.speed, mercedes.speed)

