# -*- coding: utf-8 -*-
import logging
from functools import partial
import json
import os

from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler
from app.dbmodels import models
from scripts.returnPlayerInfo import retrievePlayer

LOGGER = logging.getLogger('django')

################################
# CONNECTS TO API AND SENDS IN THE PLAYER'S STATS PER GAME
#################################
class PlayerSummary(APIView):
    logger = LOGGER
    def get(self, request, playerID):
        """Return player data"""
        print(playerID)
        # TODO: Complete API response, replace placeholder below with actual implementation that sources data from database
        playerInfo = retrievePlayer()
        callToY = playerInfo.returnValuesInPlayerId(playerID)
        callToX = playerInfo.returnNameInPlayerId(playerID)
        name_statement = "{ " + "\"name\": " + "\"" + callToX + "\"" +","
        game_statement = "\"games\": "

        ################################
        # JSON FILE CREATOR
        #################################
        with open(os.path.dirname(os.path.abspath(__file__)) + '/result.json', "w") as outfile:
            outfile.writelines(name_statement)
            outfile.writelines(game_statement)
            outfile.write(callToY)
            outfile.write("}")
        ################################
        # JSON FILE LOADER INTO WEBSITE
        #################################
        with open(os.path.dirname(os.path.abspath(__file__)) + '/result.json') as sample_response:
            data = json.load(sample_response)
        
        return Response(data)
    
        #ORIGNAL CODE GIVEN
        # print(os.path.dirname(os.path.abspath(__file__)))
        # with open(os.path.dirname(os.path.abspath(__file__)) + '/sample_response/sample_response.json') as sample_response:
        #     data = json.load(sample_response)
        # return Response(data)
