class tiles:
    def __init__(self,length,width,height):
        self.length = length
        self.screenWidth = width
        self.screenHeight = height
        self.amountWidth = int(self.screenWidth / self.length)
        self.amountHeight = int(self.screenHeight / self.length)
        self.allTiles = []
    
    def drawBoard(self):
        #calculate amount of turtles in each row / column
        for i in range(self.amountHeight):
            self.allTiles.append([])
            for j in range(self.amountWidth):
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.allTiles[i].append("lime")
                    else:
                        self.allTiles[i].append("green")
                else:
                    if j % 2 != 0:
                        self.allTiles[i].append("lime")
                    else:
                        self.allTiles[i].append("green")

    def changeColour(self, colour, x, y):
        if x >= len(self.allTiles) or y >= len(self.allTiles[x]) or x < 0 or y < 0:
            return
        if colour == "tiles":
            if x % 2 == 0:
                if y % 2 == 0:
                    self.allTiles[x][y] = "lime"
                else:
                    self.allTiles[x][y] = "green"
            else:
                if y % 2 != 0:
                    self.allTiles[x][y] = "lime"
                else:
                    self.allTiles[x][y] = "green"
        elif colour == "blue":
            self.allTiles[x][y] = "blue"
        elif colour == "lightblue":
            self.allTiles[x][y] = "lightblue"
        elif colour == "red":
            self.allTiles[x][y] = "red"

    def returnTiles(self):
        return self.allTiles

    def reset(self):
        for i in range(self.amountHeight):
            for j in range(self.amountWidth):
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.allTiles[i][j] = "lime"
                    else:
                        self.allTiles[i][j] = "green"
                else:
                    if j % 2 != 0:
                        self.allTiles[i][j] = "lime"
                    else:
                        self.allTiles[i][j] = "green"