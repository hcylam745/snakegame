import turtle
import random

class apple:
    def __init__(self):
        # create turtle for apple
        self.xcoord = 0
        self.ycoord = 0
        newturtle = turtle.Turtle()
        newturtle.up()
        newturtle.speed(0)
        newturtle.shape("apple.gif")
        self.appleTurtle = newturtle
    
    def spawnApple(self, allTiles, snake):
        x = random.randint(1,allTiles.amountWidth - 1)
        y = random.randint(1,allTiles.amountHeight - 1)
        x,y = self.checkOverlap(x,y, allTiles, snake)
        self.xcoord = allTiles.returnTiles()[x][y].xcor()
        self.ycoord = allTiles.returnTiles()[x][y].ycor()
        self.appleTurtle.goto(allTiles.returnTiles()[x][y].position())
    
    # checks if apple generation overlaps with the snake, if it does then regenerate until it doesn't overlap anymore.
    def checkOverlap(self, x,y, allTiles, snake):
        true = 0
        # dont check memory, but rather the snake.
        # this loop checks to see if the current pos is on the snake, if so, it rerolls the position, and calls the function again.
        for i in range(len(snake.snakeTurtle)):
            (snake_x, snake_y) = snake.snakeTurtle[i].pos()
            if allTiles.returnTiles()[x][y].xcor() == snake_x and allTiles.returnTiles()[x][y].ycor() == snake_y:
                true = 0
                x = random.randint(1,allTiles.amountWidth - 1)
                y = random.randint(1,allTiles.amountHeight - 1)
            else:
                true = 1
        if true == 0:
            self.checkOverlap(x,y, allTiles)
        else:
            return x,y