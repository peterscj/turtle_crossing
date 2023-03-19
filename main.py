from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car import Car
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Initialize player and scoreboard
player_1 = Player()
scoreboard = Scoreboard()

# Initialize car

# move speed, following dist, len, wid, start y
car_1 = Car(1, 25, 0.15, 1, 1, -150)
car_2 = Car(2, 50, 0.05, 4, 1, -60)
car_3 = Car(5, 100, 0.75, 2, 1, 50)
car_4 = Car(2, 200, 0.01, 6, 1, 125)
car_5 = Car(3, 35, 0.1, 2, 1, 200)

screen.listen()

# Key Bindings
screen.onkey(player_1.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    car_1.lane_management()
    car_2.lane_management()
    car_3.lane_management()
    car_4.lane_management()
    car_5.lane_management()

    # Level completion condition
    if player_1.ycor() > 220:
        player_1.starting_position()
        scoreboard.update_level()

screen.exitonclick()