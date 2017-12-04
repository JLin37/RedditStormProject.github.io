import praw

from streamparse.spout import Spout

class streamRedditSpout(Spout):
    outputs = ['redditTitle', 'redditLink']

    def initialize(self, stormconf, context):    	
    	#setup reddit client info for api access
    	reddit = praw.Reddit(client_id='UwZjWiAJlqse6w',
    	                     client_secret='-c7qxVg7w8K3_FLG-lQip-b9npY',
    	                     user_agent='StormFinalProject testing')
    	#iterate through new reddit submission on /r/all 
    	for submission in reddit.subreddit('all').stream.submissions():
    		self.redditTitle = submission.title
    		self.redditLink = submission.permalink

    def next_tuple(self):
        redditTitle = next(self.redditTitle)
        redditLink = next(self.redditLink)
        self.emit([redditTitle, redditLink])

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing