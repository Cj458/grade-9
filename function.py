"""
a function is a piece of code that does a specific thing.

to create of define a function, we use the key word:

terms: 
1. define -> def
2. call -> using the func
3. parameter -> a piece of info that you give to to your function to use
4. return -> the data your function output: return

def name_of_function():
    some code....

"""

print('hello world')


# input('prompts')

def greeting(name, age) -> None:
   return f'Hello  {name} you are {age} '

def add(x, y):
    return x+y

sum = add(10, 20)

print(sum+100)


# user1 = greeting('Kamil', 13)
# print(user1)
# print('Hello')


# print()
# input()
# max()
# min()
# round()

# print()

def func():
    return 'hello'

s = func()
print(s)
