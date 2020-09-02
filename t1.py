import turtle
import random
from random import randint
colors = []

for i in range(int(input("How many colors?: "))):
    colors.append('#%06X' % randint(0, 0xFFFFFF))




wn = turtle.Screen()
wn.bgcolor("black")
lorelei = turtle.Turtle()
length = 1
hakan = turtle.Turtle()

for i in range(70):
    color = random.choice(colors)
    lorelei.forward(length)
    lorelei.right(90)
    lorelei.color(color)
    length = length + 5
    lorelei.width(2)
    lorelei.speed(200)
    hakan.forward(length)
    hakan.right(360)
    hakan.left(90)
    hakan.color(color)
    length = length + 5
    hakan.width(2)
    hakan.speed(100)

wn.exitonclick()
