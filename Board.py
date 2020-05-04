import player


class Board:
    def __init__(self, number_of_player: int):

        self.num_of_players = number_of_player
        self.destinations = [0] * 40

