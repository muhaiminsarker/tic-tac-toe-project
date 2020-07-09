import random
board = [
    ["", "", ""], 
    ["", "", ""], 
    ["", "", ""]
    ]
#player1 = input("What is Player 1's Name? ")
#player2 = input("What is Player 2's Name? ")
count = 1
#winner = 0

def place_piece(piece, row, col):
    board[row-1][col-1] = piece
    print(board)

def has_won_vertical():
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("Player1 won")
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("Player1 won")
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("Player1 won")
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("Player2 won")
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("Player2 won")
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("Player2 won")

def tic_tac_toe():
    turn = random.random()
    if turn > 0.5:
        print("It's Player 2's turn.")
        turn = 2 
    elif turn < 0.5:
        print("It's Player 1's turn.")
        turn = 1
##    while (!has_won_vertical() or !has_won_diagonal() or !has_won_horizontal()):
while True:
    if count % 2 == 1:
        choice = input("Where do you want to put down X? Format: X, row, col")
        placements = choice.split(",")
        place_piece(placements[0], int(placements[1]), int(placements[2]))
    else:
        choice = input("Where do you want to put down O? Format: O, row, col")
        placements = choice.split(",")
        place_piece(placements[0], int(placements[1]), int(placements[2]))
    #count+=1

    has_won_vertical()

tic_tac_toe()

#def has_won_horizontal():
#def has_won_diagonal():



