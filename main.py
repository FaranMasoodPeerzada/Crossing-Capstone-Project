import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard =Scoreboard()
screen.listen()
screen.onkey(player.move_forward,'Up')
screen.onkey(player.move_backward,'Down')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        #detect collision with car
        if player.distance(car)<20:
            game_is_on = False
            scoreboard.game_over()
        #detect successful crossing
        if player.is_at_finis_line():
            player.go_to_start()
            scoreboard.increase_level()






screen.exitonclick()