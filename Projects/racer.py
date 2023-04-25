from turtle import *
from random import randint
import time


speed(0)
penup()

goto(-140, 140)


for step in range(15):
    write(step, align='center')
    right(90)
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

jim =Turtle()
jim.color('red')
jim.shape('turtle')

jim.penup()
jim.goto(-160, 100)
jim.pendown()

for turn in range(10):
    jim.right(36)


bob =Turtle()
bob.color('green')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(72):
    bob.right(5)


james =Turtle()
james.color('blue')
james.shape('turtle')

james.penup()
james.goto(-160, 40)
james.pendown()

for turn in range(60):
    james.right(6)

masha =Turtle()
masha.color('orange')
masha.shape('turtle')

masha.penup()
masha.goto(-160, 10)
masha.pendown()

for turn in range(30):
    masha.right(12)



for turn in range(100):
    jim.forward(randint(1,5))
    bob.forward(randint(1, 5))
    james.forward(randint(1, 5))
    masha.forward(randint(1, 5))
    time.sleep(0.2)


exitonclick()

