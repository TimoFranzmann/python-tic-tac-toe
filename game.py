import player
import board
import random


class Game:

    def __init__(self):
        self.winner = None
        self.human_player = player.Player('X')
        self.computer_player = player.Player('O')
        self.board = board.Board()


    def start_game(self):
        self.print_board()
        print('Du beginnst und hast Symbol ' + self.get_human_player())
        while self.winner is None:

            self.ask_player_for_turn()
            if self.player_won(self.human_player):
                self.set_winner(" --> You 👌🏼🤓")
                break

            self.make_computer_turn()
            if self.player_won(self.computer_player):
                self.set_winner(" --> Computer")
                break

    # methods for human player
    def ask_player_for_turn(self):
        allowed_fields = self.board.get_allowed_field_indexes()
        is_input_valid = False

        while not is_input_valid:
            input_index = self.request_input(allowed_fields)
            is_input_valid = self.is_input_valid(input_index, allowed_fields)
            if not is_input_valid:
                print("Eingabe war leider nicht korrekt, bitte nur ganze (erlaubte) Zahlen")

        self.board.set_symbol(int(input_index), "X")
        self.human_player.add_move(int(input_index))
        self.print_board()

    @staticmethod
    def request_input(allowed_fields):
        return input('Wo möchtest du platzieren? Erlaubt sind folgende Plätze: '
                     + str(allowed_fields))

    @staticmethod
    def is_input_valid(input_index, allowed_fields):
        try:
            if int(input_index) in allowed_fields:
                return True
            else:
                return False
        except:
            return False

    #methods for computer player
    def make_computer_turn(self):
        field_to_move = self.computer_pick_next_turn()
        self.board.set_symbol(int(field_to_move), "O")
        self.computer_player.add_move(int(field_to_move))
        self.print_board()

    def computer_pick_next_turn(self):
        allowed_fields = self.board.get_allowed_field_indexes()
        return self.get_best_option_for_computer(allowed_fields)

    def get_best_option_for_computer(self, allowed_fields):
        return random.choice(allowed_fields)
        # noch intelligentere logik einbauen
        # for index in allowed_fields:
        #     return allowed_fields[index]

    #helper methods
    def print_board(self):
        self.board.print_board()

    @staticmethod
    def player_won(player_to_check):
        return player_to_check.check_for_win()

    def set_winner(self, winner):
        self.winner = winner
        print("🎉WINNER🎉: " + self.winner)

    def get_human_player(self):
        return self.human_player.player