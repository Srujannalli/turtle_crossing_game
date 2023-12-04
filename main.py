from turtle import Turtle, Screen
from crossing_turtle import Crossing_turtle
from traffic import Traffic
from level import Level
import time

COLOUR_LIST = [(160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
               (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
               (168, 99, 102)]
screen = Screen()
cross_turtle = Crossing_turtle()
game_level = Level()
vehicles = Traffic()
screen.bgcolor("white")
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()
screen.onkey(cross_turtle.go_up, "Up")
screen.onkey(cross_turtle.go_down, "Down")
game_on = True
limit = 0.1
while game_on:
    time.sleep(limit)
    screen.update()
    vehicles.move()
    for x in range(0, len(COLOUR_LIST)):
        if vehicles.cars[x].xcor() > 0 and cross_turtle.distance(vehicles.cars[x]) < 30:
            game_on = False
            print("you were hit by a car")
        if cross_turtle.ycor() > 290:
            game_level.increase_level()
            limit -= 0.01
            cross_turtle.hideturtle()
            cross_turtle.goto(0, -280)
            cross_turtle.showturtle()

screen.exitonclick()
