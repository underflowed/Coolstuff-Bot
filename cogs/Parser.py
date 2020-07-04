import re
import requests
from bs4 import BeautifulSoup


class Parser():
    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel)'}
        self.MAIN_SEARCH_URL = "https://www.coolstuffinc.com/p/Magic%3A+The+Gathering/"

    def GetCardText(self, cardname):
        url = self.MAIN_SEARCH_URL + cardname
        parsedHtml = BeautifulSoup(requests.get(url, headers=self.header).text, 'html.parser')
        accumalator = "Card Info: "
        for tag in parsedHtml.find_all("div", class_="large-9 medium-9 small-7 columns"):
            accumalator += tag.get_text()
            accumalator += "\n"
        return (accumalator, url)
