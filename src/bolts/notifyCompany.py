import os, smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from streamparse import Bolt

class notifyCompanyBolt(Bolt):
    outputs = []

    def process(self, tup):
        redditTitle = tup.values[0] # extract the reddit Title
        redditLink = tup.values[1] # extract the reddit Link
        companyName = tup.values[2] # extract the company name

        fromaddr = "arslincars@gmail.com"
        toaddr = "mlin48@fordham.edu"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Hey " + companyName + ", there is a reddit post about your company"

        body = ("Hey " + companyName + "\n" +
            " \n" +
            "While our bot searched through posts on reddit, we noticed a post" +
            " about your company." +
            "\n" +
            " \nMaybe you would like to look at it and see what people are saying" +
            " about your comapny" +
            "\nHere is the Post Title: \n\n    " + redditTitle +
            "\n\nand Post link here: \n    www.reddit.com" + redditLink +
            "\n" +
            "\nBest," +
            "\nBots Rule the World"
            )
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "slowmotion")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()