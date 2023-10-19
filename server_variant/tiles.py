#import pygame

lime = (60, 180, 60)
green = (0, 130, 0)
blue = (30, 30, 160)
lightblue = (30, 130, 180)
red = (180, 30, 30)

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
                #xpos = self.screenWidth - j * self.length
                #ypos = self.screenHeight - i * self.length
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.allTiles[i].append("lime")
                        #pygame.draw.rect(screen,lime,(xpos, ypos, self.length, self.length))
                    else:
                        self.allTiles[i].append("green")
                        #pygame.draw.rect(screen,green,(xpos, ypos, self.length, self.length))
                else:
                    if j % 2 != 0:
                        self.allTiles[i].append("lime")
                        #pygame.draw.rect(screen,lime,(xpos, ypos, self.length, self.length))
                    else:
                        self.allTiles[i].append("green")
                        #pygame.draw.rect(screen,green,(xpos, ypos, self.length, self.length))

    def changeColour(self, colour, x, y):
        #xpos = self.screenWidth - y * self.length
        #ypos = self.screenWidth - x * self.length
        if x >= len(self.allTiles) or y >= len(self.allTiles[x]) or x < 0 or y < 0:
            return
        if colour == "tiles":
            if x % 2 == 0:
                if y % 2 == 0:
                    self.allTiles[x][y] = "lime"
                    #pygame.draw.rect(screen,lime,(xpos, ypos, self.length, self.length))
                else:
                    self.allTiles[x][y] = "green"
                    #pygame.draw.rect(screen,green,(xpos, ypos, self.length, self.length))
            else:
                if y % 2 != 0:
                    self.allTiles[x][y] = "lime"
                    #pygame.draw.rect(screen,lime,(xpos, ypos, self.length, self.length))
                else:
                    self.allTiles[x][y] = "green"
                    #pygame.draw.rect(screen,green,(xpos, ypos, self.length, self.length))
        elif colour == "blue":
            self.allTiles[x][y] = "blue"
            #pygame.draw.rect(screen, blue, (xpos, ypos, self.length, self.length))
        elif colour == "lightblue":
            self.allTiles[x][y] = "lightblue"
            #pygame.draw.rect(screen, lightblue, (xpos, ypos, self.length, self.length))
        elif colour == "red":
            self.allTiles[x][y] = "red"
            #pygame.draw.rect(screen, red, (xpos, ypos, self.length, self.length))

    def returnTiles(self):
        return self.allTiles

    def reset(self):
        for i in range(self.amountHeight):
            for j in range(self.amountWidth):
                xpos = self.screenWidth - j * self.length
                ypos = self.screenWidth - i * self.length
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.allTiles[i][j] = "lime"
                        #pygame.draw.rect(screen,lime,(xpos, ypos, self.length, self.length))
                    else:
                        self.allTiles[i][j] = "green"
                        #pygame.draw.rect(screen,green,(xpos, ypos, self.length, self.length))
                else:
                    if j % 2 != 0:
                        self.allTiles[i][j] = "lime"
                        #pygame.draw.rect(screen,lime,(xpos, ypos, self.length, self.length))
                    else:
                        self.allTiles[i][j] = "green"
                        #pygame.draw.rect(screen,green,(xpos, ypos, self.length, self.length))