from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Scoreboard_ai
import time

# Setting up the screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.bgpic("pingpong(1).png")

#Choose the game
def start_game():
        screen = Screen()
        screen.bgcolor("Black")
        screen.setup(width = 800,height = 600)
        option = screen.textinput("Choose Option", "Enter 1 for one player game, 2 for two player game")
        if option == "1":
            screen.clear()
            one_player()
        elif option == "2":
            screen.clear()
            two_player()

def one_player():
    # Code for one player mode 
    screen = Screen()
    screen.bgcolor("Black")
    screen.setup(width=800, height=600)
    screen.tracer(0)
    ball = Ball()
    scoreboard = Scoreboard_ai()
     
    player_paddle = Paddle((350, 0))
    computer_paddle = Paddle((-350, 0))

    screen.listen()
    screen.onkey(player_paddle.go_up, "Up")
    screen.onkey(player_paddle.go_down, "Down")

    def computer_paddle_move():
        y = computer_paddle.ycor()
        if y < ball.ycor() and abs(y - ball.ycor()) > 10:
            y += 15
        elif y > ball.ycor() and abs(y - ball.ycor()) > 10:
            y -= 15
        computer_paddle.sety(y)

    # Main game loop
    game_is_on = True
    while game_is_on:
        time.sleep(0.00000000001)
        screen.update()
        # Move the ball
        ball.move()
        #Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        #Detect collision with paddle
        if ball.distance(player_paddle) < 30 and ball.xcor() > 320 or ball.distance(computer_paddle) < 30 and ball.xcor() < -320:
            ball.bounce_x()

        # Computer AI
        computer_paddle_move()
        
        #Detect R paddle misses
        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.computer_point()

        #Detect L paddle misses:
        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.player_point()

        if scoreboard.computer_score == 11 or scoreboard.player_score == 11:
            break

    if scoreboard.computer_score == 11:
        scoreboard.display_winner_ai("Computer")
    else:
        scoreboard.display_winner_ai("Player")

# Function for two player mode
def two_player():
    # Your code for two player mode goes here
    screen = Screen()
    screen.bgcolor("Black")
    screen.setup(width=800, height=600)
    screen.tracer(0)
    ball = Ball()
    scoreboard = Scoreboard()
    # Write your code for two player mode here
    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    game_is_on = True
    while game_is_on:
            time.sleep(0.00000000001)
            screen.update()
            ball.move()

            #Detect collision with wall
            if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()

            #Detect collision with paddle
            if ball.distance(r_paddle) < 35 and ball.xcor() > 300 or ball.distance(l_paddle) < 35 and ball.xcor() < -300:
                ball.bounce_x()

            #Detect R paddle misses
            if ball.xcor() > 380:
                ball.reset_position()
                scoreboard.l_point()

            #Detect L paddle misses:
            if ball.xcor() < -380:
                ball.reset_position()
                scoreboard.r_point()

            if scoreboard.l_score == 11 or scoreboard.r_score == 11:
                break

    if scoreboard.l_score == 11:
        scoreboard.display_winner("Player 1")
    else:
        scoreboard.display_winner("Player 2")
        
start_game()
screen.exitonclick()
  