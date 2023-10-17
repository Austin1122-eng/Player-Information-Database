class Shot:
    def __init__(self, is_make, location_x, location_y):
        self.is_make = is_make
        self.location_x = location_x
        self.location_y = location_y

class Player:
    def __init__(self, player_id, name):
        self.id = player_id
        self.name = name
        self.is_Starter = None
        self.minutes = None
        self.points = None
        self.assists = None
        self.offensiveRebounds = None
        self.defensiveRebounds = None
        self.steals = None
        self.blocks = None
        self.turnovers = None
        self.defensiveFouls = None
        self.offensiveFouls = None
        self.freeThrowsMade = None
        self.freeThrowsAttempted = None
        self.twoPointersMade = None
        self.twoPointersAttempted = None
        self.threePointersMade = None
        self.threePointersAttempted = None
        self.shots = []

class ShotJson:
    def __init__(self):
        self.is_make = None
        self.location_x = None
        self.location_y = None

class PlayerJson:
    def __init__(self):
        self.gameDate = None
        self.is_Starter = None
        self.minutes = None
        self.points = None
        self.assists = None
        self.offensiveRebounds = None
        self.defensiveRebounds = None
        self.steals = None
        self.blocks = None
        self.turnovers = None
        self.defensiveFouls = None
        self.offensiveFouls = None
        self.freeThrowsMade = None
        self.freeThrowsAttempted = None
        self.twoPointersMade = None
        self.twoPointersAttempted = None
        self.threePointersMade = None
        self.threePointersAttempted = None
        self.shots = []

class ShotJson:
    def __init__(self):
        self.is_make = None
        self.location_x = None
        self.location_y = None