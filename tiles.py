import turtle
import time
import random

class tiles:
    def __init__(self,length,width,height):
        self.length = length
        self.screenWidth = width
        self.screenHeight = height
        self.amountWidth = int(self.screenWidth / (10 * self.length))
        self.amountHeight = int(self.screenHeight / (10 * self.length))
        self.allTiles = []

    def drawBoard(self):
        # calculate amount of turtles in each row / column
        for i in range(self.amountHeight):
            self.allTiles.append([])
            for j in range(self.amountWidth):
                # create new turtle, append to 2d list for use
                newturtle = turtle.Turtle()
                newturtle.up()
                newturtle.speed(0)
                turtle.tracer(False)
                self.allTiles[i].append(newturtle)
                
                # create checkerboard pattern
                if i % 2 == 0:
                    if j % 2 == 0:
                        self.allTiles[i][j].color("lime")
                    else:
                        self.allTiles[i][j].color("green")
                else:
                    if j % 2 != 0:
                        self.allTiles[i][j].color("lime")
                    else:
                        self.allTiles[i][j].color("green")

                # draw tiles
                self.allTiles[i][j].goto(self.screenWidth - j * 20 * self.length, self.screenHeight - i * 20 * self.length)
                self.allTiles[i][j].shapesize(self.length)
                self.allTiles[i][j].shape("square")
        turtle.tracer(True)

    def returnTiles(self):
        return self.allTiles