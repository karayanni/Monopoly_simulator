import player


class Board:
    def __init__(self, number_of_player: int):

        self.num_of_players = number_of_player
        self.destinations = [0] * 40
        self.visits = dict([(i,0) for i in range(40)])


    def visit(self,place_on_board):
        self.visits[place_on_board] = self.visits.get(place_on_board,0) + 1

