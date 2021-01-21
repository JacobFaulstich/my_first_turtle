import turtle as trtl # Imports the turtle program to be trtl


def draw_triangle():  # defines the equalateral triangle function
    i = 0  # sets the counter equal to 0
    while i <= 2:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(120)  # angle = 360 / number of sides
        i += 1  # adds 1 to the counter


def draw_square():  # defines the square function
    i = 0  # sets the counter equal to 0
    while i <= 3:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(90)  # angle = 360 / number of sides
        i += 1 #adds 1 to the counter
# pentagon
def draw_pentagon():  # defines the square function
    i = 0  # sets the counter equal to 0
    while i <= 4:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(360/5)  # angle = 360 / number of sides
        i += 1 #adds 1 to the counter
# hexagon
def draw_hexagon():  # defines the square function
    i = 0  # sets the counter equal to 0
    while i <= 5:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(60)  # angle = 360 / number of sides
        i += 1 #adds 1 to the counter
# heptagon
def draw_heptagon():  # defines the square function
    i = 0  # sets the counter equal to 0
    while i <= 6:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(360/7)  # angle = 360 / number of sides
        i += 1 #adds 1 to the counter
# octogon
def draw_octagon():  # defines the square function
    i = 0  # sets the counter equal to 0
    while i <= 7:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(360/8)  # angle = 360 / number of sides
        i += 1 #adds 1 to the counter
# nonagon
def draw_nonagon():  # defines the square function
    i = 0  # sets the counter equal to 0
    while i <= 8:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(360/9)  # angle = 360 / number of sides
        i += 1 #adds 1 to the counter
# decagon
def draw_decagon():  # defines the square function
    i = 0  # sets the counter equal to 0
    while i <= 9:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(360/10)  # angle = 360 / number of sides
        i += 1 #adds 1 to the counter
# circle
def draw_circle():  # defines the square function
    i = 0  # sets the counter equal to 0
    while i <= 359:  # becasue the counter starts @ 0, loops = sides - 1
        fred.forward(side)  # moves forward the user input amount
        fred.right(360/360)  # angle = 360 / number of sides
        i += 1 #adds 1 to the counter


fred = trtl.Turtle()  # defines the name of my turtle as fred
fred.shape("turtle")  # changes the painter shape from an arrow to a turtle...becasue I can...
window = trtl.Screen() # define the canvas as window

again = "Y"
while again.upper() == "Y":
    shape = trtl.textinput("Number of Sides:", "How many sides do you want to draw?") # Uses input to decide what shape to draw
    side = trtl.textinput("Side Length:", "How long do you want your sides?") # Uses input for length of sides
    side = float(side) # Sets the side to be a decimal number

    if shape == "3": # input equals 3 the draws a triangle
        draw_triangle()
    elif shape == "4": # input equals 4 the draws a square
        draw_square()
    elif shape == "5": # input equals 5 the draws a pentagon
        draw_pentagon()
    elif shape == "6": # input equals 6 the draws a hexagon
        draw_hexagon()
    elif shape == "7": # input equals 7 the draws a heptagon
        draw_heptagon()
    elif shape == "8": # input equals 8 the draws a octagon
        draw_octagon()
    elif shape == "9": # input equals 9 the draws a nonagon
        draw_nonagon()
    elif shape == "10": # input equals 10 the draws a decagon
        draw_decagon()
    elif shape == "0": # input equals 0 the draws a circle
        draw_circle()
    else:
        print("not in my programing...") # Types not in my programming

    again = trtl.textinput("New Shape:", "Draw a new shape?(Y/N") # Takes input to draw a shape again or not
    fred.clear() # clears what fred drew

window.done()
