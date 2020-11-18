# foot ball game

import turtle

import time

# field (screen setup)

mscreen = turtle.Screen()

mscreen.bgcolor('dark green')

mscreen.title('Football Champs')

mscreen.setup(1200,600)

# line boundary

l = turtle.Turtle()

l.hideturtle()

l.speed(25)

l.color("white")

l.pensize(10)

l.left(90)

l.forward(270)

l.left(90)

l.forward(500)

l.left(90)

l.forward(540)

l.left(90)

l.forward(990)

l.left(90)

l.forward(540)

l.left(90)

l.forward(490)

l.left(90)

l.forward(540)

l.setpos(0,0)

l.right(90)

l.penup()

l.forward(400)

l.penup()

l.forward(100)

l.pendown()

l.right(90)

l.forward(135)

l.right(90)

l.forward(100)

l.right(90)

l.forward(270)

l.right(90)

l.forward(100)

l.penup()

l.goto(0,0)

l.pendown()

l.right(180)

l.penup()

l.forward(390)

l.penup()

l.forward(100)

l.pendown()

l.left(90)

l.forward(135)

l.left(90)

l.forward(100)

l.left(90)

l.forward(270)

l.left(90)

l.forward(100)

# start circle

cir = turtle.Turtle()

cir.hideturtle()

cir.right(90)

cir.penup()

cir.forward(54)

cir.pendown()

cir.left(90)

cir.pensize(10)

cir.color('white')

cir.circle(40)

#ball

ball = turtle.Turtle()

ball.hideturtle()

ball.right(90)

ball.penup()

ball.forward(13)

ball.showturtle()

ball.shape('circle')

ball.color('orange')

ball.shapesize(2)

ball.left(45)

ball.speed(5)

ball.dx = 2

ball.dy = -2

#pad1

play1 = turtle.Turtle()

play1.hideturtle()

play1.shape('square')

play1.color('white')

play1.shapesize(2,8)

play1.left(90)

play1.penup()

play1.goto(250,0)

play1.showturtle()

#pad2

play2 = turtle.Turtle()

play2.hideturtle()

play2.shape('square')

play2.color('white')

play2.shapesize(2,8)

play2.left(90)

play2.penup()

play2.goto(-250,0)

play2.showturtle()

#pen

pen = turtle.Turtle()

pen.hideturtle()

pen.color('white')

pen.pensize(10)

pen.penup()

pen.goto(0,150)

pen.pendown()

#score board variable

s1 = turtle.Turtle()

s1.hideturtle()

s1.pensize(10)

s2 = turtle.Turtle()

s2.hideturtle()

s2.pensize(10)

    

#define

def up1():

    play1.speed(0)

    play1.forward(30)

def up2():

    play2.speed(0)

    play2.forward(30)

def down1():

    play1.speed(0)

    play1.backward(30)

def down2():

    play2.speed(0)

    play2.backward(30)

        

# functions

mscreen.listen()

mscreen.onkeypress(up1 , 'i')

mscreen.onkeypress(up2 , 'w')

mscreen.onkeypress(down1 , 'k')

mscreen.onkeypress(down2 , 's')

# pad boundary collison

def boom():

    if play1.ycor() >= 190:

        play1.setposition(250,180)

def boom2():

    if play1.ycor() <= -190:

        play1.setposition(250,-180)

                

def boom1():

    if play2.ycor() >= 190:

        play2.setposition(-250,180)

def boom3():

    if play2.ycor() <= -190:

        play2.setposition(-250,-180)


# boundary collison with ball

def collide():

    if ball.ycor() <= -230 and ball.xcor() > 0:

        ball.sety(-230)

        ball.dy *= -1

    elif ball.ycor() <= -230 and ball.xcor() < 0:

        ball.sety(-230)

        ball.dy *= -1

    elif ball.ycor() >= 230 and ball.xcor() > 0:

        ball.sety(230)

        ball.dy *= -1

    elif ball.ycor() >= 230 and ball.xcor() < 0:

        ball.sety(230)

        ball.dy *= -1

    elif ball.xcor() <= -500 and ball.ycor() < 270 and ball.ycor() > 135:

        ball.speed(1)

        ball.home()

    elif ball.xcor() >= 500 and ball.ycor() < 270 and ball.ycor() > 135:

        ball.speed(1)

        ball.home()

    elif ball.xcor() <= -500 and ball.ycor() > -270 and ball.ycor() < -135:

        ball.speed(1)

        ball.home()

    elif ball.xcor() >= 500 and ball.ycor() > -270 and ball.ycor() < -135:

        ball.speed(1)

        ball.home()

#ball and pad collison

def padoball():

    if play1.xcor() == ball.xcor() and play1.ycor() == ball.ycor() or ball.xcor() < play1.xcor() + 10 and ball.xcor() > play1.xcor() - 10 and ball.ycor() < play1.ycor() + 60 and ball.ycor() > play1.ycor() - 60:

        ball.setx(230)

        ball.dx *= -1

def padoball1():

    if play2.xcor() == ball.xcor() and play2.ycor() == ball.ycor() or ball.xcor() < play2.xcor() +10 and ball.xcor() > play2.xcor() - 10 and ball.ycor() < play2.ycor() + 60 and ball.ycor() > play2.ycor() - 60:

        ball.setx(-230)

        ball.dx *= -3

score = 0

scoree = 0

                

while True:

    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

    boom()

    boom2()

    boom1()

    boom3()

    collide()

    padoball()

    padoball1()

    padoball()

    padoball1()

    if ball.xcor() <= -400 and ball.xcor() >= -500 and ball.ycor() <=  135 and ball.ycor() >= -135:

        pen.write('GOAL BY PLAYER 2!' , align = 'center' , font = ('arial' , 26 ,'normal'))

        time.sleep(2)

        pen.undo()

        ball.speed(1)

        ball.home()

        ball.right(120)

        padoball()

        padoball1()

        score += 1

        s1.undo()

        s1.penup()

        s1.pensize(10)

        s1.goto(400,270)

        s1.color('crimson')

        scoreq = "GOAL: %s" %score

        s1.write( scoreq , False , align = 'left' , font = ('courier' , 16 , 'normal'))

        if score >= 3:

            pen.write('PLAYER 2 WINS' , align = 'center' , font = ('arial' , 26 ,'normal'))

            time.sleep(2)

            turtle.bye()

    if ball.xcor() <= 500 and ball.xcor() >= 400 and ball.ycor() <=  135 and ball.ycor() >= -135:

        pen.write('GOAL BY PLAYER 1!' , align = 'center' , font = ('arial' , 26 ,'normal'))

        time.sleep(2)

        pen.undo()

        ball.speed(1)

        ball.home()

        ball.left(120)

        padoball()

        padoball1()

        scoree += 1

        s2.undo()

        s2.penup()

        s2.goto(-400,270)

        s2.pensize(10)

        s2.color('blue')

        scorea = "GOAL: %s" %scoree

        s2.write( scorea , False , align = 'left' , font = ('courier' , 16 , 'normal'))

        if scoree >= 3:

            pen.write('PLAYER 1 WINS' , align = 'center' , font = ('arial' , 26 ,'normal'))

            time.sleep(2)

            turtle.bye()