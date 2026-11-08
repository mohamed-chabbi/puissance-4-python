
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


# Game variables
board = create_board()
player = RED
moves = 0
game_over = False

ui = None
root = None
menu_callback = None


def new_game():
    global board, player, moves, game_over

    board = create_board()
    player = RED
    moves = 0
    game_over = False

    ui["log"].delete("1.0", tk.END)

    draw_board(board, ui["cells"])

    ui["info_label"].config(text="Player 1 (Red) turn")
    write_log(ui["log"], "New game started!\n\n")



def click_column(col):
    global player, moves, game_over

    if game_over:
        return

    if not is_valid_column(board, col):
        ui["info_label"].config(text="This column is full!")
        return

    row = get_next_row(board, col)
    drop_piece(board, row, col, player)

    moves += 1


    draw_board(board, ui["cells"])

    if player == RED:
        write_log(
            ui["log"],
            "Move " + str(moves) +
            " : Player 1 (Red), Column " + str(col + 1) + "\n"
        )
    else:
        write_log(
            ui["log"],
            "Move " + str(moves) +
            " : Player 2 (Yellow), Column " + str(col + 1) + "\n"
        )

    write_log(ui["log"], board_to_text(board) + "\n")

    if check_winner(board, player):
        game_over = True

        if player == RED:
            ui["info_label"].config(text="Player 1 (Red) wins!")
            write_log(ui["log"], "Player 1 (Red) wins!\n")
        else:
            ui["info_label"].config(text="Player 2 (Yellow) wins!")
            write_log(ui["log"], "Player 2 (Yellow) wins!\n")

        return

    if is_draw(board):
        game_over = True
        ui["info_label"].config(text="Draw!")
        write_log(ui["log"], "The game is a draw!\n")
        return

    if player == RED:
        player = YELLOW
        ui["info_label"].config(text="Player 2 (Yellow) turn")
    else:
        player = RED
        ui["info_label"].config(text="Player 1 (Red) turn")


def start_human_vs_human(window, return_to_menu):
    global root, ui, menu_callback

    root = window
    menu_callback = return_to_menu

    ui = create_game_interface(
        root,
        "Puissance 4 - Human vs Human",
        click_column,
        new_game,
        menu_callback
    )

    new_game()
