#read the user file and get the average reputation for users
#also %age of users with more than 4.8K reputation
from __future__ import division
import sys
import os
import marshal
from collections import defaultdict
import Utils
from lxml import etree
infile = open(sys.argv[1],'r') #users.xml
context = etree.iterparse(infile)

repSum = 0
numUsers = 0
UsersGreater4K = 0
for event, elem in context:
        if(Utils.getReputation(elem) is not None):
            rep = int(Utils.getReputation(elem))
            if(rep > 4800):
                UsersGreater4K +=1
            numUsers +=1
            repSum += rep
        Utils.clearElem(elem)
print '%age users more than 4.8K ',UsersGreater4K/numUsers
print 'num Users greater than 4.8K', UsersGreater4K

