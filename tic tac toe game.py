"""
Tic Tac Toe (איקס עיגול)

Author: Elior Ben Naftali

Description:
This program implements a Tic-Tac-Toe game using the console.
Two players can play against each other or against the computer.
Players choose their names and symbols and take turns placing
their symbol on the board until someone wins or the board is full.
"""

import random

WINNING_COMBINATIONS = [
    (0, 1, 2),  # rows
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),  # columns
    (1, 4, 7),
    (2, 5, 8),  # diagonals
    (0, 4, 8),
    (2, 4, 6),
]


def display_title():
    print("\n=========================================")
    print(" WELCOME TO TIC TAC TOE! ")
    print("=========================================\n")


def display_positions():
    print("\nboard positions:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print("\n")


def display_board(board):
    print()
    for row in range(3):
        start = row * 3
        print(f" {board[start]} | {board[start + 1]} | {board[start + 2]}")
        if row < 2:
            print("---|---|---")
    print()


def create_board():
    return [" "] * 9


def choose_game_mode():
    while True:
        print("Choose a game mode:")
        print("1. Player vs Player")
        print("2. Player vs Computer")

        choice = input("enter 1 or 2: ")
        if choice == "1":
            return "pvp"
        elif choice == "2":
            return "pvc"
        else:
            print("Invalid choice. Please enter 1 or 2")


def get_player_name(player_number):
    while True:
        name = input(f"Enter name of player {player_number}: ").strip()
        if name:
            return name
        print("name cannot be empty. Please try again, enter a valid name")


def choose_symbol(player_name, unavailable_symbol=None):
    while True:
        if unavailable_symbol is None:
            choice = input(
                f"{player_name}, choose your symbol (X/O) or press Enter for random:"
            ).strip().upper()

            if choice == "":
                symbol = random.choice(["X", "O"])
                print(f"{player_name} was randomly assigned : {symbol}\n")
                return symbol

            if choice in ["X", "O"]:
                return choice

            print("Invalid symbol. please choose X or O.\n")

        else:
            choice = input(
                f"{player_name}, choose your symbol (X/O) or press Enter for random:"
            ).strip().upper()

            if choice == "":
                symbol = "O" if unavailable_symbol == "X" else "X"
                print(f"{player_name} was assigned : {symbol}\n")
                return symbol

            if choice in ["X", "O"] and choice != unavailable_symbol:
                return choice

            print(f"Invalid choice. {unavailable_symbol} is already taken\n")


def setup_players():
    mode = choose_game_mode()
    player1_name = get_player_name(1)
    player1_symbol = choose_symbol(player1_name)

    if mode == "pvp":
        player2_name = get_player_name(2)
        player2_symbol = choose_symbol(player2_name, player1_symbol)
        is_computer = False
    else:
        player2_name = "Computer"
        player2_symbol = "O" if player1_symbol == "X" else "X"
        is_computer = True

    player1 = {
        "name": player1_name,
        "symbol": player1_symbol,
        "is_computer": False
    }
    player2 = {
        "name": player2_name,
        "symbol": player2_symbol,
        "is_computer": is_computer
    }

    return player1, player2


def get_available_moves(board):
    return [index for index, cell in enumerate(board) if cell == " "]



def get_human_move(board, player_name):
    while True:
        try:
            move = int(input(f"{player_name} enter your move (1-9): ").strip()) - 1

            if move < 0 or move > 8:
                print("Invalid position. Please choose a number from 1 to 9.\n")
            elif board[move] != " ":
                print("That place is already taken. Please choose another place.\n")
            else:
                return move

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.\n")


def get_computer_move(board):
    available_moves = get_available_moves(board)
    return random.choice(available_moves)


def make_move(board, move, symbol):
    board[move] = symbol


def check_winner(board, symbol):
    for combo in WINNING_COMBINATIONS:
        if all(board[index] == symbol for index in combo):
            return True
    return False


def is_tie(board):
    return " " not in board


def switch_turn(current_index):
    return 1 - current_index


def play_single_game():
    board = create_board()
    player1, player2 = setup_players()
    players = [player1, player2]

    print("\nPlayers:")
    print(f"{player1['name']} | {player1['symbol']}")
    print(f"{player2['name']} | {player2['symbol']}")

    current_player_index = 0

    while True:
        current_player = players[current_player_index]
        display_board(board)

        if current_player["is_computer"]:
            print("Computer is choosing a move...")
            move = get_computer_move(board)
            print(f"Computer chose a position {move + 1}\n")
        else:
            move = get_human_move(board, current_player["name"])

        make_move(board, move, current_player["symbol"])

        if check_winner(board, current_player["symbol"]):
            display_board(board)
            print(f"{current_player['name']} wins!\n")
            break

        if is_tie(board):
            display_board(board)
            print("The game ended in a tie.\n")
            break

        current_player_index = switch_turn(current_player_index)


def ask_player_to_play_again():
    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter yes or no.\n")


def main():
    display_title()
    display_positions()
    while True:
        try:
            play_single_game()

            if not ask_player_to_play_again():
                print("\nThank you for playing!\n")
                break

        except Exception as error:
            print(f"\nUnexpected error: {error}")
            print("The game will restart safely now...\n")


if __name__ == "__main__":
    main()