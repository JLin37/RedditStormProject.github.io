import os, re

from streamparse import Bolt

class titleSplitterBolt(Bolt):
    outputs = ['splitTitle', 'redditTitle', 'redditLink']

    def process(self, tup):
        redditTitle = tup.values[0]  # extract the redditTitle
        redditLink = tup.values[1]
        #self.logger.info("Reddit Title [{:}]".format(redditTitle))
        redditTitle = re.sub(r"[,.;!\?]", "", redditTitle)  # get rid of punctuation
        splitTitles = redditTitle.split()
        if not splitTitles:
            # no splitTitles to process in the title, fail the tuple
            self.fail(tup)
            return

        for splitTitle in splitTitles:
            #self.logger.info("matched company [{:}]".format(splitTitle))
            self.emit([splitTitle, redditTitle, redditLink])
        # tuple acknowledgement is handled automatically