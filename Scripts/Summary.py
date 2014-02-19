#give the top level xml directory and this script will return 
'''
	Num users
	Num epic users
	Num famous questions
	Num questions 
	Num answers	
'''
from lxml import etree
import sys
import Utils
import os

class Stats:
	def __init__(self, users, badges, posts):
		self.users = users
		self.badges = badges
		self.posts = posts
		self.summary = dict.fromkeys(["epic", "famous", "questions", "answers", "accepted", "users"],0)
		self.userContext = etree.iterparse(self.users)
		self.badgeContext = etree.iterparse(self.badges)
		self.postContext = etree.iterparse(self.posts)
	
	def numUsers(self):
		for event, elem in self.userContext:
			self.summary["users"] += 1
			Utils.clearElem(elem)
	
	def answerFeatures(self):
		for event, elem in self.postContext:
			if Utils.getPostTypeId(elem) == "1":#is question
				self.summary["questions"] += 1
				if Utils.getViewCount(elem) > 10000:
					self.summary["famous"] += 1
				if Utils.getAcceptedId(elem):
					self.summary["accepted"] += 1
			else:
				self.summary["answers"] += 1
			Utils.clearElem(elem)
	
	def numEpic(self):
		for event, elem in self.badgeContext:
			if Utils.getBadgeName(elem) == "Epic":
				self.summary["epic"] += 1
			Utils.clearElem(elem)

	def printSummary(self):
		print 'Num Users: num epic Users : ', self.summary['users'], '\t', self.summary['epic']
		print 'num questions: answers : accepted answers: ', self.summary['questions'], self.summary['answers'], self.summary['accepted']
		print 'num famous: ', self.summary['famous']

		
		
	def generateSummary(self):
		self.numUsers()
		self.numEpic()
		self.answerFeatures()
		self.printSummary()


if __name__ == '__main__':
	if(len(sys.argv)<2):
		print 'python name.py topLevelDirectory'
		sys.exit()

	with open(os.path.join(sys.argv[1], 'users.xml')) as users, open(os.path.join(sys.argv[1], 'badges.xml')) as badges, \
		open(os.path.join(sys.argv[1], 'posts.xml')) as posts:
		summ = Stats(users, badges, posts)
		summ.generateSummary()
	
		
		
