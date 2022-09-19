import turtle

def turtle_w_move():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_a_move():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_s_move():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def turtle_d_move():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def turtle_restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(turtle_w_move, 'w')
turtle.onkey(turtle_a_move, 'a')
turtle.onkey(turtle_s_move, 's')
turtle.onkey(turtle_d_move, 'd')
turtle.onkey(turtle_restart, 'Escape')
turtle.listen()
