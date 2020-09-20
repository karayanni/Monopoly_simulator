import player as p


class Board:
    def __init__(self, number_of_player: int):

        self.num_of_players = number_of_player
        self.destinations = [0] * 40
        self.visits = dict([(i,0) for i in range(40)])


    def visit(self,place_on_board):
        self.visits[place_on_board] = self.visits.get(place_on_board,0) + 1

    def __repr__(self):
        res = f"{self.visits[20]} {self.visits[21]} {self.visits[22]} {self.visits[23]} {self.visits[24]} {self.visits[25]} {self.visits[26]} {self.visits[27]} {self.visits[28]} {self.visits[29]} {self.visits[30]}\n"
        res +=  f"{self.visits[19]}                   {self.visits[31]}\n"
        res +=  f"{self.visits[18]}                   {self.visits[32]}\n"
        res +=  f"{self.visits[17]}                   {self.visits[33]}\n"
        res +=  f"{self.visits[16]}                   {self.visits[34]}\n"
        res +=  f"{self.visits[15]}                   {self.visits[35]}\n"
        res +=  f"{self.visits[14]}                   {self.visits[36]}\n"
        res +=  f"{self.visits[13]}                   {self.visits[37]}\n"
        res +=  f"{self.visits[12]}                   {self.visits[38]}\n"
        res +=  f"{self.visits[11]}                   {self.visits[39]}\n"
        res += f"{self.visits[10]} {self.visits[9]} {self.visits[8]} {self.visits[7]} {self.visits[6]} {self.visits[5]} {self.visits[4]} {self.visits[3]} {self.visits[2]} {self.visits[1]} {self.visits[0]}\n"
        return res

    
