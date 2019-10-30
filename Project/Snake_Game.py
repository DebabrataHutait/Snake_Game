import turtle
import random
import time

delay=0.09

#Set Screen
tr=turtle.Screen()
tr.title("Snake Game....")
tr.bgcolor("yellow")
tr.setup(width=750,height=700)
tr.tracer(0)

#Snake figure
head=turtle.Turtle()
head.speed(speed=10)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction="stop"

#food figure
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(100,100)

body=[]

#move functions
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

def go_up():
    if head.direction != "down":
        head.direction="up"
def go_down():
    if head.direction != "up":
        head.direction="down"
def go_left():
    if head.direction != "right":
        head.direction="left"
def go_right():
    if head.direction != "left":
        head.direction="right"
def pause():
    head.direction=""

tr.listen()
tr.onkeypress(go_up,"w")
tr.onkeypress(go_down,"s")
tr.onkeypress(go_left,"a")
tr.onkeypress(go_right,"d")
tr.onkeypress(pause,"p")

#main game loop
while True:
    tr.update()

    #border collosion
    if head.xcor()<-370 or head.xcor()>370 or head.ycor()>335 or head.ycor()<-335 :
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide the rest bodies
        for i in body:
            i.goto(1000,1000)
        body.clear()

    #collision with food
    if(head.distance(food)<20):
        a=random.randint(-370,370)
        b=random.randint(-335,335)
        food.goto(a,b)

        #add body
        bd=turtle.Turtle()
        bd.speed(0)
        bd.shape("circle")
        bd.color("green")
        bd.penup()
        body.append(bd)

    #move the body
    for i in range(len(body)-1,0,-1):
        a=body[i-1].ycor()
        b=body[i-1].xcor()
        body[i].goto(b,a)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)

    move()

    # head collision with body
    for i in body:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for i in body:
                i.goto(1000, 1000)
            body.clear()

    time.sleep(delay)


tr.mainloop()