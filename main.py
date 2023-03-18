from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Initialize player and scoreboard
player_1 = Player()
scoreboard = Scoreboard()

screen.listen()

# Key Bindings
screen.onkey(player_1.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Level completion condition
    if player_1.ycor() > 220:
        player_1.starting_position()
        scoreboard.update_level()

screen.exitonclick()