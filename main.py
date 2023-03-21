from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car import Car
import time
import turtle
import random

"""
Welcome to the turtle crossing game! The objective is to use the arrow
keys to move your turtle across the map to reach the next level. After
completing each level, the speed of all cars across the lanes will 
increase.

If a player collides with one of the cars, then they will restart at the
beginning.

"""

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Initialize player and scoreboard
player_1 = Player()
scoreboard = Scoreboard()

# Initialize car

# move speed, following dist, len, wid, start y
car_1 = Car(1, 25, 0.15, 1, -150)
car_2 = Car(2, 50, 0.05, 4, -60)
car_3 = Car(5, 100, 0.75, 2, 50)
car_4 = Car(2, 200, 0.01, 6, 125)
car_5 = Car(3, 35, 0.1, 2, 200)

all_lanes = [car_1,car_2,car_3,car_4,car_5]

screen.listen()

# Key Bindings
screen.onkey(player_1.up, "Up")

speed = 0.01
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()

    # Generate cars in all lanes and check for collision with player
    for car in all_lanes:
        car.lane_management()
        car.detect_collision(player_1)
        if car.collision == True:
            player_1.starting_position()
            car.collision = False

    # Level completion condition
    if player_1.ycor() > 220:
        player_1.starting_position()
        scoreboard.update_level()
        speed *= 0.5

screen.exitonclick()