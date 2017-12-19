import os, datetime

from pymongo import MongoClient

from streamparse import Bolt

class storeDataBolt(Bolt):
	outputs = []

	def process(self, tup):
		redditTitle = tup.values[0]
		redditLink = tup.values[1]
		redditData = {"Title": redditTitle,
			"Link": "www.reddit.com" + redditLink,
			"timestamp": datetime.datetime.utcnow()}
		try:
			client = MongoClient('localhost', 27017)
			redditDB = client.redditSubmissions
			redditSubmissions_id = redditDB['redditData'].insert_one(redditData).inserted_id
			client.close()
		except:
			pass
			