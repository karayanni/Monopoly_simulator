

class destinations:
    '''
        each destination on the board is defined by a number 0-39
        special destinations such as surprises and lucky boxes are saved in lists accordingly 
    '''
    def __init__(self, number_of_player: int):
        self.surprises_cards = [7 ,22 ,36]
        self.luck_box_cards = [2 , 17 ,33]
        self.taxes = dict([(4,200),(38,100)])
        self.trains = [5,15,25,35]
        self.water_electric_company = [12,28]
        self.do_nothing = [10,20]
        self.go_to_jail = [30]
        self.starting_point = [0]