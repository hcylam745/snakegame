import random

class snake:
    
    def move(self, allTiles, screen):
        if self.direction == "left":
            self.ycor=self.ycor + 1
        if self.direction == "right":
            self.ycor=self.ycor - 1
        if self.direction == "up":
            self.xcor=self.xcor + 1
        if self.direction == "down":
            self.xcor=self.xcor - 1

        if self.xcor < 0 or self.ycor < 0 or self.xcor >= allTiles.amountWidth or self.ycor >= allTiles.amountHeight:
            return False

        # the last position is discarded, and is no longer in the snake, therefore, update the board.
        largest = len(self.snakeCoords)-1
        allTiles.changeColour("tiles",self.snakeCoords[largest][0], self.snakeCoords[largest][1], screen)

        # update snake's position after the current movement
        allTiles.changeColour("lightblue", self.xcor, self.ycor, screen)

        if len(self.snakeCoords) >= 2:
            allTiles.changeColour("blue",self.snakeCoords[0][0], self.snakeCoords[0][1], screen)

        self.snakeCoords.insert(0,[self.xcor,self.ycor])

        self.prev = self.snakeCoords[largest+1]
        self.snakeCoords.pop(largest+1)

        return True


    def rotate(self, direction):
        self.direction = direction

    def add(self,xcor, ycor, allTiles):
        self.snakeCoords.append(self.prev)
        x = int((allTiles.screenHeight - xcor) / (20 * allTiles.length))
        y = int((allTiles.screenWidth - ycor) / (20 * allTiles.length))
    
    def reset(self, allTiles, screen):
        x = random.randint(1, allTiles.amountWidth - 1)
        y = random.randint(1, allTiles.amountHeight - 1)
        
        self.direction = "none"
        self.xcor = x
        self.ycor = y
        self.snakeCoords = [[x,y]]
        self.prev = [x,y]

        allTiles.changeColour("lightblue",x,y, screen)
        