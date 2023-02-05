from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
#function bind it to will be defined first
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food - snake head is within 15px or less (food is 10X10)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False

    #detect if collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance() < 10:
            game_is_on = False
            scoreboard.game_over()

# create snake 40X40 - 600 X 600 -20 && -40
# snake_1 = Turtle("square")
# snake_1.color("white")
#
# snake_2 = Turtle("square")
# snake_2.color("white")
# # goto takes a tuple
# snake_2.goto(x=-20, y=0)
#
# snake_3 = Turtle("square")
# snake_3.color("white")
# snake_3.goto(x=-40, y=0)





screen.exitonclick()
