#See num questions answered before and after epic badge
import sys
import os
import marshal 
from lxml import etree
from dateutil.relativedelta import *
import datetime
import Utils

if(len(sys.argv)<2):
    print 'python name.py badges.xml posts.xml outputDict'
    sys.exit()

epicUserIds = {}
epicFile = open(sys.argv[1],'r')
context = etree.iterparse(epicFile)
epicUserIds = {}
epicDetails = {}
for event,elem in context:
    badge = Utils.getBadge(elem)
    userId = Utils.getUserId(elem)
    date = Utils.getDate(elem)
    if(badge=="Epic"):
        epicUserIds[userId]=date
    Utils.clearElem(elem)

infile = open(sys.argv[2],'r')
context = etree.iterparse(infile)
numAnswersBefore = 0
numAnswersAfter = 0
for i in epicUserIds:
    epicDetails[i]={}
    epicDetails[i]["before"]=0
    epicDetails[i]["after"]=0

def BeforeOrAfter(t1,t2):
    #Return true if epicDate(t1) before t2 or vice-versa
    return t1<t2

for event,elem in context:
    if(getPostTypeId(elem)=="1"):#is a question,I don't care. move on
        continue
    ownerId = Utils.getOwner(elem)
    time = Utils.getCreationDate(elem)

    if(ownerId in epicUserIds):
        epicTime = epicUserIds[ownerId] #Time when he got the epic badge
        if(BeforeOrAfter(time,epicTime)):#if time is before epic time 
            epicDetails[ownerId]["before"]+=1
            numAnswersBefore+=1
        else:
            epicDetails[ownerId]["after"]+=1
            numAnswersAfter+=1
    Utils.clearElem(elem)

epicFile.close()
print numAnswersBefore
print numAnswersAfter
for key in epicDetails:
    print key,'\t',epicDetails[key]

