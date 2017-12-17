# import praw

# def redditStream():
# 	#setup reddit client info for api access
# 	reddit = praw.Reddit(client_id='UwZjWiAJlqse6w',
# 	                     client_secret='-c7qxVg7w8K3_FLG-lQip-b9npY',
# 	                     user_agent='StormFinalProject testing')

# 	#iterate through new reddit submission on /r/all 
# 	for submission in reddit.subreddit('all').new():
# 		return submission.title, submission.permalink

# def printStream():
# 	print(redditStream())
# printStream()

# import praw, logging

# from multiprocessing import Process, Queue

# def redditStream():
# 	#setup reddit client info for api access
# 	reddit = praw.Reddit(client_id='UwZjWiAJlqse6w',
# 	                     client_secret='-c7qxVg7w8K3_FLG-lQip-b9npY',
# 	                     user_agent='StormFinalProject testing')

# 	#iterate through new reddit submission on /r/all 
# 	submissions = reddit.subreddit('all').stream.submissions()
# 	submission = next(submissions)
# 	redditTitle = submission.title
# 	print(redditTitle)
# 	logging.info("Reddit Title [{:}]".format(redditTitle))


# redditStream()

# def printStream():
# 	while True:
# 		q = Queue()
# 		p = Process(target = redditStream, args = (q,))
# 		p.start()
# 		print(q.get())

# printStream()