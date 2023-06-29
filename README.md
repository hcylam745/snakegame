# **Snake Made Using Pygame With Various Algorithms**

## How to play:

Run start.py, with:

```
run_greedy = False
run_bfs = False
run_player = True
```

Play using the arrow keys.

## How to run the algorithms:

### <ins>Greedy 1 (Tries to move towards the apple, without considering a full path to it.):</ins>
Run start.py, with:
```
run_greedy = True
run_bfs = False
run_player = False
```
![Greedy GIF](Greedy.GIF)
### <ins>Greedy 2 (Uses BFS to scan the whole board, and determines the shortest path to the apple.)</ins>
Run start.py, with:
```
run_greedy = False
run_bfs = True
run_player = False
```
![BFS GIF](BFS.GIF)
## Details on the algorithms:

### Greedy 1:
Before the snake moves forward each turn, the algorithm calculates which direction would result in the distance between the snake and the apple being reduced. If the direction chosen does not result in a collision or going out of bounds, the snake goes in that direction. <br/><br/>
There are then two scenarios in which the algorithm gets through the logic above without deciding on a direction: <br/>

1. The snake is moving in the entirely opposite direction of the apple, hence there is no direction that would result in the distance between the snake and the apple being reduced. Since the snake is moving in the opposite direction of the apple, if the snake is moving left or right, going up or down gives the snake options to go towards the appple, and vice versa.
2. One of the coordinates of the snake head is the same as the respective coordinate of the apple, but moving in the apple's direction would cause the snake to collide with itself. To avoid a collision, the algorithm decides to go in the direction that would not result in a collision with itself.
 <br/>

### Greedy 2:
Before the snake moves forward each turn, the algorithm does a BFS search on the board, and uses Djikstra's algorithm to determine what the shortest path to the apple is. The implementation of Djikstra's algorithm returns a list of directions that would result in the snake going to apple, and the snake chooses the list in the list of directions to move. 
<br/><br/>
After moving towards the apple, it recalculates the shortest path to the apple using Djikstra's algorithm again, and chooses the first direction in the list of directions that would lead it to the apple. 
<br/><br/>
If there is no path to the apple, then the algorithm chooses the position that is farthest from the snake currently, and takes one step of the shortest path to that, then recalculates the farthest position and repeats.