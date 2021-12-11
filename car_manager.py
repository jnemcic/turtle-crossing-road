from turtle import Turtle
import random

COLORS = ["green", "red", "yellow", "blue", "purple", "orange", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(270, random.randint(-190, 230))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)
