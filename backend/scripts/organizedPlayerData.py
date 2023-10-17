from scripts.player import PlayerJson, ShotJson

class organizedPlayerInfo:
    def __init__(self):
        self.name = None
        self.games = []
        self.player_instance = PlayerJson()

    def populateShot(self, shot_dict):
        shot_instance = ShotJson()
        shot_instance.is_make = shot_dict['ismake']
        shot_instance.location_x = shot_dict['location_x']
        shot_instance.location_y = shot_dict['location_y']

        return shot_instance
    
        

    def populateGame(self, player_dict, shots_data, game_data):

        for i in game_data:
            if i['hometeamid'] == player_dict['teamid']:
                self.player_instance.gameDate = str(i['gamedate'])
            elif i['awayteamid'] == player_dict['teamid']:
                self.player_instance.gameDate = str(i['gamedate'])
            break
        self.player_instance.is_Starter = player_dict['isstarter']
        self.player_instance.minutes = player_dict['minutes']
        self.player_instance.points = player_dict['points']
        self.player_instance.assists = player_dict['assists']
        self.player_instance.offensiveRebounds = player_dict['offensiverebounds']
        self.player_instance.defensiveRebounds = player_dict['defensiverebounds']
        self.player_instance.steals = player_dict['steals']
        self.player_instance.blocks = player_dict['blocks']
        self.player_instance.turnovers = player_dict['turnovers']
        self.player_instance.defensiveFouls = player_dict['defensivefouls']
        self.player_instance.offensiveFouls = player_dict['offensivefouls']
        self.player_instance.freeThrowsMade = player_dict['freethrowsmade']
        self.player_instance.freeThrowsAttempted = player_dict['freethrowsattempted']
        self.player_instance.twoPointersMade = player_dict['twopointersmade']
        self.player_instance.twoPointersAttempted = player_dict['twopointersattempted']
        self.player_instance.threePointersMade = player_dict['threepointersmade']
        self.player_instance.threePointersAttempted = player_dict['threepointersattempted']
        for shot_data in shots_data:

            if(shot_data['playerid'] == player_dict['playerid']):

                shot = ShotJson()
                shot.is_make = shot_data['ismake']
                shot.location_x =  shot_data['location_x']
                shot.location_y = shot_data['location_y']
                self.player_instance.shots.append(shot.__dict__)
                break
                         
        self.games.append(self.player_instance.__dict__)

    

    def populateName(self, name):
        self.name = name

    def getNames(self):
        return self.name
    
    def getGames(self):
        return self.games


    