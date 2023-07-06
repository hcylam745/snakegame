import numpy as np

from snake_game import snakegame
from tf_agents.environments import py_environment
from tf_agents.specs import array_spec
from tf_agents.trajectories import time_step as ts

import time

from snake_game import snakegame

class MachineLearning(py_environment.PyEnvironment):

    def __init__(self):
        self.game = snakegame(True, False, False, False)
        max_val = max(self.game.initTiles.amountWidth, self.game.initTiles.amountHeight)
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=3, name='action')
        # for inputs, do: 0 = apple above, 1 = apple right, 2 = apple down, 3 = apple left, 
        # 4 = distance to obstacle above, 5 = distance to obstacle right, 
        # 6 = distance to obstacle down, 7 = distance to obstacle left, 8 = direction

        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(9,), dtype=np.int32, minimum=0, maximum=max_val+1)
        self._lost = False

        self._state = []

        self.moves_since_apple = 0

        self.update_spec()

    def update_spec(self):
        self._state = []
        snakepos = []
        applepos = [self.game.initApple.ycoord, self.game.initApple.xcoord]
        tiles = self.game.initTiles.returnTiles()
        for i in range(len(tiles)):
            for j in range(len(tiles[0])):
                colour = tiles[i][j]
                if colour == "lightblue":
                    snakepos = [i, j]
                    break
        
        # apple above
        self._state.append(0)
        # apple right
        self._state.append(0)
        # apple down
        self._state.append(0)
        # apple left
        self._state.append(0)
        if snakepos[0] > applepos[0]:
            #apple is down relative to snake.
            self._state[2] = 1
        elif snakepos[0] < applepos[0]:
            #apple is up relative to snake.
            self._state[0] = 1
        
        if snakepos[1] > applepos[1]:
            #apple is right relative to the snake.
            self._state[1] = 1
        elif snakepos[1] < applepos[1]:
            #apple is left relative to the snake.
            self._state[3] = 1

        # obstacle above
        self._state.append(0)
        # obstacle right
        self._state.append(1)
        # obstacle down
        self._state.append(2)
        # obstacle left
        self._state.append(1)

        snake_x = snakepos[1] - 1
        # check for obstacles on the right.
        while (snake_x >= 0):
            self._state[5] += 1
            if tiles[snakepos[0]][snake_x] == "blue":
                break
            snake_x -= 1
        
        snake_x = snakepos[1] + 1
        # check for obstacles on the left.
        while (snake_x < self.game.initTiles.amountWidth):
            self._state[7] += 1
            if tiles[snakepos[0]][snake_x] == "blue":
                break
            snake_x += 1
            
        
        snake_y = snakepos[0] - 1
        # check for obstacles below.
        while (snake_y >= 0):
            self._state[6] += 1
            if tiles[snake_y][snakepos[1]] == "blue":
                break
            snake_y -= 1

        snake_y = snakepos[0] + 1
        # check for obstacles above.
        while (snake_y < self.game.initTiles.amountHeight):
            self._state[4] += 1
            if tiles[snake_y][snakepos[1]] == "blue":
                break
            snake_y += 1

        direction = self.game.initSnake.direction
        if direction == "up":
            self._state.append(0)
        elif direction == "right":
            self._state.append(1)
        elif direction == "down":
            self._state.append(2)
        elif direction == "left":
            self._state.append(3)
        else:
            self._state.append(0)



    def action_spec(self):
        return self._action_spec
    
    def observation_spec(self):
        return self._observation_spec

    def _reset(self):
        self._lost = False
        self.game.lost = True
        self.game.reset()
        time.sleep(0.05)
        self.game.new = 0
        self.moves_since_apple = 0
        self.update_spec()
        return ts.restart(np.asarray(self._state, dtype = np.int32))
    
    def _step(self, action):
        if self._lost:
            # snake died. reset.
            return self._reset()
        
        snakepos = []
        tiles = self.game.initTiles.returnTiles()
        for i in range(len(tiles)):
            if len(snakepos) > 0:
                break
            for j in range(len(tiles[i])):
                colour = tiles[i][j]
                if colour == "lightblue":
                    snakepos.append(i)
                    snakepos.append(j)
                    break
        dist_prev = abs(self.game.initApple.xcoord -  snakepos[0]) + abs(self.game.initApple.ycoord - snakepos[1])
        newcoords = []
        if action == 0:
            self.game.up()
        elif action == 1:
            self.game.right()
        elif action == 2:
            self.game.down()
        elif action == 3:
            self.game.left()
        else:
            raise ValueError('`action` should be 0, 1 or 2')
            
        prev_apple_count = self.game.apple_count
        self.game.updateTime()
        self.update_spec()

        tiles = self.game.initTiles.returnTiles()
        for i in range(len(tiles)):
            if len(newcoords) > 0:
                break
            for j in range(len(tiles[i])):
                colour = tiles[i][j]
                if colour == "lightblue":
                    newcoords.append(i)
                    newcoords.append(j)
                    break

        dist_new = abs(self.game.initApple.xcoord - newcoords[0]) + abs(self.game.initApple.ycoord - newcoords[1])

        #euclid_dist = math.sqrt(pow(abs(self.game.initApple.xcoord - newcoords[0]),2) + pow(abs(self.game.initApple.ycoord - newcoords[1]), 2))

        survival_multiplier = 1.0
        # this value should be adjusted
        discount_num = 0.05
        if self.moves_since_apple >= 1000:
            if self.game.apple_count > 3:
                print("resetting due to long time")
                time.sleep(5)
            self._reset()
            return ts.termination(np.asarray(self._state,dtype=np.int32), reward=-1000)
        
        if self.game.lost == True:
            self._lost = True
            return ts.termination(np.asarray(self._state, dtype=np.int32), reward=-100)

        if self.game.apple_count > prev_apple_count:
            self.moves_since_apple = 0
            if self.game.apple_count == (self.game.initTiles.amountWidth*self.game.initTiles.amountHeight - 1):
                return ts.termination(np.asarray(self._state, dtype=np.int32), reward=1000)
            else:
                return ts.transition(np.asarray(self._state, dtype=np.int32), reward=100, discount=discount_num)
        self.moves_since_apple += 1
        if dist_prev - dist_new > 0:
            return ts.transition(np.asarray(self._state, dtype=np.int32), reward=1, discount=discount_num)
        else:
            return ts.transition(np.asarray(self._state, dtype=np.int32), reward=-1, discount=discount_num)
        #return ts.transition(np.asarray(self._state, dtype=np.int32), 0, discount)