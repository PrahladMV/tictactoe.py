""" This is a of a unique Tic-Tac-Toe game in Python that I made.
The uniqueness comes from customizing the symbols used for each
player (X and O) and allowing the user to choose their symbols. """

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_player_symbol():
    return input("Enter your symbol (single character): ").upper()

def main():
    print("Welcome to Unique Tic-Tac-Toe!")
    
    player1_symbol = get_player_symbol()
    player2_symbol = get_player_symbol()
    
    while player1_symbol == player2_symbol:
        print("Please choose a unique symbol for player 2.")
        player2_symbol = get_player_symbol()

    players = {1: player1_symbol, 2: player2_symbol}
    current_player = 1

    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = players[current_player]

            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = 3 - current_player  # Switch player (1 -> 2, 2 -> 1)
            
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    main()
