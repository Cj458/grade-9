import turtle 
import random
"""
1. Counting loops
the keyword 'for' is used in python to create a counting loop(a type of loop that repeat a certain number of time)

loop variable: variable that keeps tack of how many times we have repeated a action
"""



# language = 'Python'
# for x in language:
#   print(f'{x} - I am studying, DO NOT DISTURB')

#   # x -> loop variable


# print('====================================')


# for x in range(1, 11):
#   print(f'{x} - I am studying, DO NOT DISTURB')

# t = turtle.Turtle()
# t.speed(10)
# t.shape('turtle')

# screen = turtle.Screen()
# screen.bgcolor('green')

# for x in range(36):
#   t.forward(16)
#   t.right(10)


# for x in range(36):
#   t.forward(12)
#   t.left(10)

# t.penup()
# t.goto(0, 138) 
# t.pendown()

# for x in range(36):
#   t.forward(10)
#   t.left(10)

# # left eye
# t.penup()
# t.goto(-15, 185)
# t.pendown()
# for x in range(36):
#   t.forward(2)
#   t.left(10)

# # right eye
# t.penup()
# t.goto(15, 185)
# t.pendown()
# for x in range(36):
#   t.forward(2)
#   t.left(10)

# # mouth

# t.penup()
# t.goto(-15, 160)
# t.pendown()
# t.right(80)
# t.circle(15, 180)






# turtle.exitonclick()



"""
2. Conditional loops or while loop
the keyword is 'while'

it's a type of loop that runs as long as the condition is True

break => tells python to stop and break out of a loop given a condition
continue
"""



# exercise one

# random_number = random.randint(0, 100)
# guess = int(input(" I'm thinking of a number from 0 to 100. what is it?: "))


# life = 5
# number_if_tries = 0

# while guess != random_number:
#   if guess < random_number:
#     print('Your guess is too low...')
#   elif guess > random_number:
#     print('Your guess is too high...')
#   guess = int(input('Try again... '))
#   life -= 1
#   if life == 0:

#     print('You died')
#     break
# else:
#   print(f" congratulations! {guess} was the correct number. ")


# exercise 2 -> a passwoord generator

adjectives = ['boring', 'exciting', 'red', 'wet', 'big', 'interesting','exhausting', 'fast', 'dry', 'thin', 'tremendous', 'luxurious']
nouns = ['cat', 'jenitor', 'teacher', 'gamer', 'bear', 'doggo', 'glasses']
uppers = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowers = list('abcdefghijklmnoprstuvwxyz')
characters = list(""""!@#$%^&*(_)+=][}{;:.<>?'""")

print('Welcome to password generator! We will help create a secure and strong password.')



while True:
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    upper = random.choice(uppers)
    lower = random.choice(lowers)
    char = random.choice(characters)
    number = random.randrange(0, 100)

    pwd = adj + noun + upper + lower + char + str(number)

    print(f"your password is: {pwd}")

    break









































# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(10)

# sc = turtle.Screen()
# sc.bgcolor('navy')

# #base circle
# t.pencolor('black')
# t.fillcolor('white')

# t.begin_fill()
# for i in range(36):
#   t.forward(16)
#   t.right(10)
# t.end_fill()

# t.begin_fill()
# for i in range(36):
#   t.forward(12)
#   t.left(10)
# t.end_fill()

# t.penup()
# t.goto(0,130)
# t.pendown()
# t.begin_fill()
# for i in range(36):
#   t.forward(9)
#   t.left(10)
# t.end_fill()

# t.penup()
# t.goto(-20,200)
# t.pendown()
# t.circle(4)
# t.penup()
# t.goto(20,200)
# t.pendown()
# t.circle(4)
# t.penup()
# t.goto(-25,170)
# t.pendown()
# t.right(90)
# for i in range(19):
#   t.forward(5)
#   t.left(10)

# t.hideturtle()

# turtle.mainloop()