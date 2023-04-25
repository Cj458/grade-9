import math 
import turtle as t
import turtle
import random

win_width = 500
win_height = 500

turtles = 8

t.screensize(win_width, win_height)

class Racer(object):
    def __init__(self, color, pos):
        self.pos = pos
        self.color = color
        self.turt = t.Turtle()
        self.turt.shape('turtle')
        self.turt.color(color)
        self.turt.penup()
        self.turt.setpos(pos)
        self.turt.setheading(90)

    def move(self):
        r = random.randrange(1, 3)
        self.pos = (self.pos[0], self.pos[1] + r)
        self.turt.pendown()
        self.turt.forward(r)

    def reset(self):
        self.turt.penup()
        self.turt.setpos(self.pos)


def setup_file(name, colors):
    file = open(name, 'w')
    for color in colors:
        file.write(color + '0\n')
    file.close()


def start_game():
    t_list = []
    turtle.clearscreen()
    turtle.hideturtle()
    colors = ["red", "green", "blue", "yellow", "pink", "orange", "purple", "black"]
    start = -(win_width/2) + 20

    for tu in range(turtles):
        new_posx = start + tu*(win_width)//turtles
        t_list.append(Racer(colors[tu], (new_posx, -230)))
        t_list[tu].turt.showturtle()

    user_guess = input('''who would you like to bet on? 
    red
    yellow
    purple
    orange
    blue
    green
    pink
    black
    ''').lower()
    run = True
    while run:
        for t in t_list:
            t.move()

        maxColor = []
        maxDis = 0
        for t in t_list:
            if t.pos[1] > 230 and t.pos[1] > maxDis:
                maxDis = t.pos[1]
                maxColor = []
                maxColor.append(t.color)

            elif t.pos[1] > 230 and t.pos[1] == maxDis:
                maxDis = t.pos[1]
                maxColor.append(t.color) 

        if len(maxColor) > 0:
            run = False
            for win in maxColor:   
                    print('Sorry broooo, minus 10 r from your account', 'the winner was',win)

    old_score = []
    file = open('scores.txt', 'r')
    for line in file:
        l = line.split()
        color = l[0]
        score = l[1]
        old_score.append([color, score])
    file.close()

    file = open('scores.txt', 'w')

    for entry in old_score:
        for winner in maxColor:
            if entry[0] == winner:
                entry[1] = int(entry[1] + 1)
        file.write(str(entry[0]) + ' ' + str(entry[1]) + '\n')

    file.close()


start = input('Would you like to play? y/n').lower()

if start == 'y':

    start_game()
# for winner in max
while True:
    print('------------------------')
    start = input('Would you like to play again? y/n').lower()
    if start == 'y':
        start_game()
    else:
        break




