from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

def move_forward():
    my_turtle.forward(10)

def move_backwards():
    my_turtle.backward(10)

def turn_right():
    change_heading = my_turtle.heading() -10
    my_turtle.setheading(change_heading)

def turn_left():
    change_heading = my_turtle.heading() + 10
    my_turtle.setheading(change_heading)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

screen.listen()
screen.onkey(key="f", fun=move_forward)
screen.onkey(key="b", fun=move_backwards)
screen.onkey(key="r", fun=turn_right)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="c", fun=clear)
screen.exitonclick()