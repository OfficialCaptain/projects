import turtle
import random
from random import randint
colors = []

for i in range(int(input("How many colors?: "))):
    colors.append('#%06X' % randint(0, 0xFFFFFF))


wn = turtle.Screen()
lorelei = turtle.Turtle()
length = 1

for i in range(70):
    color = random.choice(colors)
    lorelei.forward(length)
    lorelei.right(90)
    lorelei.color(color)
    length = length + 10
    lorelei.width(2)

wn.exitonclick()
