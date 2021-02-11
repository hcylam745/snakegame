import turtle
import time
import random

update_time = 100
width, height = 300,300
appleTurtle = []
allTiles = []
snakeTurtle = []
messageTurtle = []
memory = [[0],[0]]
xcoord = 0
ycoord = 0
apple_count = 0

class tiles:
    def __init__(self,length,width,height):
        self.length = length
        self.screenWidth = width
        self.screenHeight = height
        self.amountWidth = int(self.screenWidth / (10 * self.length))
        self.amountHeight = int(self.screenHeight / (10 * self.length))

    def drawBoard(self):
        # calculate amount of turtles in each row / column
        global allTiles
        for i in range(self.amountHeight):
            allTiles.append([])
            for j in range(self.amountWidth):
                # create new turtle, append to 2d list for use
                newturtle = turtle.Turtle()
                newturtle.up()
                newturtle.speed(0)
                turtle.tracer(False)
                allTiles[i].append(newturtle)
                
                # create checkerboard pattern
                if i % 2 == 0:
                    if j % 2 == 0:
                        allTiles[i][j].color("lime")
                    else:
                        allTiles[i][j].color("green")
                else:
                    if j % 2 != 0:
                        allTiles[i][j].color("lime")
                    else:
                        allTiles[i][j].color("green")

                # draw tiles
                allTiles[i][j].goto(self.screenWidth - j * 20 * self.length, self.screenHeight - i * 20 * self.length)
                allTiles[i][j].shapesize(self.length)
                allTiles[i][j].shape("square")
        turtle.tracer(True)

class apple:
    def __init__(self):
        # create turtle for apple
        global appleTurtle
        global allTiles
        newturtle = turtle.Turtle()
        newturtle.up()
        newturtle.speed(0)
        newturtle.shape("apple.gif")
        appleTurtle.append(newturtle)
    
    def spawnApple(self):
        global xcoord
        global ycoord
        x = random.randint(1,initTiles.amountWidth - 1)
        y = random.randint(1,initTiles.amountHeight - 1)
        x,y = checkOverlap(x,y)
        xcoord = allTiles[x][y].xcor()
        ycoord = allTiles[x][y].ycor()
        appleTurtle[0].goto(allTiles[x][y].position())
    
def checkOverlap(x,y):
    true = 0
    for i in range(len(memory[0])):
        if allTiles[x][y].xcor() == memory[0][i] and allTiles[x][y].ycor == memory[1][i]:
            true = 0
            x = random.randint(1,initTiles.amountWidth - 1)
            y = random.randint(1,initTiles.amountHeight - 1)
        else:
            true = 1
    if true == 0:
        initApple.checkOverlap(x,y)
    else:
        return x,y

class snake:
    def __init__(self):
        global snakeTurtle
        newturtle = turtle.Turtle()
        newturtle.up()
        newturtle.speed(0)
        x = random.randint(1,initTiles.amountWidth - 1) 
        y = random.randint(1,initTiles.amountHeight - 1) 
        while True:
            if x == xcoord and y == ycoord:
                x = random.randint(1,initTiles.amountWidth - 1)
                y = random.randint(1,initTiles.amountHeight - 1)
            else:
                break
        newturtle.goto(allTiles[x][y].position())
        self.direction = "right"
        self.xcor = allTiles[x][y].xcor()
        self.ycor = allTiles[x][y].ycor()
        snakeTurtle.append(newturtle)
    
    def move(self):
        if self.direction == "left":
            self.xcor=int(self.xcor - 20*initTiles.length)
        if self.direction == "right":
            self.xcor=int(self.xcor + 20*initTiles.length)
        if self.direction == "up":
            self.ycor=int(self.ycor + 20*initTiles.length)
        if self.direction == "down":
            self.ycor=int(self.ycor - 20*initTiles.length)
        snakeTurtle[0].goto(self.xcor,self.ycor)
        
        for k in range(len(snakeTurtle)):
            if k < len(snakeTurtle) - 1:
                snakeTurtle[k+1].goto(memory[0][k],memory[1][k])

        for j in range(len(memory[0])-1,-1,-1):
            if j > 0:
                memory[0][j] = memory[0][j-1]
                memory[1][j] = memory[1][j-1]
            else:
                memory[0][j] = self.xcor
                memory[1][j] = self.ycor

    def rotate(self, direction, angle):
        self.direction = direction
        snakeTurtle[0].setheading(angle)

    def add(self):
        newturtle = turtle.Turtle()
        newturtle.up()
        newturtle.speed(0)
        newturtle.goto(self.xcor,self.ycor)
        snakeTurtle.append(newturtle)
        memory[0].append(0)
        memory[1].append(0)

class messages:
    def __init__(self):
        newturtle = turtle.Turtle()
        newturtle.up()
        newturtle.speed(0)
        newturtle.hideturtle()
        messageTurtle.append(newturtle)
    
    def draw(self, message):
        messageTurtle[0].write(message,align="center",font=("Arial",24,"normal"))
        messageTurtle[0].goto(messageTurtle[0].xcor(),messageTurtle[0].ycor()-100)
        messageTurtle[0].write(apple_count,align="center",font=("Arial",24,"normal"))

def updateTime():
    global apple_count
    #print(f"xcor apple {xcoord}")
    #print(f"ycor apple {ycoord}")
    #print(f"xcor snake{snakeTurtle[0].xcor()}")
    #print(f"ycor snake{snakeTurtle[0].ycor()}")
    #print(initSnake.direction)
    #for i in range(len(memory)):
        #print(memory[i])
    if initSnake.xcor > width or initSnake.xcor < -width + 40 or initSnake.ycor > height or initSnake.ycor < -height + 40:
        initMessage.draw("You Lost! ")
        return
    if initSnake.xcor == xcoord and initSnake.ycor == ycoord:
        apple_count+=1
        initSnake.add()
        initApple.spawnApple()
    initSnake.move()
    for i in range(len(memory[0])-1):
        if initSnake.xcor == memory[0][i+1] and initSnake.ycor == memory[1][i+1]:
            initMessage.draw("You Lost! ")
            return
    turtle.ontimer(updateTime, update_time)

# creating objects, initialising the board and creating the first apple
screen = turtle.Screen()
turtle.addshape("apple.gif")
initTiles = tiles(2,width,height)
initTiles.drawBoard()
initApple = apple()
initApple.spawnApple()
initSnake = snake()
initMessage = messages()
new = 1

#listen for player input

def left():
    global new
    if new == 1:
        updateTime()
        new = 0
    initSnake.rotate("left",180)

def down():
    global new
    if new == 1:
        updateTime()
        new = 0
    initSnake.rotate("down",270)

def right():
    global new
    if new == 1:
        updateTime()
        new = 0
    initSnake.rotate("right",0)

def up():
    global new
    if new == 1:
        updateTime()
        new = 0
    initSnake.rotate("up",90)

turtle.onkeypress(left,'a')
turtle.onkeypress(down,'s')
turtle.onkeypress(right,'d')
turtle.onkeypress(up,'w')

turtle.listen()
turtle.done()