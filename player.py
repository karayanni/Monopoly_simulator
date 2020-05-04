import random

starting_cash = 1500


class Player:
    def __init__(self, starting_position):
        self.starting_position = starting_position
        self.place_on_board = 0
        self.cash = starting_cash

        def step(self):
            first_dice = random.randint(1, 6)
            second_dice = random.randint(1, 6)
