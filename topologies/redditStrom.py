"""
Reddit Storm Project Topology
"""

from streamparse import Grouping, Topology

from bolts.titleSplit import titleSplitterBolt
from bolts.matchKeywords import matchKeywordsBolt
from bolts.notifyCompany import notifyCompanyBolt
from bolts.storeData import storeDataBolt
from spouts.redditStream import streamRedditSpout

class WordCount(Topology):
	redditStream_spout = streamRedditSpout.spec()
	titleSplit_bolt = titleSplitterBolt.spec(inputs = {
		redditStream_spout: Grouping.fields('redditTitle')}, par = 4)
	matchKeywords_bolt = matchKeywordsBolt.spec(inputs = {
		titleSplit_bolt: Grouping.fields('splitTitle')}, par = 2)
	notifyCompany_bolt = notifyCompanyBolt.spec(inputs = {
		matchKeywords_bolt: Grouping.fields('companyName')}, par = 2)
	storeData_bolt = storeDataBolt.spec(inputs = {
		matchKeywords_bolt: Grouping.fields('redditTitle')}, par = 1)
