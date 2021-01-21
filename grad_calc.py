#Have the program ask the user for their quarter 1 and quarter 2 grades
#Ask the user what they want their final grade to be
#Then calculate the grade they would need to get on the final and dispaly as a letter

#40% Q1 + %40 Q2 + 20% Final = Semester
# (Semester - 0.4*Q1 - 0.4*Q2) / 0.2
# (90 - .4*97 -.4*86) /0.2
# (90 - 38.8 - 34.4) /0.2 = 84 >>>> You need to get a B on the final to get an A in the class

#A = 93 - 99
#A- = 90 - 92
#B+ = 87 - 89
#B = 83 - 86
#B- = 80 - 82
#C+ = 77 - 79
#C = 73 - 76
#C- = 70 - 72
#D+ = 67 - 69
#D = 63 - 66
#D- = 60 - 62
#F = 0 - 59

import turtle as trtl # Imports the turtle program to be trtl
jeb = trtl.Turtle()
window = trtl.Screen()


def draw_zero():
    jeb.right(90)
    jeb.circle(20,180)
    jeb.forward(40)
    jeb.circle(20,180)
    jeb.forward(40)
    jeb.left(90)

# Draws a one
def draw_one():
    jeb.right(90)
    jeb.forward(45)
    jeb.right(90)
    jeb.forward(20)
    jeb.backward(40)
    jeb.forward(20)
    jeb.right(90)
    jeb.forward(45)
    jeb.left(135)
    jeb.forward(20)
    jeb.right(225)

# Draws a two
def draw_two():
    jeb.circle(20,180)
    jeb.circle(20,-180)
    jeb.forward(30)



# Draws a three
def draw_three():
    jeb.circle(20,180)
    jeb.right(180)
    jeb.circle(20,180)
    jeb.right(180)


# Draws a four
def draw_four():
    jeb.left(90)
    jeb.forward(40)
    jeb.backward(40)
    jeb.right(90)
    jeb.forward(40)
    jeb.left(90)
    jeb.forward(40)
    jeb.backward(80)
    jeb.right(90)


# Draws a five
def draw_five():
    jeb.circle(20,180)
    jeb.right(90)
    jeb.forward(20)
    jeb.right(90)
    jeb.forward(20)


# Draws a six
def draw_six():
    jeb.circle(20)
    jeb.circle(40,-180)
    jeb.right(180)


# Draws a seven
def draw_seven():
    jeb.left(75)
    jeb.forward(60)
    jeb.right(75)
    jeb.backward(40)

# Draws an eight
def draw_eight():
    jeb.circle(20)
    jeb.left(90)
    jeb.penup()
    jeb.forward(40)
    jeb.pendown()
    jeb.right(90)
    jeb.circle(20)


# Draws a nine
def draw_nine():
    jeb.circle(20)
    jeb.circle(20,90)
    jeb.left(180)
    jeb.forward(50)
    jeb.left(90)

def draw_ten():
    jeb.penup()
    jeb.goto(-200,60)
    jeb.pendown()
    draw_one()
    jeb.penup()
    jeb.goto(-150,20)
    jeb.pendown()
    draw_zero()



#This block of code sets up the intial user inputs
q1 = input("What was your quarter 1 percentage? (As a decimal) ")
q1 = float(q1)
q2 = input("What was your quarter 2 percentage? (As a decimal) ")
q2 = float(q2)
semester = input("What percentage do you want for the semester? (As a decimal) ")
semester = float(semester)

# Equation for the grade calculation... (Semester - 0.4*Q1 - 0.4*Q2) / 0.2
final =(semester - (0.4 * q1) - (0.4 * q2)) / 0.2
final = float(final)


if final >= 93:
    print("You need to get an A on the final to get a " + str(semester) + " in the class.")
elif final >= 90 and final < 93:
    print("You need to get an A- on the final to get a " + str(semester) + " in the class.")
elif final >= 87  and final < 90:
    print("You need to get a B+ on the final to get a " + str(semester) + " in the class.")
elif final >= 83 and final < 87:
    print("You need to get a B on the final to get a " + str(semester) + " in the class.")
elif final >= 80 and final < 83:
    print("You need to get a B- on the final to get a " + str(semester) + " in the class.")
elif final >= 77 and final < 80:
    print("You need to get a C+ on the final to get a " + str(semester) + " in the class.")
elif final >= 73 and final < 77:
    print("You need to get a C on the final to get a " + str(semester) + " in the class.")
elif final >= 70 and final < 73:
    print("You need to get a C- on the final to get a " + str(semester) + " in the class.")
elif final >= 67 and final < 70:
    print("You need to get a D+ on the final to get a " + str(semester) + " in the class.")
elif final >= 63 and final < 67:
    print("You need to get a D on the final to get a " + str(semester) + " in the class.")
elif final >= 60 and final < 63:
    print("You need to get a D- on the final to get a " + str(semester) + " in the class.")
else:
    print("You need to get a F on the final to get a " + str(semester) + " in the class.")

ones = (final % 10)
tens = ( final - ones ) / 10
ones = int(ones)

if tens == 1: #If tens equals 1 then it draws a one in the correct spot
    jeb.penup()
    jeb.goto (-200,0)
    jeb.pendown()
    draw_one()
elif tens == 2: #If tens equals 2 then it draws a two in the correct spot
    jeb.penup()
    jeb.goto (-200,0)
    jeb.pendown()
    draw_two()
elif tens == 3: #If tens equals 3 then it draws a three in the correct spot
    jeb.penup()
    jeb.goto (-200,0)
    jeb.pendown()
    draw_three()
elif tens == 4: #If tens equals 4 then it draws a four in the correct spot
    jeb.penup()
    jeb.goto (-200,0)
    jeb.pendown()
    draw_four()
elif tens == 5: #If tens equals 5 then it draws a five in the correct spot
    jeb.penup()
    jeb.goto (-200,0)
    jeb.pendown()
    draw_five()
elif tens == 6: #If tens equals 6 then it draws a six in the correct spot
    jeb.penup()
    jeb.goto (-200,0)
    jeb.pendown()
    draw_six()
elif tens == 7: #If tens equals 7 then it draws a seven in the correct spot
    jeb.penup()
    jeb.goto (-200,0)
    jeb.pendown()
    draw_seven()
elif tens == 8: #If tens equals 8 then it draws a eight in the correct spot
    jeb.penup()
    jeb.goto (-200,0)
    jeb.pendown()
    draw_eight()
elif tens == 9: #If tens equals 9 then it draws a nine in the correct spot
    jeb.penup()
    jeb.goto (-200,0)
    jeb.pendown()
    draw_nine()
elif tens >= 10: #If tens is greater than or equal to 10 then it draws a ten in the correct spot
    draw_ten()
elif tens == 0: #If ten equals 0 than draw a zero in the correct spot
    jeb.penup()
    jeb.goto (-200,20)
    jeb.pendown()
    draw_zero()

if ones < 0.5: #If ones is less than 0.5 than draws a zero
    jeb.penup()
    jeb.goto (-100,20)
    jeb.pendown()
    draw_zero()
elif ones >= 0.5 and ones < 1.5: #If ones is greater than or equal to 0.5 and less than 1.5 draw a one
    jeb.penup()
    jeb.goto (-100,0)
    jeb.pendown()
    draw_one()
elif ones >= 1.5 and ones < 2.5: #If ones is greater than or equal to 1.5 and less than 2.5 draw a two
    jeb.penup()
    jeb.goto (-100,0)
    jeb.pendown()
    draw_two()
elif ones >= 2.5 and ones < 3.5: #If ones is greater than or equal to 2.5 and less than 3.5 draw a three
    jeb.penup()
    jeb.goto (-100,0)
    jeb.pendown()
    draw_three()
elif ones >= 3.5 and ones < 4.5: #If ones is greater than or equal to 3.5 and less than 4.5 draw a four
    jeb.penup()
    jeb.goto (-100,0)
    jeb.pendown()
    draw_four()
elif ones >= 4.5 and ones < 5.5: #If ones is greater than or equal to 4.5 and less than 5.5 draw a five
    jeb.penup()
    jeb.goto (-100,0)
    jeb.pendown()
    draw_five()
elif ones >= 5.5 and ones < 6.5: #If ones is greater than or equal to 5.5 and less than 6.5 draw a six
    jeb.penup()
    jeb.goto (-100,0)
    jeb.pendown()
    draw_six()
elif ones >= 6.5 and ones < 7.5: #If ones is greater than or equal to 6.5 and less than 7.5 draw a seven
    jeb.penup()
    jeb.goto (-100,0)
    jeb.pendown()
    draw_seven()
elif ones >= 7.5 and ones < 8.5: #If ones is greater than or equal to 7.5 and less than 8.5 draw a eight
    jeb.penup()
    jeb.goto (-100,0)
    jeb.pendown()
    draw_eight()
elif ones >= 8.5 and ones < 9.5: #If ones is greater than or equal to 8.5 and less than 9.5 draw a nine
    jeb.penup()
    jeb.goto (-100,0)
    jeb.pendown()
    draw_nine()

window.mainloop()