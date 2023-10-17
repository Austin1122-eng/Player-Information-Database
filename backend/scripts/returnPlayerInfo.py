import json
from scripts.player import Player
from scripts.databaseAction import querySQL
from scripts.organizedPlayerData import organizedPlayerInfo

retriver = querySQL()
organized_Player = organizedPlayerInfo()
################################
# CONVERTS ANY OBJECT TYPE SUCH AS GAMES INTO A DICTIONARY
#################################
def convert_to_dict(obj):
    return obj.__dict__


################################
# CLASS MADE TO RETURNS THE NEEDED INFORMATION OF THE PLAYER
#################################
class retrievePlayer:
    
    def returnValuesInPlayerId(self, playerId):
        players_information = retriver.retrieve_From_Py(playerId)

        shot_information = retriver.retrieve_Shot_From_Py(playerId)
        
        for player_dict in players_information:
            for shot_dict in shot_information:
                if(player_dict['gameid'] == shot_dict['gameid'] and player_dict['playerid'] == shot_dict['playerid']):
                    organized_Player.populateName(player_dict['playername'])
                    game_information = retriver.retrieve_Game_From_Py(player_dict['gameid'])
                    organized_Player.populateGame(player_dict, shot_information, game_information)
                    break
            
           
        y = json.dumps(organized_Player.getGames())


        return y


    def returnNameInPlayerId(self, playerId):

        players_information = retriver.retrieve_From_Py(playerId)

        for player_dict in players_information:
            organized_Player.populateName(player_dict['playername'])
 
        x = organized_Player.getNames()


        return x

     



