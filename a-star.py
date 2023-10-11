#!/usr/bin/env python

import heapq
import sys

'''Refrences:
https://github.com/topics/8-puzzle-solver
https://stackoverflow.com/questions/16318757/calculating-manhattan-distance-in-python-in-an-8-puzzle-game
https://www.youtube.com/watch?v=xNJAm3D18s0&t=605s
https://github.com/rohanpillai20/8-Puzzle-by-A-Star-Search/blob/master/Puzzle8Solver.py
'''

class PuzzleNode:
    def __init__(self, node_id, board, parent=None, move=None, cost=0, heuristic=0):
        self.node_id = node_id
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

    def __lt__(self, other):
      return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def calculate_manhattan_distance(board, goal_dict):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                goal_position = goal_dict.get(board[i][j])
                if goal_position is not None:
                    goal_x, goal_y = goal_position
                    distance += abs(i - goal_x) + abs(j - goal_y)
    return distance
    


def get_neighbors(node):
    neighbors = []
    board = list(list(row) for row in node.board)  
    #print(board)
    i, j = next((i, j) for i in range(3) for j in range(3) if board[i][j] == 0)
    #print(i,j)
    
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in moves:
        #print(dx)
        x, y = i + dx, j + dy
        #print(x,y)
        if 0 <= x < 3 and 0 <= y < 3:
            neighbor_board = [row[:] for row in board]
            neighbor_board[i][j], neighbor_board[x][y] = neighbor_board[x][y], neighbor_board[i][j]
            neighbors.append(tuple(tuple(row) for row in neighbor_board)) 
    
    return neighbors

def a_star_search(initial_board, heuristic, cost_per_step):
    goal_board = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
    goal_dict = {goal_board[i][j]: (i, j) for i in range(3) for j in range(3)}
    
    open_set = []
    closed_set = set()
    node_id_counter = 0
    max_nodes_in_memory = 0 
    nodes_expanded = 0
    depth_of_solution = 0 
    
    start_node = PuzzleNode(node_id_counter, tuple(map(tuple, initial_board)))
    heapq.heappush(open_set, start_node)
    #print(open_set)
    while open_set:
        current_node = heapq.heappop(open_set)
        #print(current_node.board)
        nodes_expanded += 1 
        
        if len(open_set) + len(closed_set) > max_nodes_in_memory:
            max_nodes_in_memory = len(open_set) + len(closed_set) 
        
        if current_node.board == goal_board:
          
            depth_of_solution = 0
            node = current_node
            while node:
                depth_of_solution += 1
                node = node.parent
            depth_of_solution -= 1 
            break
        
        if current_node.board not in closed_set:
            closed_set.add(current_node.board)
            
            for neighbor_board in get_neighbors(current_node):
                node_id_counter += 1
                
                neighbor_node = PuzzleNode(node_id_counter, neighbor_board, current_node, cost=current_node.cost + cost_per_step)
                if heuristic == 0:
                    neighbor_node.heuristic = 0
                elif heuristic == 1:
                    distance = 0
                    for i in range(3):
                        for j in range(3):
                            if neighbor_board[i][j] != goal_board[i][j]:
                                distance += 1
                    neighbor_node.heuristic = distance

                elif heuristic == 3:
                   
                      
                    out_of_place_row = 0
                    out_of_place_col = 0
                    for i in range(3):
                        for j in range(3):
                            tile = neighbor_board[i][j]
                            if tile != goal_board[i][j]:  # Check if tile is out of place
                                out_of_place_row += 1
                                for k in range(3):
                                    if neighbor_board[k][j] == goal_board[i][j]:
                                        out_of_place_col += 1
                                        break
                    neighbor_node.heuristic = out_of_place_row + out_of_place_col


                    
                elif heuristic == 2:
                    neighbor_node.heuristic = calculate_manhattan_distance(neighbor_board, goal_dict)
                    #print(neighbor_node.heuristic)

                else:
                    print("No such heuristics")
                    
                heapq.heappush(open_set, neighbor_node)
                
                
    
    return current_node, nodes_expanded, max_nodes_in_memory, depth_of_solution


''''def print_solution(node):
    path = []
    while node:
        path.append(node.board)
        node = node.parent
    path.reverse()
    for depth, board in enumerate(path):
        print(f"Depth {depth}:")
        for row in board:
            print(" ".join(map(str, row)))
        print() '''


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("two arguments <heuristic> <cost_per_step>")
        sys.exit(1)
    
    heuristic = int(sys.argv[1])
    cost_per_step = int(sys.argv[2])
    
    initial_board = []
    print("Enter board configuration:")
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_board.append(row)
    
    current_node, nodes_expanded, max_nodes_in_memory, depth_of_solution = a_star_search(initial_board, heuristic, cost_per_step)
  
    if nodes_expanded > 0 and depth_of_solution > 0:
        effective_branching_factor = max_nodes_in_memory ** (1 / depth_of_solution)
        print(f'V={nodes_expanded}')
        print(f'N={max_nodes_in_memory}')
        print(f'd={depth_of_solution}')
        print(f'b={effective_branching_factor:.5f}')
        

        node = current_node
      
      
        board_configurations = []
        
        while node:
            board_configurations.append(node.board)
            node = node.parent
        
        # in reverse order
        
        for depth, board in enumerate(reversed(board_configurations)):
           
            for row in board:
                print(" ".join(map(str, row)))
            print()
        
    else:
        print("No solution found.")

