from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
game_on = False
all_turtles = []

for n in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[n])
    tim.penup()
    tim.goto(x=-230, y=y_pos[n])
    all_turtles.append(tim)

if user_bet:
    game_on = True


while game_on:

    for t in all_turtles:
        if t.xcor() > 220:
            game_on = False
            if t.pencolor() == user_bet:
                print(f"You have won! The {t.pencolor()} turtle is the winner")
            else:
                print(f"You have lost! The winner is the {t.pencolor()} turtle")
        distance = random.randint(0, 10)
        t.forward(distance)

screen.exitonclick()
