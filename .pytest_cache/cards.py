import player

class Cards:
    def __init__(self,serial_number,card_type,player : player):
        self.serial_number = serial_number
        self.card_type = card_type = ['surprise_card','lucky_box_card']
        self.player = player

        def go_to_jail(self,player):
            self.player.go_to_jail()

        def pay_2_mil(self,player):
            self.player.cash -= 200

        def recieve_2_mil(self,player):
            self.player.cash += 200