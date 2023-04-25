# What is a method?

my_string = 'Caleb is our python teacher'


# upper case
print(my_string.upper())


# lower case
print(my_string.lower())


# white space removal
print(my_string.strip())

# replace a character in a string

print(my_string.replace('Caleb', 'Jason'))

# len
print(len(my_string))


# split

print(my_string.split())

# join substrings together


a = '-'.join(my_string)
print(a)

# password = input('Enter your password: ')

# if len(password) < 8:
#     print('your password should be at least 8 characters long')

# else:
#     print(password)


# print(dir(my_string))


# print(dir(my_string))


# String formatting

# concatination: +

# print('hello ' + 'there')


# f string

# first_name = 'Caleb '

# last_name = 'Jason'

# print(f'Hello {first_name} {last_name} how are you today')


# type casting

name = input('Enter your name: ')

year_of_birth = input('When were your born: ')
year_of_birth = '1996'

age = 2022 - int(year_of_birth)

print(f' hello {name}, you are {age}')


# Write a program that asks someone's weight in lbs then convert into kg

# your homework was ---> a madlib 
