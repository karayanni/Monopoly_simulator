from api.SimulationLogic import player as p
import random

class Special_Cards:

    def __init__(self,player : p.Player):
        self.player = player
        self.lucky_box_cards = []
        self.surprise_cards = []

    def get_surprise_card(self):
        rand_card_index = random.randint(0,19)
        return self.surprise_cards[rand_card_index]
