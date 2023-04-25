

"""
we use if statements to make decisions in our code

"""
name = 'Jason'

if 100>10:
    print('Hi Caleb!')

else:
    print('You are not Caleb, you are an imposter')



"""
making multiple decisions.
in python, we use the "elif" keyword to add multiple decisions

"""


name = input('What is your name?: ').lower()


if name == 'caleb':
    print('Hi, Caleb')
elif name == 'darya':
    print('Hello, miss Darya. welcome back')
elif name == 'timur':
    print('Oups, Tim is absent today')
elif name == 'alfia':
    print('Stray kids note is the best')
else:
    print('Kamil is awesome')


    # admin/ customer
    # ask a user if they are admin or customer.
    # if admin  return a list of salaries [2000, 3300, 5000]
    # if customer print hello mister Customer. 

# print(5%2) -> this is an odd number because, the remainder is 1(different than 0)
# print(4%2) -> this is an even number because, the remainder is 0