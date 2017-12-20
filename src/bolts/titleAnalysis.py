import os, re, unicodedata

from streamparse import Bolt

class titleAnalysisBolt(Bolt):
    outputs = ['splitTitle', 'redditTitle', 'redditLink']

    def process(self, tup):
        redditTitle = tup.values[0]  # extract the reddit Title
        redditLink = tup.values[1]  #extract reddit Link
        
        try:
            redditTitle = str(unicodedata.normalize('NFKD', redditTitle).encode('ascii', 'ignore'))
            redditTitle = re.sub(r"[({',.;!\/|?})]", "", redditTitle)  # get rid of punctuation
            splitTitles = redditTitle.split()
            if not splitTitles:
            # no splitTitles to process in the title, fail the tuple
                pass
            for splitTitle in splitTitles:
                self.emit([splitTitle, redditTitle, redditLink])
        
        except:
            pass

        
