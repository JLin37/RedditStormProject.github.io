import os

from streamparse import Bolt

class matchKeywordsBolt(Bolt):
    outputs = ['redditTitle', 'redditLink', 'companyName']

    def process(self, tup):
        splitTitle = tup.values[0] # extract the split Title
        redditTitle = tup.values[1] # extract the reddit Title
        redditLink = tup.values[2] # extract the reddit Link
        companyNames = ["Microsoft",
                "Apple",
                "Google",
                "Blizzard",
                "AMD",
                "Nvidia",
                "Intel",
                "Aetna"]
        for companyName in companyNames:
            if companyName == splitTitle:
                self.logger.info("matched company [{:}]".format(companyName))
                self.emit([redditTitle, redditLink, companyName])