import sys
import os
from lxml import etree
import Utils


count = 0
with open(sys.argv[1]) as infile:
	context = etree.iterparse(infile)
	for event, elem in context:
		if(getBadge(elem)=="Epic"):
			count+=1
		Utils.clearElem(elem)

print count

