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
#inputs
infile_post = open(sys.argv[1], 'rb')
usersDict = marshal.load(open(sys.argv[2],'rb'))
context = etree.iterparse(infile_post)

#outputs
trainingcsv = csv.writer(open(sys.argv[3], 'wb'), delimiter='\t')
testcsv = csv.writer(open(sys.argv[4],'wb'),delimiter='\t')
results = open(sys.argv[6],'w')
rand = open(sys.argv[5],'r')
testIds = fillIds(rand)

questionsDict = {}
print len(testIds)
for event, elem in context:
    postTypeId = getPostTypeId(elem)
    if postTypeId == '1':
        owner = getOwner(elem)

        user = User(owner,usersDict[owner])
        question = Question(elem)
        
        postId = getId(elem)
        

        allTags = getTags(elem).lstrip('<').rstrip('>').split('><')
        numTags = len(allTags)
        
        
       
        row = \
        [owner, question.lengthTitle, question.length, question.score, question.favCount, question.commentCount, question.answerCount, numTags,\
        user.reputation, user.views, user.upvotes, user.downvotes]

        if(int(postId) in testIds):
            #print 'Id found in test id ',postId
            questionsDict[postId] = row
            results.write(postId+'\t'+str(question.isFamous)+'\n')
        else:
            row.append(question.isFamous)
            questionsDict[postId] = row
    clearElem(elem)

for postId in questionsDict:
    if(int(postId) in testIds):
        testcsv.writerow(questionsDict[postId])
        continue
    trainingcsv.writerow(questionsDict[postId])

