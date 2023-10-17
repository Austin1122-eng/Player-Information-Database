import json
from player import Player
from player import Shot
class Team:
    def __init__(self, team_id, name):
        self.id = team_id
        self.name = name
        self.players = []

    def addPlayer(self, playertest):
        #print(f"CASE 0000 - {playertest.name}")
        self.players.append(playertest)
        # for i in self.players:
        #      print(f"CASE 0001 - {i.id}")
        

    def getPlayerList(self):
        return self.players
    
    def populate_player(self, players_data_list, team_json, players_json):
        #teamPlayers = []
        for player_data_game in players_data_list:
            player_id = player_data_game['id']
            # print(f"CASE 0001 before: {player_id}")
            for key in players_json:               
                if key['id'] == player_id:
                    player_instance = Player(player_id, key['name'])
                    # Player.id = player_id
                    # Player.name = key['name']
                    player_instance.is_Starter = player_data_game['isStarter']
                    player_instance.minutes = player_data_game['minutes']
                    player_instance.points = player_data_game['points']
                    player_instance.assists = player_data_game['assists']
                    player_instance.offensiveRebounds = player_data_game['offensiveRebounds']
                    player_instance.defensiveRebounds = player_data_game['defensiveRebounds']
                    player_instance.steals = player_data_game['steals']
                    player_instance.blocks = player_data_game['blocks']
                    player_instance.turnovers = player_data_game['turnovers']
                    player_instance.defensiveFouls = player_data_game['defensiveFouls']
                    player_instance.offensiveFouls = player_data_game['offensiveFouls']
                    player_instance.freeThrowsMade = player_data_game['freeThrowsMade']
                    player_instance.freeThrowsAttempted = player_data_game['freeThrowsAttempted']
                    player_instance.twoPointersMade = player_data_game['twoPointersMade']
                    player_instance.twoPointersAttempted = player_data_game['twoPointersAttempted']
                    player_instance.threePointersMade = player_data_game['threePointersMade']
                    player_instance.threePointersAttempted = player_data_game['threePointersAttempted']
                    #print(f"777---- {Player.id}")
                    shots_data = player_data_game['shots']
                    for shot_data in shots_data:
                         is_make = shot_data['isMake']
                         location_x = shot_data['locationX']
                         location_y = shot_data['locationY']
                         shot = Shot(is_make, location_x, location_y)
                         player_instance.shots.append(shot)
                    self.addPlayer(player_instance)
                    
                    break

