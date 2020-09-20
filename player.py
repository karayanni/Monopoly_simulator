import random

starting_cash = 1500


class Player:
    def __init__(self, starting_position):
        self.starting_position = starting_position
        self.place_on_board = 0
        self.cash = starting_cash
        self.in_jail = False

    def steps(self,waiting_turn):
        
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        
        if self.in_jail:
            if first_dice == second_dice or waiting_turn == 3:
                self.in_jail = False
                first_dice = random.randint(1, 6)
                second_dice = random.randint(1, 6)

            

        self.place_on_board += first_dice + second_dice
        self.place_on_board %= 40

    def go_to_jail(self):
        self.in_jail = True

    def get_out_of_jail(self):
        if self.cash > 50:
            self.cash -= 50
            self.in_jail = False
        else:
            print("dont have enough money to get out of jail")
