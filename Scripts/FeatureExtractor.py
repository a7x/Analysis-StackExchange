import types
import sys
import marshal
from Utils import *
from lxml import etree
import csv
class User:
    #this is for user features
    def __init__(self, userId, d):
        self.reputation = d['reputation']
        self.upvotes = d['upvotes']
        self.downvotes = d['downvotes']
        self.views = d['views']
        self.userId = userId
        self.asked = d['asked']
        self.accepted = d['accepted']
        self.answered = d['answered']
        

class Question:
    #this is for the question attributes
    def __init__(self, elem):
        self.length = len(getBody(elem).split(' '))
        self.title = getTitle(elem)
        self.commentCount = getCommentCount(elem)
        self.favCount = getFavouriteCount(elem)
        self.score = getScore(elem)
        self.answerCount = getAnswerCount(elem)
        self.lengthTitle = len(self.title.split(' '))
        self.isFamous = 1 if self.isFamousQuestion(elem) else 0

        self.numTags = 0

    def isFamousQuestion(self,elem):
        return int(getViewCount(elem)) > 10000
def fillIds(f):
    
    ''' given a list of question Ids, use these for test csv '''
    s = set([])
    for line in f:
        s.add(int(line.rstrip('\n')))
    return s

if(len(sys.argv)<2):
    print 'python name.py posts.xml userDetails.dict training.csv test.csv \
    randomIds result'
    sys.exit()

headers = ['userId', 'lenTitle', 'lenBody', 'qScore', 'qFav', 'qComment', \
'qAnswers', 'numTags', 'userRep', 'userViews', 'userUpVotes', \
'userDownVotes','famous']
#inputs
infile_post = open(sys.argv[1], 'rb')
usersDict = marshal.load(open(sys.argv[2],'rb'))
context = etree.iterparse(infile_post)

#outputs
trainingcsv = csv.DictWriter(open(sys.argv[3], 'wb'), fieldnames=headers, delimiter='\t')
testcsv = csv.DictWriter(open(sys.argv[4],'wb'),fieldnames = headers, delimiter='\t')
results = open(sys.argv[6],'w')
rand = open(sys.argv[5],'r')
testIds = fillIds(rand)

questionsDict = {}
trainingcsv.writerow(dict((fn,fn) for fn in headers))
testcsv.writerow(dict((fn,fn) for fn in headers))

def addRow(d,user,question):
    element = \
    { 'userId':user.userId,'lenTitle':question.lengthTitle,'lenBody':question.length,\
     'qScore':question.score, 'qFav':question.favCount, 'qComment':\
     question.commentCount, 'qAnswers':question.answerCount, 'numTags':question.numTags, \
     'userRep':user.reputation, 'userViews':user.views,\
     'userUpVotes':user.upvotes,'userDownVotes':user.downvotes,\
     'famous':question.isFamous }
    d.append(element)
    return d
trainingRows = []
testRows = []
for event, elem in context:
    postTypeId = getPostTypeId(elem)
    if postTypeId == '1':
        owner = getOwner(elem)

        user = User(owner,usersDict[owner])
        question = Question(elem)
        
        postId = getId(elem)
        

        allTags = getTags(elem).lstrip('<').rstrip('>').split('><')
        numTags = len(allTags)
        question.numTags = numTags
        if(int(postId) in testIds):
            addRow(testRows,user,question)
        else:
            addRow(trainingRows, user, question)
    clearElem(elem)

for obj in trainingRows:
    trainingcsv.writerow(obj)

for obj in testRows:
    testcsv.writerow(obj)

