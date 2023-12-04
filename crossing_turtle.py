from turtle import Turtle


class Crossing_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(0, -280)

    def go_up(self):
        y_coordinate = self.ycor() + 10
        self.goto(0, y_coordinate)

    def go_down(self):
        y_cord = self.ycor() - 10
        self.goto(0, y_cord)