class Animal:
    def __init__(self, name, species, age, gender, hunger_level, happiness_level):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender
        self.hunger_level = hunger_level
        self.happiness_level = happiness_level
        
    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nAge: {self.age}\nGender: {self.gender}\nHunger level: {self.hunger_level}\nHappiness level: {self.happiness_level}\n"
        

class Shelter:
    def __init__(self):
        self.animals = []
        
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} has been added to the shelter.")
        
    def feed_animal(self, animal):
        if animal in self.animals:
            animal.hunger_level -= 1
            animal.happiness_level += 1
            print(f"{animal.name} has been fed.")
        else:
            print(f"{animal.name} is not in the shelter.")
            
    def play_with_animal(self, animal):
        if animal in self.animals:
            animal.happiness_level += 1
            print(f"{animal.name} has been played with.")
        else:
            print(f"{animal.name} is not in the shelter.")
            
    def adopt_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} has been adopted.")
        else:
            print(f"{animal.name} is not in the shelter.")
            
    def display_animals(self):
        if self.animals:
            for animal in self.animals:
                print(animal)
        else:
            print("There are no animals in the shelter.")
            
            
# Example usage
animal1 = Animal("Fluffy", "Cat", 2, "Female", 3, 5)
animal2 = Animal("Buddy", "Dog", 3, "Male", 2, 6)
shelter1 = Shelter()
shelter1.add_animal(animal1)
shelter1.add_animal(animal2)
shelter1.feed_animal(animal1)
shelter1.play_with_animal(animal2)
shelter1.adopt_animal(animal1)
shelter1.display_animals()




# school = School()

# print('Welcome to AIS record system')


# command = ''

# while command != 'exit':
#     command = input(' what action do you want to take? (add, get, delete and update): ')
#     if command == 'add':
#         name = input('Name: ')
#         age = input('Age: ')
#         grade_level = input('Grade: ')
#         school.add_student(name, age, grade_level)

#     elif command == 'delete':
#         pass

#     elif command == 'get':
#         pass

#     elif command == 'update':
#         pass