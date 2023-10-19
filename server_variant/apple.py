import random

class apple:
    def __init__(self):
        # create turtle for apple
        self.xcoord = 0
        self.ycoord = 0
    
    def spawnApple(self, allTiles, snake):
        x = random.randint(1,allTiles.amountWidth - 1)
        y = random.randint(1,allTiles.amountHeight - 1)
        x,y = self.checkOverlap(x,y, allTiles, snake)
        self.xcoord = x
        self.ycoord = y
        allTiles.changeColour("red",x, y)
    
    # checks if apple generation overlaps with the snake, if it does then regenerate until it doesn't overlap anymore.
    def checkOverlap(self, x,y, allTiles, snake):
        true = 1
        for i in range(len(snake.snakeCoords)):
            if x == snake.snakeCoords[i][0] and y == snake.snakeCoords[i][1]:
                true = 0
                x = random.randint(1,allTiles.amountWidth - 1)
                y = random.randint(1,allTiles.amountWidth - 1)
        if true == 0:
            return self.checkOverlap(x,y, allTiles, snake)
        else:
            return x,y