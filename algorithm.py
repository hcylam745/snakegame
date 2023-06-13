class algorithm:
    def __init__(self, update_time, allTiles):
        self.update_time = update_time
        self.screenWidth = allTiles.screenWidth
        self.screenHeight = allTiles.screenHeight
        self.length = allTiles.length

    # tries to find the shortest path from current to apple.
    # it does not consider future moves, just tries to take the path that brings it closer to the
    # target. Improvement could be having the system run a simulation, probably using BFS
    # such that it doesnt run itself into a corner
    def shortestpath(self, allTiles, initApple, initSnake):
        (apple_y, apple_x) = initApple.appleTurtle.position()
        apple_x = (self.screenHeight - apple_x)/(20*self.length)
        apple_y = (self.screenWidth - apple_y)/(20*self.length)
        # apple_x and apple_y store the coordinates of the apple.
        
        tiles = allTiles.returnTiles()
        direction = initSnake.direction

        snake = []

        # this isnt really necessary, just get the position of the head.
        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                if tiles[i][j].fillcolor() == "lightblue":
                    snake.insert(0,[i,j])
                else:
                    if tiles[i][j].fillcolor() == "blue":
                        snake.append([i,j])

        # snake now stores the positions of each tile that the snake is on. 
        # is not sorted in any order other than 0th position being the front.
        dist = abs(apple_x - snake[0][0]) + abs(apple_y - snake[0][1])

        #up_dist, right_dist, ...
        u_dist = abs(apple_x - (snake[0][0]-1)) + abs(apple_y - snake[0][1])
        if u_dist < dist and direction != "down" and ([snake[0][0] - 1,snake[0][1]] not in snake):
            return "up"
        r_dist = abs(apple_x - snake[0][0]) + abs(apple_y - (snake[0][1]-1))
        if r_dist < dist and direction != "left" and ([snake[0][0],snake[0][1] - 1] not in snake):
            return "right"
        d_dist = abs(apple_x - (snake[0][0]+1)) + abs(apple_y - snake[0][1])
        if d_dist < dist and direction != "up" and ([snake[0][0] + 1,snake[0][1]] not in snake):
            return "down"
        l_dist = abs(apple_x - snake[0][0]) + abs(apple_y - (snake[0][1]+1))
        if l_dist < dist and direction != "right" and ([snake[0][0],snake[0][1] + 1] not in snake):
            return "left"

        # this is when we are moving in the entirely opposite
        # direction of the apple, while on the axis that we aren't moving on, the snake head's 
        # coordinate is the same as the apple.
        if ((snake[0][0] == int(apple_x) and (direction == "right" or direction == "left")) 
        or (snake[0][1] == int(apple_y) and (direction == "up" or direction == "down"))):
            if direction == "right" or direction == "left":
                if snake[0][1] == 0 or [snake[0][0]-1, snake[0][1]] in snake:
                    return "down"
                else:
                    return "up"
            else:
                if snake[0][0] == 0  or [snake[0][0], snake[0][1]-1] in snake:
                    return "left"
                else:
                    return "right"
        else:
            # this is when the snake head has one same coordinate on one of the axis as the apple,
            # but moving in the apple's direction would cause the snake to collide with itself.
            if (direction == "up" and [snake[0][0]-1, snake[0][1]] in snake) or (direction == "down" and [snake[0][0]+1, snake[0][1]] in snake):
                if [snake[0][0],snake[0][1] + 1] in snake:
                    if [snake[0][0],snake[0][1] - 1] not in snake:
                        return "right"
                else:
                    return "left"
            
            if (direction == "right" and [snake[0][0], snake[0][1] - 1] in snake) or (direction == "left" and [snake[0][0], snake[0][1] + 1] in snake):
                if [snake[0][0]-1, snake[0][1]] in snake:
                    if[snake[0][0]+1, snake[0][1]] not in snake:
                        return "down"
                else:
                    return "up"
            return "none"
            
                
