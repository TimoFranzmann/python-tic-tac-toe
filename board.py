class Board:
    def __init__(self):
        # initialisation of empty 'new' board
        self.board = {
            1: "_", 2: "_", 3: "_",
            4: "_", 5: "_", 6: "_",
            7: "_", 8: "_", 9: "_",
        }

    def print_board(self):
        board_as_string = ""
        for index in self.board:
            if index % 3 == 0:
                board_as_string += self.board[index] + '\n'
            else:
                board_as_string += self.board[index] + "|"
        print(board_as_string)


    def get_allowed_field_indexes(self):
        allowed_indexes = []
        for k, v in self.board.items():
            if v == "_":
                allowed_indexes.append(k)

        return allowed_indexes
        # print(allowed_indexes)


    def set_symbol(self, index, symbol):
        self.board[index] = symbol
