import curses
import time


class BoardUi(object):
    def __init__(self, board, player_symbols, window: curses.window, start_x, start_y, width, height):
        # the game state
        self.board = board

        # setup for drawing
        self.player_smybols = player_symbols

        self.window = window
        self.screen_start_x = start_x
        self.screen_start_y = start_y
        self.screen_width = width
        self.screen_height = height

        # coordinated relative to the origin, which will be drawn at the center of the screen
        self.camera_x = 0
        self.camera_y = 0

    def move_camera(self, dx, dy):
        self.camera_x += dx
        self.camera_y += dy

    def draw(self):
        # calculate the board coordinates of the top left corner of the screen
        board_start_x = self.camera_x - (self.screen_width // 2)
        board_start_y = self.camera_y + (self.screen_height // 2)

        # draw the board
        for y in range(self.screen_height):
            for x in range(self.screen_width):
                screen_x = self.screen_start_x + x
                screen_y = self.screen_start_y + y

                board_x = board_start_x + x
                board_y = board_start_y - y
                
                # get the symbol at the board coordinates
                player_number = self.board.get_symbol(board_x, board_y)

                symbol = self.player_smybols[player_number] if player_number is not None else " "

                # draw the symbol
                self.window.addstr(screen_y, screen_x, symbol)
            
    def pick_board_coordinates(self):
        last_cursor_change_timestamp = round(time.time() * 1000)
        cursor_visible = True
                
        self.window.nodelay(True)

        while True:
            # draw the board
            self.draw()

            # draw the cursor, middle of the sceen maps to camera position
            if cursor_visible:
                cursor_x = self.screen_start_x + (self.screen_width // 2)
                cursor_y = self.screen_start_y + (self.screen_height // 2)

                self.window.addstr(cursor_y, cursor_x, "█")

            key = self.window.getch()
            
            # confirm the selection (enter = ASCII 10 apparently)
            if key == 10:
                return self.camera_x, self.camera_y

            # or move the camera
            if key == curses.KEY_UP:
                self.move_camera(0, 1)
            elif key == curses.KEY_DOWN:
                self.move_camera(0, -1)
            elif key == curses.KEY_LEFT:
                self.move_camera(-1, 0)
            elif key == curses.KEY_RIGHT:
                self.move_camera(1, 0)

            # sleep for 50ms
            time.sleep(0.05)
            
            # toggle cursor visibility if more than 500ms since last change passed
            current_timestamp = round(time.time() * 1000)

            if current_timestamp - last_cursor_change_timestamp > 500:
                cursor_visible = not cursor_visible
                last_cursor_change_timestamp = current_timestamp









