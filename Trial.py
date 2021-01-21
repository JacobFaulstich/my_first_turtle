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
        a = -200
        while (a < 200):
            a += 50
            b = 160
            jane.goto(a,b)
            jane.color("blue")
            jane.stamp()
            c = -200
            while (c < 200):
                c += 50
                d = 120
                jane.goto(c,d)
                jane.color("blue")
                jane.stamp()
                e = -200
                while (e < 200):
                    e += 50
                    f = 80
                    jane.goto(e,f)
                    jane.color("blue")
                    jane.stamp()
                    g = -200
                    while (g < 200):
                        g += 50
                        h = 40
                        jane.goto(g,h)
                        jane.color("blue")
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
else:
    print("Not a valid function number")





        x = -150
    while (x < 200):
        x += 50
        y = 250
        f = 200
        jane.goto(x,f)
        jane.color("yellow")
        jane.stamp()

        while (y > -150) and x == -100:
            y -= 50
            e = -150
            jane.goto(e, y)
            jane.color("purple")
            jane.stamp()