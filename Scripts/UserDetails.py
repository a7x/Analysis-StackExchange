import sys
import os
import marshal
import Utils
from lxml import etree
if len(sys.argv)<2:
    print 'python name.py posts.xml acceptedIdsList users.xml userDictOutput'
    sys.exit()
userdict = {}

'''{'accepted':,'answered':,'asked':,'reputation':,'upvotes',downvotes,views}'''

infile = open(sys.argv[1],'r')
context = etree.iterparse(infile)
acceptedids = open(sys.argv[2],'r')

setAccepted = set([])

for line in acceptedids:
    setAccepted.add(line.rstrip('\n'))
def initializeDict(d,userId):
    d[userId] = {}
    d[userId]['answered'] = 0
    d[userId]['asked'] = 0
    d[userId]['accepted'] = 0
    d[userId]['upvotes'] = 0
    d[userId]['downvotes'] = 0
    d[userId]['views'] = 0
    d[userId]['reputation'] = 0
    return d


for event, elem in context:
    if(getPostTypeId(elem)=="1"): # is a question
        userId = getOwner(elem)
        if(userId in userdict):
            userdict[userId]['asked'] += 1
        else:
            initializeDict(userdict,userId)
            userdict[userId]['asked'] += 1
    
    else:
        userId = getOwner(elem)
        idAnswer = getId(elem)
        if(userId in userdict):
            userdict[userId]['answered'] += 1
            
        else:
            initializeDict(userdict,userId)
            userdict[userId]['answered'] += 1
        if(idAnswer in setAccepted):
            userdict[userId]['accepted'] += 1
    clearElem(elem)

userfile = open(sys.argv[3],'r')
userContext = etree.iterparse(userfile)
for event, elem in userContext:
    ''' id, upvotes, downvotes, views, reputation'''   

    (userId,upvotes,downvotes,views,reputation) = getUserInfo(elem)
    if(userId not in userdict):
        initializeDict(userdict,userId)
    userdict[userId]['upvotes'] = upvotes
    userdict[userId]['downvotes'] = downvotes
    userdict[userId]['views'] = views
    userdict[userId]['reputation'] = reputation
    clearElem(elem)

marshal.dump(userdict,open(sys.argv[4],'wb'))



