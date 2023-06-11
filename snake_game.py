import turtle
import time
import random

from messages import messages
from snake import snake
from apple import apple
from tiles import tiles

update_time = 100
width, height = 300,300
apple_count = 0
buffer = ["none", "none"]

def updateTime():
    global apple_count
    start = time.time()
    if initSnake.xcor < 0 or initSnake.ycor < 0 or initSnake.xcor >= initTiles.amountWidth or initSnake.ycor >= initTiles.amountHeight:
        initMessage.draw("You Lost! ", apple_count)
        return
    (x, y) = initTiles.returnTiles()[initSnake.xcor][initSnake.ycor].pos()
    if x == initApple.xcoord and y == initApple.ycoord:
        apple_count+=1
        initApple.appleTurtle.hideturtle()
        initTiles.returnTiles()[initSnake.xcor][initSnake.ycor].showturtle()
        initSnake.add()
        initApple.spawnApple(initTiles, initSnake)
    if initSnake.move(initTiles) == False:
        initMessage.draw("You Lost! ", apple_count)
        return
    for i in range(1, len(initSnake.snakeCoords)):
        if initSnake.xcor == initSnake.snakeCoords[i][0] and initSnake.ycor == initSnake.snakeCoords[i][1]:
            initMessage.draw("You Lost! ", apple_count)
            return
    if buffer[1] != "none":
        initSnake.rotate(buffer[1])
    buffer[0] = "none"
    buffer[1] = "none"
    turtle.ontimer(updateTime, update_time)

# creating objects, initialising the board and creating the first apple
screen = turtle.Screen()
turtle.addshape("apple.gif")
initTiles = tiles(2,width,height)
initTiles.drawBoard()
initSnake = snake(initTiles)
initApple = apple()
initApple.spawnApple(initTiles, initSnake)
initMessage = messages()
new = 1

#listen for player input

def left():
    global new, buffer
    if initSnake.direction == "right":
        return
    if new == 1:
        updateTime()
        new = 0
    if buffer[0] == "none":
        buffer[0] = "left"
        initSnake.rotate("left")
    else:
        if buffer[1] == "none":
            buffer[1] = "left"
    

def down():
    global new, buffer
    if initSnake.direction == "up":
        return
    if new == 1:
        updateTime()
        new = 0
    if buffer[0] == "none":
        buffer[0] = "down"
        initSnake.rotate("down")
    else:
        if buffer[1] == "none":
            buffer[1] = "down"
    

def right():
    global new, buffer
    if initSnake.direction == "left":
        return
    if new == 1:
        updateTime()
        new = 0
    if buffer[0] == "none":
        buffer[0] = "right"
        initSnake.rotate("right")
    else:
        if buffer[1] == "none":
            buffer[1] = "right"
    

def up():
    global new, buffer
    if initSnake.direction == "down":
        return
    if new == 1:
        updateTime()
        new = 0
    if buffer[0] == "none":
        buffer[0] = "up"
        initSnake.rotate("up")
    else:
        if buffer[1] == "none":
            buffer[1] = "up"
    

turtle.onkeypress(left,'a')
turtle.onkeypress(down,'s')
turtle.onkeypress(right,'d')
turtle.onkeypress(up,'w')

turtle.listen()
turtle.done()