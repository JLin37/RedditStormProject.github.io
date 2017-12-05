import os, datetime

from pymongo import MongoClient

from streamparse import Bolt

class storeDataBolt(Bolt):
	outputs = []

	# MongoDB connection
	client = MongoClient('localhost', 27017)
	redditDB = client.redditSubmissions

	def process(self, tup):
		redditTitle = tup.values[0]
		redditLink = tup.values[1]
		redditData = {"Title": redditTitle,
			"Link": redditLink,
			"timestamp": datetime.datetime.utcnow()}
		try:
			redditSubmissions_id = redditDB['redditData'].insert_one(redditData).inserted_id
			self.logger.info("matched company [{:}]".format(redditTitle))
			self.emit(["redditTitle"])
		except:
			self.fail(tup)