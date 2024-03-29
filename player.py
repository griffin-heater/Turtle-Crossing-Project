from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.setheading(90)
        self.go_to_start()
        
    def go_up(self):
        self.forward(10)
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)

        
    def cross_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False