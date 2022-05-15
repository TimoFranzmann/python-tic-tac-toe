class Player:
    _winning_combinations = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]

    def __init__(self, symbol):
        self.player = symbol
        self.turns_made = []


    def check_for_win(self):
        if len(self.turns_made) < 2:
            return False

        for combi in self._winning_combinations:
            if all(item in self.turns_made for item in combi):
                return True

        return False

    def add_move(self, move):
        self.turns_made.append(move)