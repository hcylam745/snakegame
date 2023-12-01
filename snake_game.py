import time
import pygame

from messages import messages
from snake import snake
from apple import apple
from tiles import tiles
from algorithm import algorithm

class snakegame:
    def __init__(self, ml, greedy, bfs, player):
        self.update_time = 150
        self.width = 550
        self.height = 550
        self.window_width = 650
        self.window_height = 650
        self.apple_count = 0
        self.buffer = ["none", "none"]
        self.run_algo_greedy = greedy
        self.run_algo_bfs = bfs
        self.run_bfs_repeat = False
        self.run_algo_shortestlongest = True
        self.run_player = player
        self.run_ml = False
        self.list_of_directions = []
        self.lost = False

        pygame.init()
        # double the size of with turtles.
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.screen.fill((255,255,255))
        self.initTiles = tiles(36, self.width, self.height)
        self.initTiles.drawBoard(self.screen)
        self.initSnake = snake()
        self.initSnake.reset(self.initTiles, self.screen)
        self.initApple = apple()
        self.initApple.spawnApple(self.initTiles, self.initSnake,self.screen)
        self.initMessage = messages()

        self.new = 1

        if ml == True:
            self.run_ml = True
            self.run_player = False
            self.run_algo_bfs = False
            self.run_algo_greedy = False
            self.new = 0

    def start(self):
        while self.lost == False and self.run_ml == False:
            if self.run_player == True:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.left()
                        elif event.key == pygame.K_RIGHT:
                            self.right()
                        elif event.key == pygame.K_UP:
                            self.up()
                        elif event.key == pygame.K_DOWN:
                            self.down()
            self.updateTime()
            pygame.time.delay(self.update_time)
        
        while self.lost == True:
            pygame.draw.rect(self.screen, (170, 170, 170), [self.window_width//2-15, self.height+50, 30, 30])
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if self.window_width//2-15 <= mouse[0] <= self.window_width//2+15 and self.height+50 <= mouse[1] <= self.height + 80:
                        self.reset()
            pygame.display.update()

    def left(self):
        if self.initSnake.direction == "right":
            return
        if self.buffer[0] == "none":
            self.buffer[0] = "left"
            self.initSnake.rotate("left")
        elif self.buffer[1] == "none":
            self.buffer[1] = "left"
        if self.new == 1:
            self.new = 0
            self.updateTime()
    
    def down(self):
        if self.initSnake.direction == "up":
            return
        if self.buffer[0] == "none":
            self.buffer[0] = "down"
            self.initSnake.rotate("down")
        elif self.buffer[1] == "none":
            self.buffer[1] = "down"
        if self.new == 1:
            self.new = 0
            self.updateTime()
    
    def right(self):
        if self.initSnake.direction == "left":
            return
        if self.buffer[0] == "none":
            self.buffer[0] = "return"
            self.initSnake.rotate("right")
        elif self.buffer[1] == "none":
            self.buffer[1] = "right"
        if self.new == 1:
            self.new = 0
            self.updateTime()
    
    def up(self):
        if self.initSnake.direction == "down":
            return
        if self.buffer[0] == "none":
            self.buffer[0] = "up"
            self.initSnake.rotate("up")
        elif self.buffer[1] == "none":
            self.buffer[1] = "up"
        if self.new == 1:
            self.new = 0
            self.updateTime()
    
    def runGreedy(self):
        alg = algorithm(self.update_time, self.initTiles)
        direction = alg.shortestpath(self.initTiles, self.initApple, self.initSnake)

        if direction != "none":
            if direction == "up":
                self.list_of_directions.append("up")
            elif direction == "left":
                self.list_of_directions.append("left")
            elif direction == "right":
                self.list_of_directions.append("right")
            else:
                self.list_of_directions.append("down")
    
    def runGreedyBFS(self):
        alg = algorithm(self.update_time, self.initTiles)
        direction, failed_to_get_apple = alg.shortestpathbfs(self.initTiles, self.initApple)

        if failed_to_get_apple:
            self.run_bfs_repeat = True

        dir_list = direction[1].split(",")

        if len(dir_list) >= 2:
            self.list_of_directions.append(dir_list[1])
    
    def runShortestLongest(self):
        alg = algorithm(self.update_time, self.initTiles)
        directions = alg.shortestandlongestpathefficient(self.initTiles, self.initApple, self.initSnake)

        dir_list = directions[1].split(",")

        if len(dir_list) >= 2:
            self.list_of_directions.append(dir_list[1])

    def updateTime(self):
        if self.run_algo_greedy == True:
            self.runGreedy()
        if self.run_algo_bfs == True:
            self.runGreedyBFS()
        if self.run_algo_shortestlongest == True:
            self.runShortestLongest()
        
        if len(self.list_of_directions) > 0:
            curr_dir = self.list_of_directions[0]
            del self.list_of_directions[0]
            if curr_dir == "up":
                self.up()
            if curr_dir == "down":
                self.down()
            if curr_dir == "right":
                self.right()
            if curr_dir == "left":
                self.left()

        if self.initSnake.xcor < 0 or self.initSnake.ycor < 0 or self.initSnake.xcor >= self.initTiles.amountWidth or self.initSnake.ycor >= self.initTiles.amountHeight:
            self.lost = True
            self.initMessage.draw("You Lost! ", self.apple_count, self.screen, self.width, self.height)
            return

        if self.initSnake.direction != "none" and self.initSnake.move(self.initTiles, self.screen) == False:
            self.lost = True
            self.initMessage.draw("You Lost! ", self.apple_count, self.screen, self.width, self.height)
            return

        if self.initSnake.xcor == self.initApple.xcoord and self.initSnake.ycor == self.initApple.ycoord:
            self.apple_count += 1
            self.initSnake.add(self.initApple.xcoord, self.initApple.ycoord, self.initTiles)
            self.initApple.spawnApple(self.initTiles, self.initSnake, self.screen)
        
        for i in range(1, len(self.initSnake.snakeCoords)):
            if self.initSnake.xcor == self.initSnake.snakeCoords[i][0] and self.initSnake.ycor == self.initSnake.snakeCoords[i][1]:
                self.lost = True
                self.initMessage.draw("You Lost! ", self.apple_count, self.screen, self.width, self.height)
                return
        
        if self.buffer[1] != "none":
            self.initSnake.rotate(self.buffer[1])
        self.buffer[0] = "none"
        self.buffer[1] = "none"

        pygame.display.update()
    
    def reset(self):
        if self.lost == True:
            apple_x = self.initApple.xcoord
            apple_y = self.initApple.ycoord

            self.screen.fill((255,255,255))
            self.initTiles.changeColour("tiles", apple_x, apple_y, self.screen)
            self.initTiles.reset(self.screen)
            self.initSnake.reset(self.initTiles, self.screen)
            self.initApple.spawnApple(self.initTiles, self.initSnake, self.screen)
            self.apple_count = 0
            self.new = 1
            self.buffer = ["none", "none"]
            self.list_of_directions = []
            self.initSnake.direction = "none"
            self.run_bfs_repeat = False
            self.lost = False

            pygame.display.update()

            self.start()