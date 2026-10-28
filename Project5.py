import turtle
# I am setting the turtle
t = turtle.Turtle()
t.speed (5)
t.penup ()
t.goto (0,-150)
t.pendown ()
t.color ("black")

# start drawing the first side!
t.begin_fill ()
t.left (10)
t.forward (115)
for i in range (25):
    t.left (2)
    t.forward (1)
t.forward (75)
t.setheading (90)
for i in range (10):
    t.left (2)
    t.forward (1)
t.forward (120)
t.left (125)
t.forward (120)
for i in range (10):
    t.right (7)
    t.forward (1)
t.forward (40)
for i in range (7):
    t.left (5)
    t.forward (1)
t.forward (43)
t.end_fill ()
t.penup ()
t.goto (1,-150)
t.setheading (180)
t.pendown ()
# other side!
t.begin_fill ()
t.right (10)
t.forward (115)
for i in range (25):
    t.right (2)
    t.forward (1)
t.forward (75)
t.setheading (50)
for i in range (10):
    t.left (2)
    t.forward (1)
t.forward (130)
t.right (125)
t.forward (140)
t.setheading (20)
t.forward (10)
t.end_fill ()
t.hideturtle()
