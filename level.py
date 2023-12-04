from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.write(f"level : {self.level}", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"level : {self.level}", align='center', font=FONT)