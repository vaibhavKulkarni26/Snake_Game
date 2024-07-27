from turtle import Screen

from scoreboard import Scoreboard
from snake import snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
food=Food()
scorboard = Scoreboard()


screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

game_is_on = True

snake = snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    #Collution with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorboard.increase_score()




    # detect Collotion with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scorboard.Game_over()

    # detect collectionswith tail
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on= False
            scorboard.Game_over()




screen.exitonclick()