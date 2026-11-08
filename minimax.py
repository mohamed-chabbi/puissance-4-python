
from puissance4_logic import (
    ROWS, COLS, EMPTY,
    is_valid_column, get_next_row,
    drop_piece, check_winner, is_draw
)

from heuristics import evaluate_board


WIN_SCORE = 100000

COLUMN_ORDER = [3, 2, 4, 1, 5, 0, 6]


def get_valid_columns(board):

    valid_columns = []

    for col in COLUMN_ORDER:
        if is_valid_column(board, col):
            valid_columns.append(col)

    return valid_columns


def minimax(board, depth, maximizing_player, computer, human):

    if check_winner(board, computer):
        return None, WIN_SCORE + depth

    if check_winner(board, human):
        return None, -WIN_SCORE - depth

    if is_draw(board):
        return None, 0

    if depth == 0:
        return None, evaluate_board(board, computer, human)

    valid_columns = get_valid_columns(board)

    if maximizing_player:

        best_score = float("-inf")
        best_column = valid_columns[0]

        for col in valid_columns:

            new_board = [row[:] for row in board]

            row = get_next_row(new_board, col)
            drop_piece(new_board, row, col, computer)

            column, score = minimax(
                new_board,
                depth - 1,
                False,
                computer,
                human
            )

            if score > best_score:
                best_score = score
                best_column = col

        return best_column, best_score

    else:

        best_score = float("inf")
        best_column = valid_columns[0]

        for col in valid_columns:

            new_board = [row[:] for row in board]

            row = get_next_row(new_board, col)
            drop_piece(new_board, row, col, human)

            column, score = minimax(
                new_board,
                depth - 1,
                True,
                computer,
                human
            )

            if score < best_score:
                best_score = score
                best_column = col

        return best_column, best_score


def find_best_move(board, computer, human, depth):

    column, score = minimax(
        board,
        depth,
        True,
        computer,
        human
    )

    return column
