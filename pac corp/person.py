"""
Inheritence.


override
extend
"""


class Employee:
    raise_rate = 2

    #constructor -> where you put your instance attributes
    def __init__(self, first_name, last_name,gender, salary, email):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.salary = salary
        self.email = email

    def raise_sal(self):
        return self.salary * self.raise_rate

#inheritance

class Developer(Employee):
   raise_rate = 5
   def __init__(self, first_name, last_name, gender, salary, email):
       super().__init__(first_name, last_name, gender, salary, email)
        

class Manager(Employee):
    raise_rate = 10
    


class Mechanic:
    pass

class Cleaner:
    pass

# employee = Employee()
dev1 = Developer('Kamil', 'Tazutdinov', 'male', 2000, 'abc@gmail.com')
new_sal =dev1.raise_sal()
print(new_sal)

manager1 = Manager('Turan', 'Turan', 'male', 4000, 'bcd@gmail.com')

cleaner = Cleaner()
# print(employee.first_name)


# founder = Ceo('Caleb', 'Jason', 26, 'male', 3000, 'Calebjason90@gmail.com')

# print(founder.salary)