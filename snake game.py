from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
screen=Screen()
screen.bgcolor("black")
screen.title("my snake game")
screen.setup(width=600,height=600)
screen.tracer(0)
snake=Snake()
screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_right,"Right")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_down,"Down")
snake_segments=[]
snake.detect_head(snake_segments)
snake_head=snake_segments[0]
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    snake.take_food()
    if snake_head.xcor()>280 or snake_head.xcor()<-300 or snake_head.ycor()>300 or snake_head.ycor()<-280:
        snake_head.color("white")
        snake_head.goto(0,0)
        snake_head.write("Game Over!",align="center",font=("Arial",14,"normal"))
        is_game_on=False
    for segment in snake_segments[1:]:
        if snake_head.distance(segment)<10:
            snake_head.color("white")
            snake_head.goto(0,0)
            snake_head.write("Game Over!",align="center",font=("Arial",14,"normal"))
            is_game_on=False
            

                     
