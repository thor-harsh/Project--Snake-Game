from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen=Screen()
screen.bgcolor("orange")
screen.setup(width=600,height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
scoreboard=ScoreBoard()

fooooods=Food(shape="circle")
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(fooooods)<20:
        scoreboard.function()
        fooooods.refresh()
        snake.extend_segment()
    if snake.head.xcor()<-350 or snake.head.xcor()>350 or snake.head.ycor()<-350 or snake.head.ycor()>350:
        scoreboard.reset()
        snake.reset()

    for leon in snake.turtlesss[1:]:

        if snake.head.distance(leon)<10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

