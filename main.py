from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialization
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
scoreboard.hideturtle()
car_manager.hideturtle()

# Player controls
screen.listen()
screen.onkey(key="Up", fun=player.move)

# Game
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    # Generate cars
    car_manager.create_car()

    # Generate traffic
    car_manager.move()

    # Detect turtle/car collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    # Detect passed level and increase traffic speed
    if player.ycor() > player.finish_line:
        scoreboard.increase_score()
        player.go_to_start()
        car_manager.speed += 3

    # Keep track of score


screen.exitonclick()
