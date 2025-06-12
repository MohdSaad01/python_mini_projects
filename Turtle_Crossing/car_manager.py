COLORS = ["red", "orange", "yellow", "green", "pink","blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3

from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE


    def create_car(self):
        if random.randint(1,6)==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(280,random.randint(-250,250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def increase_speed(self):
        self.car_speed+=MOVE_INCREMENT

