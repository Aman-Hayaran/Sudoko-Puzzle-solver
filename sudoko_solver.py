"""
BACTRACKING : SUDOKO SOLVER
pick empty cell
try all numerbers from 1 to 9
Find one no that fits
repeat it for next empty cell
if the options for numbers exhausted then backtrack to previous cell and change the
number putted in
"""
import pygame


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
def sudoko_solver(board):
    empty_cell_pos = find_empty(board)
    if not empty_cell_pos :
        return True
    else:
        row_no,col_no = empty_cell_pos
        for i in range(1,10):
            if valid(board,i,(row_no,col_no)):
                board[row_no][col_no] = i
                if sudoko_solver(board):
                    return True
                board[row_no][col_no] = 0
    return False

def valid(bo, num, pos):
    for i in range(len(bo[0])):
        # row check

        if bo[pos[0]][i] == num and pos[1] != i :
            return False
    for i in range(len(bo)):
        # column check
        if bo[i][pos[1]] == num and pos[0] != i :
            return False
        # box check
    x_cor_box = pos[1]//3
    y_cor_box = pos[0]//3
    for i in range(y_cor_box*3,y_cor_box*3+3):
        for j in range(x_cor_box*3 , x_cor_box*3+3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i %3 == 0 and i != 0 :
            print("---------------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j !=0 :
                print("|",end=" ")
            if j == 8 :
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ",end = "")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]== 0:
                return (i,j)

    return None
print_board(board)
sudoko_solver(board)
print("                    ")
print_board(board)


