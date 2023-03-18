from turtle import Turtle


START_X = 0
START_Y = -280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("white")
        self.starting_position()


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def starting_position(self):
        self.goto(START_X, START_Y)
