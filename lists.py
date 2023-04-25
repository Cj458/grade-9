"""
collection data types -> LIST, TUPLE, DICT, SET -> 
"""

students = ['Alfia', 'Tim', 'Turan', 'Kamil', 'Isaf']

salaries = [2500, 2500, 2000]

everything = ["Alfia", 2500, True]


# to create a list in python, we use square bracket -> [], list()

# use list()


my_list = []



todo_list = ['1) Go to school', '2) Clean my room', '3) Talk to a friend', '4) buy groceries']
# print(todo_list)


# accessing an item from your list -> indexing: your_list[index]

todo_list = ['Go to school', 'Clean my room', 'Talk to a friend', 'buy groceries', 'go to bed at 10.00']
#               0                      1                     2                   3                       4

# print(dir(todo_list))


# adding an element to a list -> append(), insert()

# append(): it adds an item to the end of the list

todo_list.append('6) Take a shower')


print(todo_list)

# insert():

todo_list.insert(4, 'Take a shower')

print(todo_list)

#operators

a = ['a', 'b']

b = ['c', 'd']

# b.append(a)
# print(b)