import turtle as trtl
import random

painter = trtl.Turtle()

colors = ['#FF0000','#FF7F00','#FFFF00']

painter.color('black', 'yellow')
painter.begin_fill()
painter.forward(100)
painter.left(90)
painter.forward(100)
painter.left(90)
painter.forward(100)
painter.left(90)
painter.forward(100)
painter.end_fill()
painter.penup()
painter.goto(25,0)
painter.left(180)
painter.color('black')
painter.pendown()
painter.forward(25)
painter.right(90)
painter.forward(25)
painter.right(90)
painter.forward(25)
painter.left(90)
painter.forward(25)
painter.end_fill
painter.penup()
painter.goto(50,0)
painter.pendown()
painter.forward(25)
painter.left(90)
painter.forward(25)
painter.left(90)
painter.forward(25)
painter.penup()
painter.goto(0,100)
painter.right(135)
painter.pendown()
painter.color('white', '#560c01')
painter.begin_fill()
painter.forward(70)
painter.right(90)
painter.forward(70)
painter.end_fill()
painter.penup()
painter.goto(40,75)
painter.pendown()
painter.color('black', '#26619c')
painter.begin_fill()
painter.circle(10)
painter.end_fill()
painter.penup()
painter.goto(200,0)
painter.color('black', '#964B00')
painter.left(45)
painter.begin_fill()
painter.forward(30)
painter.left(90)
painter.forward(40)
painter.left(90)
painter.forward(30)
painter.left(90)
painter.forward(40)
painter.end_fill()
painter.penup()
painter.goto(180,40)
painter.left(90)
painter.pendown()
painter.color('#42692F')
painter.begin_fill()
painter.forward(70)
painter.left(100)
painter.forward(160)
painter.end_fill()
painter.penup()

window = trtl.Screen()
window.bgcolor('#87ceeb')
window.mainloop()