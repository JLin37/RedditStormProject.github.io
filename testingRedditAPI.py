import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(companyName, redditTitle, redditLink):
    fromaddr = "arslincars@gmail.com"
    toaddr = "mlin48@fordham.edu"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Hey" + companyName + "There is a reddit post about your company"

    body = ("Hey" + companyName + "\n" +
        " \n" +
        "While our bot searched through posts on reddit, we noticed a post" +
        "\n about your company." +
        "\n" +
        " \n Maybe you would like to look at it and see what people are saying" +
        "\n about your comapny" +
        "\n Here is the Post Title: " + redditTitle +
        "\n and Post link: " + redditLink
        )
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "slowmotion")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def main():
	companyName = "Apple"
	redditTitle = "this is testing stupid"
	redditLink = "reddit.com"
	sendEmail(companyName, redditTitle, redditLink)

main()

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