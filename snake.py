import turtle
import random

class snake:
    def __init__(self, allTiles):
        x = random.randint(1,allTiles.amountWidth - 1) 
        y = random.randint(1,allTiles.amountHeight - 1) 

        # don't need to care whether the snake is spawning on the apple, since the
        # apple spawns after the snake, and the apple spawning checks for
        # overlap with the snake.

        self.direction = "none"
        self.xcor = x
        self.ycor = y
        self.snakeCoords = [[x,y]]

        allTiles.changeColour("blue",x,y)
    
    def move(self, allTiles):
        if self.direction == "left":
            self.ycor=self.ycor + 1
        if self.direction == "right":
            self.ycor=self.ycor - 1
        if self.direction == "up":
            self.xcor=self.xcor - 1
        if self.direction == "down":
            self.xcor=self.xcor + 1

        if self.xcor < 0 or self.ycor < 0 or self.xcor >= allTiles.amountWidth or self.ycor >= allTiles.amountHeight:
            return False

        #update snake's position after the current movement

        xpos = self.snakeCoords[0][0]
        ypos = self.snakeCoords[0][1]

        allTiles.changeColour("blue", self.xcor, self.ycor)
        self.snakeCoords[0][0] = self.xcor
        self.snakeCoords[0][1] = self.ycor

        for i in range(len(self.snakeCoords)-1):
            curr_xpos = xpos
            curr_ypos = ypos
            
            xpos = self.snakeCoords[i+1][0]
            ypos = self.snakeCoords[i+1][1]

            self.snakeCoords[i+1] = [curr_xpos, curr_ypos]
        
        # the last position is discarded, and is no longer in the snake, therefore, update the board.

        allTiles.changeColour("tiles",xpos, ypos)

        return True


    def rotate(self, direction):
        self.direction = direction

    def add(self):
        x = self.snakeCoords[len(self.snakeCoords)-1][0]
        y = self.snakeCoords[len(self.snakeCoords)-1][1]
        self.snakeCoords.append([x,y])