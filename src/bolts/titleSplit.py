import os

from streamparse import Bolt

class titleSplitterBolt(Bolt):
    outputs = ['splitTitle', 'redditTitle', 'redditLink']

    def process(self, tup):
        redditTitle = tup.values[0]  # extract the redditTitle
        redditLink = tup.values[1]
        redditTitle = re.sub(r"[,.;!\?]", "", redditTitle)  # get rid of punctuation
        splitTitles = [[splitTitle.strip()] for splitTitle in redditTitle.split(" ") if splitTitle.strip()]
        if not splitTitles:
            # no splitTitles to process in the title, fail the tuple
            self.fail(tup)
            return

        for splitTitle in splitTitles:
            self.emit([splitTitle, redditTitle, redditLink])
        # tuple acknowledgement is handled automatically