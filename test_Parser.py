
from cogs.Parser import Parser

testparser = Parser()
cards = ["Snapcaster Mage", "Tarmogoyf", "Farseek", "Surgical Extraction", "Lighting Bolt"]
for cardnames in cards:
    card = testparser.GetCardText(cardnames)
    print(card)
    