#find out number of views for all Famous questions
#and all non Famous ones. 
#and compare
from __future__ import division
import sys
import os
from lxml import etree
import Utils
infile = open(sys.argv[1],'r')

context = etree.iterparse(infile)
sumFamous = 0
sumNonFamous = 0
numFamous = 0
numNonFamous = 0
for event,elem in context:
    if(Utils.getPostTypeId(elem)=="1"):
        if(Utils.getViewCount(elem)):
            viewCount = int(Utils.getViewCount(elem))
            if(viewCount>10000):
                sumFamous += viewCount
                numFamous += 1
            else:
                sumNonFamous += viewCount
                numNonFamous += 1
    Utils.clearElem(elem)
print 'average views Famous is ',sumFamous/numFamous
print 'average views non Famous is ',sumNonFamous/numNonFamous
