
from puissance4_logic import ROWS, COLS, EMPTY


# Evaluate a group of four cells
def evaluate_window(window, computer, human):

    computer_count = window.count(computer)
    human_count = window.count(human)
    empty_count = window.count(EMPTY)

    # Mixed window
    if computer_count > 0 and human_count > 0:
        return 0

    # Computer
    if computer_count == 3 and empty_count == 1:
        return 5

    elif computer_count == 2 and empty_count == 2:
        return 2

    # Human
    if human_count == 3 and empty_count == 1:
        return -5

    elif human_count == 2 and empty_count == 2:
        return -2

    return 0


# Evaluate the complete board using Heuristic B
def evaluate_board(board, computer, human):

    score = 0

    # Center column bonus
    center_col = COLS // 2

    for r in range(ROWS):
        if board[r][center_col] == computer:
            score += 3

        elif board[r][center_col] == human:
            score -= 3

    # Horizontal windows
    for r in range(ROWS):
        for c in range(COLS - 3):

            window = [
                board[r][c],
                board[r][c + 1],
                board[r][c + 2],
                board[r][c + 3]
            ]

            score += evaluate_window(window, computer, human)

    # Vertical windows
    for r in range(ROWS - 3):
        for c in range(COLS):

            window = [
                board[r][c],
                board[r + 1][c],
                board[r + 2][c],
                board[r + 3][c]
            ]

            score += evaluate_window(window, computer, human)

    # Positive diagonal windows
    for r in range(ROWS - 3):
        for c in range(COLS - 3):

            window = [
                board[r][c],
                board[r + 1][c + 1],
                board[r + 2][c + 2],
                board[r + 3][c + 3]
            ]

            score += evaluate_window(window, computer, human)

    # Negative diagonal windows
    for r in range(3, ROWS):
        for c in range(COLS - 3):

            window = [
                board[r][c],
                board[r - 1][c + 1],
                board[r - 2][c + 2],
                board[r - 3][c + 3]
            ]

            score += evaluate_window(window, computer, human)

    return score
