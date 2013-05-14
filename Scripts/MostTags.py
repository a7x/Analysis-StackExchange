#Find out the tags that are most often used with questions tagged famous
import sys
import os
import marshal
from lxml import etree
from collections import *
import operator
from Utils import *
if(len(sys.argv)<2):
    print 'python name.py posts.xml tagDistributionDict'
    sys.exit()

infile = open(sys.argv[1],'r')

context = etree.iterparse(infile)
tagsDict = defaultdict(int)
tagString = ''
for event,elem in context:
    
    if(getPostTypeId(elem)=="1"):
        ViewCount = int(getViewCount(elem))
        if(ViewCount>10000):
            allTags = elem.get("Tags").lstrip('<').rstrip('>').split('><')
            for l in allTags:
                tagString += l + ' '
                tagsDict[l]+=1

    clearElem(elem)

top20Dict = \
dict(sorted(tagsDict.iteritems(),key=operator.itemgetter(1),reverse=True)[:20])

marshal.dump(top20Dict,open(sys.argv[2],'wb'))

bottom5Dict = \
dict(sorted(tagsDict.iteritems(),key=operator.itemgetter(1))[:5])

