''' 
Jacob Faulstich
2/4/21
I think that the program should have 2 seperate functions. The first function should start from (0,0) and draw a part of an octagon. Then pen should switch shapes and colors on each side drawn. The second function should do the same thing but improve on it. What i did for mine is to use user input to decide the color of each side.
'''

def turtle_1():
  import turtle as trtl

# Sets a blank list that is called my_turtles 
  my_turtles = []

# Sets a list of turtle shapes and turtle colors 
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
  turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# Itterates through the shape list, creates a new turtle with the shape from the list, and adds it to the my_turtle list
  for s in turtle_shapes:
    t = trtl.Turtle(shape = s)
    popped_color = turtle_colors.pop() # Removes the last color form the color list and sets it to the variable popped color
    t.color(popped_color) # Changes the turtle color to the color removed from the turtle color list
    my_turtles.append(t)





# Sets the variable of starting x and y positions
  startx = 0
  starty = 0
  header = 90 # Stets the headers start to 90



# Itterates through the myturtle list, stest the turtles position to the starting x and y, then has the turtle turn rught 45 and forwars 50
  for t in my_turtles:
    t.penup() # Picks up the pen when the turtle is made
    t.goto(startx, starty)
    t.setheading(header)  # Sets the new turtles heading to what the previous one was
    t.pendown() # Sets the pen down when starting position is reached
    t.right(45)  
    t.forward(50)
    header = t.heading() # sets header to th turtles current heading


# 	 Add 50 to the start x and y varible
    startx = t.xcor() # Sets the start x to the turtles current x cordinate
    starty = t.ycor() # Sets the start x to the turtles current y cordinate

# Creates the turtle canvas and screen
  wn = trtl.Screen()
  wn.mainloop()



def turtle_2():
  import turtle as trtl

  color1 = input("What basic color do you want the first turtle to be? ")
  color2 = input("What basic color do you want the second turtle to be? ")
  color3 = input("What basic color do you want the third turtle to be? ")
  color4 = input("What basic color do you want the fourth turtle to be? ")
  color5 = input("What basic color do you want the fifth turtle to be? ")
  color6 = input("What basic color do you want the sixth turtle to be? ")


# Sets a blank list that is called my_turtles 
  my_turtles = []

# Sets a list of turtle shapes and turtle colors 
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
  turtle_colors = []
  turtle_colors.append(color6)
  turtle_colors.append(color5)
  turtle_colors.append(color4)
  turtle_colors.append(color3)
  turtle_colors.append(color2)
  turtle_colors.append(color1)


# For the shapes in the turtle shape list have t be equal to the turtles shape which is equal to s
  for s in turtle_shapes:
    t = trtl.Turtle(shape = s)
    popped_color = turtle_colors.pop() # Removes the last color form the color list and sets it to a variable
    t.color(popped_color) # Changes the turtle color to the color removed from the turtle color list
    my_turtles.append(t)




# Sets the variable of starting x and y to zero


  startx = 0
  starty = 0
  header = 90 # Sets the header to 90


# For the turtle shapes in the myturtles list go to start x and y variable and turn right 45 and go foraward 50
  for t in my_turtles:
    t.penup()
    t.goto(startx, starty)
    t.setheading(header)  # Sets the heading to the previuos turtles heading
    t.pendown()
    t.right(45)  
    t.forward(50)
    header = t.heading() # sets header to the turtles current heading






# 	 Add 50 to the start x and y varible
    startx = t.xcor() # Sets the start x to the tutrtles current x cordinate
    starty = t.ycor() # Sets the start x to the tutrtles current x cordinate




# Sets wn to the turtle screen and opens the turtle screen
  wn = trtl.Screen()
  wn.mainloop()

def turtle_3():
  import turtle as trtl
  import random

# Sets a blank list that is called my_turtles 
  my_turtles = []

# Sets a list of turtle shapes and turtle colors 
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
  turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

# Itterates through the shape list, creates a new turtle with the shape from the list, and adds it to the my_turtle list
  for s in turtle_shapes:
    t = trtl.Turtle(shape = s)
    popped_color = turtle_colors.pop() # Removes the last color form the color list and sets it to the variable popped color
    t.color(popped_color) # Changes the turtle color to the color removed from the turtle color list
    my_turtles.append(t)





# Sets the variable of starting x and y positions
  startx = 0
  starty = 0
  header = 90 # Stets the headers start to 90



# Itterates through the myturtle list, stest the turtles position to the starting x and y, then has the turtle turn rught 45 and forwars 50
  for t in my_turtles:
    t.penup() # Picks up the pen when the turtle is made
    t.goto(startx, starty)
    t.setheading(header)  # Sets the new turtles heading to what the previous one was
    t.pendown() # Sets the pen down when starting position is reached
    t.right(45)  
    t.forward(50)
    header = t.heading() # sets header to th turtles current heading


# 	 Add 50 to the start x and y varible
    startx = t.xcor() # Sets the start x to the turtles current x cordinate
    starty = t.ycor() # Sets the start x to the turtles current y cordinate

# Creates the turtle canvas and screen
  wn = trtl.Screen()
  wn.mainloop()


import turtle as trtl

program_run = input("What function do you want to run, 1, 2, or 3? ")
program_run = int(program_run)
if (program_run == 1):
  turtle_1()
elif (program_run == 2):
  turtle_2()
elif (program_run == 3):
  turtle_3()

