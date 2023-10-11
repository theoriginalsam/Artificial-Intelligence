# Artificial-Intelligence

# 8-Puzzle Solver

This repository contains Python programs for generating random 8-puzzle board configurations and solving them using the A* search algorithm.

## `random-board.py`

To generate a random starting state for the 8-puzzle problem, use `random-board.py`. It takes two command-line arguments: the random number generator seed and the number of random moves to make. For example:

```shell
python random-board.py 10 50
astar.py
astar.py performs A* search for the 8-puzzle problem. It reads an 8-puzzle board configuration from standard input and takes two command-line arguments: the heuristic to use and the cost per step. For example:

shell
Copy code
python astar.py 2 1
Heuristic Options:

0 - h(n) = 0
1 - h(n) = Number of tiles displaced from the goal
2 - h(n) = Sum of Manhattan (city-block) distances of all tiles from the goal
3 - h(n) = Your novel heuristic
Cost Per Step:

0 - g(step) = 0
1 - g(step) = 1
2 - g(step) = 2
...
Output
The program will output the following information:

Total number of nodes visited/expanded (V)
Maximum number of nodes stored in memory (closed list + open list size) (N)
Depth of the optimal solution (d)
Approximate effective branching factor (b)
Example Usage
Provide examples of how to use your programs with different configurations and heuristics.

Author
Samir Poudel
