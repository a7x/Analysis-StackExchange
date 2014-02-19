#read the user file and get the average reputation for users
#also %age of users with more than 4.8K reputation
from __future__ import division
import sys
import os
import marshal
from collections import defaultdict
import Utils
from lxml import etree


repSum = 0
numUsers = 0
UsersGreater4K = 0

with open(sys.argv[1]) as infile:
	context = etree.iterparse(infile)
	for event, elem in context:
			reputation = int(Utils.getReputation(elem))
	        if reputation:
	            if reputation > 4800:
	                UsersGreater4K +=1
	            numUsers +=1
	            repSum += rep
	        Utils.clearElem(elem)

print '%age users more than 4.8K ',UsersGreater4K/numUsers
print 'Num Users greater than 4.8K', UsersGreater4K

