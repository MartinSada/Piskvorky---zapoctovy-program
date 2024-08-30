

class Board(object):
    def __init__(self, symbols_to_win = 5):
        # the symbols put on the board will be stored in a two level dictionary
        self.board = {}

        # how many symbols in line to win
        self.symbols_to_win = symbols_to_win

    def get_symbol(self, x, y):
        if x not in self.board or y not in self.board[x]:
            return None

        return self.board[x][y]

    def add_symbol(self, player, x, y):
        # if there is already a symbol at this xy position, return -1 (error)
        if self.get_symbol(x, y) is not None:
            return -1
        
        # ensure there is a second-level dictionary at this x index
        if x not in self.board:
            self.board[x] = {}
        
        # place the symbol
        self.board[x][y] = player

        # check if there are enough symbols in any straight or diagonal direction
        # from this player to win
        if self.check_win(player, x, y):
            return 1

        return 0

    def check_win(self, player, x, y):
        # check horizontal direction
        if self.check_direction(player, x, y, 1, 0) or self.check_direction(player, x, y, -1, 0):
            return True

        # check vertical direction
        if self.check_direction(player, x, y, 0, 1) or self.check_direction(player, x, y, 0, -1):
            return True

        # check diagonal directions
        if self.check_direction(player, x, y, 1, 1) or self.check_direction(player, x, y, -1, -1) or self.check_direction(player, x, y, 1, -1) or self.check_direction(player, x, y, -1, 1):
            return True

        return False

    def check_direction(self, player, x, y, dx, dy):
        count = 0
        current_x = x
        current_y = y

        # check in one direction
        for i in range(self.symbols_to_win):
            # if the position is out of bounds or the symbol is not the same as the player's symbol, stop checking
            if self.get_symbol(current_x, current_y) != player:
                break

            count += 1

            current_x += dx
            current_y += dy

        return count == self.symbols_to_win
