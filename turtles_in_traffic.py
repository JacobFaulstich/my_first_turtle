'''
Jacob Faulstich
2/9/21
I think the program is supposed to make turtles with specific shapes and colors. Then the turtles are supoosed to miove across the screen vertically and horizontally. The turtles aren't supposed to colide each other and simualte traffic.

'''
def function_1 ():
    import turtle as trtl

    # Creates a list for horizontal turtles and vertical turtles
    horiz_turtles = []
    vert_turtles = []

    # Creates three lists, turtle shapes, horziontal colors, and vertical colors
    turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
    horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
    vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

    # The tloc variable is set to 50
    tloc = 50

    # Itterates through the shapes in the turtle shapes list
    for s in turtle_shapes:
        # (Itterates through) Creates new turtle with their shape from the shape list. Adds the turtle to the horizantal turtles list. Picks the pen up. Sets the horizantal turtles fill to the colors from horizontal turtles list. Makes the turtle goto (-350, tloc) and sets the heading  to zero
        ht = trtl.Turtle(shape=s)
        horiz_turtles.append(ht)
        ht.penup()
        new_color = horiz_colors.pop()
        ht.fillcolor(new_color)
        ht.speed(0)
        ht.goto(-350, tloc)
        ht.setheading(0)

        # Creates new turtle with it's shape from the shape list. Adds it to the vertical turtles list. Picks the pen up. Sets the fill color to a color from vertical color list. Gos to (-tloc, 350) and sets heading to 270.
        vt = trtl.Turtle(shape=s)
        vert_turtles.append(vt)
        vt.penup()
        new_color = vert_colors.pop()
        vt.fillcolor(new_color)
        vt.speed(0)
        vt.goto( -tloc, 350)
        vt.setheading(270)

        # Adds fifty to the tolc variable which is the turtles location
        tloc += 50

    # TODO: move turtles across and down screen, stopping for collisions

    steps = 0
    while steps < 50:
        for ht in horiz_turtles:
            for vt in vert_turtles:
                ht.forward(3)# Changed to three to speed up
                htx = ht.xcor()
                hty = ht.ycor()
                vt.forward(3) # Changed to three to speed up
                vtx = vt.xcor()
                vty = vt.ycor()
                if (abs(htx - vtx) <= 20):
                    if (abs(hty - vty) <= 20):
                        horiz_turtles.remove(ht)
                        vert_turtles.remove(vt)


            
        steps += 1


    wn = trtl.Screen()
    wn.mainloop()


def function_2 ():
    import turtle as trtl
    trtl.register_shape('')

    # Creates a list for horizontal turtles and vertical turtles
    horiz_turtles = []
    vert_turtles = []

    # Creates three lists, turtle shapes, horziontal colors, and vertical colors
    turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
    horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
    vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

    # The tloc variable is set to 50
    tloc = 50

    # Itterates through the shapes in the turtle shapes list
    for s in turtle_shapes:
        # (Itterates through) Creates new turtle with their shape from the shape list. Adds the turtle to the horizantal turtles list. Picks the pen up. Sets the horizantal turtles fill to the colors from horizontal turtles list. Makes the turtle goto (-350, tloc) and sets the heading  to zero
        ht = trtl.Turtle(shape=s)
        horiz_turtles.append(ht)
        ht.penup()
        new_color = horiz_colors.pop()
        ht.fillcolor(new_color)
        ht.speed(0)
        ht.goto(-350, tloc)
        ht.setheading(0)

        # Creates new turtle with it's shape from the shape list. Adds it to the vertical turtles list. Picks the pen up. Sets the fill color to a color from vertical color list. Gos to (-tloc, 350) and sets heading to 270.
        vt = trtl.Turtle(shape=s)
        vert_turtles.append(vt)
        vt.penup()
        new_color = vert_colors.pop()
        vt.fillcolor(new_color)
        vt.speed(0)
        vt.goto( -tloc, 350)
        vt.setheading(270)

        # Adds fifty to the tolc variable which is the turtles location
        tloc += 50

    # TODO: move turtles across and down screen, stopping for collisions

    steps = 0
    while steps < 50:
        for ht in horiz_turtles:
            for vt in vert_turtles:
                ht.forward(3)# Changed to three to speed up
                htx = ht.xcor()
                hty = ht.ycor()
                vt.forward(3) # Changed to three to speed up
                vtx = vt.xcor()
                vty = vt.ycor()
                if (abs(htx - vtx) <= 20):
                    if (abs(hty - vty) <= 20):
                        ht.shape('expolsion.png')
                        horiz_turtles.remove(ht)
                        vert_turtles.remove(vt)


            
        steps += 1


    wn = trtl.Screen()
    wn.mainloop()


which_function = input("Which function do you want to run? (1 or 2)? ")
if (which_function == ("1")):
    function_1()
elif (which_function  == ("2")):
    function_2()