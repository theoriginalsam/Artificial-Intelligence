#!/usr/bin/env python

import random
import sys


BOARD_SIZE = 3
GOAL_STATE = [[0, 1, 2], [3, 4, 5], [6, 7, 8]] 


def randomize_board(board, moves):
    for _ in range(moves):
        legal_moves = []
        blank_row, blank_col = None, None

     
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == 0:
                    blank_row, blank_col = row, col

     
        if blank_row > 0:
            legal_moves.append((-1, 0))  # Move up
        if blank_row < BOARD_SIZE - 1:
            legal_moves.append((1, 0))   # Move down
        if blank_col > 0:
            legal_moves.append((0, -1))  # Move left
        if blank_col < BOARD_SIZE - 1:
            legal_moves.append((0, 1))   # Move right

      
        move = random.choice(legal_moves)
        new_row, new_col = blank_row + move[0], blank_col + move[1]
        board[blank_row][blank_col], board[new_row][new_col] = board[new_row][new_col], board[blank_row][blank_col]


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
 
    initial_state = []
    for _ in range(BOARD_SIZE):
        row = list(map(int, input().split()))
        initial_state.append(row)

   
    if len(sys.argv) != 3:
        print("Usage: python random_board.py <seed> <num_moves>")
        sys.exit(1)

    seed = int(sys.argv[1])
    num_moves = int(sys.argv[2])

   
    random.seed(seed)
    random_board = [row[:] for row in initial_state]

   
    randomize_board(random_board, num_moves)

   

    print_board(random_board)
