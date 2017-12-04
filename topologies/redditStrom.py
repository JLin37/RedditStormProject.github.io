"""
Reddit Storm Project Topology
"""

from streamparse import Grouping, Topology

from bolts.titleSplit import titleSplitterBolt
from bolts.matchKeywords import matchKeywordsBolt
from spouts.redditStream import streamRedditSpout

class WordCount(Topology):
	redditStream_spout = streamRedditSpout.spec()
	titleSplit_bolt = titleSplitterBolt.spec(inputs = {redditStream_spout: Grouping.fields('redditTitle', 'redditLink')}, par = 2)
	matchKeywords_bolt = matchKeywordsBolt.spec(inputs = {titleSplit_bolt: Grouping.fields('splitTitle', 'redditTitle', 'redditLink')}, par = 2)
