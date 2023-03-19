from turtle import Turtle
import time

class Car(Turtle):
    def __init__(self,movement_dist, following_dist, speed,len,wid,y):
        super().__init__()
        self.move_x = -1
        self.move_y = 0
        self.cars = list()
        self.speed = speed
        self.len = len
        self.wid = wid
        self.x = 270
        self.y = y
        self.movement_dist = movement_dist
        self.following_dist = following_dist
        self.make_car()

    def make_car(self):
        new_car = Turtle(shape="square")
        new_car.color("white")
        new_car.shapesize(stretch_len=self.len, stretch_wid=self.wid)
        new_car.penup()
        new_car.goto(self.x,self.y)
        self.cars.append(new_car)

    def move_car(self):
        new_x = self.xcor()+self.move_x
        new_y = self.ycor()+self.move_y
        self.goto(new_x,new_y)

    def lane_management(self):
        self.move_cars_in_lane_forward()
        self.new_car_to_lane()

    def move_cars_in_lane_forward(self):
        for i in range(len(self.cars)):
            self.cars[i].setheading(180)
            self.cars[i].forward(self.movement_dist)
    def new_car_to_lane(self):
        if self.cars[-1].xcor() < (self.x-self.following_dist):
            self.make_car()
            starting_pos_x = self.cars[-1].xcor() + 150
            starting_pos_y = self.cars[-1].ycor()
            self.cars[-1].goto(starting_pos_x, starting_pos_y)


    # def car_speed(self):


