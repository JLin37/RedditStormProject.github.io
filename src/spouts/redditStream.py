import praw

from streamparse.spout import Spout

class streamRedditSpout(Spout):
    outputs = ['redditTitle', 'redditLink']

    def initialize(self, stormconf, context):
        #setup reddit client info for api access
        reddit = praw.Reddit(client_id='UwZjWiAJlqse6w',
                         client_secret='-c7qxVg7w8K3_FLG-lQip-b9npY',
                         user_agent='StormFinalProject testing')

        self.submissions = reddit.subreddit('all').stream.submissions()

    def next_tuple(self):
        submission = next(self.submissions)
        redditTitle = submission.title
        redditLink = submission.permalink
        #self.logger.info("Reddit Title [{:}]".format(redditTitle))
        self.emit([redditTitle, redditLink])

    def ack(self, tup_id):
        pass  # if a tuple is processed properly, do nothing

    def fail(self, tup_id):
        pass  # if a tuple fails to process, do nothing

# def redditStream(q):
#     #setup reddit client info for api access
#     reddit = praw.Reddit(client_id='UwZjWiAJlqse6w',
#                          client_secret='-c7qxVg7w8K3_FLG-lQip-b9npY',
#                          user_agent='StormFinalProject testing')

#     #iterate through new reddit submission on /r/all 
#     for submission in reddit.subreddit('all').stream.submissions():
#         return q.put([submission.title, submission.permalink])

# import time

# from itertools import cycle

# from streamparse import Spout


# class streamRedditSpout(Spout):
#     outputs = ['redditTitle', 'redditLink']

#     def initialize(self, stormconf, context):
#         self.titles = cycle([
#             "She advised him to take a long holiday",
#             "Microsoft is making a new Surface Laptop",
#             "I was very glad to get a present from her",
#             "The new Apple iPhone",
#             "He will be here in half an hour",
#             "She saw him eating a sandwich",
#             "amazon is selling everything",
#             "She advised him to take a long holiday, so he immediately quit work and took a trip around the world",
#             "I was very glad to get a present from her",
#             "He will be here in half an hour",
#             "She saw him eating a sandwich",
#             "She advised him to take a long holiday, so he immediately quit work and took a trip around the world",
#             "I was very glad to get a present from her",
#             "He will be here in half an hour",
#             "She saw him eating a sandwich",
#             "She advised him to take a long holiday, so he immediately quit work and took a trip around the world",
#             "I was very glad to get a present from her",
#             "He will be here in half an hour",
#             "She saw him eating a sandwich"
#         ])

#     def next_tuple(self):
#         time.sleep(1)
#         redditTitle = next(self.titles)
#         redditLink = "https://www.reddit.com"
#         self.emit([redditTitle, redditLink])

#     def ack(self, tup_id):
#         pass  # if a tuple is processed properly, do nothing

#     def fail(self, tup_id):
#         pass  # if a tuple fails to process, do nothing