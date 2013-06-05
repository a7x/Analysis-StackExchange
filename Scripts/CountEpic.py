import sys
import os
from lxml import etree
from Utils import *
infile = open(sys.argv[1],'r')

context = etree.iterparse(infile)

count = 0
for event, elem in context:
	if(getBadge(elem)=="Epic"):
		count+=1
	clearElem(elem)

print count

