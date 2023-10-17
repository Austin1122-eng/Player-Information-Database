

/* sql script to create game table */ 
CREATE TABLE game(
	gameId INT NOT NULL PRIMARY KEY,
	gameDate DATE NOT NULL,
	homeTeamId INT NOT NULL,
	awayTeamId INT NOT NUll
);

/* sql script to create homeTeam table */
CREATE TABLE homeTeam(
	gameId INT NOT NULL,
	teamId INT NOT NULL
);

ALTER TABLE homeTeam
ADD PRIMARY KEY(gameId, teamId);

/* sql script to create awayTeam table */

CREATE TABLE awayTeam(
	gameId INT NOT NULL,
	teamId INT NOT NULL
);

ALTER TABLE awayTeam
ADD PRIMARY KEY(gameId, teamId);



/* sql script to create player table */

CREATE TABLE player(
	gameId INT NOT NULL,
	teamId INT NOT NULL,
	playerId INT NOT NULL,
	playerName VARCHAR(50) NOT NULL,
	isStarter BOOL NOT NULL,
	minutes INT NOT NULL,
	points INT NOT NULL,
	assists INT NOT NULL,
	offensiveRebounds INT NOT NULL,
	defensiveRebounds INT NOT NULL,
	steals INT NOT NULL,
	blocks INT NOT NULL,
	turnovers INT NOT NULL,
	defensiveFouls INT NOT NULL,
	offensiveFouls INT NOT NULL,
	freeThrowsMade INT NOT NULL,
	freeThrowsAttempted INT NOT NULL,
	twoPointersMade INT NOT NULL,
	twoPointersAttempted INT NOT NULL,
	threePointersMade INT NOT NULL,
	threePointersAttempted INT NOT NULL
);

ALTER TABLE player
ADD PRIMARY KEY (gameId, teamId, playerId);

/* sql script to create shot table */

CREATE TABLE shot(
	shotId SERIAL PRIMARY KEY,
	gameId INT NOT NULL,
	teamId INT NOT NULL,
	playerId INT NOT NULL,
	isMake BOOL NOT NULL,
	location_X NUMERIC NOT NULL,
	location_y NUMERIC NOT NULL
);


SELECT * FROM game;
SELECT * FROM homeTeam;
SELECT * FROM awayTeam;
SELECT * FROM player;
SELECT * FROM shot;


