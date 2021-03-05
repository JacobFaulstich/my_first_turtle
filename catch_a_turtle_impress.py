''' Jacob Faulstich, 2/17/21
    Create a turtle in a random location. If the turtle is clicked have the
    turtle move to a new random location and add 1 point to the score.'''


#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
shape = "turtle"
color = "green"
colors = ['#FF0000','#FF7F00','#FFFF00','#C0C0C0','#808080','#000000','#800000','#808000','#00FF00','#008000','#00FFFF','#008080','#0000FF','#000080','#FF00FF','#800080']
speed = 0
score = 1
size = 2
font_setup = ("Arial", 20, "normal")
time_keeper = 30
timer_interval = 1000
time_up = False


#-----initialize turtle-----
jumpy = trtl.Turtle()
jumpy.shape(shape)
jumpy.shapesize(size)
jumpy.color(color)
jumpy.penup()
jumpy.speed(speed)

writer = trtl.Turtle()
writer.speed(speed)
writer.hideturtle()
writer.penup()
writer.goto(0, 280)

timer = trtl.Turtle()
timer.speed(speed)
timer.hideturtle()
timer.penup()
timer.goto(0, 260)

wn = trtl.Screen()

#-----game functions--------
def start_message():
    start = "Click the turtle to start"
    writer.write(start, font = font_setup)
    start_timer = "Time: "
    timer.write(start_timer, font = font_setup)


def jumpy_clicked(x, y):
    global time_up
    if (not time_up):
        change_pos()
        increase_score()
        change_size()
        change_color()
        print("X cord:",x)
        print("Y cord:",y)
    else: 
        jumpy.hideturtle()


def change_color():
    jumpy.color(rand.choice(colors))


def change_size():
    jumpy.shapesize(rand.randint(1,10))


def jumpy_not_clicked(x,y):
    global time_up
    if (not time_up):
        decrease_score()
    else: 
        jumpy.hideturtle()


def change_pos():
    new_x = rand.randint(-250, 250)
    new_y = rand.randint(-250, 250)
    jumpy.goto(new_x, new_y)


def increase_score():
    global score
    score += 2
    writer.clear()
    writer.write(score, font = font_setup)


def decrease_score():
    global score
    score -= 1
    writer.clear()
    writer.write(score, font = font_setup)

def game(x,y):
    jumpy.onclick(jumpy_clicked)
    wn.onclick(jumpy_not_clicked)
    wn.ontimer(timer_countdown, timer_interval)


def timer_countdown():
    global time_keeper, time_up
    timer.clear()
    if time_keeper <= 0:
        time_up = True
    else:
        timer.write(("Time: " + str(time_keeper)), font = font_setup)
        time_keeper -= 1
        timer.getscreen().ontimer(timer_countdown, timer_interval)


#-----events----------------
start_message()
jumpy.onclick(game)
wn.mainloop()
