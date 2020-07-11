#WORK IN PROGRESS
#This is meant to showcase how to acquire tournament data from a challonge bracket
#this file is grabbing tournament data from a dummy tournament at https://challonge.com/7y3m8oss
import challonge
import json
class ChallongeTournament():
    def __init__(self,tournamentid):
        
        self.API_CREDS = ("Dudeinyoursmash", "ARJEEdkLRY3bpSLJ4gvC1j8qKwEUOb1TfnAdGwiL")

        challonge.set_credentials(self.API_CREDS[0], self.API_CREDS[1])
        self.tournament = challonge.tournaments.show(tournamentid)
        self.matches = challonge.matches.index(self.tournament["id"])
        self.participants = challonge.participants.index(self.tournament["id"])

    def GetPairings(self):
        accumalator = ""
        for match in self.matches:
            player1 = None
            player2 = None
            for participant in self.participants:
                if match["state"] == "open":
                    if match["player1-id"]  == participant["id"]:
                        player1 = participant["name"]
                    elif match["player2-id"] == participant["id"]:
                        player2 = participant["name"]
                else:
                    pass
            if match["state"] == "open":
                pairing = "@{0} is playing @{1}\n".format(player1, player2)
                accumalator += pairing
                print("@{0} is playing @{1}".format(player1, player2))
        return accumalator
