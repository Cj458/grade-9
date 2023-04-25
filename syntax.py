# print("hello world")

# # from turtle import delay
# # import requests
# # from time import delay

# # def nam():
# #     print("my name is Caleb")



# # url = "https://httpbin.org/"


# # get = requests.get(url)


# # print(delay(get))


# print(9) 

# print(4.5)



# i eat 9 apples

" i eat 9 apples"
# print("9" + 9)



import turtle
pen = turtle.Turtle()
pen.speed(10)
screen = turtle.Screen()
screen.bgcolor("Yellow")

for x in range(36):
  pen.forward(16)
  pen.right(10)

for x in range(36):
  pen.forward(12)
  pen.left(10)

pen.penup()
pen.goto(0,138)
pen.pendown()

for x in range(36):
  pen.forward(8)
  pen.left(10)

pen.penup()
pen.goto(-15,185)
pen.pendown()
pen.circle(6)

pen.penup()
pen.goto(15,185)
pen.pendown()
pen.circle(6)

pen.penup()
pen.goto(-15,160)
pen.pendown()
pen.right(80)
pen.circle(15,180)

