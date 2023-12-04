from turtle import Turtle, Screen
import random

COLOUR_LIST = [(160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
screen = Screen()
screen.colormode(255)


class Traffic(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        for x in range(0, len(COLOUR_LIST)):
            rand_x = random.randint(-60, 300)
            rand_y = random.randint(-280, 280)
            new_turtle = Turtle(shape="square")
            new_turtle.color(COLOUR_LIST[x])
            new_turtle.penup()
            new_turtle.shapesize(1, 3, 1)
            new_turtle.goto(rand_x, rand_y)
            self.cars.append(new_turtle)

    def move(self):
        y_cord = random.randint(-280, 280)
        for x in range(0, len(COLOUR_LIST)):
            self.cars[x].back(10)
            if self.cars[x].xcor() < -300:
                self.cars[x].hideturtle()
                self.cars[x].goto(300, y_cord)
                self.cars[x].showturtle()



