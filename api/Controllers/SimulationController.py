#region imports

import flask
import json
from api.SimulationLogic.GameHandler import GameHandler

#endregion

app = flask.Flask(__name__)

#region entries

@app.route('/api/new-simulation', methods=['POST'])
def NewSimulation():
    new_game = CreateNewGame()
    SaveGame(new_game)
    return new_game.id


#endregion

#region utils

# in the future we should save to a database instead of local memory
gamesDict = dict()


def CreateNewGame():
    '''
    reads params from request body and creates a new game.
    '''
    json_param = flask.request.get_json(force=True)
    num_of_players=json_param['num_of_players']
    starting_cash= json_param['starting_cash']
    return GameHandler(num_of_players, starting_cash)


def SaveGame(new_game: GameHandler):
    '''
    receives a newly defined game and saves it to the database for future usage of the game
    '''
    if(gamesDict.__contains__(new_game.id)):
        raise Exception("game id already in use, make sure to send a new game")
    gamesDict[new_game.id] = new_game


#endregion

app.run(port=1000)