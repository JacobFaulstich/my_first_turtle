import turtle as trtl

jeb = trtl.Turtle()
ben = trtl.Turtle()
#Makes the draiwng go fast
jeb.speed(100)

'''r = input("What radius do you want to use for your circle? Less than 10 ")
r = int(r)
outC = input("What color do you want your outline? ")
fillC = input("What color do you want to fill your circle with? ")
jeb.color(outC, fillC)
jeb.begin_fill()
jeb.circle(r)
jeb.end_fill()'''
# asks for input for color of ornament
or1 = input("What color do you want the ornaments outline to be? ")
or2 = input("What color do you want the fill of the ornament to be? ")
r1 = float(input("What do you want the radius of the ornaments to be? Less than 7. "))
str1 = input("What color do you want the outline of the star? ")
str2 = input("What color do you want the fill of the star? ")
present1 = input(" What do you want your present fill color to be? ")
present2 = input(" What do you want your present stripe to be? ")
i = 0
w = 0

#Draws brown stump 
jeb.color('#000000', '#a44801')
jeb.begin_fill()
jeb.forward(25)
jeb.left(90)
jeb.forward(50)
jeb.left(90)
jeb.forward(25)
jeb.left(90)
jeb.forward(50)
jeb.end_fill()

#Green triangle leaves
jeb.penup()
jeb.goto(-25,50)
jeb.left(90)
jeb.pendown()
jeb.color('#000000', '#42692f')
jeb.begin_fill()
jeb.goto(50,50)
jeb.goto(0,200)
jeb.goto(-25,50)
jeb.end_fill()

#Uses user input for color of ornaments 
jeb.color(or1, or2)
jeb.penup()
jeb.goto(0,75)
jeb.pendown()
jeb.begin_fill()
jeb.circle(r1)
jeb.end_fill()
jeb.penup()
jeb.goto(25,60)
jeb.pendown()
jeb.begin_fill()
jeb.circle(r1)
jeb.end_fill()
jeb.penup()
jeb.goto(0,100)
jeb.pendown()
jeb.begin_fill()
jeb.circle(r1)
jeb.penup()
jeb.end_fill()
jeb.goto(15, 125)
jeb.pendown()
jeb.begin_fill()
jeb.circle(r1)
jeb.end_fill()
jeb.penup()

#Makes a star colors use user inputs 
jeb.goto(-25,220)
jeb.color(str1, str2)
jeb.pendown()
jeb.begin_fill()
while i <= 5:  
    jeb.forward(50)
    jeb.right(144)
    i += 1
jeb.end_fill()

#Present
ben.penup()
ben.goto(-50, -100)
ben.color(present1)
ben.pendown()
ben.forward(40)
ben.right(90)
ben.forward(40)
ben.right(90)
ben.forward(40)
ben.right(90)
ben.forward(40)
ben.penup()
ben.goto(-50, -110)
ben.color(present2)
ben.pendown()
ben.begin_fill()
ben.end_fill()


window = trtl.Screen()
window.bgcolor('sky blue')
window.mainloop()