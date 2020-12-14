import turtle as trtl

painter = trtl.Turtle()

# Sets the speed of drawing
painter.speed(0)

# Draws the grey rectangle rocket body
painter.color('grey')
painter.begin_fill()
painter.forward(100)
painter.right(90)
painter.backward(150)
painter.right(90)
painter.forward(100)
painter.left(90)
painter.forward(150)
painter.backward(150)
painter.end_fill()

# Draws the red triangle rocket top
painter.left(135)
painter.pencolor('#8b0000')
painter.color('#8b0000')
painter.begin_fill()
painter.forward(70)
painter.right(90)
painter.forward(71)
painter.right(135)
painter.forward(100)
painter.end_fill()

# Sets the position to draw left fin
painter.penup()
painter.goto(0,0)
painter.right(90)
painter.forward(50)
painter.left(135)
painter.pendown()

# Draws blue fin left
painter.color('#26619c')
painter.pencolor('#26619c')
painter.begin_fill()
painter.forward(70)
painter.left(135)
painter.forward(50)
painter.left(90)
painter.forward(50)
painter.end_fill()

# Sets the position of the right fin
painter.penup()
painter.goto(100,0)
painter.forward(50)
painter.right(135)
painter.pendown()

# Draws right blue fin
painter.begin_fill()
painter.forward(70)
painter.right(135)
painter.forward(50)
painter.right(90)
painter.forward(50)
painter.end_fill()

# Sets the positon for my windown
painter.penup()
painter.left(90)
painter.goto(50,125)

# Draws the light blue circle window
painter.color('white', 'light blue')
painter.pendown()
painter.begin_fill()
painter.circle(25)
painter.end_fill()

# Sets the position for  moon
painter.penup()
painter.goto(-200,250)
painter.pendown()

# Draws the moon
painter.color('black', 'white')
painter.begin_fill()
painter.circle(50)
painter.end_fill()

# Sets color and position for  star
painter.penup()
painter.color('#DAA520')
painter.pencolor('#DAA520')
painter.goto(300,200)
painter.pendown()

# Draws yellow star
painter.begin_fill()
painter.forward(100)
painter.right(144)
painter.forward(100)
painter.right(144)
painter.forward(100)
painter.right(144)
painter.forward(100)
painter.right(144)
painter.forward(100)
painter.right(144)
painter.end_fill()

# Sets color and location for flames
painter.penup()
painter.goto(0,0)
painter.pendown()
painter.color('yellow', 'orange')

# Draws flames
painter.begin_fill()
painter.left(135)
painter.forward(20)
painter.goto(25,0)
painter.forward(20)
painter.goto(50,0)
painter.forward(20)
painter.goto(75,0)
painter.forward(20)
painter.goto(100,0)
painter.left(225)
painter.forward(100)
painter.end_fill()
painter.penup()

# Draws tiny white dot
painter.goto(150,220)
painter.color('white', 'white')
painter.begin_fill()
painter.pendown()
painter.circle(2)
painter.end_fill()
painter.penup()

# Draws tiny white dot
painter.goto(-10,-300)
painter.color('white', 'white')
painter.begin_fill()
painter.pendown()
painter.circle(2)
painter.end_fill()
painter.penup()

# Draws tiny white dot
painter.goto(-30,-320)
painter.color('white', 'white')
painter.begin_fill()
painter.pendown()
painter.circle(2)
painter.end_fill()
painter.penup()

# Draws tiny white dot
painter.goto(50,280)
painter.color('white', 'white')
painter.begin_fill()
painter.pendown()
painter.circle(2)
painter.end_fill()
painter.penup()

# Draws tiny white dot
painter.goto(180,-220)
painter.color('white', 'white')
painter.begin_fill()
painter.pendown()
painter.circle(2)
painter.end_fill()
painter.penup()

# Draws tiny white dot
painter.goto(-150,-220)
painter.color('white', 'white')
painter.begin_fill()
painter.pendown()
painter.circle(2)
painter.end_fill()
painter.penup()

# Draws tiny white dot
painter.goto(0,-50)
painter.color('white', 'white')
painter.begin_fill()
painter.pendown()
painter.circle(2)
painter.end_fill()
painter.penup()

# Draws tiny white dot
painter.goto(250,0)
painter.color('white', 'white')
painter.begin_fill()
painter.pendown()
painter.circle(2)
painter.end_fill()
painter.penup()

# Draws tiny white dot
painter.goto(-250,-20)
painter.color('white', 'white')
painter.begin_fill()
painter.pendown()
painter.circle(2)
painter.end_fill()
painter.penup()

# Takes the painter off the screen
painter.penup()
painter.goto(500,500)

window = trtl.Screen()
window.bgcolor('#414a4c')
window.mainloop()