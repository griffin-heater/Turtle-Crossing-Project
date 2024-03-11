import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creates the screen
screen = Screen()
screen.title('Turtle Crossing Game')
screen.setup(width=600, height=600)
screen.tracer(0)

# Creates player, car manager, and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Allows the user to control the turtle with up arrow
screen.listen()
screen.onkeypress(player.go_up, key='Up')

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    # Creates cars and tells them to move
    car_manager.create_car()
    car_manager.move_car()
    
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    # Detect when player reaches finish
    if player.cross_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
    
screen.exitonclick()