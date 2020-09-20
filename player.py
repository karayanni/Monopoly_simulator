import random

starting_cash = 1500


class Player:
    def __init__(self):
        self.place_on_board = 0
        self.cash = starting_cash
        self.in_jail = False
        self.destinations = []
        self.waiting = 0

    def steps(self,waiting_turn):
        
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        
        if self.in_jail:
            self.waiting += 1 
            if self.waiting_turn == 4:
                self.in_jail = False
                self.waiting = 0
            elif first_dice == second_dice :
                self.in_jail = False
                self.waiting = 0
                first_dice = random.randint(1, 6)
                second_dice = random.randint(1, 6)

        self.place_on_board += first_dice + second_dice
        self.place_on_board %= 40

    def go_to_jail(self):
        self.in_jail = True
        self.waiting += 1

    def get_out_of_jail(self):
        if self.cash >= 50:
            self.cash -= 50
            self.in_jail = False
            self.waiting = 0
        else:
            print("dont have enough money to get out of jail")

    def buy(self,dest,price):
        if self.cash < price:
            print("not enough money")
        else:
            self.destinations.append(dest)
            self.cash -= price

    def pay(self,amount):
        self.cash -= amount

    def payed(self,amount):
        self.cash += amount

