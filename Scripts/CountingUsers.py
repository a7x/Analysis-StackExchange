''' Count the number of users for each site and write the output to a file '''
import sys
import os
from lxml import etree
import Utils
if(len(sys.argv)<2):
	print 'python CountingUsers.py users.xml'
	sys.exit()

inp = open(sys.argv[1],'r')
context = etree.iterparse(inp)
userCount = 0
with open(sys.argv[1]) as infile:
	context = etree.iterparse(infile)
	for event, elem in context:
		userCount += 1
		Utils.clearElem(elem)
print userCount




