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

def updateTime():
    global apple_count
    if initSnake.xcor > width or initSnake.xcor < -width + 40 or initSnake.ycor > height or initSnake.ycor < -height + 40:
        initMessage.draw("You Lost! ", apple_count)
        return
    if initSnake.xcor == initApple.xcoord and initSnake.ycor == initApple.ycoord:
        apple_count+=1
        initSnake.add()
        initApple.spawnApple(initTiles, initSnake)
    initSnake.move(initTiles)
    # you need to add a condition for checking if the snake overlaps itself
    # you dont need to check all overlaps, only if the most recent overlaps with anything.
    for i in range(1,len(initSnake.snakeTurtle)):
        if initSnake.xcor == initSnake.snakeTurtle[i].xcor() and initSnake.ycor == initSnake.snakeTurtle[i].ycor():
            initMessage.draw("You Lost! ", apple_count)
            return
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
    global new
    initSnake.rotate("left",180)
    if new == 1:
        updateTime()
        new = 0
    

def down():
    global new
    initSnake.rotate("down",270)
    if new == 1:
        updateTime()
        new = 0
    

def right():
    global new
    initSnake.rotate("right",0)
    if new == 1:
        updateTime()
        new = 0
    

def up():
    global new
    initSnake.rotate("up",90)
    if new == 1:
        updateTime()
        new = 0
    

turtle.onkeypress(left,'a')
turtle.onkeypress(down,'s')
turtle.onkeypress(right,'d')
turtle.onkeypress(up,'w')

turtle.listen()
turtle.done()