import json
from team import Team

#Game Class used to define populate the players in it's respective team as well as keep track of the game ID and Date
class Game:
    def __init__(self, game_json, teams_json, players_json):
        self.id = game_json['id']
        self.date = game_json['date']
        self.home_team = None
        self.away_team = None
        #self.players = []

        home_team_data = game_json['homeTeam']
        away_team_data = game_json['awayTeam']

 
        for key in teams_json:
            if key['id'] == home_team_data['id']:
                team = Team(home_team_data['id'], key['name'])
                team.populate_player(home_team_data['players'], self.home_team, players_json)
                # Team.id = home_team_data['id']
                # Team.nameTest = key['name']
                #self.populate_player(home_team_data['players'], self.home_team, players_json, Team)
                #print(f"CASE 0000- {Team.id}")
                # for item in players:
                #     print(f"           CASE 0002- {item.name}")
                #test = ['1']
                #Team.addPlayer(players)
                self.home_team = team
                break

        for key in teams_json:
            if key['id'] == away_team_data['id']:
                team = Team(away_team_data['id'], key['name'])
                team.populate_player(away_team_data['players'], self.away_team, players_json)
                # Team.id = away_team_data['id']
                # Team.nameTest = key['name']
                # Team.player.append(self.populate_player(away_team_data['players'], self.away_team, players_json))
                self.away_team = team
                break
