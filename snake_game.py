import turtle
import time
import random

from messages import messages
from snake import snake
from apple import apple
from tiles import tiles
from algorithm import algorithm

update_time = 100
width, height = 300,300
apple_count = 0
buffer = ["none", "none"]
run_algo = True

def left():
    global new, buffer
    if initSnake.direction == "right":
        return
    if buffer[0] == "none":
        buffer[0] = "left"
        initSnake.rotate("left")
    else:
        if buffer[1] == "none":
            buffer[1] = "left"
    if new == 1:
        new = 0
        updateTime()
    

def down():
    global new, buffer
    if initSnake.direction == "up":
        return
    if buffer[0] == "none":
        buffer[0] = "down"
        initSnake.rotate("down")
    else:
        if buffer[1] == "none":
            buffer[1] = "down"
    if new == 1:
        new = 0
        updateTime()
    

def right():
    global new, buffer
    if initSnake.direction == "left":
        return
    if buffer[0] == "none":
        buffer[0] = "right"
        initSnake.rotate("right")
    else:
        if buffer[1] == "none":
            buffer[1] = "right"
    if new == 1:
        new = 0
        updateTime()
    

def up():
    global new, buffer
    if initSnake.direction == "down":
        return
    if buffer[0] == "none":
        buffer[0] = "up"
        initSnake.rotate("up")
    else:
        if buffer[1] == "none":
            buffer[1] = "up"
    if new == 1:
        new = 0
        updateTime()

def runGreedy():
    alg = algorithm(update_time, initTiles)
    direction = alg.shortestpath(initTiles, initApple, initSnake)

    if direction != "none":
        if direction == "up":
            up()
        else:
            if direction == "left":
                left()
            else: 
                if direction == "right":
                    right()
                else:
                    down()

def updateTime():
    global apple_count
    if initSnake.xcor < 0 or initSnake.ycor < 0 or initSnake.xcor >= initTiles.amountWidth or initSnake.ycor >= initTiles.amountHeight:
        initMessage.draw("You Lost! ", apple_count)
        return
    if initSnake.move(initTiles) == False:
        initMessage.draw("You Lost! ", apple_count)
        return
    (x, y) = initTiles.returnTiles()[initSnake.xcor][initSnake.ycor].pos()
    if x == initApple.xcoord and y == initApple.ycoord:
        apple_count+=1
        initApple.appleTurtle.hideturtle()
        initTiles.returnTiles()[initSnake.xcor][initSnake.ycor].showturtle()
        initSnake.add(initApple.xcoord, initApple.ycoord, initTiles)
        initApple.spawnApple(initTiles, initSnake)
        
    for i in range(1, len(initSnake.snakeCoords)):
        if initSnake.xcor == initSnake.snakeCoords[i][0] and initSnake.ycor == initSnake.snakeCoords[i][1]:
            initMessage.draw("You Lost! ", apple_count)
            return
    if buffer[1] != "none":
        initSnake.rotate(buffer[1])
    buffer[0] = "none"
    buffer[1] = "none"

    if run_algo == True:
        runGreedy()

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

if run_algo == True:
    runGreedy()

#listen for player input
    

turtle.onkeypress(left,'a')
turtle.onkeypress(down,'s')
turtle.onkeypress(right,'d')
turtle.onkeypress(up,'w')

turtle.listen()
turtle.done()