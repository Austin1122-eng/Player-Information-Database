import json
import os
from databaseAction import querySQL
from game import Game


################################
# JSON FILE READER
#################################
cwd = os.getcwd()
with open(cwd + '/raw_data/games.json', 'r') as games_file:
    games_json = json.load(games_file)

with open(cwd + '/raw_data/players.json', 'r') as players_file:
    players_json = json.load(players_file)

with open(cwd + '/raw_data/teams.json', 'r') as teams_file:
    teams_json = json.load(teams_file)

#print(players_json)

################################
# INITIALIZE TEAM ID's
#################################
artificialHomeTeamId = 1
artificialAwayTeamId = 2

################################
# ADD TO DB
#################################
def addGameToDB(gameId, homeTeamId, awayTeamId):
    game_values = (game.id, game.date ,game.home_team.id, game.away_team.id)
    queryFunction.insert_From_Py(game_values, insertQueryGame)

def addHomeTeamToDB(gameId, teamId):
    homeTeam_values = (gameId, teamId)
    queryFunction.insert_From_Py(homeTeam_values, insertQueryHomeTeam)

def addAwayTeamToDB(gameId, teamId):
    awayTeam_values = (gameId, teamId)
    queryFunction.insert_From_Py(awayTeam_values, insertQueryAwayTeam)

def addPlayerToDB(gameId, artificialId, player):
    player_values = (game.id, artificialHomeTeamId,player.id, player.name ,player.is_Starter, player.minutes, player.points, player.assists, player.offensiveRebounds, 
                         player.defensiveRebounds, player.steals, player.blocks, player.turnovers, player.offensiveFouls, player.defensiveFouls, 
                         player.freeThrowsMade, player.freeThrowsAttempted, player.twoPointersMade, player.twoPointersAttempted, player.threePointersMade, 
                         player.threePointersAttempted)
        
    queryFunction.insert_From_Py(player_values, insertQueryPlayer)

def addShotToDB(gameId, teamId, playerId, shot):
    shot_values = (gameId, teamId ,playerId, shot.is_make, shot.location_x, shot.location_y)
    queryFunction.insert_From_Py(shot_values, insertQueryShot)

################################
# TRUNCATE QUERY INSTRUCTIONS
#################################
def truncateTables():
    truncateQueryGame = "TRUNCATE game"
    truncateQueryhomeTeam = "TRUNCATE homeTeam"
    truncateQueryawayTeam = "TRUNCATE awayTeam"
    truncateQueryPlayer = "TRUNCATE player"
    truncateQueryShot = "TRUNCATE shot"

    queryFunction.truncate_From_Py(truncateQueryGame)
    queryFunction.truncate_From_Py(truncateQueryhomeTeam)
    queryFunction.truncate_From_Py(truncateQueryawayTeam)
    queryFunction.truncate_From_Py(truncateQueryPlayer)
    queryFunction.truncate_From_Py(truncateQueryShot)

################################
# GAME PROCESS
#################################
games = []
for game_data_json_index in games_json:
        game = Game(game_data_json_index, teams_json, players_json)
        games.append(game)

################################
# QUERY CLASSES
#################################
queryFunction = querySQL()


################################
# TRUNCATE ALL TABLE BEFORE LOADING
#################################

truncateTables()



################################
# INSERT QUERY INSTRUCTIONS
#################################
insertQueryGame = "INSERT INTO game (gameId, gameDate ,homeTeamId, awayTeamId) VALUES (%s, %s ,%s, %s)"
insertQueryHomeTeam = "INSERT INTO homeTeam(gameId, teamId) VALUES (%s,%s)"
insertQueryAwayTeam = "INSERT INTO awayTeam(gameId, teamId) VALUES (%s, %s)"
insertQueryPlayer = """INSERT INTO player(gameId, teamId, playerId, playerName, isStarter, minutes, points, assists, offensiveRebounds, 
                        defensiveRebounds, steals, blocks, turnovers, defensiveFouls, offensiveFouls, freeThrowsMade, freeThrowsAttempted, 
                        twoPointersMade, twoPointersAttempted, threePointersMade, threePointersAttempted) 
                        VALUES(%s,%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

insertQueryShot = "INSERT INTO shot(gameId, teamId ,playerId, isMake, location_X, location_Y) VALUES (%s,%s,%s,%s,%s, %s)"


################################
# FUNCTION TO ADD HOME TEAM TO DB
#################################
def addHomeTeamDB():
    addHomeTeamToDB(game.id,game.home_team.id)
    
    for player in game.home_team.players:
        addPlayerToDB(game.id, artificialHomeTeamId, player)        
        for shot in player.shots:
             addShotToDB(game.id, game.home_team.id, player.id, shot)
             

################################
# FUNCTION TO ADD AWAY TEAM TO DB
#################################
def addAwayTeamDB():
    addAwayTeamToDB(game.id,game.away_team.id)
       
    for player in game.away_team.players:
        addPlayerToDB(game.id, artificialAwayTeamId, player)       
        for shot in player.shots:             
             addShotToDB(game.id, game.away_team.id, player.id, shot)



    # retrieve = databaseAction.retriveGame
    # retrieve.retriveGameFromDB()


################################
#ADD ALL GAME INTO DB
#################################
for game in games:
    addGameToDB(game.id, game.home_team.id, game.away_team.id)
    addHomeTeamDB()
    addAwayTeamDB()
    



    
del queryFunction

