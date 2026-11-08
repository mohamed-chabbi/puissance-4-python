
import tkinter as tk
from puissance4_logic import ROWS, COLS, RED, YELLOW


def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()


def create_main_menu(root, on_human_vs_human, on_human_vs_computer):
    clear_window(root)

    root.title("Puissance 4")
    
    title = tk.Label(
        root,
        text="PUISSANCE 4",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=25)

    tk.Button(
        root,
        text="Human vs Human",
        width=25,
        font=("Arial", 13),
        command=on_human_vs_human
    ).pack(pady=10)

    tk.Button(
        root,
        text="Human vs Computer",
        width=25,
        font=("Arial", 13),
        command=on_human_vs_computer
    ).pack(pady=10)


def create_game_interface(
    root,
    title,
    on_column_click,
    on_new_game,
    on_menu
):
    clear_window(root)
    root.title(title)

    left = tk.Frame(root)
    left.grid(row=0, column=0, padx=10, pady=10)

    right = tk.Frame(root)
    right.grid(row=0, column=1, padx=10, pady=10)

    column_frame = tk.Frame(left)
    column_frame.pack()

    for c in range(COLS):
        button = tk.Button(
            column_frame,
            text=str(c + 1),
            font=("Arial", 14),
            width=4,
            command=lambda c=c: on_column_click(c)
        )
        button.grid(row=0, column=c, padx=2, pady=2)

    board_frame = tk.Frame(left, bg="blue")
    board_frame.pack(pady=5)

    cells = []

    for r in range(ROWS):
        line = []

        for c in range(COLS):
            cell = tk.Label(
                board_frame,
                text="●",
                font=("Arial", 28),
                width=3,
                height=1,
                bg="blue",
                fg="white"
            )
            cell.grid(row=r, column=c, padx=2, pady=2)
            line.append(cell)

        cells.append(line)

    info_label = tk.Label(
        left,
        text="",
        font=("Arial", 12)
    )
    info_label.pack(pady=8)

 
    tk.Button(
        left,
        text="New Game",
        width=20,
        command=on_new_game
    ).pack(pady=5)

    tk.Button(
        left,
        text="Main Menu",
        width=20,
        command=on_menu
    ).pack(pady=5)

    scroll = tk.Scrollbar(right)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    log = tk.Text(
        right,
        width=42,
        height=28,
        font=("Courier", 10),
        yscrollcommand=scroll.set
    )
    log.pack(side=tk.LEFT)

    scroll.config(command=log.yview)

    return {
        "cells": cells,
        "info_label": info_label,
        "log": log
    }


def draw_board(board, cells):
    for r in range(ROWS):
        for c in range(COLS):

            if board[r][c] == RED:
                cells[r][c].config(fg="red")

            elif board[r][c] == YELLOW:
                cells[r][c].config(fg="yellow")

            else:
                cells[r][c].config(fg="white")


def board_to_text(board):
    text = ""

    for r in range(ROWS):
        line = ""

        for c in range(COLS):
            if board[r][c] == RED:
                line += "R "
            elif board[r][c] == YELLOW:
                line += "Y "
            else:
                line += ". "

        text += line + "\n"

    return text


def write_log(log, text):
    log.insert(tk.END, text)
    log.see(tk.END)
