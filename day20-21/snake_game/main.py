from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
from boundry import Boundry
import time

BOUNDRY = 279

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.tracer(0)

snake = Snake()
boundry = Boundry()
snake = Snake()
food = Food()
score = Score()

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

    # if snake.head.distance(food) < 15:
    #     food.relocate()
    #     snake.extend_snake()
    #     score.add_points()

    # # detecting collision with the wall
    # if snake.head.xcor() > BOUNDRY or snake.head.ycor() > BOUNDRY or snake.head.xcor() < -BOUNDRY or snake.head.ycor() < -BOUNDRY:
    #     # print("Collison")
    #     game_is_on = False
    #     score.set_highscore()
    #     # print(snake.head.ycor())
    #     score.game_over()
    
    # # detecting collision with the tail
    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score.set_highscore()
    #         # print(snake.head.ycor()) ###
    #         score.game_over()

sc.exitonclick()
