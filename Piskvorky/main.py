import curses
import json

from curses import wrapper, textpad

from board import Board
from board_ui import BoardUi


def draw_row_centered_text(window, row, text):
    rows, cols = window.getmaxyx()
    
    text_center_x = cols // 2
    text_len = len(text)

    x = text_center_x - (text_len // 2)
    
    left_pad = x
    right_pad = cols - (x + text_len)

    final_text = (" " * left_pad) + text + (" " * right_pad)

    window.addstr(0, 0, final_text)
    window.refresh()


def main(stdscr):
    curses.curs_set(False)
    
    # Clear screen
    stdscr.clear()
    
    symbols = [player["symbol"] for player in config["players"]]

    rows, cols = stdscr.getmaxyx()

    # make a sub-window to draw a border around the game board, leave first line to info texts
    board_window = stdscr.subwin(rows - 1, cols, 1, 0)
    board_window.box()

    # draw the board inside the border
    board_ui = BoardUi(board, symbols, board_window, 1, 1, cols - 2, rows - 3)

    while True:
        player_number = 0

        # let all palyers play their turn
        for player in config["players"]:
            move_result = None

            # draw the information text
            draw_row_centered_text(stdscr, 0, f"Player {player["name"]}'s turn!")

            # let the player pick a move
            if player["type"] == "human":
                move_result = human_player_move(player_number, board_ui)
            elif player["type"] == "ai":
                move_result = ai_player_move(player_number)
            else:
                raise "Unknown player type"

            # evaluate the move result
            if move_result == 1:
                # redraw the board and display the winner
                board_ui.draw()
                board_window.refresh()

                draw_row_centered_text(stdscr, 0, f"Player {player["name"]} won!")

                # wait for a key press
                stdscr.nodelay(False)
                stdscr.getch()
                
                return

            player_number += 1

def human_player_move(player_number, board_ui):
    while True:
        # human player only picks a coordinate form the board
        x, y = board_ui.pick_board_coordinates()

        # try to place a symbol at the picked coordinate
        result = board.add_symbol(player_number, x, y)

        # if the symbol was placed successfully, return the result
        if result != -1:
            return result



def ai_player_move(player_number):
    raise "Not implemented"


# load config
with open("config.json", encoding="utf-8") as file:
    config = json.load(file)

# define game state
board = Board(config["symbols_to_win"])

# run the game
wrapper(main)