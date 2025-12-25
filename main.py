from turtle import Turtle,Screen
from snake import Snake
from score import Score
from food import Food
import time
screen=Screen()
snake=Snake()
score=Score()
food=Food()

screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
game_over=Turtle()
game_over.penup()
game_over.hideturtle()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        score.game_end()
        game_on=False
    if snake.head.distance(food)<15:
        food.random_food()
        score.updates()
        snake.expand()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            game_on=False
            score.game_end()
        











screen.exitonclick()