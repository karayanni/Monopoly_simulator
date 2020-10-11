from api.SimulationLogic.Player import Player
from api.SimulationLogic.Board import Board

import uuid

class GameHandler():
    def __init__(self, num_of_players: int, starting_cash: int):
        '''
        this class is responsible for handling a game, saving its current state and updating it using the classes functions
        '''
        self.Players = [Player(starting_cash) for i in range(num_of_players)]
        self.Board = Board()
        self.id = str(uuid.uuid4())
