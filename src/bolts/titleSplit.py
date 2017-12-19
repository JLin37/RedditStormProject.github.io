import os, re, unicodedata

from streamparse import Bolt

class titleSplitterBolt(Bolt):
    outputs = ['splitTitle', 'redditTitle', 'redditLink']

    def process(self, tup):
        redditTitle = tup.values[0]  # extract the redditTitle
        redditLink = tup.values[1]
        #self.logger.info("Reddit Title [{:}]".format(redditTitle))
        redditTitle = str(unicodedata.normalize('NFKD', redditTitle).encode('ascii', 'ignore'))
        redditTitle = re.sub(r"[({',.;!\/|?})]", "", redditTitle)  # get rid of punctuation
        splitTitles = redditTitle.split()
        if not splitTitles:
            # no splitTitles to process in the title, fail the tuple
            pass

        for splitTitle in splitTitles:
            self.emit([splitTitle, redditTitle, redditLink])
