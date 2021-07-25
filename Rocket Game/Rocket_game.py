from turtle import Turtle, Screen
import random

MAXIMUM_POINTS = 6
FONT = ('Arial', 16, 'normal')
WIDTH, HEIGHT = 600, 400

wn = Screen()
wn.bgcolor('lightblue')
# Score Variable
score = 0

# Turtle Player
spaceship = Turtle()
spaceship.color('red')
spaceship.penup()

speed = 1

# Border
border = Turtle(visible=False)
border.pensize(5)
border.color('darkblue')

border.penup()
border.goto(-WIDTH/2, -HEIGHT/2)
border.pendown()

for _ in range(2):
    border.forward(WIDTH)
    border.left(90)
    border.forward(HEIGHT)
    border.left(90)

border.penup()
border.goto(-WIDTH/2 + 10, HEIGHT/2 + 10)
border.write('Score: {}'.format(score), align='left', font=FONT)

# Create Goals
points = []

for _ in range(MAXIMUM_POINTS):
    goal = Turtle('circle')
    goal.color('green')
    goal.penup()
    goal.goto(random.randint(20 - WIDTH/2, WIDTH/2 - 20), \
        random.randint(20 - HEIGHT/2, HEIGHT/2 - 20))
    points.append(goal)

# Functions
def left():
    spaceship.left(30)

def right():
    spaceship.right(30)

def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    speed -= 1

def iscollision(turtle1, turtle2):
    return turtle1.distance(turtle2) < 20

# Keyboard Bindings
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')
wn.onkey(increasespeed, 'Up')
wn.onkey(decreasespeed, 'Down')
wn.onkey(wn.bye, 'q')

wn.listen()

timer = 30

def countdown():
    global timer

    timer -= 1

    if timer <= 0:  # time is up, disable user control
        wn.onkey(None, 'Left')
        wn.onkey(None, 'Right')
        wn.onkey(None, 'Up')
        wn.onkey(None, 'Down')
    else:
        wn.ontimer(countdown, 1000)  # one second from now

wn.ontimer(countdown, 1000)

def travel():
    global score

    spaceship.forward(speed)

    # Boundary
    if not -WIDTH/2 < spaceship.xcor() < WIDTH/2:
        spaceship.left(180)

    if not -HEIGHT/2 < spaceship.ycor() < HEIGHT/2:
        spaceship.left(180)

    # Point collection
    for count in range(MAXIMUM_POINTS):
        if iscollision(spaceship, points[count]):
            points[count].goto(random.randint(20 - WIDTH/2, WIDTH/2 - 20), \
                random.randint(20 - HEIGHT/2, HEIGHT/2 - 20))
            score += 1
            # Screen Score
            border.undo()
            border.write('Score: {}'.format(score), align='left', font=FONT)

    if timer:
        wn.ontimer(travel, 10)

travel()

wn.mainloop()