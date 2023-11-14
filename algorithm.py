import queue
import copy

class algorithm:
    def __init__(self, update_time, allTiles):
        self.update_time = update_time
        self.screenWidth = allTiles.screenWidth
        self.screenHeight = allTiles.screenHeight
        self.length = allTiles.length

    def djikstra(self, allTiles, initApple):
        apple_x = initApple.xcoord
        apple_y = initApple.ycoord
        # apple_x and apple_y store the coordinates of the apple.

        tiles = allTiles.returnTiles()
        snake = []

        visited = {}

        coords = []

        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                if tiles[i][j]== "blue":
                    snake.append([i,j])
                else:
                    if tiles[i][j] == "lightblue":
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

            curr_key = [str(curr_pos[0] + 1) + "," + str(curr_pos[1]), str(curr_pos[0] - 1) + "," + str(curr_pos[1]), str(curr_pos[0]) + "," + str(curr_pos[1] - 1), str(curr_pos[0]) + "," + str(curr_pos[1] + 1)]
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
        return visited[str(int(apple_x)) + "," + str(int(apple_y))], visited

    # create a greedy algorithm that uses djikstra's algorithm to consider the shortest path to the apple,
    # rather than choosing a direction that leads the snake to the apple.
    # returns an array of the movements that the snake should make to go to the apple
    def shortestpathbfs(self, allTiles, initApple):
        
        result, visited = self.djikstra(allTiles, initApple)

        #if there is no path to apple, then tell the snake to stall, and scan again to see if there is a path to the apple.
        if result == float('inf'):
            largest = [0,""]
            for key in visited:
                if visited[key][0] != float('inf'):
                    if visited[key][0] > largest[0]:
                        largest = visited[key]
            return largest, True
        else:
            return result, False
            

        # given all outgoing edges, add them to a queue if the destination doesn't have value of inf.
        # we don't need to check if the newest distance we found is shorter than prev, since all edges
        # have weight 1, therefore if we search edges in the queue order that they were added in, we will
        # always have the minimum 

    # tries to find the shortest path from current to apple.
    # it does not consider future moves, just tries to take the path that brings it closer to the
    # target. Improvement could be having the system run a simulation, probably using BFS
    # such that it doesnt run itself into a corner
    def shortestpath(self, allTiles, initApple, initSnake):
        apple_x = initApple.xcoord
        apple_y = initApple.ycoord
        # apple_x and apple_y store the coordinates of the apple.
        
        tiles = allTiles.returnTiles()
        direction = initSnake.direction

        snake = []

        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                if tiles[i][j] == "lightblue":
                    snake.insert(0,[i,j])
                else:
                    if tiles[i][j] == "blue":
                        snake.append([i,j])

        # snake now stores the positions of each tile that the snake is on. 
        # is not sorted in any order other than 0th position being the front.
        dist = abs(apple_x - snake[0][0]) + abs(apple_y - snake[0][1])

        #up_dist, right_dist, ...
        u_dist = abs(apple_x - (snake[0][0]+1)) + abs(apple_y - snake[0][1])
        if u_dist < dist and direction != "down" and ([snake[0][0] + 1,snake[0][1]] not in snake):
            return "up"
        r_dist = abs(apple_x - snake[0][0]) + abs(apple_y - (snake[0][1]-1))
        if r_dist < dist and direction != "left" and ([snake[0][0],snake[0][1] - 1] not in snake):
            return "right"
        d_dist = abs(apple_x - (snake[0][0]-1)) + abs(apple_y - snake[0][1])
        if d_dist < dist and direction != "up" and ([snake[0][0] - 1,snake[0][1]] not in snake):
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
                if snake[0][1] == 0 or [snake[0][0]+1, snake[0][1]] in snake:
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
                if [snake[0][0]+1, snake[0][1]] in snake:
                    if[snake[0][0]-1, snake[0][1]] not in snake:
                        return "down"
                else:
                    return "up"
            return "none"

    def shortestandlongestpath(self, allTiles, initApple):

        result, visited = self.djikstra(allTiles, initApple)

        #print(result)

        result[0] = float('inf')

        #if there is no path to apple, take the longest possible path.
        if result[0] == float('inf'):
            # to find the longest path, do a bfs search. The last bfs search to complete is the longest path possible.
            
            snakepos = [-1, -1]

            # get snake position.
            tiles = copy.deepcopy(allTiles.returnTiles())
            for i in range(len(tiles)):
                for j in range(len(tiles[i])):
                    tile = tiles[i][j]
                    if tile == "lightblue":
                        snakepos[0] = i
                        snakepos[1] = j
                        tiles[i][j] = "invalid"
                    elif tile == "blue":
                        tiles[i][j] = "invalid"
                    else:
                        tiles[i][j] = "valid"

            path = []

            state = None
            bfs_q = queue.Queue()
            bfs_q.put([snakepos, path, tiles])

            loops = 0

            while not bfs_q.empty():
                #print(loops)
                loops+=1

                state = bfs_q.get()
                snake = state[0]
                curr_path = state[1]
                curr_tiles = state[2]

                # print("newloop")
                # for vert_tile in tiles:
                #     print(vert_tile)
                # print([state[0],state[1]])

                # print(snake)

                if ((tiles[snake[0]][snake[1]].isdigit() and (len(curr_path) + 1 > int(tiles[snake[0]][snake[1]]))) or (tiles[snake[0]][snake[1]] == "valid")) and (curr_tiles[snake[0]][snake[1]] != "invalid"):
                    tiles[snake[0]][snake[1]] = str(len(curr_path) + 1)

                tmp_tiles = copy.deepcopy(curr_tiles)
                tmp_tiles[snake[0]][snake[1]] = "invalid"

                # print("tmp tiles = ")
                # for vert_tile in tmp_tiles:
                #     print(vert_tile)
                # print([state[0],state[1]])

                # try to move up

                if (snake[0] != 0) and (tiles[snake[0]-1][snake[1]] != "invalid") and (curr_tiles[snake[0]-1][snake[1]] != "invalid"):
                    valid = False
                    
                    if (tiles[snake[0]-1][snake[1]]).isdigit():
                        if (len(curr_path) + 1 > int(tiles[snake[0]-1][snake[1]])):
                            valid = True
                    else:
                        valid = True

                    if valid:
                        #print("trying to move up")

                        tmp_snakepos = copy.deepcopy(snake)
                        tmp_snakepos[0] -= 1
                        tmp_path = copy.deepcopy(curr_path)
                        tmp_path.append("down")

                        temp_tiles = copy.deepcopy(tmp_tiles)
                        

                        bfs_q.put([tmp_snakepos, tmp_path, temp_tiles])
                    

                # try to move right
                if (snake[1]+1 < len(tiles[0])) and (tiles[snake[0]][snake[1]+1] != "invalid") and (curr_tiles[snake[0]][snake[1]+1] != "invalid"):
                    valid = False

                    if (tiles[snake[0]][snake[1]+1]).isdigit():
                        if (len(curr_path) + 1 > int(tiles[snake[0]][snake[1]+1])):
                            valid = True
                    else:
                        valid = True

                    if valid:
                        #print("trying to move right")

                        tmp_snakepos = copy.deepcopy(snake)
                        tmp_snakepos[1] += 1
                        tmp_path = copy.deepcopy(curr_path)
                        tmp_path.append("left")

                        temp_tiles = copy.deepcopy(tmp_tiles)
                        

                        bfs_q.put([tmp_snakepos, tmp_path, temp_tiles])
                
                # try to move down
                if (snake[0]+1 < len(tiles)) and (tiles[snake[0]+1][snake[1]] != "invalid") and (curr_tiles[snake[0]+1][snake[1]] != "invalid"):
                    valid = False
                    
                    if (tiles[snake[0]+1][snake[1]]).isdigit():
                        if (len(curr_path) + 1 > int(tiles[snake[0]+1][snake[1]])):
                            valid = True
                    else:
                        valid = True

                    if valid:
                        #print("trying to move down")

                        tmp_snakepos = copy.deepcopy(snake)
                        tmp_snakepos[0] += 1
                        tmp_path = copy.deepcopy(curr_path)
                        tmp_path.append("up")

                        temp_tiles = copy.deepcopy(tmp_tiles)
                        

                        bfs_q.put([tmp_snakepos, tmp_path, temp_tiles])

                # try to move left
                if (snake[1] != 0) and (tiles[snake[0]][snake[1]-1] != "invalid") and (curr_tiles[snake[0]][snake[1]-1] != "invalid"):
                    valid = False

                    # print(tiles[snake[0]][snake[1]-1].isdigit())
                    # print(tiles[snake[0]][snake[1]-1])
                    if (tiles[snake[0]][snake[1]-1]).isdigit():
                        if (len(curr_path) + 1 > int(tiles[snake[0]][snake[1]-1])):
                            valid = True
                    else:
                        valid = True
                    
                    if valid:
                        #print("trying to move left")

                        tmp_snakepos = copy.deepcopy(snake)
                        tmp_snakepos[1] -= 1
                        tmp_path = copy.deepcopy(curr_path)
                        tmp_path.append("right")

                        temp_tiles = copy.deepcopy(tmp_tiles)
                        

                        bfs_q.put([tmp_snakepos, tmp_path, temp_tiles])
            
            longest_path = state[1]
            
            # print("longest_path")
            # print(longest_path)

            path_string = ","
            for direction in longest_path:
                path_string += direction + ","

            return [1, path_string]
        else:
            return result