import turtle as trtl


#Circle
def draw_circle():
    side = float(input("How long do you want the sides of your shape? "))
    i = 0

    peppa = trtl.Turtle()
    peppa.speed(100)

    while i <= 720:  
        peppa.forward(side)
        peppa.right(1)
        i += 1
#Square
def draw_square():
    side = float(input("How long do you want the sides of your shape? "))
    i = 0

    peppa = trtl.Turtle()
    peppa.speed(100)
    while i <= 3:
        peppa.forward(side)
        peppa.right(90)
        i += 1
    

#Octagon
def draw_octagon():
    side = float(input("How long do you want the sides of your shape? "))
    i = 0

    peppa = trtl.Turtle()
    peppa.speed(100)
    while i <= 7:
        peppa.forward(side)
        peppa.right(45)
        i += 1

draw_square()

window = trtl.Screen()
window.exitonclick()