import random
import string


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

#     print('Game Over!')
#     print(f'the number was {random_number}')
#     break
# else:
#   print(f" congratulations! {guess} was the correct number. ")



adjectives = ['sleepy', 'slow', 'wet', 'fat', 'red', 'interesting','exhausting', 'fast', 'dry', 'thin', 'tremendous', 'luxurious']
nouns = ['cat', 'dog', 'jenitor', 'teacher', 'gamer', 'bear', 'phone', 'charger', 'cake', 'motorbike']
uppers = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowers = list('abcdefghijklmnoprstuvwxyz')


characters = list("""!@#$%^&*(_)+=][}{;:.<>?'-/\,""")

print('Welcome to password generator!')

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    character = random.choice(characters)
    upper = random.choice(uppers)
    lower = random.choice(lowers)

    pwd = adjective+noun+ str(number)+ character + upper+ lower

    print(f'Your password is {pwd}')

    res = input('Would you like another password? Type y or n: ')

    if res == 'n':
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