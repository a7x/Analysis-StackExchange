''' Count the number of users for each site and write the output to a file '''
import sys
import os
from lxml import etree
from Utils import *
if(len(sys.argv)<2):
	print 'python CountingUsers.py xmlTopDirectory outputfile'

output = open(sys.argv[2], 'w')
for l in os.listdir(sys.argv[1]):
	if('.DS_Store' not in l):
		userCount = 0
		infile = open(os.path.join(sys.argv[1], l, 'users.xml'))
		context = etree.iterparse(infile)
		for event, elem in context:
			userCount += 1
			clearElem(elem)
		output.write(l + '\t' + str(userCount) + '\n')



