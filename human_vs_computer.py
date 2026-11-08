
import tkinter as tk

from puissance4_logic import (
    RED, YELLOW,
    create_board, is_valid_column, get_next_row,
    drop_piece, check_winner, is_draw
)

from gui import (
    create_game_interface,
    draw_board,
    board_to_text,
    write_log
)

from minimax import find_best_move


# Game configuration
HUMAN = RED
COMPUTER = YELLOW
SEARCH_DEPTH = 4

# Game variables
board = create_board()
moves = 0
game_over = False

ui = None
root = None
menu_callback = None


# Start a new game
def new_game():
    global board, moves, game_over

    board = create_board()
    moves = 0
    game_over = False

    ui["log"].delete("1.0", tk.END)

    draw_board(board, ui["cells"])

    ui["info_label"].config(text="Your turn (Red)")
    write_log(ui["log"], "New game started!\n")
    write_log(ui["log"], "You are Red. Computer is Yellow.\n\n")


# Check the result after a move
def check_game_result(player):

    global game_over

    if check_winner(board, player):
        game_over = True

        if player == HUMAN:
            ui["info_label"].config(text="You win!")
            write_log(ui["log"], "You win!\n")
        else:
            ui["info_label"].config(text="Computer wins!")
            write_log(ui["log"], "Computer wins!\n")

        return True

    if is_draw(board):
        game_over = True

        ui["info_label"].config(text="Draw!")
        write_log(ui["log"], "The game is a draw!\n")

        return True

    return False


# Handle the human move
def click_column(col):

    global moves

    if game_over:
        return

    # Check if the column is valid
    if not is_valid_column(board, col):
        ui["info_label"].config(text="This column is full!")
        return

    # Place the human piece
    row = get_next_row(board, col)
    drop_piece(board, row, col, HUMAN)

    moves += 1

    draw_board(board, ui["cells"])

    write_log(
        ui["log"],
        "Move " + str(moves) +
        " : You (Red), Column " + str(col + 1) + "\n"
    )

    write_log(ui["log"], board_to_text(board) + "\n")

    if check_game_result(HUMAN):
        return

    # Computer's turn
    ui["info_label"].config(text="Computer is thinking...")

    root.after(200, computer_turn)


# Handle the computer move
def computer_turn():

    global moves

    if game_over:
        return

    # Find the best column using Minimax
    col = find_best_move(
        board,
        COMPUTER,
        HUMAN,
        SEARCH_DEPTH
    )

    if col is None:
        return

    # Place the computer piece
    row = get_next_row(board, col)
    drop_piece(board, row, col, COMPUTER)

    moves += 1

    draw_board(board, ui["cells"])

    write_log(
        ui["log"],
        "Move " + str(moves) +
        " : Computer (Yellow), Column " + str(col + 1) + "\n"
    )

    write_log(ui["log"], board_to_text(board) + "\n")

    if check_game_result(COMPUTER):
        return

    ui["info_label"].config(text="Your turn (Red)")


# Start Human vs Computer mode
def start_human_vs_computer(window, return_to_menu):

    global root, ui, menu_callback

    root = window
    menu_callback = return_to_menu

    ui = create_game_interface(
        root,
        "Puissance 4 - Human vs Computer",
        click_column,
        new_game,
        menu_callback
    )

    new_game()
