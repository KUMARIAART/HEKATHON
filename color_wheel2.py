from turtle import*
import turtle
t=Turtle()
wn=Screen()
wn.title("COLOR WHEEL")
wn.bgcolor("BLACK")
colors=["red","blue","pink","skyblue","yellow","violet","green","orange"]
import random
t.backward(250)
t.speed(0)
t.width(5)
t.begin_fill()
for i in range (99):
    colorchoice=random.choice(colors)
    t.color(colorchoice)
    t.forward(600)
    t.right(170)
t.end_fill() 
Turtle.done()
