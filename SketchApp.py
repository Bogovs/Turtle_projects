import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
state = True


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def left():
    tim.left(10)


def right():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    tim.width(1)


def undo():
    tim.undo()


def pen():
    global state
    if state:
        tim.penup()
        state = False
    else:
        tim.pendown()
        state = True


def dot():
    tim.dot(10)


def width_up():
    tim.width(tim.pensize() + 2)


def width_down():
    if tim.pensize() > 2:
        tim.width(tim.pensize() - 2)


screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=left)
screen.onkeypress(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.onkey(key="p", fun=pen)
screen.onkey(key="t", fun=dot)
screen.onkey(key="BackSpace", fun=undo)
screen.onkey(key="Up", fun=width_up)
screen.onkey(key="Down", fun=width_down)
screen.exitonclick()

