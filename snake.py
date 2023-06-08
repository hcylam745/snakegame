import turtle
import random

class snake:
    def __init__(self, allTiles):
        self.snakeTurtle = []
        newturtle = turtle.Turtle()
        newturtle.up()
        newturtle.speed(0)
        x = random.randint(1,allTiles.amountWidth - 1) 
        y = random.randint(1,allTiles.amountHeight - 1) 
        newturtle.goto(allTiles.returnTiles()[x][y].position())

        # don't need to care whether the snake is spawning on the apple, since the
        # apple spawns after the snake, and the apple spawning checks for
        # overlap with the snake.

        self.direction = "right"
        self.xcor = allTiles.returnTiles()[x][y].xcor()
        self.ycor = allTiles.returnTiles()[x][y].ycor()
        self.snakeTurtle.append(newturtle)
    
    def move(self, allTiles):
        if self.direction == "left":
            self.xcor=int(self.xcor - 20*allTiles.length)
        if self.direction == "right":
            self.xcor=int(self.xcor + 20*allTiles.length)
        if self.direction == "up":
            self.ycor=int(self.ycor + 20*allTiles.length)
        if self.direction == "down":
            self.ycor=int(self.ycor - 20*allTiles.length)

        (xpos, ypos) = self.snakeTurtle[0].pos()

        for i in range(len(self.snakeTurtle)-1):
            (curr_xpos, curr_ypos) = (xpos, ypos)

            (xpos, ypos) = self.snakeTurtle[i+1].pos()
            self.snakeTurtle[i+1].goto(curr_xpos, curr_ypos)
    
        self.snakeTurtle[0].goto(self.xcor,self.ycor)

    def rotate(self, direction, angle):
        self.direction = direction
        self.snakeTurtle[0].setheading(angle)

    def add(self):
        newturtle = turtle.Turtle()
        newturtle.up()
        newturtle.speed(0)
        newturtle.goto(self.xcor,self.ycor)
        self.snakeTurtle.append(newturtle)