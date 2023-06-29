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
        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=2, name='action')
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(self.game.initTiles.amountWidth*self.game.initTiles.amountHeight+1,), dtype=np.int32, minimum=0, maximum=3)
        self._lost = False

        self._state = []

        self.moves_since_apple = 0

        self.update_spec()

    def update_spec(self):
        self._state = []
        tiles = self.game.initTiles.returnTiles()
        for i in range(len(tiles)):
            for j in range(len(tiles[0])):
                colour = tiles[i][j]
                if colour == "red":
                    self._state.append(3)
                elif colour == "lightblue":
                    self._state.append(1)
                elif colour == "blue":
                    self._state.append(2)
                else:
                    self._state.append(0)

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
        time.sleep(0.2)
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

        #tiles_height = self.game.initTiles.amountHeight
        #tiles_width = self.game.initTiles.amountWidth

        # do something based on action by snake
        '''direction = self.game.initSnake.direction
        if action == 0:
            if direction == "down":
                if snakepos[1] + 1 == tiles_width:
                    #left will result in death, so change direction.
                    self.game.right()
                else:
                    self.game.left()
            else:
                if snakepos[0]+1 == tiles_height:
                    #up will result in death, so change direction.
                    if direction == "left":
                        self.game.down()
                    else:
                        if snakepos[1] == 0:
                            #right will result in death, so change direction
                            if direction == "up":
                                self.game.left()
                            else:
                                self.game.down()
                        else:
                            self.game.right()
                else:
                    self.game.up()
        elif action == 1:
            if direction == "right":
                if snakepos[1] == 0:
                    #right will result in death, so change direction.
                    if snakepos[0] == 0:
                        #down will result in death, so change direction.
                        self.game.up()
                    else:
                        self.game.down()
                else:
                    self.game.right()
            else:
                if direction == "down":
                    if snakepos[1] == 0:
                        #right will result in death, so change direction
                        self.game.left()
                    else:
                        self.game.right()
                else:
                    if snakepos[1] + 1 == tiles_width:
                        #left will result in death, so change direction.
                        if snakepos[0] + 1 == tiles_height:
                            #up will result in death, so change direction
                            if direction == "up":
                                self.game.right()
                            else:
                                self.game.down()
                        else:
                            self.game.up()
                    else:
                        self.game.left()
        elif action == 2:
            if direction == "up":
                if snakepos[1] == 0:
                    #right will result in death, so change direction.
                    self.game.left()
                else:
                    self.game.right()
            else:
                if snakepos[0] == 0:
                    #down will result in death, so change direction.
                    if direction == "left":
                        self.game.up()
                    else:
                        if snakepos[1] == 0:
                            #right will result in death, so change direction
                            if direction == "down":
                                self.game.left()
                            else:
                                self.game.up()
                        else:
                            self.game.right()
                else:
                    self.game.down()
        else:
            raise ValueError('`action` should be 0, 1, or 2')'''
        dist_prev = abs(self.game.initApple.xcoord -  snakepos[0]) + abs(self.game.initApple.ycoord - snakepos[1])
        newcoords = []
        direction = self.game.initSnake.direction
        if direction == "up":
            if action == 0:
                self.game.left()
            elif action == 1:
                self.game.up()
            elif action == 2:
                self.game.right()
            else:
                raise ValueError('`action` should be 0, 1 or 2')
        elif direction == "right":
            if action == 0:
                self.game.up()
            elif action == 1:
                self.game.right()
            elif action == 2:
                self.game.down()
            else:
                raise ValueError('`action` should be 0, 1 or 2')
        elif direction == "down":
            if action == 0:
                self.game.right()
            elif action == 1:
                self.game.down()
            elif action == 2:
                self.game.left()
            else:
                raise ValueError('`action` should be 0, 1 or 2')
        elif direction == "left":
            if action == 0:
                self.game.down()
            elif action == 1:
                self.game.left()
            elif action == 2:
                self.game.up()
            else:
                raise ValueError('`action` should be 0, 1 or 2')
        else:
            if action == 0:
                self.game.left()
            elif action == 1:
                self.game.up()
            elif action == 2:
                self.game.right()
            else:
                raise ValueError('`action` should be 0, 1 or 2')
            
        prev_apple_count = self.game.apple_count
        self.game.updateTime()
        self.update_spec()
        time.sleep(0.01)

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

        apple_multiplier = 2.0
        survival_multiplier = 1.0
        # this value should be adjusted
        discount = 0.95
        if self.moves_since_apple >= 150:
            self._reset()
            return ts.termination(np.asarray(self._state,dtype=np.int32), -100)
        
        if self.game.lost == True:
            self._lost = True
            return ts.termination(np.asarray(self._state, dtype=np.int32), -10)

        if self.game.apple_count > prev_apple_count:
            if self.game.apple_count == (self.game.initTiles.amountWidth*self.game.initTiles.amountHeight - 1):
                return ts.termination(np.asarray(self._state, dtype=np.int32), 10)
            else:
                apple_multiplier *= 2.0
                self.moves_since_apple = 0
                return ts.transition(np.asarray(self._state, dtype=np.int32), 20*apple_multiplier, discount)
        self.moves_since_apple += 1
        #if dist_prev - dist_new > 0:
        #    return ts.transition(np.asarray(self._state, dtype=np.int32), survival_multiplier, discount)
        #else:
        #    return ts.transition(np.asarray(self._state, dtype=np.int32), -survival_multiplier, discount)
        return ts.transition(np.asarray(self._state, dtype=np.int32), 0, discount)
