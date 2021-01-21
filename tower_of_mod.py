''' Jacob Faulstich
This program uses the turtle module to draw a tower with different colored floors based 
on the number of the floor. Ex. all even floors blue, all odd floor grey.
'''
# set the turtle X
# set tower width
# set tower height
# set floor counter
# while floor number us less than tower height
#   if the floor number is an even multiple of 5
#       set the color to grey
#    else
#       set the color to blue
# move the painter forward tiwer width
# increase the floor number
# move the painter backwars the tower width

import turtle as trtl

rem = 0
switcher = 20
floor_height = 5
tower_width = 150
x = -150
y = -150

dill = trtl.Turtle()
dill.speed(0)
dill.pensize(floor_height)

height = 80
floor = 0

while floor < height:
    dill.penup()
    dill.goto(x,y)
    rem = floor % switcher
    if rem >= (switcher /  2):
        dill.color("blue")
    else:
        dill.color("grey")
    y += floor_height
    floor += 1
    dill.pendown()
    dill.forward(tower_width)

window = trtl.Screen()
window.mainloop
