from turtle import Screen, Turtle
from snake import Snake
import time

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

snake = Snake()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.07)

    snake.move()

sc.exitonclick()
        