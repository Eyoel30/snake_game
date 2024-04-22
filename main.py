from turtle import Screen
from snake import Snake
from food import Food
from scorebord import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game ")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()     # this creates the snake
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()    # display the snake after the snake is created and after all the parts of the snake moved
    time.sleep(0.1)

    snake.move()       # in relation to the to update() due to the while loop
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        scoreboard.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
        # or
        # elif snake.head.position() == segment.position():
        #     game_is_on = False
        #     scoreboard.game_over()

screen.exitonclick()
