#WORK IN PROGRESS
import challonge
import json
API_CREDS = ("Dudeinyoursmash", "ARJEEdkLRY3bpSLJ4gvC1j8qKwEUOb1TfnAdGwiL")

challonge.set_credentials(API_CREDS[0], API_CREDS[1])
tournament = challonge.tournaments.show("7y3m8oss")
matches = challonge.matches.index(tournament["id"])
participants = challonge.participants.index(tournament["id"])
for match in matches:
    for participant in participants:
        if match["state"] == "open":
            if match["player1-id"]  == participant["id"]:
                print(participant["name"]+ " is dueling ")
            if match["player2-id"] == participant["id"]:
                print(participant["name"]+ "!!!!")

   
