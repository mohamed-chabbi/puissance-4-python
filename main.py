
import tkinter as tk

from gui import create_main_menu

from human_vs_human import start_human_vs_human
from human_vs_computer import start_human_vs_computer

root = tk.Tk()
root.title("Puissance 4")


def launch_human_vs_human():
    start_human_vs_human(root, show_main_menu)


def launch_human_vs_computer():
    start_human_vs_computer(root, show_main_menu)


def show_main_menu():
    create_main_menu(
        root,
        launch_human_vs_human,
        launch_human_vs_computer
    )

show_main_menu()
root.mainloop()
