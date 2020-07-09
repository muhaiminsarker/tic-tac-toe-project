import random
board = [
    ["", "", ""], 
    ["", "", ""], 
    ["", "", ""]
    ]
def place_piece(piece, row, col):
    board[row-1][col-1] = piece
    print(board)
def has_won_vertical():
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("Player1 won")
        return True
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("Player1 won")
        return True
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("Player1 won")
        return True
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("Player2 won")
        return True
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("Player2 won")
        return True
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("Player2 won")
        return True
    else:
        return False
def has_won_horizontal():
    for i in range(len(board)):
        if board[i].count("X") == 3:               
            print("Player1 won")
            return True
        elif board[i].count("O") == 3:
            print("Player2 won")
            return True
    return False
def tic_tac_toe():
    count = 1
    while (has_won_vertical()==False or has_won_horizontal()==False):
        if count % 2 == 1:
            choice = input("Where do you want to put down X? Format: X, row, col")
            placements = choice.split(",")
            place_piece(placements[0], int(placements[1]), int(placements[2]))
        else:
            choice = input("Where do you want to put down O? Format: O, row, col")
            placements = choice.split(",")
            place_piece(placements[0], int(placements[1]), int(placements[2]))
        count+=1
tic_tac_toe()