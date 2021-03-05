''' Jacob Faulstich, 3/1/21
The purpose of the program is to have the user inpit their missing value of a right triangle. 
The Program should first draw a traingle and assign vaiable to each side, then ask for inputs/.
With this information the prigram should be able to caluclate the area, permiter, and the value of the missing side.
To make the program more appealing the colors of the letters change.
    '''


#-----import statements-----
import turtle as trtl
import math #Imports a library for commands to do math
import random # Imports a library for commands to randomly do things



#-----game configuration----
speed = 0
width = 2
font_setup = ("Arial", 20, "normal")
colors = ['#8B0000', '#FF8247', '#FF9912', '#7FFF00', '#27408B', '#8B008B']
wn = trtl.Screen()

#-----initialize turtle-----
triangle = trtl.Turtle()
triangle.hideturtle()
triangle.speed(speed)
triangle.width(width) #This is used to change the thickness of the line that the turtle draws


c = trtl.Turtle()
c.hideturtle()
c.speed(speed)
c.width(width)
c.penup()
c.color(random.choice(colors))

b = trtl.Turtle()
b.hideturtle()
b.speed(speed)
b.width(width)
b.penup()
b.color(random.choice(colors))

a = trtl.Turtle()
a.hideturtle()
a.speed(speed)
a.width(width)
a.penup()
a.color(random.choice(colors))

writer = trtl.Turtle()
writer.hideturtle()
writer.speed(speed)
writer.width(width)
writer.penup()

#-----game functions--------
def draw_triangle():
    triangle.forward(200)
    triangle.left(135)
    triangle.forward(283)
    triangle.left(135)
    triangle.forward(200)
    triangle.left(90)
    triangle.forward(15)
    triangle.left(90)
    triangle.forward(15)
    triangle.left(90)
    triangle.forward(15)

def draw_c():
    c.goto(115,110)
    c.write("c", font = font_setup)


def draw_b():
    b.goto(72, -35)
    b.write("b", font = font_setup)


def draw_a():
    a.goto(-25, 72)
    a.write("a", font = font_setup)

def draw_diagram():
    draw_triangle()
    draw_a()
    draw_b()
    draw_c()

def missing_var():
    missing = wn.textinput("Missing variable:", "What is your missing variable?")
    if (missing == "a"):
        b = wn.textinput("B value:", "What is your b value?")
        b = float(b)
        c = wn.textinput("C value:", "What is your c value?")
        c = float(c)
        a_missing_leg(b,c)
    elif (missing == "b"):
        a = wn.textinput("A value:", "What is your a value?")
        a = float(a)
        c = wn.textinput("C value:", "What is your c value?")
        c = float(c)
        b_missing_leg(a,c)
    elif (missing == "c"):
        a = wn.textinput("A value:", "What is your a value?")
        a = float(a)
        b = wn.textinput("B value:", "What is your b value?")
        b = float(b)
        c_missing_leg(a,b)
    else:
        writer.goto(0,-100)
        writer.write("Not in my programming", font= font_setup)


def a_missing_leg(b,c):
    c2 = (c**2)
    b2 = (b**2)
    a2 = c2 - b2
    a = math.sqrt(a2)
    writer.goto(0,-100)
    writer.write("A=", font = font_setup)
    writer.goto(30, -100)
    writer.write(a, font=font_setup)
    area(a,b,c)
    perimeter(a,b,c)


def b_missing_leg(a,c):
    c2 = (c**2)
    a2 = (a**2)
    b2 = c2 - a2
    b = math.sqrt(b2)
    writer.goto(0,-100)
    writer.write("B=", font = font_setup)
    writer.goto(30, -100)
    writer.write(b, font=font_setup)
    area(a,b,c)
    perimeter(a,b,c)

def c_missing_leg(a,b):
    a2 = (a**2)
    b2 = (b**2)
    c2 = a2 + b2
    c = math.sqrt(c2)
    writer.goto(0,-100)
    writer.write("C=", font = font_setup)
    writer.goto(30, -100)
    writer.write(c, font=font_setup)
    area(a,b,c)
    perimeter(a,b,c)


def area(a,b,c):
    area = 0.5 * b * a
    writer.goto(0, -150)
    writer.write("Area=", font=font_setup)
    writer.goto(60, -150)
    writer.write(area, font=font_setup)

def perimeter(a,b,c):
    perimeter = a + b + c
    writer.goto(0, -200)
    writer.write("Perimeter=", font=font_setup)
    writer.goto(100, -200)
    writer.write(perimeter, font=font_setup)



#-----events----------------
draw_diagram()
missing_var()
wn.mainloop()
