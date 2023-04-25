"""
1. Arithmetic operators:

+  addition
- substraction
* mult
/ float division
// integer division
% modulo operator  = gives you the remainder of a division

"""


print(12%2)


"""
2. comparision operators -> boolean (True or False)
> greater than
< less
== equal
>= greater or equal to
<= less or equal to
!= not equal to

"""




# x = 10
# y = 100

# if x == y:
#     x+= 200

# print(x)



"""
3. logical operators

and -> True if both statementы are True, otherwise False
or -> True if either one of the statement is True, false if both statements are false
"""



# Boy and 18 -> True

boy = True
age_18 = True

if boy and age_18:
    True
else:
    print('не годен')


"""
4. Membership operator

in -> returns  True if the item is found in the collection(list) otherwise -> False.
not in 
"""


# create a list of color: black, white, brown, yellow, pink
# using the input(), ask the user to enter his favorite color,
# then check if the color is in your list of color then print('We have a common favorite color'), 
# if the color is not in the list of color, then print("Too bad we don't share a common color")



love_minecraft = False

print(not love_minecraft)


print(True and True)