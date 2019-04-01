# Matt's first Python Game

import turtle

# window setup
win = turtle.Screen()
win.title("Pong by Mstrblueskys")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Score
score_one = 0
score_two = 0

# Player 1
player_one = turtle.Turtle()
player_one.speed(0)
player_one.shape("square")
player_one.color("green")
player_one.shapesize(stretch_wid=5, stretch_len=1)
player_one.penup()
player_one.goto(-350, 0)

# Player 2
player_two = turtle.Turtle()
player_two.speed(0)
player_two.shape("square")
player_two.color("green")
player_two.shapesize(stretch_wid=5, stretch_len=1)
player_two.penup()
player_two.goto(350, 0)

# Pong
pong_ball = turtle.Turtle()
pong_ball.speed(0)
pong_ball.shape("square")
pong_ball.color("green")
pong_ball.penup()
pong_ball.goto(0, 0)
pong_ball.dx = 1
pong_ball.dy = 1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1 - 0  ||  0 - Player 2", align="center", font=("Courier", 20,"normal"))

# Move Player 
def player_one_up():
    if player_one.ycor() < 250:
        y = player_one.ycor()
        y += 20
        player_one.sety(y)

def player_one_down():
    if player_one.ycor() > -250:
        y = player_one.ycor()
        y -= 20
        player_one.sety(y)

def player_two_up():
    if player_two.ycor() < 250:
        y = player_two.ycor()
        y += 20
        player_two.sety(y)

def player_two_down():
    if player_two.ycor() > -250:
        y = player_two.ycor()
        y -= 20
        player_two.sety(y)

# Keyboard Input
win.listen()
win.onkeypress(player_one_up, "w")
win.onkeypress(player_one_down, "s")
win.onkeypress(player_two_up, "Up")
win.onkeypress(player_two_down, "Down")

# Game Loop
while True:
    win.update()

    # Move the ball
    pong_ball.setx(pong_ball.xcor() + pong_ball.dx)
    pong_ball.sety(pong_ball.ycor() + pong_ball.dy)

    # Bounce off walls
    if pong_ball.ycor() > 290:
        pong_ball.sety(290)
        pong_ball.dy *= -1
    if pong_ball.ycor() < -290:
        pong_ball.sety(-290)
        pong_ball.dy *= -1
    # Look for paddles    
    if pong_ball.xcor() > 330 and pong_ball.xcor() < 340 and (pong_ball.ycor() < player_two.ycor() + 50 and pong_ball.ycor() > player_two.ycor() -50):
        pong_ball.setx(330)
        pong_ball.dx *= -1
    if pong_ball.xcor() < -330 and pong_ball.xcor() > -340 and (pong_ball.ycor() < player_one.ycor() + 50 and pong_ball.ycor() > player_one.ycor() -50):
        pong_ball.setx(-330)
        pong_ball.dx *= -1
    # Reset ball postion
    if pong_ball.xcor() > 390:
        pong_ball.goto(0, 0)
        pong_ball.dx *= -1
        score_one += 1
        pen.clear()
        pen.write("Player 1 - {}  ||  {} - Player 2".format(score_one, score_two), align="center", font=("Courier", 20,"normal"))
    if pong_ball.xcor() < -390:
        pong_ball.goto(0, 0)
        pong_ball.dx *= -1
        score_two +=1
        pen.clear()
        pen.write("Player 1 - {}  ||  {} - Player 2".format(score_one, score_two), align="center", font=("Courier", 20,"normal"))
    