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
run_algo_greedy = False
run_algo_bfs = True
run_bfs_repeat = False
list_of_directions = []
lost = False

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
            list_of_directions.append("up")
        else:
            if direction == "left":
                list_of_directions.append("left")
            else: 
                if direction == "right":
                    list_of_directions.append("right")
                else:
                    list_of_directions.append("down")

def runGreedyBFS():
    global run_bfs_repeat
    alg = algorithm(update_time, initTiles)
    direction, failed_to_get_apple = alg.shortestpathbfs(initTiles, initApple)

    if failed_to_get_apple:
        run_bfs_repeat = True

    dir_list = direction[1].split(",")

    if len(dir_list) >= 2:
        list_of_directions.append(dir_list[1]) 

def updateTime():
    global run_bfs_repeat
    global lost
    if run_algo_greedy == True:
        runGreedy()
    if run_algo_bfs == True:
        runGreedyBFS()

    if len(list_of_directions) > 0:
        curr_dir = list_of_directions[0]
        del list_of_directions[0]
        if curr_dir == "up":
            up()
        if curr_dir == "down":
            down()
        if curr_dir == "right":
            right()
        if curr_dir == "left":
            left()

    global apple_count
    if initSnake.xcor < 0 or initSnake.ycor < 0 or initSnake.xcor >= initTiles.amountWidth or initSnake.ycor >= initTiles.amountHeight:
        lost = True
        initMessage.draw("You Lost! ", apple_count)
        return
    if initSnake.move(initTiles) == False:
        lost = True
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
            lost = True
            initMessage.draw("You Lost! ", apple_count)
            return
    if buffer[1] != "none":
        initSnake.rotate(buffer[1])
    buffer[0] = "none"
    buffer[1] = "none"
    
    if lost == False:
        turtle.ontimer(updateTime, update_time)

# creating objects, initialising the board and creating the first apple
screen = turtle.Screen()
turtle.addshape("apple.gif")
initTiles = tiles(2,width,height)
initTiles.drawBoard()
initSnake = snake()
initSnake.reset(initTiles)
initApple = apple()
initApple.spawnApple(initTiles, initSnake)
initMessage = messages()
new = 1

if run_algo_greedy == True and new == 1:
    new = 0
    updateTime()
else:
    if run_algo_bfs == True and new == 1:
        new = 0
        updateTime()

def reset(x, y):
    global lost
    if lost == True:
        global buffer
        global run_bfs_repeat
        global new
        global apple_count
        global list_of_directions
        (apple_y, apple_x) = initApple.appleTurtle.position()
        apple_x = int((initTiles.screenHeight - apple_x) / (20*initTiles.length))
        apple_y = int((initTiles.screenWidth - apple_y) / (20*initTiles.length))
        initTiles.returnTiles()[apple_x][apple_y].showturtle()
        initTiles.changeColour("tiles", apple_x, apple_y)
        initTiles.reset()
        initSnake.reset(initTiles)
        initApple.spawnApple(initTiles, initSnake)
        apple_count = 0
        new = 1
        buffer = ["none", "none"]
        list_of_directions = []
        initSnake.direction = "none"
        run_bfs_repeat = False
        lost = False

        time.sleep(2)

        if run_algo_greedy == True and new == 1:
            new = 0
            updateTime()
        else:
            if run_algo_bfs == True and new == 1:
                new = 0
                updateTime()

#create a reset button
button = turtle.Turtle()
button.hideturtle()
button.shape('square')
button.fillcolor('grey')
button.penup()
button.shapesize(3)
button.goto(0,-350)
button.showturtle()
button.write("R", align='center', font=('Arial', 16, 'bold'))
button.onclick(reset)

#listen for player input
    

turtle.onkeypress(left,'a')
turtle.onkeypress(down,'s')
turtle.onkeypress(right,'d')
turtle.onkeypress(up,'w')

turtle.listen()
turtle.done()