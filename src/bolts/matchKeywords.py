import os
from collections import Counter

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from streamparse import Bolt

class matchKeywordsBolt(Bolt):
    outputs = ['redditTitle', 'redditLink']

    def process(self, tup):
        splitTitle = tup.values[0] # extract the splitTitle
        redditTitle = tup.values[1] # extract the redditTitle
        redditLink = tup.values[2] # extract the redditLink
        # file = open("~/companynames.txt", "r")
        # companyNames = file.readlines()
        companyNames = ["Microsoft",
                "Apple",
                "google",
                "blizzard",
                "amd",
                "nvidia",
                "intel",
                "aetna",
                "amazon",
                ]
        for companyName in companyNames:
            if companyName == splitTitle:
                #sent email to company support
                self.sendEmail(companyName, redditTitle, redditLink)
                self.logger.info("matched company [{:}]".format(companyName))
                self.logger.info("Reddit Title [{:}]".format(redditTitle))
                self.logger.info("Reddit Link [{:}]".format(redditLink))
                self.emit([redditTitle, redditLink])

    def sendEmail(self, companyName, redditTitle, redditLink):
        fromaddr = "arslincars@gmail.com"
        toaddr = "mlin48@fordham.edu"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Hey" + companyName + "There is a reddit post about your company"

        body = (" Dear Sir/Madam \n" +
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