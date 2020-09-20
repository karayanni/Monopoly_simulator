

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

        self.available_destinations = {1:('eilat',40),3:('eilat',60),6:('tiberias',100),8:('tiberias',100)\
        ,9:('tiberias',120),11:('ber-sheva',140),13:('ber-sheva',140),14:('ber-sheva',160),16:('natanya',180)\
        ,18:('natanya',180),19:('natanya',200),21:('ramat-gan',220),23:('ramat-gan',220),24:('ramat-gan',240)\
        ,26:('jerusalem',260),27:('jerusalem',260),29:('jerusalem',280),31:('haifa',300),32:('haifa',300)\
        ,24:('haifa',320),37:('tel-aviv',350),39 :('tel-aviv',400)}