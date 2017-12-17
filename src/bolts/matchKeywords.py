import os
from collections import Counter

from streamparse import Bolt

class matchKeywordsBolt(Bolt):
    outputs = ['redditTitle', 'redditLink', 'companyName']

    def process(self, tup):
        splitTitle = tup.values[0] # extract the splitTitle
        redditTitle = tup.values[1] # extract the redditTitle
        redditLink = tup.values[2] # extract the redditLink
        # file = open("~/companynames.txt", "r")
        # companyNames = file.readlines()
        companyNames = ["Microsoft",
                "Apple",
                "Google",
                "Blizzard",
                "AMD",
                "Nvidia",
                "Intel",
                "Aetna",
                "Amazon"]
        for companyName in companyNames:
            if companyName == splitTitle:
                self.logger.info("matched company [{:}]".format(companyName))
                self.emit([redditTitle, redditLink, companyName])