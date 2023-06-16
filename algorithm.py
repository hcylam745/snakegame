import time

class algorithm:
    def __init__(self, update_time, allTiles):
        self.update_time = update_time
        self.screenWidth = allTiles.screenWidth
        self.screenHeight = allTiles.screenHeight
        self.length = allTiles.length

    # create a greedy algorithm that uses djikstra's algorithm to consider the shortest path to the apple,
    # rather than choosing a direction that leads the snake to the apple.
    # returns an array of the movements that the snake should make to go to the apple
    def shortestpathbfs(self, allTiles, initApple):
        (apple_y, apple_x) = initApple.appleTurtle.position()
        apple_x = (self.screenHeight - apple_x) / (20*self.length)
        apple_y = (self.screenWidth - apple_y) / (20*self.length)
        # apple_x and apple_y store the coordinates of the apple.

        tiles = allTiles.returnTiles()
        snake = []

        visited = {}

        coords = []

        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                if tiles[i][j].fillcolor() == "blue":
                    snake.append([i,j])
                else:
                    if tiles[i][j].fillcolor() == "lightblue":
                        snake.insert(0, [i,j])
                        visited[str(i) + "," + str(j)] = [0, ""]
                        coords.append(i)
                        coords.append(j)
                    else:
                        visited[str(i) + "," + str(j)] = [float('inf'), ""]
        # for a coordinate to be in visited, it must be on the board, as well as not be the snake.
        # hence, keys of visited can be used as a filter to make sure the movement is valid.

        # edges_queue stores a queue of all edges outgoing from the already scanned section
        # each edge is represented by its destination.
        # initialise with an edge that goes to the starting pos
        edges_queue = [str(coords[0]) + "," + str(coords[1])]

        # for loop checks all outgoing edges to make sure they are not part of the snake, 
        # not already scanned and are in the board, then appends those edges to the queue
        # as well as assignging distance values for the nodes those edges go to.
        while len(edges_queue) > 0:
            # take the top of the queue, store the coordinates in curr_pos, remove the top of queue
            curr_pos = edges_queue[0].split(",")
            curr_pos[0] = int(curr_pos[0])
            curr_pos[1] = int(curr_pos[1])
            del edges_queue[0]

            curr_key = [str(curr_pos[0] - 1) + "," + str(curr_pos[1]), str(curr_pos[0] + 1) + "," + str(curr_pos[1]), str(curr_pos[0]) + "," + str(curr_pos[1] - 1), str(curr_pos[0]) + "," + str(curr_pos[1] + 1)]
            for i in range(len(curr_key)):
                if curr_key[i] in visited and visited[curr_key[i]][0] == float('inf'):
                    edges_queue.append(curr_key[i])
                    direction = "none"
                    if i == 0:
                        direction = "up"
                    if i == 1:
                        direction = "down"
                    if i == 2:
                        direction = "right"
                    if i == 3:
                        direction = "left"
                    visited[curr_key[i]] = [visited[str(curr_pos[0]) + "," + str(curr_pos[1])][0] + 1, visited[str(curr_pos[0]) + "," + str(curr_pos[1])][1] + "," + direction]
        
        #if there is no path to apple, then tell the snake to stall, and scan again to see if there is a path to the apple.
        if visited[str(int(apple_x)) + "," + str(int(apple_y))][0] == float('inf'):
            largest = [0,""]
            for key in visited:
                if visited[key][0] != float('inf'):
                    if visited[key][0] > largest[0]:
                        largest = visited[key]
            return largest, True
        else:
            return visited[str(int(apple_x)) + "," + str(int(apple_y))], False
            

        # given all outgoing edges, add them to a queue if the destination doesn't have value of inf.
        # we don't need to check if the newest distance we found is shorter than prev, since all edges
        # have weight 1, therefore if we search edges in the queue order that they were added in, we will
        # always have the minimum 

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