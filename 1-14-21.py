def code_stem_1():
    import turtle as trtl
    
    jon = trtl.Turtle()
    jon.speed(0)
    jon.penup()
    jon.goto(-150, 5)
    jon.shape("square")
    jon.color("salmon")

    line = 6

    while (line > 5):
        jon.pendown()
        jon.circle(5)
        jon.penup()
        jon.forward(20)
        line += 1

    window = trtl.Screen()
    window.exitonclick()


def code_stem_2():
    j = 0
    while (j < 10):
        print("j: ", j) # Print the string "j: " and then print the int j
        j += 1

        d = 0
        while (d < 5):
            print(" d: ", d)
            d += 1

            b = 0
            while  (b < 4):
                print("  b: ", b)
                b += 1


def code_stem_3 ():
    import turtle as trtl

    jane = trtl.Turtle()
    jane.shape("circle")
    jane.hideturtle()
    jane.speed(0)
    jane.penup()
    
    x = -200
    while (x < 200):
        x += 50
        y = 200
        jane.goto(x,y)
        jane.color("red")
        jane.stamp()

        while (y > 0):
            y -= 50
            jane.goto(x, y)
            jane.color("blue")
            jane.stamp()


    window = trtl.Screen()
    window.exitonclick()


def code_stem_4 ():
    import turtle as trtl

    jane = trtl.Turtle()
    jane.shape("circle")
    jane.hideturtle()
    jane.speed(0)
    jane.penup()
    
    y = 300
    while (y > -100):
        y -= 50
        x = -200
        jane.goto(x,y)
        jane.color("purple")
        jane.stamp()

        while (x < 100):
            x += 50
            jane.goto(x, y)
            jane.color("orange")
            jane.stamp()


    window = trtl.Screen()
    window.exitonclick()


code_stem = input("Which code stem do you want to run? ")

if (code_stem == "1"):
    code_stem_1()
elif (code_stem == "2"):
    code_stem_2()
elif (code_stem == "3"):
    code_stem_3()
elif (code_stem == "4"):
    code_stem_4()
else:
    print("Not a valid function number")